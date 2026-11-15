# Guide adapter — Inventory and stock

## Contents

- what guided means here
- the topics, and what to check with the user

These are not buttons. They are decisions and concepts where Frappe's behaviour depends on a choice the
user has to make — and the wrong choice is expensive to reverse later. Claude explains the options from
the documentation, asks which case applies, and then acts through `api.md` or `browser.md` on the records
that follow from the answer.

## Topics

### Choose a valuation method
- **What the page says:** ERPNext values stock **perpetually**: every stock movement (receipt, issue, transfer, manufacture) updates the item's quantity *and* its monetary value in real time through the **Stock Ledger**. The **Valuation Method** decides *how the value of each outgoing unit is calculated* and therefore what your remaining invent
- **It covers:** 1. Overview, 2. FIFO (First In, First Out), 2.1 How it works, 2.2 Worked example, 2.3 Accounting impact, 2.4 Pros, 2.5 Cons, 3. Moving Average
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/erpnext/erpnext-07.md` lines 1888–2073  (https://docs.frappe.io/erpnext/fifo-and-moving-average)

### Run perpetual inventory
- **What the page says:** As per the perpetual inventory system, accounting entry is done for every stock transaction. Otherwise, it's done in larger intervals for example monthly or quarterly. Each warehouse is linked with a corresponding account head.
- **It covers:** 1. Activate perpetual inventory, 2. Example, 2.5 Sales Invoice with Update Stock
- **Documented detail:**
  1. Accounting Of Inventory Stock
  2. Migrate to Perpetual Inventory
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/erpnext/erpnext-11.md` lines 1479–1750  (https://docs.frappe.io/erpnext/perpetual-inventory)

