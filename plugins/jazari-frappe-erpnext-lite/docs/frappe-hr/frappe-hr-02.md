<!-- Frappe documentation: frappe-hr, part 2 of 3. Index: docs/INDEX.md -->

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

![](https://frappehr.com/files/Qg0MQwo.png)  


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

![](https://frappehr.com/files/RgZapW8.png)
7. Save

![135508716-5c416fef-7ceb-44b4-b0f4-4994f8a8a4a1](https://frappehr.com/files/135508716-5c416fef-7ceb-44b4-b0f4-4994f8a8a4a1.png "135508716-5c416fef-7ceb-44b4-b0f4-4994f8a8a4a1.png")  


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

![image](https://user-images.githubusercontent.com/24353136/135508652-94fbd439-f953-423c-ba10-990067f308c4.png)  


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

![](https://frappehr.com/files/wNX9smG.png)  


After saving the Interview, you can reschedule the interview using the Reschedule Interview button. You can also directly [Submit Feedback](https://docs.frappe.io/hr/interview-feedback) from the dashboard.

> **Note:** Only Interviewers associated with the selected [Interview Round](https://docs.frappe.io/hr/interview-round) can submit Feedback.

**3. Features**
---------------

### **3.1 Calendar View**

Scheduled interviews can be viewed in a color-coded calendar format by going to the Interview list, clicking on List View, and selecting Calendar.

![image](https://user-images.githubusercontent.com/24353136/135509119-e9584525-7c4e-4384-ab1f-d32e605fcde5.png)  


### **3.2 Interview Feedback**

After an interview has received [Feedback](https://docs.frappe.io/hr/interview-feedback), you can click on the Feedback tab to access a summary of the feedback. This summary includes the overall average rating, the distribution of ratings for each Feedback, the average rating for each Skill, and the individual Feedback comments.

![](https://frappehr.com/files/T7SxrmG.png)  


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

  

<!-- page: frappe-hr/hr__introduction.md -->
---
title: "Frappe HR"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/introduction"
updated: "2026-02-04"
---

Frappe HR is an open Source, modern, and easy-to-use HR and Payroll Software for all organizations. It has everything you need to drive excellence within the company. It is a complete HRMS solution with over 13 different modules right from Employee Management, Onboarding, Leaves, to Payroll, Taxation, and more!

![](/files/imagee5004c.png)

## Why Frappe HR

Businesses often struggle with scattered HR processes, manual payroll calculations, disconnected employee records, and time-consuming approvals.

- Frappe HR brings everything under one roof so HR teams can focus on people, not paperwork.
- Built for organizations that need a flexible and cost-effective solution, Frappe HR eliminates inefficiencies, ensures compliance, and gives employees a seamless experience. 
- Whether you are managing a handful of employees or scaling to thousands, it helps you stay organized without getting bogged down in administrative overhead.

## Key Features

- **Employee Lifecycle**: From onboarding employees, managing promotions and transfers, all the way to documenting feedback with exit interviews, make life easier for employees throughout their life cycle.
- **Leave and Attendance**: Configure leave policies, pull regional holidays with a click, check-in and check-out with geolocation capturing, track leave balances and attendance with reports.
- **Expense Claims and Advances**: Manage employee advances, claim expenses, configure multi-level approval workflows, all this with seamless integration with ERPNext accounting.
- **Performance Management**: Track goals, align goals with key result areas (KRAs), enable employees to evaluate themselves, make managing appraisal cycles easy.
- **Payroll & Taxation**: Create salary structures, configure income tax slabs, run standard payroll, accomodate additional salaries and off cycle payments, view income breakup on salary slips and so much more.
- **Frappe HR Mobile App**: Apply for and approve leaves on the go, check-in and check-out, access employee profile right from the mobile app.

And more.

## Under the Hood

- **[Frappe Framework](https://github.com/frappe/frappe)**: A full-stack web application framework written in Python and Javascript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.
- **[Frappe UI](https://github.com/frappe/frappe-ui)**: A Vue-based UI library, to provide a modern user interface. The Frappe UI library provides a variety of components that can be used to build single-page applications on top of the Frappe Framework.

## Installation

To install/setup the app, follow the [guidelines here](https://github.com/frappe/hrms/?tab=readme-ov-file#production-setup).

### Learning and Community

1. [Frappe School](https://frappe.school) - Learn Frappe Framework and ERPNext from the various courses by the maintainers or from the community.
2. [Documentation](https://docs.frappe.io/hr) - Extensive documentation for Frappe HR.
3. [User Forum](https://discuss.erpnext.com/) - Engage with the community of ERPNext users and service providers.
4. [Telegram Group](https://t.me/frappehr) - Get instant help from the community of users.

<!-- page: frappe-hr/hr__job-applicant.md -->
---
title: "Job Applicant"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/job-applicant"
updated: "2026-02-04"
---

**A Job Applicant is a person who applies for a job in your Company against a particular Job Opening.**

In Frappe HR, you can maintain a list of people who have applied against a particular [Job Opening](https://docs.frappe.io/hr/job-opening).

To create a Job Applicant, go to:

> Home > Human Resource > Recruitment > Job Applicant

**1. Prerequisites**
--------------------

Before creating a Job Applicant, it is advisable you create the following:

* [Staffing Plan](https://docs.frappe.io/hr/staffing-plan)
* [Department](https://docs.frappe.io/hr/department)
* [Job Opening](https://docs.frappe.io/hr/job-opening)

**2. How to Create a Job Applicant**
------------------------------------

1. Go to Job Applicant list, click on New.
2. Enter Applicant Name and Email Address.
3. Select Job Opening.
4. Select Source (Campaign, Employee Referral, Walk In, Website Listing).

> **Note:** If you select the Source as Employee Referral, you will have to select the Employee name in the Source Name Field.

![Job Applicant](https://frappehr.com/files/job-applicant.png)  


**3. Features**
---------------

### **3.1 Linking with an Email Account**

You can link Job Application with an Email account. Suppose you link Job Application with an email [job@example.com](mailto:job@example.com), the system will create a New Job Applicant against each email received on the mailbox.

* To link Email Account with Job Applicant, go to:

> Settings > Email Account > New Email Account

* Enter the Email Address and the password, and select 'Enable Incoming'
* In 'Append To' select 'Job Applicant'

![Email Account](https://frappehr.com/files/email-account.png)  


### **3.2 Tracking Interviews**

After creating [Interviews](https://docs.frappe.io/hr/interview), you can easily track them within the Job Applicant dashboard. This enables you to compare all the interviews conducted with the applicant and evaluate their overall performance to make an acceptance decision.

![image](https://user-images.githubusercontent.com/24353136/135509483-97c4f78b-66a4-4a7a-b86f-37f20cf86956.png)  


**4. Related Topics**
---------------------

1. [Interview](https://docs.frappe.io/hr/interview)
2. [Job Offer](https://docs.frappe.io/hr/job-offer)
3. [Employee](https://docs.frappe.io/hr/employee)

  

<!-- page: frappe-hr/hr__job-offer.md -->
---
title: "Job Offer"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/job-offer"
updated: "2026-02-04"
---

**Job Offer is given to selected candidates after interview and selection which states the offered salary package, designation, grade, department, number of days entitled for leave among other information.**

In Frappe HR you can make a record of the Job Offers that you can give to candidates. To access Job Offer, go to:

> Home > Human Resource > Recruitment > Job Offer

**1. Prerequisites**
--------------------

Before creating a Job Offer, it is advisable to create the following:

* [Staffing Plan](https://docs.frappe.io/hr/staffing-plan)
* [Job Applicant](https://docs.frappe.io/hr/job-applicant)
* [Job Opening](https://docs.frappe.io/hr/job-opening)

**2. How to Create a Job Offer**
--------------------------------

1. Go to Job Offer list, click on New.
2. Select the Job Applicant, Offer Date and Designation.
3. Set the Status of the Job Offer (Awaiting Response, Accepted, Rejected).
4. Save and Submit.

![Job Offer](https://frappehr.com/files/job-offer.png)

> **Note:** A Job Offer can be made only against a [Job Applicant](https://docs.frappe.io/hr/job-applicant)

**3. Features**
---------------

### **3.1 Job Offer Terms**

In this section, you can enter the Job Offer Term such as job description, notice period, incentives, leaves per year, etc. and specify its Value/ Description.

### **3.2 Select Terms and Conditions**

All the Terms and Conditions related to the Job Offer can be specified in this section. To do this, create a new Terms and Conditions template and link it to the Job Offer.

### **3.3 Printing Details**

You can create a pre-designed print format to print you Job Offer. To do so, select the Letter Head and Print Heading in the Printing Details section.

![Job Offer](https://frappehr.com/files/job-offer-print.png)  


  

<!-- page: frappe-hr/hr__job-opening.md -->
---
title: "Job Opening"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/job-opening"
updated: "2026-08-10"
---

**A Job Opening is a job vacancy in your Company. You can make a record of the open vacancies in your company using Job Opening.**



Frappe HR allows to plan recruitment for your company. The number of Job Openings you can create for a Designation is restricted according to the vacancies planned by the Staffing Plan defined for the company or one of its parent group companies in the hierarchy.

:::note
Make sure the "Check Vacancies On Job Offer Creation" checkbox is checked in the Hiring Settings section of the HR Settings.
:::



To access Job Opening, go to:

> Home &gt; Human Resource &gt; Recruitment &gt; Job Opening

## **1. Prerequisites**

Before creating a Job Opening, it is advisable you create the following:

- [Staffing Plan](https://docs.frappe.io/hr/staffing-plan)
- [Department](https://docs.frappe.io/hr/department)

## **2. How to create a Job Opening**

1. Go to Job Opening list, click on New.
2. Enter the Job Title.
3. Select the Designation and Department. Based on Designation selected, appropriate Staffing Plan and Planned Number of Positions will be fetched.
4. Save.

![](/files/Screenshot From 2026-08-10 14-16-21.webp)
*You can also use Job Opening Template to populate the common fields*

Once the Job Opening is saved, you can directly create a new [Job Applicant](https://docs.frappe.io/hr/job-opening) from the dashboard.

:::note
You can close/reopen a Job Opening as and when required. Once a Job Opening is Closed, you cannot create a Job Applicant against it.
:::



## **3. Features**

### **3.1 Job Portal**

You can enable 'Publish on website' to publish a Job Opening to the [Job Portal](https://docs.frappe.io/hr/job-portal). This will make it possible for users to view and apply to these openings from your site.

![](/files/Screenshot From 2026-08-10 14-24-20.webp)

## **4. Related Topics**

1. [Job Applicant](https://docs.frappe.io/hr/job-applicant)
2. [Job Offer](https://docs.frappe.io/hr/job-offer)

Frappe HR allows to plan your recruitment at a group company level. The number of Job Openings you can create for a Designation is restricted according to the Vacancies planned by the Staffing Plan defined for the company or one of it's parent group companies in the hierarchy. To understand how you can do configure this, check [Staffing Plan](https://docs.frappe.io/hr/staffing-plan)

<!-- page: frappe-hr/hr__job-portal.md -->
---
title: "Job Portal"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/job-portal"
updated: "2026-02-04"
---

**The Job Portal provides an interface for applicants to browse and apply to published Job Openings.**

**1. Prerequisites**
--------------------

Before using the Job Portal, it is advisable you create the following:

* [Job Opening](https://docs.frappe.io/hr/job-opening)


> **Note: For an opening to be visible on the Job Portal, you must enable the 'Publish on website' field for that specific Job Opening.**
> 
> 

**2. How to Apply Using the Job Portal**
----------------------------------------

1. To visit the Job Portal, go to https://<sitename>/jobs. For example, if my site name is <https://frappeio.frappe.cloud>, the Job Portal can be accessed from <https://frappeio.frappe.cloud/jobs>

  


![273578470-fdc33ca4-12b1-49e6-958c-6d627faee6fc](https://frappehr.com/files/273578470-fdc33ca4-12b1-49e6-958c-6d627faee6fc.png "273578470-fdc33ca4-12b1-49e6-958c-6d627faee6fc.png")
2. You can use the search bar to search for jobs by title or description. You can also filter jobs by company, department, location, or employment type, and sort them by the latest or oldest posting date.
3. Click on a job card to view it in detail.

  


![](https://frappehr.com/files/0CTCsNp.png)
4. Click on the 'Apply Now' button at the top-right corner. This will open a web form where applicants can enter their details.

  


![](https://frappehr.com/files/tyfAC5s.png)
5. Fill in the appropriate details and click on Submit. This will result in the creation of the corresponding Job Applicant document.

  


![](https://frappehr.com/files/xj3PDmO.png)

**3. Related Topics**
---------------------

1. [Job Applicant](https://docs.frappe.io/hr/job-applicant)
2. [Interview Management](https://docs.frappe.io/hr/interview-management)

  

<!-- page: frappe-hr/hr__job-requisition.md -->
---
title: "Job Requisition"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/job-requisition"
updated: "2026-02-04"
---

Job Requisition is an internal document raised to request a new hire. These requisitions are then converted to Job Openings or considered for budgeting while making the Staffing Plan.

To access Job Requisition, go to:


> **Home > Human Resources > Recruitment > Job Requisition**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Job Requisition, you should create the following:

* [Designation](https://docs.frappe.io/hr/designation)
* [Department](https://docs.frappe.io/hr/department) (Optional)

**2. How to create a Job Requisition**
--------------------------------------

1. Go to the Job Requisition list, and click on New.
2. Enter the Designation you want to place the request for.
3. Enter the No of Positions, Expected Compensation, Company, and Department (optional).
4. Select the employee who is applying for the requisition in the Requested By field.
5. Optionally, you can set the **Expected By** date.
6. The Job Description will be fetched from the Designation. If you want to add additional information for the opening, you can do so here.
7. Save.
8. By default, the status will be Pending. You can set up [workflows](https://docs.erpnext.com/docs/v14/user/manual/en/setting-up/workflows) to change the status to Open & Approved.

![Job Requisition](https://frappehr.com/files/job_req.png)  


![Job Requisition List](https://frappehr.com/files/job_req_list.png)

**3. Actions**
--------------

### **3.1 Create Job Opening**

Once the Job Requisition is **Open & Approved**, you can create a new Job Opening against the Job Requisition or associate an existing one.

![create job opening](https://frappehr.com/files/create-job-openingafcb2d.gif)  


### **3.2 Associate Job Opening**

If you already have an existing Open Job Opening for that designation, you can associate it with the requisition.

![Associate Job Opening](https://frappehr.com/files/associate-job-opening.gif)  


Once the Job Opening is closed, the Job Requisition's status is updated to **Filled**

**4. Features**
---------------

### **4.1 Check existing Employee Referrals**

If there is an existing Employee Referral for that designation, you might want to consider referrals instead of creating new openings. A banner is visible on the Job Requisition form with the links to these employee referrals in these cases.

![employee referral](https://frappehr.com/files/employee-referral.png)  


### **4.2 Get Job Requisitions in Staffing Plan**

While creating a budget with the Staffing Plan, you can fetch the existing **Pending** or **Open & Approved** Job Requisitions.

![Get Job Requisition](https://frappehr.com/files/get-job-req8e955b.gif)  


### **4.3 Time to Fill Metric**

Time to Fill measures the number of days it takes to fill an open position, from the date a job requisition is posted to the date when it is marked as Filled. This metric is auto-calculated and set in Job Requisition.

The Average Time to Fill is also displayed on the Hiring Dashboard:

![time to fill](https://frappehr.com/files/time-to-fill.png)  


**5. Related Topics**
---------------------

1. [Job Opening](https://docs.frappe.io/hr/job-opening)
2. [Staffing Plan](https://docs.frappe.io/hr/staffing-plan)

  

<!-- page: frappe-hr/hr__leave-allocation-after-compensatory-leave-request.md -->
---
title: "Leave allocation after Compensatory Leave Request"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-allocation-after-compensatory-leave-request"
updated: "2026-02-04"
---

**Use case:** If an employee works on a Holiday and wants to apply for a compensatory off, the following process is important in Frappe HR:

1) Create an **Employee** with the mandatory details and assign a **Holiday List** and a **Leave Policy** to it.

2) Attendance should be marked for the Employee, it is mandatory for the employee to be marked as present on the Holiday [this Holiday should be in the Holiday List.]

![](https://docs.erpnext.com/files/9NHbSR1.png)  


3) Create a **Leave allocation** for the **Employee**.

4) In the **Leave Type list**, for all the types that allow Compensatory off, tick the checkbox.

![](https://docs.erpnext.com/files/zO860kS.png)  


5) Now, create a **Compensatory Leave Request** for the employee.

![](https://docs.erpnext.com/files/QuIeV7V.png)  


6) Go back and check the **Leave allocation** for the leave added for the Employee.

![](https://docs.erpnext.com/files/PstYtuX.png)

<!-- page: frappe-hr/hr__leave-allocation.md -->
---
title: "Leave Allocation"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-allocation"
updated: "2026-02-26"
---

**Leave Allocation enables you to allocate a specific number of leaves of a particular type to an Employee.**

To access Leave Allocation, go to:

> Home > Human Resources > Leaves > Leave Allocation

**1. Prerequisites**
--------------------

Before creating a Leave Allocation, it is advisable you create the following documents:

* [Employee](https://docs.frappe.io/hr/employee)
* [Leave Type](https://docs.frappe.io/hr/leave-type)
* [Leave Period](https://docs.frappe.io/hr/leave-period)
* [Leave Policy](https://docs.frappe.io/hr/leave-policy)

**2. How to create a Leave Allocation**
---------------------------------------

1. Go to Leave Allocation list, click on New.
2. Select the Employee, Leave Type, From Date and To Date.
3. Enter the number of New Leaves Allocated for that particular Leave Type.
4. Save and Submit.

![Leave Allocation](https://frappehr.com/files/leave-allocation.png)

> **Note:** Enable the 'Add unused leaves from previous allocations' option in case you want to carry forward unused leaves from the previous allocation period for this particular Leave Type.


**3. Features**
---------------------------------------

### 1. Manually adding leaves to the current allocation

If your earned leave allocation failed due to some reasons like background jobs weren’t running, you can manually allocate leaves for an allocation

Click on **Actions > Allocate Leaves**

![Allocate Leaves Button](/files/allocate.png)

And set the number of leaves you want to allocate. You can also set the **From Date** from when these leaves will be applicable. By default, it will consider today’s date.

![Manual Leave Allocation](/files/manual-allocation.png)

Click on allocate to add leaves to the balance

**4. Related Topics**
---------------------

1. [Leave Application](https://docs.frappe.io/hr/leave-application)
2. [Compensatory Leave Request](https://docs.frappe.io/hr/compensatory-leave-request)
3. [Leave Encashment](https://docs.frappe.io/hr/leave-encashment)
4. [Leave Block List](https://docs.frappe.io/hr/leave-block-list)
5. [Holiday List](https://docs.frappe.io/hr/holiday-list)

<!-- page: frappe-hr/hr__leave-application.md -->
---
title: "Leave Application"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-application"
updated: "2026-02-04"
---

**Leave Application is a formal document created by an Employee to apply for Leaves for a particular time period.**

Frappe HR allows your employees to apply for leaves via Leave Applications and get them approved by the Leave Approvers.

To access Leave Application, go to:


> **Home > Human Resources > Leaves > Leave Application**
> 
> 

**1. Prerequisites**
--------------------

Before you create a Leave Application, it is advisable you have the following documents:

* [Department](https://docs.frappe.io/hr/department)
* [Leave Period](https://docs.frappe.io/hr/leave-period)
* [Holiday List](https://docs.frappe.io/hr/holiday-list)
* [Leave Type](https://docs.frappe.io/hr/leave-type)
* [Leave Policy](https://docs.frappe.io/hr/leave-policy)
* [Leave Allocation](https://docs.frappe.io/hr/leave-allocation)

**2. How to create a Leave Application**
----------------------------------------

1. Go to Leave Application list, click on New.
2. A table of Allocated Leaves will be shown. Based on the Leaves taken, the available leaves are displayed for each Leave Type.

![Leave Application](https://frappehr.com/files/leave-app.png)
3. Select the Employee Name and Leave Type.
4. Set the Leave duration using From Date and To Date. Based on the dates selected, the 'Total Leave Days' and the 'Leave Balance Before Application' fields will be displayed.
5. If the Leave applied is for a half-day, select the 'Half Day' checkbox.
6. Enter the Reason for Leave.

![Leave Application](https://frappehr.com/files/leave-app1.png)
7. Select Leave Approver.
8. Select the Posting Date of the Leave Application.
9. Check the 'Follow via Email' checkbox to send notification of the Leave Application to the Leave Approver.
10. You can also link the Salary Slip of the Employee in the Leave Application for the record.

![Leave Application](https://frappehr.com/files/leave-app3.png)
11. Click on Save. Once the Employee saves the Leave Application, the status of the Leave Application changes to 'Open', and an email is sent to the Leave Approver for approval. The Leave Approval Notification Template can be configured in [HR Settings](https://docs.frappe.io/hr/hr-settings) under the Leave Settings section.
12. Once the Leave Approver receives the email, they can Approve, Reject, or Cancel the Leave Application. Once this is done, the Leave Approver can submit the Leave Application. On submission, the status of the document changes accordingly, and an email is sent to the Employee notifying them the same.


> **Note: Leave Application cannot be submitted if the Salary is already processed for the leave period.**
> 
> 

The Leave Application process flow is summarized below:

* The employee applies for leave through Leave Application.
* Approver gets notification via email. For this, the "Follow via Email" checkbox should be checked.
* Approver reviews Leave Application.
* Approver approves/rejects/cancels Leave Application
* The employee gets the notification on the status of his/her Leave Application

**3. Features**
---------------

### **3.1 Setting Leave Approver**

A leave approver is a user who can approve a Leave Application of an Employee. In Frappe HR version 12, Leave Approvers can be set at two levels:

* **Department Level:** Leave Approvers for each department can be configured in the [Department](https://docs.frappe.io/hr/department) master. Multiple Leave Approvers can be set in a Department. The first Leave Approver in the list will be considered as the default Leave Approver.

![Leave Application - Leave Approvers](https://frappehr.com/files/leave-app4.png)  


When an Employee belonging to a particular department applies for leave, the Leave Approvers set in that Employee's department master will be considered as his Leave Approvers.
* **Employee Level:** Leave Approvers can also be set Employee-wise in the employee master.

![Leave Application - Leave Approvers](https://frappehr.com/files/employee-level-approvers.png)

If Leave Approvers are set at both Employee-level and Department-level, the Employee-level Leave Approver will be considered as the default Leave Approver in this case.

When a new Leave Application is created, if the selected leave approver does not have access to it, the document is shared with the approver with "submit" permission.

**Tip:** If you want all users to create their own Leave Applications, you can set their “Employee ID” as a match rule in the Leave Application Permission settings. Check [Setting Up Permissions](https://docs.erpnext.com/docs/v144/user/manual/en/setting-up/users-and-permissions/user-permissions) for more information.


> **Additional Notes:**
> 
> 


> * **Leave Application period must be within a single Leave Allocation period. In case, you are applying for leave across the leave allocation period, you have to create two Leave Application records.**
> * **Leave Application period must be in the latest Leave Allocation period.**
> * **Employee cannot apply for leave on the dates which are added in the** [**Leave Block List**](https://docs.frappe.io/hr/leave-block-list)**.**
> 

To understand how Frappe HR allows you configure leaves for employees, check [Leaves](https://docs.frappe.io/hr/leave-management-intro/).

**3. Related Topics**
---------------------

1. [Leave Type](https://docs.frappe.io/hr/leave-type)
2. [Leave Period](https://docs.frappe.io/hr/leave-period)
3. [Leave Policy](https://docs.frappe.io/hr/leave-policy)
4. [Leave Allocation](https://docs.frappe.io/hr/leave-allocation)
5. [Leave Block List](https://docs.frappe.io/hr/leave-block-list)

  

<!-- page: frappe-hr/hr__leave-block-list.md -->
---
title: "Leave Block List"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-block-list"
updated: "2026-02-04"
---

**Leave Block List is a list of dates in a year, on which employees cannot apply for leave.**

To access Leave Block List, go to:

> Home > Human Resources > Leaves > Leave Block List

Frappe HR allows you to define a list of Leave Approvers who can approve Leave Applications on blocked days, in case of urgency. You can also define whether the list will be applied to the entire company or on any specific departments.

**1. Prerequisites**
--------------------

Before you create a Leave Block List, it is advisable you have the following documents:

* [Company](https://docs.erpnext.com/docs/user/manual/en/company-setup)
* [Department](https://docs.frappe.io/hr/department)
* [Leave Period](https://docs.frappe.io/hr/leave-period)
* [Holiday List](https://docs.frappe.io/hr/holiday-list)

**2. How to create a Leave Block List**
---------------------------------------

1. Go to Leave Block list, and click on New.
2. Enter Leave Block List Name.
3. Enter Block Date and Reason in the 'Leave Block List Dates' table.
4. Enter Users to approve Leave Applications for Blocked Days in the 'Leave BLock List Allowed' table.
5. Save.

![Leave Block List](https://frappehr.com/files/leave-block-list.png)

> **Note:** Enable the 'Applies to Company' option if you want the Leave Block List to be applicable for the entire Company. If not checked, the list will have to be added to each [Department](https://docs.frappe.io/hr/department) where it has to be applied.

**3. Related Topics**
---------------------

1. [Leave Type](https://docs.frappe.io/hr/leave-type)
2. [Leave Period](https://docs.frappe.io/hr/leave-period)
3. [Leave Policy](https://docs.frappe.io/hr/leave-policy)
4. [Leave Allocation](https://docs.frappe.io/hr/leave-allocation)
5. [Leave Application](https://docs.frappe.io/hr/leave-application)

  

<!-- page: frappe-hr/hr__leave-calculation-in-salary-slip.md -->
---
title: "Leave Calculation In Salary Slip"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-calculation-in-salary-slip"
updated: "2026-02-04"
---

There are two types of leave which user can apply for.

* Paid Leave (Sick Leave, Privilege Leave, Casual Leave etc.)
* Unpaid Leave

Paid Leave are firstly allocated by HR manager. As and when Employee creates Leave Application, leaves allocated to him/her are deducted. These leaves doesn't have impact on the employee's Salary Slip.

When Employee is out of paid leave, he create Leave Application for unpaid leave. The term used for unpaid leave in Frappe HR is Leave Without Pay (LWP). These leaves does have impact on the Employee's Salary Slip.

Just marking Absent in the Attendance record do not have impact on salary calculation of an Employee, as that absenteeism could be because of paid leave. Hence creating Leave Application should be created incase of absenteeism. Let's consider a scenario to understand how leaves impact employees Salary Slip. 1. Setup Employee 1. Allocate him paid leaves 1. Create Salary Structure for that Employee. In the Earning and Deduction table, select which component of salary should be affected if Employee takes LWP. 1. Create Holiday List (if any), and link it with Employee master. **Working Days:** Working Days in Salary Slip are calculated based on number of days selected above. If you don't wish to consider holiday in Working Days, then you should do following setting. > Human Resource > Setup > HR Setting Uncheck field "Include Holidays in Total No. of Working Days" Holidays are counted based on Holiday List attached to the Employee's master. **Leave Without Pay:** Leave Without Pay is updated based on Leave Application made for this Employee, in the month for which Salary Slip is created, and which has Leave Type as "Leave Without Pay". Payment Days: Following is how Payment Days are calculated: Payment Days = Working Days - Leave Without Pay If you have LWP checked for the Salary Component, there will be reduction in Amount based on no. of LWP of an Employee for that month.

<!-- page: frappe-hr/hr__leave-control-panel.md -->
---
title: "Leave Control Panel"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-control-panel"
updated: "2026-02-04"
---

The Leave Control Panel allows you to allocate leaves in bulk based on a specific Leave Policy or Leave Type.


> **Home > Human Resources > Leaves > Leave Control Panel**
> 
> 

**1. Prerequisites**
--------------------

Before using the Leave Control Panel, it is advisable to create the following documents:

* [Employee](https://docs.frappe.io/hr/employee)
* [Leave Period](https://docs.frappe.io/hr/leave-period) (optional)
* [Leave Policy](https://docs.frappe.io/hr/leave-policy) / [Leave Type](https://docs.frappe.io/hr/leave-type)

**2. How to allocate leave using the Leave Control Panel**
----------------------------------------------------------

1. Choose the appropriate option from Dates Based On and fill in the corresponding data. This would include Leave Period or From Date and/or To Date.
2. If you wish to assign a Leave Policy, select the intended one. Alternatively, you can allocate leave directly by disabling Allocate Based On Leave Policy, selecting the desired Leave Type, and filling in the corresponding number of New Leaves Allocated.
3. Select Carry Forward if you wish to add unused leaves from the previous allocation into this one.
4. Use Quick Filters for filtering employees based on specific fields, or add additional custom filters through Advanced Filters.
5. Select suitable employees from the Select Employees table below and click on the Allocate Leave button at the top right corner.

![](https://frappehr.com/files/dZbeNka.png)  



> **Note: Leave cannot be allocated for past dates.**
> 
> 

[Leave Policy Assignments](https://docs.frappe.io/hr/leave-policy-assignment) and [Leave Allocations](https://docs.frappe.io/hr/leave-allocation) made using the Leave Control Panel are reflected in their respective DocTypes as shown below:

* Leave Policy Assignment

![](https://frappehr.com/files/91LxRtw.png)  


* Leave Allocation

![](https://frappehr.com/files/2fi9z2Z.png)  

<!-- page: frappe-hr/hr__leave-encashment.md -->
---
title: "Leave Encashment                                          "
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-encashment"
updated: "2026-02-04"
---

**Leave Encashment refers to an amount of money received in exchange for Leaves not availed by an Employee. You can submit Leave Encashment for Leave Types which are encashable.**

To access Leave Encashment, go to:

> Home > Human Resources > Leaves > Leave Encashment

**1. Prerequisites**
--------------------

Before creating Leave Encashment, it is advisable you create the following documents:

1. [Employee](https://docs.frappe.io/hr/leave-allocation)
2. [Leave Type](https://docs.frappe.io/hr/leave-type)
3. [Leave Policy](https://docs.frappe.io/hr/leave-policy)
4. [Leave Period](https://docs.frappe.io/hr/leave-period)
5. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
6. [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)

**2. How to create a Leave Encashment**
---------------------------------------

1. Go to Leave Encashment list, click on New.
2. Select Leave Period.
3. Select the Employee. Once the Employee is selected, the Employee's Department is automatically fetched.
4. Select Leave Type for which the Leave is encashed. Make sure the Leave Type is encashable (the 'Allow Encashment' checkbox in the Leave Type is checked).
5. Select Encashment Date, if you want payment via Salary Slip. Based on the date selected, the amount will be encashed in that particular Payroll Entry.
6. Save and Submit.

![Leave Encashment](https://frappehr.com/files/leave-encashment-new.png)

> **Note:** As you select Employee and Leave Type, Leave Balance and Encashable Days (which is total leave balance minus the threshold days set in Leave Type) will be shown along with the Encashment Amount based on the Leave Encashment per day as configured in the Employee's assigned Salary Structure.

**3. Leave Encashment Payment Methods**
---------------------------------------

In Frappe HR, we allow you to pay the encashment amount via Salary Slip or Payment Entry.

### **3.1 Payment via Payment Entry**

1. To pay the Leave Encashment amount via Payment Entry you need to check Pay via Payment Entry checkbox. 
2. After that, it will allow you to select Payable Account and Expense Account. 
3. After Submitting the record click on the button "Create Payment Entry" which will redirect you to the Payment Entry Form fill in the details, save, and submit.

### **3.2 Payment via Salary Slip**

1. To pay the Leave Encashment amount via Salary Slip you need to make sure that checkbox Pay via Payment Entry is unchecked.
2. Select the Encashment Date. Based on the date selected, the amount will be encashed in that particular Payroll Entry. Save and Submit. 
On submitting a Leave Encashment for an Employee, Frappe HR automatically creates an [Additional Salary](https://docs.frappe.io/hr/additional-salary) which will get added to the Salary Slip of the Employee when processing the payroll.


**3. Related Topics**
---------------------

1. [Payroll Period](https://docs.frappe.io/hr/payroll-period)
2. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)
3. [Additional Salary](https://docs.frappe.io/hr/additional-salary)

  

<!-- page: frappe-hr/hr__leave-ledger-entry.md -->
---
title: "Leave Ledger Entry"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-ledger-entry"
updated: "2026-02-26"
---

A unified ledger for all leave related transactions for an employee. This maintains all the leaves related transactions, this includes the leave allocations, leave applications and leave encashments of your employees.

![Leave Ledger Entry](https://frappehr.com/files/leave-ledger-entry.png)  


  

<!-- page: frappe-hr/hr__leave-ledger-report.md -->
---
title: "Leave Ledger Report"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-ledger-report"
updated: "2026-02-26"
---

This report allows you to view the ledger impact for all your leave-related transactions:

1. Leave Allocation
2. Leave Application
3. Leave Encashment

![ledger-report](https://frappehr.com/files/ledger-report.png "ledger-report.png")  


This report gives you an overview of:

1. Ledger entry creation date
2. Ledger transaction dates (From Date - To Date)
3. Leaves (added/consumed/deducted)
4. Leave Type
5. Linked transaction details (Type & Name)
6. Any special flags: Is Carry Forward, Is Expired, Is Leave Without Pay
7. Company & Holiday List linked to it

You can use the **View Ledger** button in transactions to view the linked ledger entries in the report view

![leave-ledger](https://frappehr.com/files/leave-ledger.gif "leave-ledger.gif")  


  

<!-- page: frappe-hr/hr__leave-management__help-articles__how-to-sanction-leave-encashment-amount-in-salary-slip.md -->
---
title: "How to Sanction Leave Encashment Amount in Salary Slip"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-management/help-articles/how-to-sanction-leave-encashment-amount-in-salary-slip"
updated: "2026-07-05"
---

Leave Encashment is used to pay an employee for unused leaves. In Frappe HR, this amount can be paid through a **Salary Slip** or through a separate **Payment Entry**.

This article explains how to sanction the leave encashment amount through Salary Slip.

## When To Use This

Use this method when the encashment amount should be paid along with the employee's regular payroll.

For example, if an employee has unused earned leaves at the end of the year, you can create a Leave Encashment record and include the encashment amount in the employee's Salary Slip for that payroll period.

## Prerequisites

Before creating Leave Encashment, make sure the following are configured:

- The employee has an active **Salary Structure Assignment**.
- The **Leave Type** is marked as encashable.
- The Leave Type has an **Earning Component** set for encashment.
- The employee has a submitted **Leave Allocation** for that Leave Type.
- The employee has unused leave balance available for encashment.
- The per-day encashment amount is set in the Salary Structure or Salary Structure Assignment.

## Step 1: Enable Encashment In Leave Type

Open the relevant **Leave Type** and enable **Allow Encashment**.

You can also configure limits such as:

- Non-encashable leaves
- Maximum encashable leaves
- Earning Component

The Earning Component is important because it decides which salary component will be used when the encashment amount is added to payroll.

## Step 2: Set Leave Encashment Amount Per Day

Open the employee's **Salary Structure** or **Salary Structure Assignment** and set the leave encashment amount per day.

Frappe HR uses this amount to calculate:

```text
Encashment Amount = Encashment Days x Leave Encashment Amount Per Day
```

If the per-day amount is not set, the encashment amount may be calculated as zero.

## Step 3: Create Leave Encashment

Go to:

```text
Home > Human Resources > Leaves > Leave Encashment
```

Create a new Leave Encashment record and select:

- Leave Period
- Employee
- Leave Type
- Encashment Date

The system fetches the employee's leave balance and calculates the encashable days and encashment amount.

## Step 4: Pay Through Salary Slip

To pay the amount through Salary Slip, keep **Pay Via Payment Entry** unchecked.

When the Leave Encashment is submitted, Frappe HR creates an **Additional Salary** record for the employee. This Additional Salary record is linked to the Leave Encashment and uses the earning component selected in the Leave Type.

## Step 5: Process Payroll

Create the **Payroll Entry** or **Salary Slip** for the payroll period that includes the encashment date.

When the Salary Slip is created, the Additional Salary from the Leave Encashment is included in the employee's earnings.

Review the Salary Slip and check that:

- The encashment earning component is visible.
- The amount is correct.
- The total earnings include the encashment amount.

Submit the Salary Slip to sanction and pay the amount through payroll.

## Example

An employee has 5 earned leaves available for encashment.

The leave encashment amount per day is set to 1,000.

```text
5 x 1,000 = 5,000
```

When the Leave Encashment is submitted, Frappe HR creates an Additional Salary for 5,000. The amount is then added to the Salary Slip for the payroll period that includes the encashment date.

## Common Checks

If the encashment amount is not appearing in the Salary Slip, check the following:

- The Leave Encashment is submitted.
- **Pay Via Payment Entry** is not checked.
- The encashment date falls within the Salary Slip or Payroll Entry period.
- The Additional Salary record was created.
- The Additional Salary payroll date is within the payroll period.
- The Leave Type has an earning component.
- The employee has an active Salary Structure Assignment.
- The leave encashment amount per day is configured.

## Salary Slip Or Payment Entry?

Use **Salary Slip** when the encashment should be part of payroll and paid along with salary.

Use **Payment Entry** when the encashment should be paid separately and accounted for directly through accounts.

## Related Topics

- [Leave Encashment](https://docs.frappe.io/hr/leave-encashment)
- [Leave Type](https://docs.frappe.io/hr/leave-type)
- [Salary Structure](https://docs.frappe.io/hr/salary-structure)
- [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)
- [Salary Slip](https://docs.frappe.io/hr/salary-slip)
- [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)
- [Additional Salary](https://docs.frappe.io/hr/additional-salary)

<!-- page: frappe-hr/hr__leave-management__help-articles__leave-calculation-in-salary-slip.md -->
---
title: "Leave Calculation in Salary Slip"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-management/help-articles/leave-calculation-in-salary-slip"
updated: "2026-07-05"
---

Frappe HR calculates leave impact in the Salary Slip by reducing the employee's payable days for the payroll period. This is mainly controlled by Leave Without Pay, Partially Paid Leave, attendance records, holidays, and the employee's joining or relieving date.

The calculation decides two important values in the Salary Slip:

- **Total Working Days**
- **Payment Days**

The salary components that depend on payment days are calculated based on the final Payment Days.

## How Leave Affects Salary Slip

When a Salary Slip is created, Frappe HR checks the payroll period and calculates how many days the employee should be paid for.

In simple terms:

```text
Payment Days = Eligible Working Days - Leave Without Pay - Absent Days
```

The exact calculation can change depending on payroll settings, holiday settings, attendance records, and leave type settings.

## Leave Without Pay

If an employee has an approved Leave Application for a Leave Type marked as **Leave Without Pay**, those days reduce the Payment Days in the Salary Slip.

For example, if the payroll period has 30 working days and the employee has 2 days of Leave Without Pay:

```text
Payment Days = 30 - 2 = 28
```

Salary components that depend on payment days are then calculated for 28 days instead of 30.

## Partially Paid Leave

Frappe HR also supports **Partially Paid Leave**. In this case, the leave does not reduce the full day's salary. It reduces salary based on the fraction configured in the Leave Type.

For example, if a leave type pays 50% of daily salary for one day, the Salary Slip treats it as a partial reduction instead of a full Leave Without Pay day.

Use Partially Paid Leave when employees should receive part of their salary during a leave period.

## Calculation Based On Leave Application Or Attendance

Payroll can be calculated based on either leave applications or attendance records, depending on the payroll configuration.

### Based On Leave Application

When payroll is based on leave applications, Frappe HR checks approved leave records during the Salary Slip period.

It considers:

- Leave Without Pay
- Partially Paid Leave
- Half-day leave
- Whether the Leave Type includes holidays

### Based On Attendance

When payroll is based on attendance, Frappe HR checks submitted Attendance records for the Salary Slip period.

It considers:

- Absent days
- Half-day attendance
- Attendance marked on holidays, depending on settings
- Leave Type used in attendance records
- Unmarked attendance, depending on payroll settings

If unmarked attendance is configured to be treated as absent, those unmarked days can also reduce Payment Days.

## Half-Day Leave And Half-Day Attendance

Half-day leave or half-day attendance reduces salary based on the half-day fraction configured in payroll settings.

For example, if the daily wages fraction for half day is 0.5, then one half-day Leave Without Pay reduces Payment Days by 0.5.

## Holidays In Salary Slip Calculation

Holiday handling depends on payroll settings and the employee's holiday list.

If holidays are included in total working days, holidays are part of the working day count.

If holidays are not included, holidays are removed from Total Working Days before Payment Days are calculated.

Some Leave Types can also be configured to include holidays. If holidays are included for that Leave Type, leave falling on holidays may be considered in the leave calculation.

## Joining Date And Relieving Date

Salary Slip calculation also considers the employee's joining and relieving dates.

If an employee joins in the middle of the payroll period, Payment Days are calculated from the joining date.

If an employee leaves in the middle of the payroll period, Payment Days are calculated only up to the relieving date.

This prevents salary from being calculated for dates before joining or after relieving.

## Example

Suppose the payroll period is from 1 April to 30 April.

- Total days in period: 30
- Holidays excluded from working days: 4
- Total Working Days: 26
- Leave Without Pay: 2
- Half-day Leave Without Pay: 0.5

The Payment Days will be:

```text
26 - 2 - 0.5 = 23.5
```

Salary components that depend on payment days are calculated for 23.5 payment days.

## Why The Salary Amount May Look Different

If the salary amount in the Salary Slip is not what you expected, check:

- Whether payroll is based on Attendance or Leave Application.
- Whether the Leave Application is submitted and approved.
- Whether the Leave Type is marked as Leave Without Pay or Partially Paid Leave.
- Whether holidays are included in Total Working Days.
- Whether the Leave Type includes holidays.
- Whether attendance is marked for the full period.
- Whether unmarked attendance is treated as absent.
- Whether the employee joined or left during the payroll period.
- Whether the salary component depends on payment days.

## Components That Depend On Payment Days

Only salary components configured to depend on payment days are reduced based on leave calculation.

If a component does not depend on payment days, it may remain the same even when Payment Days are reduced.

Check the Salary Component and Salary Structure configuration if a particular earning or deduction is not changing as expected.

## Related Topics

- [Salary Slip](https://docs.frappe.io/hr/salary-slip)
- [Payroll Settings](https://docs.frappe.io/hr/payroll-settings)
- [Leave Application](https://docs.frappe.io/hr/leave-application)
- [Leave Type](https://docs.frappe.io/hr/leave-type)
- [Attendance](https://docs.frappe.io/hr/attendance)
- [Holiday List](https://docs.frappe.io/hr/holiday-list)
- [Salary Component](https://docs.frappe.io/hr/salary-component)
- [Salary Structure](https://docs.frappe.io/hr/salary-structure)

<!-- page: frappe-hr/hr__leave-management__help-articles__setting-employee-wise-leave-approver.md -->
---
title: "Setting Employee Wise Leave Approver"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-management/help-articles/setting-employee-wise-leave-approver"
updated: "2026-07-05"
---

Frappe HR supports more than one way to decide who should approve an employee's leave application. The right method depends on whether the approver is specific to one employee, shared by a department, or selected while creating the leave application.

## 1. Set Leave Approver In Employee Master

Use this when an employee should always have a specific default leave approver.

Steps:

1. Open the employee record from **Employee**.
2. Go to the **Attendance and Leave Details** section.
3. Select the **Leave Approver** for that employee.
4. Save the employee record.

When the employee creates a **Leave Application**, Frappe HR automatically fetches this approver as the default **Leave Approver**.

This is the best option when approvals are handled by each employee's reporting manager or by a specific HR person.

## 2. Set Leave Approvers In Department

Use this when all employees in a department should be approved by one or more department-level approvers.

Steps:

1. Open the relevant **Department**.
2. Add one or more users in the **Leave Approvers** table.
3. Save the department.

When an employee from that department applies for leave, the department leave approvers are available on the Leave Application.

If both employee-wise and department-wise approvers are configured, the approver set in the employee master is used as the default approver, while department approvers can also be available for selection.

## 3. Select The Leave Approver On Leave Application

The **Leave Approver** field is also available on the **Leave Application** itself.

When creating a leave application:

1. Select the employee.
2. Select the leave type and dates.
3. Check the **Leave Approver** field.
4. Change the approver if another eligible approver should approve this specific request.

This is useful for exceptions, temporary reporting changes, or cases where a leave request should go to a different approver than usual.

## 4. Use User Permissions For Department-Level Access

Setting the approver decides who can be selected as the approver. Access can be controlled separately using **User Permissions**.

For example, if a department manager should only see and approve leave applications from their own department, configure User Permissions for that approver based on:

- Company
- Department
- Employee

This keeps the approval process clean and prevents approvers from seeing leave applications outside their permitted scope.

## Which Method Should You Use?

Use employee-wise approver when each employee has a fixed manager or approver.

Use department-wise approver when the same approver or approver group handles leaves for an entire department.

Use the Leave Application approver field when the approver needs to be changed for a specific request.

Use User Permissions when you also need to restrict what leave records an approver can access.

## Important Notes

- The approver must be a valid Frappe user.
- The approver should have the **Leave Approver** role.
- Employee-wise approver is treated as the default when both employee and department approvers are configured.
- Department approvers are useful for shared approval responsibility.
- User Permissions control access; they do not replace setting the approver.

## Related Topics

- [Setting Employee-wise Leave Approver](https://docs.frappe.io/hr/setting-employee-wise-leave-approver)
- [Department-wise Leave Approval in ERPNext](https://docs.frappe.io/hr/department-wise-leave-approval-in-erpnext)
- [Leave Application](https://docs.frappe.io/hr/leave-application)
- [Employee](https://docs.frappe.io/hr/employee)
- [Department](https://docs.frappe.io/hr/department)
- [HR Settings](https://docs.frappe.io/hr/hr-settings)

<!-- page: frappe-hr/hr__leave-period.md -->
---
title: "Leave Period"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-period"
updated: "2026-02-04"
---

**A Leave Period is a duration of time for which leaves are allocated.**

Most companies manage leaves based on a Leave Period, corresponding to a calendar year or the fiscal year. To access Leave Period, go to:

> Home > Human Resources > Leaves > Leave Period

**1. Prerequisites**
--------------------

Before creating a Leave Period, it is advisable to create the following:

* [Company](https://docs.erpnext.com/docs/user/manual/en/company-setup)
* [Holiday List](https://docs.frappe.io/hr/holiday-list)

**2. How to create a Leave Period**
-----------------------------------

1. Go to Leave Period list, click on New.
2. Enter the From Date and To Date of the Leave Period.
3. Select the Company name for which the Leave Period is applicable.
4. Save.

The Leave Period also allows you to select a [Holiday List for Optional Leaves](https://docs.frappe.io/hr/holiday-list) (optional) which will be considered for allocating Optional Leaves for the period.

> **Note:** The 'Holiday List for Optional Leaves' is not the same as the usual 'Holiday List'. This list will contain a list of optional holidays only. 'Holiday List for Optional Leaves' can be created from the [Holiday List](https://docs.frappe.io/hr/holiday-list) document. You can create two Holiday Lists for a Leave Period; one containing the usual set of holidays and the other for optional holidays.

Additionally, you can check the 'Is Active' checkbox if you want to enable this particular Leave Period.

![Leave Period](https://frappehr.com/files/leave-period.png)  


**3. Granting leaves based on Leave Period**
--------------------------------------------

To grant leaves based on Leave Period, use the [Leave Policy Assignment](https://docs.frappe.io/hr/leave-policy-assignment).

**4. Related Topics**
---------------------

1. [Leave Allocation](https://docs.frappe.io/hr/leave-allocation)
2. [Leave Policy](https://docs.frappe.io/hr/leave-policy)
3. [Leave Type](https://docs.frappe.io/hr/leave-type)


  

<!-- page: frappe-hr/hr__leave-policy-assignment.md -->
---
title: "Leave Policy Assignment"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-policy-assignment"
updated: "2026-02-04"
---


> **Introduced in Version 13**
> 
> 

Leave Policy Assignment in Frappe HR is used to assign leaves to employees based on created policies. To access Leave policy assignment, go to:


> **Home > Human Resources > Leaves > Leave Policy Assignment**
> 
> 

**1. Prerequisites**
--------------------

Before creating a Leave Policy Assignment, it is advisable to create the following:

* [Employee](https://docs.frappe.io/hr/employee)
* [Leave Policy](https://docs.frappe.io/hr/leave-policy)

**2. How to create a Leave Policy Assignment**
----------------------------------------------

1. Go to Leave Policy Assignment, click on New.
2. Select Employee and Leave Policy.
3. Select Assignment based on the following as needed:


	* If "Assignment based on" is set to Leave Period, you need to select the applicable Leave Period. The Effective From and Effective To dates will be set automatically based on the Leave Period selected.
	* If "Assignment based on" is set to Joining Date, the Effective From date will be set to the employee's Date of Joining.
	* If "Assignment based on" is left blank, then you will have to set the Effective From and Effective To date manually.
4. Save and Submit.

![Leave Policy Assignment](https://frappehr.com/files/leave-policy-assignment.png)  


On submission, Leave Allocation documents would be created automatically based on the [Leave Policy](https://docs.frappe.io/hr/leave-policy) as shown below.

![Leave Allocations](https://frappehr.com/files/granted-leaves.png)  


**3. Features**
---------------

### **3.1 Bulk Leave Policy Assignment**

Frappe HR also allows creating Leave Policy Assignments for multiple employees at once.

1. Go to the Leave Policy Assignment list.
2. Click on Bulk Leave Policy Assignment.
3. This will take you to the [Leave Control Panel](https://docs.frappe.io/hr/leave-control-panel), where you can assign Leave Policies in bulk.

![](https://frappehr.com/files/NUL3M8C.png)  


### **3.2 Allocating Earned Leaves**

Leave Policy Assignments can also be used to allocate [Earned Leaves](https://docs.frappe.io/hr/configuring-earned-leave).

  

<!-- page: frappe-hr/hr__leave-policy.md -->
---
title: "Leave Policy"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-policy"
updated: "2026-02-04"
---

**The amount of entitled leaves in a Company for an Employee in a Leave Period is known as Leave Policy.**

It is a practice for many enterprises to enforce a general Leave Policy to effectively track and manage Employee leaves. Frappe HR allows you to create and manage multiple Leave Policies and allocate leaves to Employees as defined by the policy.

To access Leave Policy, go to:


> **Home > Human Resources > Leaves > Leave Policy**
> 
> 

**1. How to create a Leave Policy**
-----------------------------------

1. Go to Leave Policy list, click on New.
2. Select the Leave Type and enter its Annual Allocation.
3. Save and Submit.

![Leave Policy](https://frappehr.com/files/leave-policy.png)

Once submitted, you can create [Leave Policy Assignment](https://docs.frappe.io/hr/leave-policy-assignment) to assign this policy to multiple employees.

**2. Related Topics**
---------------------

1. [Leave Period](https://docs.frappe.io/hr/leave-period)
2. [Leave Type](https://docs.frappe.io/hr/leave-type)
3. [Leave Policy Assignment](https://docs.frappe.io/hr/leave-policy-assignment)

  

<!-- page: frappe-hr/hr__leave-type.md -->
---
title: "Leave Type"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leave-type"
updated: "2026-07-15"
---

**Leave Type refers to the types of leaves allocated to an Employee which they can use while making Leave Applications.**

You can create any number of Leave Types based on your company’s requirements.

To access Leave Type, go to:


> **Home > Human Resources > Leaves > Leave Type**
> 
> 

**1. How to create a Leave Type**
---------------------------------

1. Go to Leave Type list, click on New.
2. Enter Leave Type Name.
3. Enter Maximum Leave Allocation Allowed, Applicable After (Working Days), Maximum Consecutive Leaves Allowed (optional).
4. Save.

![](/files/leave-type-settings.png)

Below is a detailed explanation of all the fields and checkboxes in Leave Type.

* **Maximum Leave Allocation Allowed per Leave Period:** This field allows you to set the maximum number of the allocation allowed per Leave Period of this Leave Type while creating the Leave Policy.
* **Allow Leave Application After (Working Days):** Enter the minimum number of working days here. Only the employees who have worked for this number of days or more since their Date of Joining will be allowed to apply for this particular leave type. Any other leaves (such as Casual Leave, Sick Leave.etc.) availed by the Employees after their joining date will also be considered while calculating working days of the Employee.
* **Maximum Consecutive Leaves Allowed:** It refers to the maximum number of days this particular Leave Type can be availed at a stretch. If an employee exceeds the maximum number of days, their extended leave will be considered as ‘Leave Without Pay'.
* **Is Carry Forward:** If checked, the balance leaves of this Leave Type will be carried forward to the next allocation period.
* **Is Leave Without Pay:** This ensures that the Leave Type will be treated as leaves without pay and salary will get deducted for this Leave Type.
* **Is Optional Leave:** Optional Leaves are holidays that Employees can choose to avail from a list of holidays published by the company. The Holiday List for Optional Leaves can have any number of holidays, but you can restrict the number of such leaves by setting the Max Days Leave Allowed field.
* **Allow Negative Balance:** If checked, the system will always allow to apply and approve [Leave Applications](https://docs.frappe.io/hr/leave-application) for the Leave Type, even if there is no leave balance.
* **Allow Over Allocation:** If checked, the system will allow allocating more leaves than the number of days in the allocation period. Enabling this option does not bypass or override the limit configured in the **Maximum Leave Allocation Allowed per Leave Period** field.
* **Include holidays within leaves as leaves:** Check this option if you wish to count holidays within leaves as a ‘leave’. For example, if an Employee has applied for leave on Friday and Monday, and Saturday and Sunday are weekly offs, if the 'Include holidays within leaves as leaves' checkbox for the Leave Type is checked, the system will consider Saturday as Sunday as leaves too. Such holidays will be deducted from the total number of leaves.
* **Is Compensatory:** Compensatory leaves are leaves granted for working overtime or on holidays, normally compensated as an encashable leave. You can check this option to mark the Leave Type as compensatory. An Employee can request for compensatory leaves using [Compensatory Leave Request](https://docs.frappe.io/hr/compensatory-leave-request).


> **Introduced in version 13**
> 
> 

* **Is Partially Paid Leaves:** This checkbox ensures that Leave Type will be treated as partially paid and some part of daily earnings will be paid through salary slip. If this checkbox is enabled then a field "Fraction of Daily Salary Per Leave" appears where you can define the fraction of daily salary paid on the partial leave day.

![](https://frappehr.com/files/8IeXPo5.png)


> **Note: The Leave Type can be either Leave Without pay or Partially Paid.**
> 
> 

**2. Features**
---------------

### **2.1 Leave Encashment**

It is possible that Employees can receive cash from their Employer for unused leaves granted to them in a Leave Period. Not all Leave Types need to be encashable, so, you should set "Allow Encashment" for only those Leave Types which are encashable.


> **Note: Leave encashment is allowed only in the last month of the Leave Period.**
> 
> 

![](https://frappehr.com/files/N7AiiYE.png)  


**Non-Encashable Leaves:** This field indicates the number of leave days the Employees won't be able to encash. Above the mentioned days, the Employee is eligible to encash leaves.

For example, if there are 10 leaves of a particular Leave Type which is encashable, and the Employee has 8 leaves left. If Non-Encashable Leaves = 5, the Employee is given encashment of only 8 - 5 = 3 leaves.

**Earning Component:** This field allows you to specify the Salary Component that will be encashed to Employees as a part of their Salary in the Salary Slip.


> **Note: On submitting a** [**Leave Encashment**](https://docs.frappe.io/hr/leave-encashment) **for an Employee, Frappe HR automatically creates an** [**Additional Salary**](https://docs.frappe.io/hr/additional-salary) **which will get added to the Salary Slip of the Employee when processing the next payroll.**
> 
> 

### **2.2 Earned Leave**

Earned Leaves are leaves earned by an Employee after working with the company for a certain amount of time. Checking "Is Earned Leave" will allot leaves pro-rata basis by automatically updating Leave Allocation for leaves of this type at intervals set by 'Earned Leave Frequency'.

For example, an Employee is allotted 24 Privilege Leaves in a year, wherein the Privilege Leave is set as Earned Leave with Monthly allotment. In this case, the Employee will earn 2 (24 leaves/12 months) Privilege Leaves at the end of every month. The leave allotment process (background job) will only allot leaves considering the max leaves for the leave type and will round to 'Rounding' for fractions.

![](https://frappehr.com/files/1SrI5mm.png)  



> **Note: The initial allocation of this Leave Type will be 0. Leaves will be updated at the end of the Month (or as per the 'Earned Leave Frequency' set).**
> 
> 

### **2.3 Default Leave Types**

There are some pre-loaded Leave Types in the system, as below:

* **Leave Without Pay:** You can avail these leaves for different purposes, such as extended medical issues, educational purposes, or unavoidable personal reasons. The 'Leave Without Pay' checkbox for this Leave Type is checked by default. The employee does not get paid for such leaves.
* **Privilege leave:** These are like earned leaves that can be availed for travel, family vacation, and so on.
* **Sick leave:** You can avail of these leaves if you are unwell.
* **Compensatory off:** These are compensatory leaves allotted to employees for overtime work. The 'Is Compensatory' checkbox for this Leave Type is checked by default.
* **Casual leave:** You can avail of this leave to take care of urgent and unseen matters.

**3. Related Topics**
---------------------

1. [Leave Period](https://docs.frappe.io/hr/leave-period)
2. [Leave Policy](https://docs.frappe.io/hr/leave-policy)
3. [Leave Allocation](https://docs.frappe.io/hr/leave-allocation)
4. [Leave Application](https://docs.frappe.io/hr/leave-application)
5. [Compensatory Leave Request](https://docs.frappe.io/hr/compensatory-leave-request)
6. [Leave Encashment](https://docs.frappe.io/hr/leave-encashment)

  

<!-- page: frappe-hr/hr__leaves.md -->
---
title: "Leaves"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/leaves"
updated: "2026-02-04"
---

This section will help you understand how Frappe HR enables you to efficiently manage the leave schedule of your organization. It also explains how employees can apply for leaves.

The number and type of leaves an Employee can apply is controlled by Leave Allocation. You can create Leave Allocation for a Leave Period based on the Company's Leave Policy. You can also allocate Additional Leaves to your employees and generate reports to track leaves taken by Employees.

Employees can also create leave requests, which their respective managers (leave approvers) can approve or reject. An Employee can select leaves from a number of leave types such as Sick Leave, Casual Leave, Privilege Leave and so on.

**Related Topics**
------------------

1. [Holiday List](https://docs.frappe.io/hr/holiday-list)
2. [Leave Type](https://docs.frappe.io/hr/leave-type)
3. [Leave Period](https://docs.frappe.io/hr/leave-period)
4. [Leave Policy](https://docs.frappe.io/hr/leave-policy)
5. [Leave Policy Assignment](https://docs.frappe.io/hr/leave-policy-assignment)
6. [Leave Allocation](https://docs.frappe.io/hr/leave-allocation)
7. [Leave Control Panel](https://docs.frappe.io/hr/leave-control-panel)
8. [Leave Application](https://docs.frappe.io/hr/leave-application)
9. [Compensatory Leave Request](https://docs.frappe.io/hr/compensatory-leave-request)
10. [Leave Encashment](https://docs.frappe.io/hr/leave-encashment)
11. [Leave Block List](https://docs.frappe.io/hr/leave-block-list)
12. [Leave Ledger Entry](https://docs.frappe.io/hr/leave-ledger-entry)

  

<!-- page: frappe-hr/hr__loan-application.md -->
---
title: "Loan Application"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/loan-application"
updated: "2026-02-04"
---

**Loan Application is a document which contains the information regarding the Loan Applicant, Loan Type, Repayment Method, Loan Amount and Rate of Interest.**

Employee can apply for loan by going to:

> Human Resources > Loan > Loan Application

**1. Prerequisites**
--------------------

Before creating a Loan Application, it is advisable to create the following documents:

* [Employee](https://docs.frappe.io/hr/employee)
* [Loan Type](https://docs.frappe.io/hr/loan-type)

**2. How to create a Loan Application**
---------------------------------------

1. Go to: Loan Application > New.
2. Enter the Applicant name.
3. Enter loan information such as a Loan Type, Loan Amount and Required by Date.
4. Select the [Repayment Method](https://docs.frappe.io/hr/loan-application#3-1-repayment-method) and based on loan information, information such as Total Payable Amount and Interest will be calculated.
5. Save and Submit.

![Loan Application](https://frappehr.com/files/loan-application99399a.png)

**3. Features**
---------------

### **3.1 Repayment Method**

There are two types of Repayment Methods in Loan Application:

#### **1. Repay Fixed Amount Per Period**

* Enter the Monthly Payment Amount.
* Save.
* Once saved, based on the Rate of Interest, the Total Payable Interest and Total Payable Amount will be calculated along with Period in Months.
* Submit.

![Repayment Fixed Amount Per Period](https://frappehr.com/files/repayment-period-in-months.png)

#### **2. Repay Over Number Of Periods**

* Enter the Repayment Period in Months.
* Save.
* Once saved, based on the Rate of Interest, the Total Payable Interest and Total Payable Amount will be calculated along with Monthly Repayment Amount.
* Submit.

![Repayment Fixed Amount Per Period](https://frappehr.com/files/repayment2.png)

**4. Related Topics**
---------------------

1. [Loan Type](https://docs.frappe.io/hr/loan-type)
2. [Loan](https://docs.frappe.io/hr/loan)

  

<!-- page: frappe-hr/hr__loan-type.md -->
---
title: "Loan Type"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/loan-type"
updated: "2026-02-04"
---

**Loans can be categorized into different types based on their specific characteristics.**

In Frappe HR, you can define different Loan Types, their Rate of Interest and other related information in the Loan Type doctype.

To access Loan Type go to:

> Human Resources > Loans > Loan Type

**1. How to create a Loan Type**
--------------------------------

1. Go to: Loan Type.
2. Enter the Loan Name.
3. Enter the Rate of Interest (%) Yearly.
4. Optionally, you can also enter the Maximum Loan Amount and Description of the Loan Type.
5. Save.

![Loan Type](https://frappehr.com/files/loan-type.png)

**2. Related Topics**
---------------------

1. [Loan Application](https://docs.frappe.io/hr/loan-application)
2. [Loan](https://docs.frappe.io/hr/loan)

  

<!-- page: frappe-hr/hr__loan.md -->
---
title: "Loan"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/loan"
updated: "2026-02-04"
---

**Once the Loan Application is approved by the manager, a Loan record and repayment schedule can be created for the Applicant using the Loan.**

To access Loan, go to:

> Human Resources > Loans > Loan

**1. Prerequisites**
--------------------

Before creating a Loan record, it is necessary that you create the following documents:

* [Loan Type](https://docs.frappe.io/hr/loan-type)
* [Loan Application](https://docs.frappe.io/hr/loan-application)
* [Chart of Accounts](https://docs.erpnext.com/docs/v14/user/manual/en/accounts/chart-of-accounts)

**2. How to create a Loan record**
----------------------------------

1. Go to: Loan > New.
2. Select the Applicant name.
3. Select the Loan Application. Once selected, loan information such as Loan Type, Loan Amount, Rate of Interest, Repayment Method, Repayment Period in Months and Monthly Repayment Amount will be fetched.
4. Enter Repayment Start Date.

![Loan](https://frappehr.com/files/loan1.png)
5. Enter Account Information such as Mode of Payment, Payment Account, Loan Account and Interest Income Account.
6. Save. Once saved, a Repayment Schedule is automatically generated. The first repayment payment date would be set as per the "Repayment Start Date". The

![Repayment Schedule](https://frappehr.com/files/loan2.png)

> Note: Check "Repay from Salary" if the loan repayment will be deducted from the salary

You can alternatively create a Loan record directly from [Loan Application](https://docs.frappe.io/hr/loan-application)

**3. Features**
---------------

### **3.1 Creation of Disbursement Entry**

After submitting the Loan document, if the status is "Sanctioned", you can click on "Create Disbursement Entry" to create a Journal Entry of the Loan.

![Disbursement Entry](https://frappehr.com/files/disbursement-entry.png)  


### **3.2 Loan repayment deduction from Salary**

To auto deduct the Loan repayment from Salary, check "Repay from Salary" in Loan. It will appear as Loan Repayment in Salary Slip.

![Salary Slip](https://frappehr.com/files/salary-slip-loan.png)  


### **3.3 Extending the Loan**

Loan amount is deducted from the salary. If the employee is on leave without pay for some period, the existing loan can be extended without the need for creating a new loan. This can be done be editing the Repayment Schedule table even after submitting the loan.

![Extending Loan](https://frappehr.com/files/change-loan-amount.gif)  


**4. Related Topics**
---------------------

1. [Journal Entry](https://docs.erpnext.com/docs/v14/user/manual/en/accounts/journal-entry)
2. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)

  

<!-- page: frappe-hr/hr__mobile-app-installation.md -->
---
title: "Mobile App Installation"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/mobile-app-installation"
updated: "2026-02-04"
---

Frappe HR ships with a mobile frontend (progressive web app) v15 onwards. To install the app on your phones, go to https://<sitename>/hrms eg: if my site name is <https://frappeio.frappe.cloud>, the mobile app can be installed from <https://frappeio.frappe.cloud/hrms> 
Go to this URL on your mobile browser (Chrome/Safari) and install the app.
> Note: Firefox does not support PWA installation unless you have a plugin. 

## Android

1. On Android, you will get a prompt to install the app on this URL. 
2. If you do not see the prompt, tap on the hamburger menu (three dots), and tap on Install app from the list of options.
3. Tap on Install, and wait for a few seconds.
4. You will then be able to find the Frappe HR app in your applications. You can login to this app with your site credentials. 

![](https://gameplan.frappe.cloud/files/wqkysO0.jpg) 

### Installation GIF

<img src="/files/frappehr-android-pwa.gif" alt="frappehr-android-pwa-install" width="350"> 

## iOS

1. On iOS, if you're using Safari, tap on the share button shown in the image below. 
2. Scroll down the list of options, then tap Add to Home Screen. 
3. If you do not see "Add to Home Screen", click on "Edit Actions" and you should find the option. 
4. The icon will then appear on your home screen. You can login to this app with your site credentials. 

![](https://gameplan.frappe.cloud/files/bG9exfR.jpg) 

### Installation GIF

<img src="/files/frappehr-ios-pwa.gif" alt="frappehr-ios-pwa-install" width="350">

<!-- page: frappe-hr/hr__multicurrency-employee-advance-expense-claim.md -->
---
title: "Multi Currency Advance & Claim"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/multicurrency-employee-advance-expense-claim"
updated: "2026-04-03"
---

**Employees working internationally or handling expenses in foreign currencies may receive advances in currencies different from the company’s base currency. Frappe HR now supports Multi-Currency handling for both Employee Advance and Expense Claim to be recorded, paid, adjusted, and managed in any currency while maintaining accurate accounting and exchange rate impact.**

With this feature in v16, it now supports:

- Multi Currency Employee Advances
- Multi Currency Expense Claims
- Accurate exchange rate conversions
- Automatic exchange gain/loss entries
- Multiple Payment Entry against the same advance

## **1. Prerequisites**

1. Employee
2. Department
3. Chart of Accounts
4. Multi Currency Setup
5. Employee Advance
6. Expense Claim

**1.1 Create Expense Claim Type & Mode of Payment**

Before creating multicurrency records, make sure your **Expense Claim Types** and **Modes of Payment** are configured with accounts that use the correct currency.

For example, the standard **Expense Claim Type** (such as *Travel*) may be linked to an account in the company’s base currency. So such a type won’t accept a claim in a different currency. In these cases, create a separate expense type (e.g., *Travel — USD*) and link it to an account that uses the same transaction currency

![](/files/Expense Claim Type.png)
*Expense Claim Type*



Similarly, if you are paying via Bank or Cash in a foreign currency, the Mode of Payment must link to a corresponding currency account. This ensures that expense claims and advances in currencies other than the company’s base currency are captured and processed correctly.

![](/files/Mode of Payment.png)
*Mode of Payment*

## **2. Multi-Currency in Employee Advance**

Before creating an Employee Advance, ensure that the **Employee Salary Currency** is correctly set in the Employee master.  

A new field **Employee Advance Account** is added in the Employee master. This account should match the employee’s salary currency.  

> **Note:** If these fields are not set, Employee Advance allows manual selection. Make sure the advance account exists with the correct currency before creating an advance.

**2.1 How to Create a Multi-Currency Employee Advance**

1. Go to: **Employee Advance > New**
2. Select the **Employee**
3. Choose the **Currency** if not fetched automatically and enter the **Advance Amount**
4. Under the Accounting section:
  - **Advance Account** is fetched from **Employee Advance Account** in the Employee master; if not fetched, select manually  
  - Select **Mode of Payment** if applicable
5. Save the document

![emp-advance](/files/MultiCurrencyEmployeeAdvance.png)

## **3. Payment of Multi-Currency Advances**

Payment for a submitted Employee Advance can be made via **Payment Entry**.  

> **Note**

- At the time of payment, the current exchange rate will be fetched. This rate is used to calculate the base currency amounts and determine exchange gain/loss during Expense Claim.  
- The original exchange rate on the Employee Advance is no longer used; the payment exchange rate is used for all further calculations.

**3.1 Multiple Payment Entries**

If the same advance has multiple payments:  

- Each payment is tracked separately  
- Multi-currency payments with different exchange rates are supported  
- Correct amounts are reflected in Expense Claim

## **4.Multi Currency Expense Claim**

1. From **Employee Advance → Make Expense Claim**

- The advance currency will be fetched in the Expense Claim.  
- All linked advances will appear in the **Advances Table**.  
- Exchange rate at the time of payment will also be fetched in Advances Table. 
- Base currency values are auto-calculated based on the exchange rate at the time of claim.  
- If the same advance has multiple payments, each payment will appear as a separate row in Advances Table with the corresponding **Payment Entry** reference. This helps in reconciling partially claimed advances.

![multi-payments](/files/multi-payments.jpeg)

Once the Expense Claim is Submitted, the claim amount is allocated from the Advance table

![advance-claimed](/files/advance-claimed.jpeg)

## **5. Exchange Gain/Loss Handling**

- If the exchange rate at the time of Expense Claim differs from the exchange rate at the time of advance payment:  
  - Exchange gain/loss is calculated for each advance row  
  - Total gain/loss is posted via **Journal Entry**, ensuring accurate accounting

![gain_loss](/files/gain_loss.jpeg)

![gain_loss-booked](/files/gain_loss-booked.jpeg)

**References:**  

- Employee Advance
- Expense Claim

<!-- page: frappe-hr/hr__organizational-chart.md -->
---
title: "Organizational Chart"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/organizational-chart"
updated: "2026-02-04"
---

**An organizational chart shows the organizational structure by depicting connections between different employees with their designation, image, and name. In large organizations where it's difficult to remember names, people can interact with the org chart and know the hierarchy through faces and other info.**

To access Employee Grade, go to:

> Home > Human Resources > Employee > Organizational Chart

* The org chart is created based on the "Reports To" field in Employee master.
* The employees that don't report to anyone are shown in the first level.
* The chart expands horizontally on the desktop view and vertically on mobile.
* Each node has details like the Employee Name, Image, Designation, and the total number of connections.
* The connections are the total number of descendants a particular node has till the end of the hierarchy.
* The edit button in every node navigates to the Employee Master.
* As you navigate through the chart, the active hierarchy is highlighted.
* You can use the Company filter to check the org chart for individual companies.

![Org Chart](https://frappehr.com/files/org-chart.png)  


![Org Chart Mobile](https://frappehr.com/files/org-chart-mobile-2.png)  


  

<!-- page: frappe-hr/hr__overtime.md -->
---
title: "Overtime"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/overtime"
updated: "2026-02-04"
---

Overtime allows employees to be compensated or granted compensatory leave for working beyond their standard working hours. Overtime is calculated based on employee check-in and check-out times and processed through Attendance and Overtime Slip records

### Create an Overtime Type

Navigate to the **Overtime Type** doctype to configure how overtime is handled:

- **Maximum Overtime Hours Allowed Per Day**: If set, overtime exceeding this limit won’t be considered for payment.
- **Overtime Salary Component**: The salary component through which overtime earnings are paid.
- **Overtime Amount Calculation**:
  - **Fixed Hourly Rate**: A predefined per-hour rate multiplied by total overtime hours.
  - **Salary Component-Based**: Select applicable salary components. The total amount is divided by the salary cycle's payment days and standard working hours to determine the hourly rate.
- **Pay Rate Multipliers**:
  - **Standard Multiplier**: The hourly rate is multiplied by this value.
  - **Holiday/Weekend Multipliers**: If enabled, separate multipliers can be set for public holidays and weekends; otherwise, the standard multiplier applies.
 
![](/files/Screenshot%202025-03-25%20at%204.27.08%E2%80%AFPM.png)


### To allow overtime for a specific **Shift Type**:

1. Navigate to the **Shift Type** doctype.
2. Enable **Allow Overtime**.
3. Set the applicable **Overtime Type**.
4. Assign the shift to employee(s).

![](/files/Screenshot%202025-03-25%20at%204.38.16%E2%80%AFPM.png)

### Record Employee Check-ins & Mark Attendance

- Employees' **check-in and check-out times** must be recorded.
- **Attendance must be processed** for the shift type as overtime details are fetched based on this.


### Generate & Approve Overtime Slip

1. Create an **Overtime Slip** and select the **employee** and **date range**.
2. Click **Fetch Overtime Details** to populate the **Overtime Details** table based on attendance records.
3. **HR can approve or reject** the overtime slip.
4. Upon approval, an **Additional Salary** record is created, ensuring payment is included in the salary cycle corresponding to the slip’s **from date**.

![](/files/Screenshot%202025-03-25%20at%204.40.52%E2%80%AFPM.png)

<!-- page: frappe-hr/hr__payroll-articles__make-bank-entry-from-payroll-entry.md -->
---
title: "Make Bank Entry from Payroll Entry"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-articles/make-bank-entry-from-payroll-entry"
updated: "2026-07-02"
---

After payroll is processed, companies usually need to record the actual salary payment made from the bank account. In Frappe HR, this can be done from the Payroll Entry by creating a Bank Entry.

A Bank Entry records the movement of money from the company's bank account to settle the payroll liability created during payroll processing.

## When to use this

Use Make Bank Entry when:

- Payroll Entry has been created for a payroll period.
- Salary Slips have been created and submitted.
- Payroll accounting entries have been posted.
- The company is ready to record payment of salaries through a bank account.

## Before you begin

Make sure the following setup is complete:

- Employees have valid salary structures and salary slips.
- Payroll Entry has been processed for the correct payroll period.
- Salary Slips are submitted.
- Payroll accounting has been posted.
- The company has a bank account configured in ERPNext.
- The payable account and bank account used for payroll are correct.

## How it works

When payroll is processed, ERPNext/Frappe HR records the salary expense and the amount payable to employees. The Bank Entry is then used to record the payment of that payable amount from the bank.

Simple flow:

```
Create Payroll Entry
        |
        v
Create Salary Slips
        |
        v
Submit Salary Slips
        |
        v
Post Payroll Accounting Entry
        |
        v
Make Bank Entry
        |
        v
Submit Bank Entry
        |
        v
Salary Payable is settled
```

## Steps to make a Bank Entry

1. Open the submitted Payroll Entry.
2. Check that the Salary Slips are created and submitted.
3. Check that the payroll accounting entry has been created.
4. Click Make Bank Entry from the Payroll Entry actions.
5. Review the generated Bank Entry.
6. Confirm the bank account, payable account, posting date, and amount.
7. Save and submit the Bank Entry.

Once submitted, the Bank Entry records the salary payment and reduces the outstanding payroll payable balance.

## What the Bank Entry represents

The Bank Entry usually records two sides of the transaction:

- Debit: Payroll payable or salary payable account
- Credit: Bank account from which salaries are paid

This means the liability created during payroll processing is reduced, and the bank balance is reduced by the salary payment amount.

## Things to check before submitting

Before submitting the Bank Entry, verify:

- The posting date matches the salary payment date.
- The bank account is correct.
- The payable account is correct.
- The amount matches the salary amount to be paid.
- The company and cost center details are correct, if applicable.

## Common mistakes

### Salary Slips are not submitted

The Bank Entry should be made only after salary slips are submitted and payroll accounting is posted.

### Wrong bank account selected

If the wrong bank account is selected, the accounting impact will be incorrect. Always review the bank account before submission.

### Payroll accounting not posted

If the salary payable entry has not been created, the Bank Entry may not correctly settle the payroll liability.

## Summary

Make Bank Entry from Payroll Entry is used to record salary payment after payroll has been processed. It connects payroll processing with accounting by settling the salary payable amount against the company's bank account.

<!-- page: frappe-hr/hr__payroll-correction.md -->
---
title: "Payroll Correction"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-correction"
updated: "2026-02-04"
---

The feature ensures accurate payroll calculations by allowing users to reverse a portion of LWP days, automatically recalculating earnings and deductions based on the reversal.

How to Use

Step 1: Navigate to Payroll Correction
1.	Go to HR > Payroll > Payroll Correction.
2.	Click New to create a new Payroll Correction entry.
Step 2: Select Employee and Payroll Period

- Choose the Employee whose LWP needs correction.
- Select the Payroll Period.
- The system will fetch available Salary Slips with LWP and absent days applied.

Step 3: Select the Month for LWP Reversal

- In the "Select Month for LWP Reversal" field, choose the month from the dropdown.
- Once that is done system fetches:
  - Salary Slip Reference
  - Absent Days
  - LWP Days
  - Total Working Days
  - Total LWP Applied

Step 4: Enter the number of days to reverse in the Days to Reverse field.

Step 5: Save

- Upon save arrear details will be populated for Earnings, Deductions and Accrued Benefits

Step 5: Submit the Payroll Correction

- •	Once validated, submit the document.
- •	The system will:
  - Create Additional Salary Entries against earnings and deductions for the reversed amount.
  - Record accruals in Employee Benefit Ledger

<!-- page: frappe-hr/hr__payroll-entry.md -->
---
title: "Payroll Entry"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-entry"
updated: "2026-02-04"
---

**Payroll is the sum total of all compensation a business must pay to its employees for a set period of time or on a given date.**

In Frappe HR, Payroll Entry enables bulk processing of payroll for employees. In other words, processing salary slips of all employees in one go. The bulk processing can be Company-wide or based on these categories: Branch, Department, or Designation.

To access Payroll Entry, go to:


> **Home > Human Resources > Payroll > Payroll Entry**
> 
> 

**1. How to create a Payroll Entry**
------------------------------------

1. Go to to Payroll Entry list, click on New.
2. Select the Payroll Frequency.
3. Select Branch, Designation and Department to filter out employees (optional).
4. Select Project (optional) if you want to run the payroll against a project.
5. Select 'Validate Attendance' and 'Salary Slip Based on Timesheet' checkboxes in case you want to deduct the salary based on attendance and if you want to also consider the timesheets of the employees respectively.
6. Select the Payment Account to make the Bank Entry.
7. Save.

Once the information is saved, click on the **Get Employees** button to get a list of Employees for which the Salary Slips will be created based on the selected criteria.

Once the list of Employees is fetched, click on the **Create Salary Slips** button to generate Salary Slips.

![Payroll Entry](https://frappehr.com/files/payroll-entry-get-employees.png)  



> **Note: If the Salary Slips are already created, the system will not create any more Salary Slips. You can also just save the form as Draft and create the Salary Slips later.**
> 
> 

**2. Features**
---------------

### **2.1 Salary Accrual**

After verifying the Salary Slips, you can Submit them all together by clicking on the **Submit Salary Slip** button.

![Payroll Entry](https://frappehr.com/files/payroll-entry.png)  


This will also book the default Payroll Payable account against respective Expense Heads (as configured in Salary Components) to record the accrual of salary to employees.

**Cost Center:**

You can select Cost Center in the Payroll Entry against which the expenses will be posted.

If you want to book expenses against multiple cost centers based on Employee/Department, you can do so by setting Payroll Cost Center in the Employee/Department master.

![](https://frappehr.com/files/ViFAtRT.png)  


Even multiple cost centers can be assigned against a single Employee. You can do so via the Salary Structure Assignment document.

![](https://frappehr.com/files/hUnTWPJ.png)  


Cost Center assigned in Salary Structure Assignment gets the highest priority and then Employee and Department master respectively. The least priority is given to the Cost Center selected in Payroll Entry.

![Payroll Entry](https://frappehr.com/files/payroll-make-accrual-entry.png)  



> **Note: Submitting Salary Slips one by one manually will not create the Journal Entry to record salary accrual.**
> 
> 

### **2.2 Salary Payment**

The final step is to book the Salary Payment.

Salaries in businesses are usually dealt with extreme privacy. In most cases, companies issue a single payment to the bank combining all salaries and the bank distributes the salaries to each employee’s salary account.

This way there is only one payment entry in the company’s books of accounts and anyone with access to the company’s accounts will not have access to the individual salaries.

The salary payment entry is a Journal Entry that debits the total of the Earnings type salary component and credits the total of Deductions type salary component of all Employees to the default account set at the Salary Component level for each component.

To generate your salary payment voucher from Payroll Entry, click on the **Make Bank Entry** button.

Payroll Entry will route you to Journal Entry with relevant filters to view the draft Journal Vouchers created. You will have to set the reference number and date for the transactions and Submit the Journal Entry.

![Payroll Entry](https://frappehr.com/files/payroll-make-bank-entry.png)  



> **Note: For Salary Components which are Flexible Benefits and has *Create Separate Payment Entry Against Benefit Claim* checked, Frappe HR will book separate draft Journal Entries.**
> 
> 

**3. Related Topics**
---------------------

1. [Salary Component](https://docs.frappe.io/hr/salary-component)
2. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
3. [Payroll Period](https://docs.frappe.io/hr/payroll-period)
4. [Journal Entry](https://docs.erpnext.com/docs/user/manual/en/journal-entry)

  

<!-- page: frappe-hr/hr__payroll-management.md -->
---
title: "Payroll Management"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-management"
updated: "2026-02-04"
---

Payroll processing is an important function of every enterprise HR. Frappe HR greatly simplifies this process by offering an array of features that you can utilize from Salary Structure management to bulk processing Payroll of employees. Read the following documentation to understand how to configure and use Frappe HR Human Resources to super power your Payroll processing.

**Related Topics**
------------------

1. [Payroll Period](https://docs.frappe.io/hr/payroll-period)
2. [Salary Component](https://docs.frappe.io/hr/salary-component)
3. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
4. [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment)
5. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)
6. [Additional Salary](https://docs.frappe.io/hr/additional-salary)
7. [Retention Bonus](https://docs.frappe.io/hr/retention-bonus)
8. [Employee Incentive](https://docs.frappe.io/hr/employee-incentive)

  

<!-- page: frappe-hr/hr__payroll-period.md -->
---
title: "Payroll Period"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-period"
updated: "2026-02-04"
---

**A Payroll Period is a period for which Employees get paid for their occupation with the Company.**

Payroll Period helps you define Salary Structures and to calculate tax for a specific period based on applicable Income Tax Slab.

To access Payroll Period, go to:


> **Home > Human Resources > Payroll > Payroll Period**
> 
> 

**1. How to create a Payroll Period**
-------------------------------------

1. Go to Payroll Period list, click on New.
2. Enter Name.
3. Select Start Date and End Date of Payroll Period.
4. Save.

**2. Related Topics**
---------------------

1. [Salary Component](https://docs.frappe.io/hr/salary-component)
2. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
3. [Income Tax Slab](https://docs.frappe.io/hr/income-tax-slab)
4. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)
5. [Employee Tax Exemption Proof Submission](https://docs.frappe.io/hr/employee-tax-exemption-proof-submission)
6. [Employee Tax Exemption Declaration](https://docs.frappe.io/hr/employee-tax-exemption-declaration)

  

<!-- page: frappe-hr/hr__payroll-settings.md -->
---
title: "Payroll Settings"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-settings"
updated: "2026-02-04"
---

**Payroll Settings allow you to configure global settings for the Payroll module.**

To access Payroll Settings, go to: > Home > Payroll > Settings > Payroll Settings

**1. Working Days & Hours**
---------------------------

![](https://frappehr.com/files/0jpZNkE.png)  


#### **1.1 Calculate Payroll Working Days Based On**

Working Days in Salary Slip can be calculated based on Leave Application or Attendance records.

#### **1.2 Consider Unmarked Attendance As**

If you set payroll based on Attendance, this option will be shown. It allows you to control the status of unmarked attendance. Eg: If you set it as Present, you don't need to explicitly mark attendance for every employee throughout the month. Just mark the absent days and the rest would be considered as Present by default.

#### **1.3 Include holidays in Total no. of Working Days**

If checked, the total number of working days will include holidays, and this will reduce the value of salary per day. Eg: If there are 10 holidays in a 30-day month, the Total Working Days will be considered as 30 if this checkbox is enabled and 20 if disabled. Then attendance will be checked for these 30/20 days to find out the payment days.

#### **1.4 Consider Marked Attendance on Holidays**

By default, holidays are considered as paid days. If this is enabled and you mark attendance on a holiday, the marked attendance will override holiday status on that day. Eg: if you mark an employee as Absent on a holiday, it will be counted as an absent day and not a paid one.

#### **1.5 Max working hours against Timesheet**

For salary slips based on the timesheet, you can set the maximum allowed hours against a single timesheet. Set this value to zero to disable this validation.

#### **1.6 Fraction of Daily Salary for Half Day**

Based on this fraction, the salary for Half Day will be calculated. For example, if the value is set as 0.75, then the three-fourth salary will be given for half-day attendance.

**2. Salary Slip**
------------------

![](https://frappehr.com/files/8i1mB1S.png)  


#### **2.1 Disable Rounded Total**

If enabled, hides and disables Rounded Total field in Salary Slips

#### **2.2 Show Leave Balances in Salary Slip**

**3. Email**
------------

![](https://frappehr.com/files/g2R6b5Z.png)  


#### **3.1 Email Salary Slip to Employee**

An email with the salary slip is sent to the respective employee's preferred email address on submission of the salary slip.

#### **3.2 Encrypt Salary Slips in Emails**

The salary slip PDF sent to the employee is encrypted using the mentioned Password Policy.

#### **3.3 Password Policy**

This field becomes visible and mandatory on checking the above option for encrypting the salary slip in email.

Here is an example of how to set a Password Policy for the salary slip PDF.

**Example:**


```
SAL-{first_name}-{date_of_birth.year}
```
This will generate a password like SAL-Jane-1972

**4. Other Settings**
---------------------

![](https://frappehr.com/files/gMl5WRl.png)  


#### **4.1 Define Opening Balance for Earning and Deduction**

If enabled, it will allow you to set up opening entries for **Taxable Earnings till Date** and **Tax Deducted till Date** in the Salary Structure Assignment if there are no existing salary slips for the employee.**![](https://frappehr.com/files/bYBjuyW.png)**  


#### **4.2 Process Payroll Accounting Entry based on Employee**

By default, a consolidated Journal Entry is created against the Payroll Entry for all the employees. If you want a better breakup of payroll amounts per employee, enable this to process employee-wise accounting entries.

![](https://frappehr.com/files/B9OY6ym.png)  


  

<!-- page: frappe-hr/hr__payroll-setup.md -->
---
title: "Payroll Setup"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/payroll-setup"
updated: "2026-02-04"
---

Salary is a fixed amount of money or compensation paid to an employee by an employer in return for the work performed.

Payroll is the administration of financial records of employees' salaries, wages, bonuses, net pay, and deductions.

To process Payroll in Frappe HR,

1. Define [Payroll Period](https://docs.frappe.io/hr/payroll-period.html) (optional)
2. Define [Income Tax Slab](https://docs.frappe.io/hr/income-tax-slab.html) (optional)
3. Create Salary Structure with Salary Components (Earnings and Deductions)
4. Assign Salary Structures to each Employee via Salary Structure Assignment
5. Generate Salary Slips via [Payroll Entry](https://docs.frappe.io/hr/payroll-entry.html).
6. Book the Salary in your Accounts.

**Payroll Period**
------------------

[Payroll Period](https://docs.frappe.io/hr/payroll-period.html), in Frappe HR, is a period for which Employees get paid for their occupation with the Company. Payroll period helps you define Tax slabs applicable for the period, making it easier to manage changing laws.

> Note: Configuring Payroll Period is optional if you do not intend to use Flexible Benefits or Tax Slabs

**Salary Component**
--------------------

This document allows you to define each Earning and Deduction component which can be used to create a Salary Structure and subsequently create Salary Slip or Additional Salary. You can also configure the type, condition and formula as well as other settings which are discussed below. You should be able to enable various combinations of the following options to configure each component as it fits your Company / Regional policies.

* Depends on Leave Without Pay: Leave Without Pay (LWP) happens when an Employee runs out of allocated leaves or takes a leave without an approval (via Leave Application). If enabled, Frappe HR will automatically deduct the pay in proportion of LWP days divided by the total working days for the month (based on the Holiday List).

> Note: If you don’t want Frappe HR to manage LWP, don’t turn on this flag in any of the Salary Components
* Do not include in total: If this option is enabled, the component wont be added to the total of the Earnings or Deductions of the Salary Slip

#### **Earning**

![Salary Component Earnings](https://frappehr.com/files/salary-component.png)  


* Is Additional Component: This option specify that the component can only be paid as Additional Salary. Examples of this component could be Performance Bonus or pay received for on-site deputation etc. Such components are not considered to be part of normal Salary Structure. Instead, Additional Salary with these components can be submitted as required which will be added to the Salary Slip automatically.
* Is Tax Applicable: If a component needs to be considered for Tax calculations specified as per the Payroll Period you may want to enable this option. It would be required that you have a Payroll Period and Income Tax Slab configured with valid Tax Slabs for payroll processing.
* Is Payable: Such components can be booked against separate payable accounts and the Accounts shall be configured in the Accounts table
* Flexible Benefits: Flexible Benefits are earning components which Employees can choose to receive on a pro-rata basis or annually when they claim for. These are mostly tax exempted, unless the Employee fail to file the claim with adequate bills / documents. If turned on, you can specify the maximum benefit allowed for an employee in a year. Employees can create [Employee Benefit Application](https://docs.frappe.io/hr/employee-benefit-application) with the ones they opt for.

>Note: Employee Benefit Application will only allow Employees to only choose from the flexible components which are present in the Salary Structure assigned to the Employee


	+ Pay Against Benefit Claim: Employees can opt to receive flexible benefits annually via Employee Benefit Claim or along with their salary every month. If you enable this, the amount allocated for the component will be paid as the Employee submits an [Employee Benefit Claim](https://docs.frappe.io/hr/employee-benefit-claim.html). Else the amount will be dispersed as part of the Employee's salary on a pro-rata basis.
	
	
		- Only Tax Impact (Cannot Claim But Part of Taxable Income): Such components are those which the company has already paid to the Employee in cash or by some other means, for example a car purchased for the Employee's use. The Employee cannot claim but is liable to pay tax. The amount allocated for this component will be considered while calculating the taxable income of the Employee.
		- Create Separate Payment Entry Against Benefit Claim: Some of the flexible benefits may be legally required to be paid via separate vouchers. If you enable this, while posting the bank entry the amount paid for such components will be posted as a separate entry for each Employee.![Flexible Salary Component](https://frappehr.com/files/salary-component-1.png)  
	
	
	> Note: Normal Tax calculation does not include Flexible Benefits as in most cases these are exempted from Tax. To tax these components anytime before that last payroll, use "Deduct Tax For Unclaimed Employee Benefits" in Payroll Entry / Salary Slip while processing the Salary.

#### **Deduction**

![Salary Component Deduction](https://frappehr.com/files/salary-component-2.png)  


* Variable Based On Taxable Salary: If you enable this, the component will be considered as the standard Tax deduction component. Tax will be calculated based on the Income Tax Slab linked to the employee.

**Salary Structure**
--------------------

Salary Structure represents how Salaries are structured and calculated based on Earnings and Deductions. Salary structures are used to help organizations:

1. Maintain pay levels that are competitive with the external labor market,
2. Maintain internal pay relationships among jobs,
3. Recognize and reward differences in the level of responsibility, skill, and performance, and manage pay expenditures.

Usual components of a salary structure (in India) include:

* Basic Salary: It is the taxable base income and generally not more than 40% of CTC.
* House Rent Allowance: The HRA constitutes 40 to 50% of the basic salary.
* Special Allowances: Makes up for the remainder part of the salary, mostly smaller than the basic salary which is completely taxable.
* Leave Travel Allowance: The non-taxable amount paid by the employer to the employee for vacation/trips with family within India.
* Gratuity: It is basically a lump sum amount paid by the employer when the employee resigns from the organization or retires.
* PF: Fund collected during emergency or old age. 12% of the basic salary is automatically deducted and goes to the employee provident fund.
* Medical Allowance: The employer pays the employee for the medical expenditures incurred. It is tax-free up to Rs.15,000.
* Bonus: Taxable part of the CTC, usually a once a year lump sum amount, given to the employee based on the individual’s as well as the organizational performance for the year.
* Employee Stock Options: ESOPS are Free/discounted shares given by the company to the employees. This is done to primarily increase employee retention.

![Submitted Salary Structure](https://frappehr.com/files/salary-structure.png) A submitted Salary Structure

### **Creating a New Salary Structure**

To create a new Salary Structure go to:

> Human Resources > Payroll Setup > Salary Structure > New Salary Structure

In the new Salary Structure,

1. Name the salary Structure and set the company, letterhead for Salary Slip printing and frequency of payroll etc.
2. Set the starting date from which this is valid (Note: There can only be one Salary Structure that can be “Active” for an Employee during any period).
3. Configure Leave Encashment Amount per Day which will be the amount payable to Employees on Leave Encashment requests.
4. Max Benefits amount is the maximum amount eligible as Flexible Components to employees.

#### **Salary Slip Based on Timesheet**

Salary Slip based on Timesheet is applicable if you have timesheet based payroll system

1. Check "Salary Slip Based on Timesheet"
2. Select the salary component and enter Hour Rate (Note: This salary component gets added to earnings in Salary Slip)

![Salary Slip based on Timesheet](https://frappehr.com/files/salary-timesheet.png)  


#### **Earnings and Deductions in Salary Structure**

In the “Earnings” and “Deductions” tables, you can select the earnings and deductions components The condition and formula configured in Salary Component will be copied by default, but you may change this if required. You may also want to select the Base component in the Earnings table. Note that the amount eligible for each employee should be configured in Salary Structure Assignment.

If the condition and formula for any of the earnings or deductions are not configured in Salary Component, you can calculate the values of Salary Components based on,

#### **Condition and Formula**

![Condition and Formula](https://frappehr.com/files/condition-formula.png)  


#### **Condition and Amount**

![Condition and Amount](https://frappehr.com/files/condition-amount.png)  


In conditions and formulas,

* Use field "base" for using base salary of the Employee
* Use Salary Component abbreviations. For example: BS for Basic Salary
* Use field name for employee details. For example: Employment Type for employment_type

#### **Account Details**

![Salary Structure Account](https://frappehr.com/files/salary-structure-account.png)  


* Select Mode of Payment and Payment Account for the Salary Slips which will be generated using this Salary Structure

Finally, *Save* the Salary Structure.

### **Leave Without Pay (LWP)**

Leave Without Pay (LWP) happens when an Employee runs out of allocated leaves or takes a leave without an approval (via Leave Application). If you want Frappe HR to automatically deduct salary in case of LWP, then you must check on the “Apply LWP” column in the Earning Type and Deduction Type masters. The amount of pay cut is the proportion of LWP days divided by the total working days for the month (based on the Holiday List).

If you don’t want Frappe HR to manage LWP, leave the LWP unchecked in all of the Earning Types and Deduction Types.

**Salary Structure Assignment**
-------------------------------

Salary Structure Assignment allows you to assign salary structure and specify the base pay eligible for each employee. It is important that you set the base salary for each assignment as this will be the base salary used for calculations as per the Salary Structure.

To create a new Salary Structure Assignment go to:

> Human Resources > Payroll > Salary Structure Assignment > New Salary Structure Assignment

![Salary Structure Assignment](https://frappehr.com/files/salary-structure-assignment.png)  




---

**Processing Payroll**
======================

You can either bulk process payroll for Employees under a department, branch or designation or process payroll individually by creating Salary Slips for each employee.

**Payroll Processing Using Payroll Entry**
------------------------------------------

You can also create salary slip for multiple employees using Payroll Entry:

> Human Resources > Payroll > Payroll Entry > New Payroll Entry

#### **Payroll Entry**

![Payroll Entry](https://frappehr.com/files/payroll-entry.png)  


In Payroll Entry,

1. Select the Company for which you want to create the Salary Slips. You can also select the other fields like Branch, Department, Designation or Project to be more specific.
2. Check *Salary Slip based on Timesheet* if you want to process timesheet based Salary Slips.
3. Select the Posting Date and the frequency of payroll which you want to create the Salary Slips.
4. Click on "Get Employee Details" to get a list of Employees for which the Salary Slips will be created based on the selected criteria.
5. Enter the Start and End dates for the payroll period.
6. You can check *Deduct Tax For Unclaimed Employee Benefits* if you want to deduct taxes for all benefits (Salary Components which are *Is Flexible Benefit*) paid to employees till the current payroll
7. Similarly, *Deduct Tax For Unsubmitted Tax Exemption Proof* allows you to deduct taxes for the earnings which were exempted in the previous payrolls as declared in [Employee Tax Exemption Declaration](https://docs.frappe.io/hr/employee-tax-exemption-declaration) but the Employee has not submitted sufficient proof [Employee Tax Exemption Proof Submission](https://docs.frappe.io/hr/employee-tax-exemption-proof-submission)
8. Select the Cost Center and Payment Account.
9. Save the form and Submit it to create Salary Slip records for each active Employee for the time period selected. If the Salary Slips are already created, the system will not create any more Salary Slips. You can also just save the form as Draft and create the Salary Slips later.

![Submitted Payroll Entry](https://frappehr.com/files/created-payroll.png)  


Once all Salary Slips are created, you can use *View Salary Slips* to verify if they are created correctly or edit it if you want to deduct Leave Without Pay (LWP).

After checking, you can "Submit" them all together by clicking on "Submit Salary Slip".

>Note: Submitting Salary Slips will also book the default Payroll Payable account to record the accrual of salary.

#### **Booking Salaries in Accounts**

The final step is to book the Salaries in your Accounts.

Salaries in businesses are usually dealt with extreme privacy. In most cases, the companies issues a single payment to the bank combining all salaries and the bank distributes the salaries to each employee’s salary account. This way there is only one payment entry in the company’s books of accounts and anyone with access to the company’s accounts will not have access to the individual salaries.

The salary payment entry is a Journal Entry that debits the total of the earning type salary component and credits the total of deduction type salary component of all Employees to the default account set at Salary Component level for each component.

To generate your salary payment voucher from Payroll Entry, click on - > Make > Bank Entry

![Payroll Make Entry](https://frappehr.com/files/payroll-make-bank-entry.png)  


Payroll Entry will route you to Journal Entry with relevant filters to view the draft Journal Vouchers created. You shall set reference number and date for the transactions and Submit the Journal Entries.

>Note: For Salary Components which are Flexible Benefits and has *Create Separate Payment Entry Against Benefit Claim* checked, Frappe HR will book separate draft Journal Entries.

![Payroll Entry](https://frappehr.com/files/payroll-journal-entry.png)  


**Creating Salary Slips Manually**
----------------------------------

Once the Salary Structure is created and assigned to employees via Salary Structure Assignment, you can make a Salary Slip individually. Go to:

> Human Resources > Payroll > Salary Slip > New Salary Slip

#### **Salary Slip**

![Salary Slip](https://frappehr.com/files/salary-slip.png)  


  

<!-- page: frappe-hr/hr__project-profitability-report.md -->
---
title: "Project Profitability Report\n"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/project-profitability-report"
updated: "2026-02-16"
---


The Project Profitability Report shows the Profitability and Utilization of each employee based on the Timesheets generated.

To view this report, you can go to:

> Home > Projects > Reports > Project Profitability

This report shows the Project Profitability with the following data:

- Timesheet
- Salary Slip generated using the Timesheet
- Sales Invoice generated using the Timesheet

![](/files/profitability-report.gif)

### Calculation of Utilization

The Utilization of the Employee is calculated using the Total Billed Hours from the Timesheet, Working Days from the Salary Slip, and the Standard Working Hours from HR Settings.

The formula for Utilization is as follows,
```
Utilization = Total Billed Hours / (Working Days * Standard Working Hours)
```

### Calculation of Profit
The Profit is calculated using the Gross Pay from the Salary Slip, Grand Total from the Sales Invoice, and Utilization.

The formula for Profit is as follows,
```
Profit = Grand Total - Gross Pay * Utilization
```

### Calculation of Fractional Cost
The Fractional Cost is calculated using Gross Pay from Salary Slip and Utilization.

The formula for Fractional Cost is as follows,
```
Fractional Cost = Gross Pay * Utilization
```

<!-- page: frappe-hr/hr__push-notification.md -->
---
title: "Push Notification"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/push-notification"
updated: "2026-02-04"
---

v15 onwards, all sites hosted on Frappe Cloud can enable Push Notifications for the mobile app.

Go to


> **Integrations > Push Notification Settings**
> 
> 

Check the **Enable Push Notification Relay** checkbox

![](https://frappehr.com/files/LoM5jEH.png)  


In your mobile app:

Go to **Profile > Settings** or **Notification Icon > Settings** and click on "**Enable Push Notifications"**

![push](https://frappehr.com/files/push.png "push.png")  


This will register your site on the Frappe Cloud relay server and you will receive push notifications.

![push-notifications](https://frappehr.com/files/push-notifications.png "push-notifications.png")  


  

<!-- page: frappe-hr/hr__recruitment.md -->
---
title: "Recruitment"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/recruitment"
updated: "2026-02-04"
---

It is important for enterprises to create and manage vacant positions, job applicants and also create and manage recruitment plans. Frappe HR helps you create recruitment plans and create and publish job openings accordingly, making it easy to manage your hiring process. To understand how you can do configure this, check [Staffing Plan](https://docs.frappe.io/hr/staffing-plan)

  

<!-- page: frappe-hr/hr__reports__employee-ctc-break-up.md -->
---
title: "Employee CTC Break-Up"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/reports/employee-ctc-break-up"
updated: "2026-06-24"
---

**The Employee CTC Break-up report presents an employee's Cost to Company broken down by salary component. For each component it shows the per-cycle amount, the annual amount, and the share of CTC that the component represents.**

The report is generated for a single [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment), so it always reflects the structure and CTC assigned to that employee.

To access the Employee CTC Break-up report, go to:

> Home > Payroll > Employee CTC Break-up

**1. Prerequisites**
--------------------

Before viewing the report, the following must exist:

1. [Employee](https://docs.frappe.io/hr/employee)
2. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
3. [Salary Structure Assignment](https://docs.frappe.io/hr/salary-structure-assignment) with a CTC set

**2. How to view the report**
-----------------------------

There are two ways to open the report:

1. From a Salary Structure Assignment, click Actions > See CTC Break-up. The Employee and Salary Structure Assignment are selected automatically.
2. Go to Employee CTC Break-up and select the Company, Employee, and Salary Structure Assignment.

![Employee CTC Break-up report](/files/Screenshot From 2026-06-24 11-50-31.webp)

**3. Report columns**
---------------------

| Column | Description |
| --- | --- |
| Component | The salary component, shown with its abbreviation. |
| Type | Fixed for a flat amount, or Formula for a derived one. |
| Formula/Amount | The formula text, or the fixed amount. |
| Monthly / Fortnightly / ... | The per-cycle amount. The column title follows the payroll frequency. |
| Annual | The per-cycle amount multiplied by the number of cycles per year. |
| Percent of CTC (%) | The component's share of total CTC. |

**4. Sections**
---------------

The components are grouped into sections. Each section opens with a bold totals row that sums the components below it. The sections appear in this order:

1. Earnings
2. Deductions
3. Tax Deductions
4. Employer Contributions
5. Total Net Earnings
6. Total Gross Earnings

Employer contributions appear after the Tax Deductions section and before the net and gross totals. A section with no components still shows its totals row at zero, so the layout is consistent across employees.

**5. Understanding the totals**
-------------------------------

- Gross is the sum of payable earnings.
- Net is gross minus deductions and tax.
- CTC is gross plus employer contributions and any non-payout earnings, annualised.

Because employer contributions are part of CTC but not of net pay, two assignments with the same CTC can result in different take-home pay, depending on how much of the CTC is made up of employer contributions. The report makes this split visible.

For how employer-contribution components are configured, see [Salary Component](https://docs.frappe.io/hr/salary-component).

<!-- page: frappe-hr/hr__retention-bonus.md -->
---
title: "Retention Bonus"
space: "Frappe HR"
url: "https://docs.frappe.io/hr/retention-bonus"
updated: "2026-02-04"
---

**Retention bonus is a payment or reward outside of an employee's regular salary that is offered as an incentive to keep a key employee on the job.**

Frappe HR allows you to configure Retention Bonus for an Employee for a particular period.

To access Retention Bonus, go to: > Home > Human Resources > Payroll > Retention Bonus

**1. Prerequisites**
--------------------

Before creating a Retention Bonus, it is advisable to create the following:

* [Employee](https://docs.frappe.io/hr/employee)
* [Salary Component](https://docs.frappe.io/hr/salary-component)

**2. How to create a Retention Bonus**
--------------------------------------

1. Go to Retention Bonus list, click on New.
2. Select Employee and Bonus Payment Date.
3. Enter the Bonus Amount.
4. Select the [Salary Component](https://docs.frappe.io/hr/salary-component) under which you want to give the bonus.
5. Save and Submit.
6. On submit, 'Additional Salary' document of the specified 'Salary Component' is created. This will be fetched while running Payroll Entry.

![Retention Bonus](https://frappehr.com/files/retention-bonus.png)

**3. Related Topics**
---------------------

1. [Employee Incentive](https://docs.frappe.io/hr/employee-incentive)
2. [Additional Salary](https://docs.frappe.io/hr/additional-salary)
3. [Salary Component](https://docs.frappe.io/hr/salary-component)
4. [Salary Structure](https://docs.frappe.io/hr/salary-structure)
5. [Payroll Entry](https://docs.frappe.io/hr/payroll-entry)

  
