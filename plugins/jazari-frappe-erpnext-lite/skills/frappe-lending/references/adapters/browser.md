# Interface adapter — Loans and lending

## Contents

- which interface each capability lives in
- ground rules
- where each action lives, step by step
- what cannot be done in the interface

Everything in this file can be done by a person clicking, with no API key. Most of it can also be done
through the API — see `api.md`. The two are alternatives, not a split of the work.

## Which interface

| Open | Which product |
|---|---|
| `https://your-site/app` | the Desk |

Frappe's apps do not share one interface. The Desk (`/app`) has the awesomebar — the search box at the
top — where typing a DocType name jumps straight to its list. Frappe CRM, Helpdesk, Insights, Learning,
Drive, Wiki, Builder and Studio are separate single-page apps with their own left sidebar and no awesomebar.
Frappe Cloud is a different site entirely. Use the base that matches the capability's row.

## Ground rules

- **The Path line is the checked one.** Lines marked *checked on v16.55* were matched against a live v16 Desk (which lives at `/desk`; old `/app` links redirect there). When a numbered step names a different menu ("Go to Accounting > …"), that is the documentation's older menu: follow the Path line, then continue from the next step.
- **Verify the label on screen before clicking.** These paths come from Frappe's documentation as it stood
  on 2026-08-31. Interfaces move. If the screen does not match, say so instead of clicking something similar.
- Ask before each change on a live system, and never type the user's password.
- **The numbered steps are the page's main procedure, not the whole page.** Prerequisites, options, and follow-on sections such as saving and submitting are in the bundled page — read it before acting.
- Where a row gives a sidebar item rather than a menu path, that is what the documentation published —
  open the product, use that sidebar entry, and follow the linked page.
- Where a row has no path at all, open the product at its base URL and follow the documentation link.
  Do not invent a menu that might not exist.

## Where each action lives

### Set up a loan product
- **Path (checked on v16.55):** https://your-site/desk → type *Loan Product* in the search bar at the top and open the doctype
- **Record type:** Loan Product
- **Documented steps:**
  1. Go to the Loan Product List, and click on Add Loan Product
  2. Enter the loan product details like product code, product name, rate of interest, repayment schedule type, etc
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/lending/lending__loan-product.md`  (https://docs.frappe.io/lending/loan-product)

### Process a loan application
- **Path (checked on v16.55):** https://your-site/desk → type *Loan Application* in the search bar at the top and open the doctype
- **Record type:** Loan Application
- **Documented steps:**
  1. Go to Loan Application List and click on Add Loan Application
  2. Select Applicant Type and enter applicant details
  3. Select Company and Loan Product
  4. Enter Loan Amount and review repayment inputs
  5. For secured loans, add Proposed Pledges
  6. Add co-applicants and documents if required
  7. Save and Submit
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/lending/lending__loan-application.md`  (https://docs.frappe.io/lending/loan-application)

### Disburse a loan
- **Path (checked on v16.55):** https://your-site/desk → type *Loan Disbursement* in the search bar at the top and open the doctype
- **Record type:** Loan Disbursement
- **Documented steps:**
  1. Go to the Loan Disbursement List, and click on Add Loan Disbursement
  2. Enter the loan account number and the disbursement amount
  3. Optional user can also select the bank account ledger of disbursement or else the default one from Loan Product will be used
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/lending/lending__loan-disbursement.md`  (https://docs.frappe.io/lending/loan-disbursement)

### Record a loan repayment
- **Path (checked on v16.55):** https://your-site/desk → type *Loan Repayment* in the search bar at the top and open the doctype
- **Record type:** Loan Repayment
- **Documented steps:**
  1. Go to the Loan Repayment List, and click on Add Loan Repayment
  2. Enter the loan account, repayment type and the amount to be repaid
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/lending/lending__loan-repayment.md`  (https://docs.frappe.io/lending/loan-repayment)

### Accrue interest
- **Path (checked on v16.55):** https://your-site/desk → type *Loan Interest Accrual* in the search bar at the top and open the doctype
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/lending/lending__loan-interest-accrual.md`  (https://docs.frappe.io/lending/loan-interest-accrual)

### Manage loan security
- **Path (checked on v16.55):** https://your-site/desk → type *Loan Security* in the search bar at the top and open the doctype
- **Record type:** Loan Security
- **Documented steps:**
  1. Go to the Loan Security List, and click on Add Loan Security
  2. Enter the loan security name/code, loan security type
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/lending/lending__loan-security.md`  (https://docs.frappe.io/lending/loan-security)

