# Guide adapter — Accounting, invoicing and tax

## Contents

- what guided means here
- the topics, and what to check with the user

These are not buttons. They are decisions and concepts where Frappe's behaviour depends on a choice the
user has to make — and the wrong choice is expensive to reverse later. Claude explains the options from
the documentation, asks which case applies, and then acts through `api.md` or `browser.md` on the records
that follow from the answer.

## Topics

### Handle multi-currency accounting
- **What the page says:** Nova Industries manufactures electronics, buys components abroad, and distributes finished products in several currencies.
- **It covers:** The three currencies to distinguish, Before you begin, Set up foreign-currency accounts, Configure Customers and Suppliers, Configure exchange-rate behavior, Create a foreign-currency Sales Invoice, Record foreign-currency purchases and payments, Use multi-currency Journal Entries
- **Documented detail:**
  1. Create a Sales Invoice for the foreign Customer
  2. Confirm the transaction Currency and Exchange Rate
  3. Select a Price List and verify its currency and conversion rate
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/erpnext/erpnext__multi-currency-accounting.md`  (https://docs.frappe.io/erpnext/multi-currency-accounting)

