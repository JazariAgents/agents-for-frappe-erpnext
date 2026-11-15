<!-- Frappe documentation: frappe-hr, part 5 of 10. Index: docs/INDEX.md -->

<!-- page: frappe-hr/hr__india-payroll__multi-company-settings.md -->
---
title: "Multi-Company Settings"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/india-payroll/multi-company-settings"
updated: "2026-08-31"
---

Payroll Settings is a single, site-wide document, so by default, one India Payroll configuration applies to every company on the site. That works for a single legal entity, but a group running two or more entities has only one place to record an ESIC employer code or an EPF establishment code, and each registered entity has its own.

Multi-company payroll lifts that limit. It adds a table where you record statutory registration details per company, and it scopes statutory deductions to the companies you list.

It is **off by default**. Existing sites are unaffected until you turn it on.

![](/files/imagecbd416.webp)
*Multi-Company Settinga*

## **When you need it**

Turn it on when either is true:

- You run payroll for more than one company on this site, and they have **different** statutory registration numbers.
- Some companies on this site are registered under a scheme (EPF, ESIC, LWF, Professional Tax), and others are not. For example, a newly incorporated entity still below the headcount threshold.

You do **not** need it when every company on the site shares one registration, or when only one company runs payroll.

## **Enabling it**

1. Go to **Payroll Settings &gt; India Payroll**.
2. Under **Multi-Company Payroll**, tick **Enable Multi-Company Payroll**.
3. In the **Company Payroll Settings** table that appears, add a row for each company that participates in statutory payroll.
4. Save.

Each row holds:


| Field                                    | Description                                                                       |
| :---------------------------------------- | :--------------------------------------------------------------------------------- |
| **Company**                              | The company this row configures. Required, and each company may appear only once. |
| **ESIC Registration Number**             | 17-digit ESIC employer code for this company.                                     |
| **EPF Establishment Code**               | EPFO Establishment Code used in this company's ECR file header.                   |
| **Professional Tax Registration Number** | State Professional Tax enrolment / registration number.                           |
| **LWF Registration Number**              | State Labour Welfare Fund establishment registration number.                      |


Only **Company** is mandatory. Leave a registration number blank if the company is not registered under that scheme, or if you have not received the number yet.

While multi-company payroll is on, the site-wide **ESIC Registration Number** and **EPF Establishment Code** fields are hidden, so there is never any question about which value applies to a given company.

## **How it changes payroll**

The per-scheme checkboxes (**Enable Professional Tax Deduction**, **Enable ESIC Deduction**, **Enable LWF Deduction**, **Enable EPF Deduction**) remain the master switches. Multi-company payroll narrows their reach; it does not override them.

A statutory deduction is applied to a salary slip only when **both** are true:

1. The scheme is enabled in Payroll Settings, **and**
2. The slip's company appears in the Company Payroll Settings table.

A company with no row is treated as **not configured** and gets no statutory deduction:


| Multi-company | Scheme enabled | Company listed | Deduction applied |
| :------------- | :-------------- | :-------------- | :----------------- |
| Off           | No             | n/a            | No                |
| Off           | Yes            | n/a            | Yes               |
| On            | No             | Any            | No                |
| On            | Yes            | Yes            | Yes               |
| On            | Yes            | No             | **No**            |


This applies to all four schemes and takes effect the next time a salary slip is created or saved. Salary slips already submitted are not altered. See [Removing a company](https://file+.vscode-resource.vscode-cdn.net/Users/deepesh/frappe/my-bench/apps/india_payroll/docs/setup/multi-company-payroll.md#removing-a-company) below.

One related behaviour: the Salary Structure Assignment warning about a missing **Employment State** is also scoped this way. Assignments for a company outside Professional Tax scope will not raise it.

## **How it changes reports**

The statutory registers (**Employee Provident Fund Register**, **ESIC Register** and **LWF Register**) follow the same scope, with one deliberate exception that protects filed records.

A salary slip appears in a register when **either**:

- its company is currently in scope for that scheme, **or**
- the slip **actually recorded** that deduction.

The second rule matters. A register is a record of liabilities that were incurred, not a projection of current configuration. If a company deducted ESI in June and you remove it from the table in September, the June contributions were still deducted from employees and remitted to ESIC, so they must remain reportable, and the June ECR file must still regenerate identically. The registers therefore never erase history when scope changes.

The practical effect of the two rules together:

- Slips from **before** a company was removed keep their deductions and stay reported.
- Slips created **after** removal carry no statutory deductions, so they drop out.

The **Bank Mandate Report** is not scoped, by design: it lists salary payment instructions, not statutory liabilities.

### **ECR export**

An ECR file is filed against a **single** EPF establishment code. Once codes are recorded per company, a file spanning several companies cannot be filed.

So while multi-company payroll is on, **Generate ECR File** requires a Company filter, and will show *"Select a Company before generating the ECR file"* if one is not set. In single-company mode, the filter stays optional, as before.

## **Validation**

Saving Payroll Settings enforces three rules:

- **A company may appear only once.** A duplicate is rejected, naming both row numbers.
- **Registration numbers are trimmed** of leading and trailing whitespace.
- **The table cannot be empty while multi-company payroll is on.** Without this, ticking the box would silently switch off every statutory deduction across the site.

## **Removing a company**

Removing a company's row stops it accruing new statutory deductions from the next salary slip onward. Its history is preserved: past slips keep the deductions they recorded, and those amounts continue to appear in the registers and the ECR export.

To also strip deductions from slips that are already **draft**, re-save them after removing the row. **Submitted** slips are unchanged. Amending a submitted slip to remove a statutory deduction is a payroll correction and should be done deliberately, not as a side effect of a settings change.

## **Turning it off**

Unticking **Enable Multi-Company Payroll** returns the site to a single shared configuration:

- The site-wide ESIC and EPF registration fields reappear, holding whatever they held before.
- Every company is back in scope for whichever schemes are enabled.
- The Company Payroll Settings rows are retained, so re-enabling restores your per-company details.

Check the site-wide registration numbers after switching back, since they are not populated from the table.

## **Developer reference**

`india_payroll/india_payroll/company_settings.py` is the single place that resolves statutory configuration. Use it rather than reading Payroll Settings fields directly, so behaviour stays consistent across schemes.

```python
from india_payroll.india_payroll.company_settings import (
    is_statutory_enabled,
    get_applicable_companies,
    get_registration_number,
)

```

`is_statutory_enabled(statute, company)` **→** `bool`

Whether a scheme applies to a company right now. This is the salary-slip gate. `statute` is one of `"professional_tax"`, `"esic"`, `"lwf"`, `"epf"`.

`get_applicable_companies(statute)` **→** `list[str] | None`

The company scope for a register. Three-valued, and the distinction matters:


| Return    | Meaning                                                                                                         |
| :--------- | :--------------------------------------------------------------------------------------------------------------- |
| `None`    | No restriction. Multi-company payroll is off, so reports behave exactly as they did before the feature existed. |
| `[]`      | Multi-company payroll is on but the scheme is globally disabled, so no company is currently in scope.           |
| `[names]` | Only these companies are currently in scope.                                                                    |


`None` is not the same as an empty list, and a caller that treats them alike will silently change single-company behaviour.

Because this returns *current* scope, never apply it as a bare filter to historical records. Combine it with evidence from the slip, as the registers do:

```python
applicable = get_applicable_companies("esic")
if applicable is not None:
    with_esi = get_slips_with_deduction([r.slip for r in rows], [ESI_EMPLOYEE_COMPONENT])
    rows = [r for r in rows if r.company in applicable or r.slip in with_esi]

```

`get_slips_with_deduction` lives in `india_payroll/india_payroll/utils.py`. It returns the subset of slips carrying a given deduction with a positive amount. Statutory deduction rows are only ever written when the amount is above zero, so a row's presence is the slip's own record that the liability was incurred, independent of how Payroll Settings is configured today.

`get_registration_number(statute, company)` **→** `str | None`

The registration identifier for a scheme. Reads the company's row when multi-company payroll is on, and falls back to the site-wide field otherwise.

## **Current limitations**

- **Registration numbers are stored but not yet consumed.** No report or export currently prints them: the ECR file format carries no header, and the ESIC Register has no registration column. The fields are in place so entities can be recorded correctly now, and so the values are available when those outputs are added.
- **No site-wide fallback for Professional Tax and LWF.** Those two registration numbers exist only on the per-company table. In single-company mode `get_registration_number` returns `None` for them.
- **Registers ignore the master switches in single-company mode.** With multi-company payroll off, the registers report computed liabilities regardless of whether the scheme's checkbox is ticked. This predates multi-company payroll and is unchanged by it.
- **TDS is configured separately.** Deductor details for Form 24Q (TAN, deductor type, responsible person) live on the Company record itself and were already per-company. They are not affected by this setting.

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

![](/files/image4a4563.webp)
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



![](/files/image2d5f45.webp)
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

![](/files/Screenshot 2026-07-09 at 15.33.52.webp)

## LWF Register

A state-wise Labour Welfare Fund deduction register showing each employee's deduction status for the selected month — whether LWF was deducted, it was a non-deduction month, the employee is exempted, or their state has no LWF. Use it to prepare the remittance challan for the State Labour Welfare Board.



![](/files/Screenshot 2026-07-09 at 15.31.46.webp)

## Bank Mandate Report

Lists each employee's net pay alongside their bank details (account number, IFSC, MICR, payment mode). Hand this to your bank or upload it to your ECS/NEFT batch processing system for salary disbursement.



![](/files/Screenshot 2026-07-09 at 15.35.35.webp)

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



![](/files/Screenshot 2026-07-03 at 12.28.05.webp)

## 1. How to select a tax regime

To compare regimes and save a choice for an employee:

- Open the Tax Regime Selector. The Payroll Period is set to the active period for the company and the Employee defaults to the logged-in user. HR users can select any employee.
- Confirm the Annual Gross Earning. It is fetched from the employee's latest Salary Structure Assignment and can be edited.
- Enter the employee's declarations in the table below.
- Review the comparison shown on the right. The recommended regime and the resulting saving are highlighted.
- Select a regime and click Save Regime in the toolbar.

![](/files/tax-select-docs.mp4)

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



![](/files/tax-email.mp4)



## 3. Declaring tax exemptions

The declarations entered in the tool are used for the comparison only; they are not saved on their own. To record them as the employee's official declaration, click Declare Tax Exemptions

This opens a new Employee Tax Exemption Declaration, prefilled with:

- Selected employee and payroll period,
- Monthly rent and metro-city flag, if the salary structure includes HRA,
- Row for each declared sub-category and its amount.



![](/files/declare.mp4)

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
