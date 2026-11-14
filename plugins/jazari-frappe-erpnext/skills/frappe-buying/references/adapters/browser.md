# Interface adapter — Buying and procurement

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

- **Verify the label on screen before clicking.** These paths come from Frappe's documentation as it stood
  on 2026-08-31. Interfaces move. If the screen does not match, say so instead of clicking something similar.
- Ask before each change on a live system, and never type the user's password.
- **The numbered steps are the page's main procedure, not the whole page.** Prerequisites, options, and follow-on sections such as saving and submitting are in the bundled page — read it before acting.
- Where a row gives a sidebar item rather than a menu path, that is what the documentation published —
  open the product, use that sidebar entry, and follow the linked page.
- Where a row has no path at all, open the product at its base URL and follow the documentation link.
  Do not invent a menu that might not exist.

## Where each action lives

### Create and manage suppliers
- **Path:** https://your-site/app → **Home > Buying > Supplier > Supplier**
- **Record type:** Supplier
- **Documented steps:**
  1. Go to the Supplier list and click on New
  2. Enter a name for the supplier
  3. Select the supplier group whether Pharmaceutical, Hardware etc
  4. Save. !Supplier Master
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__supplier.md`  (https://docs.frappe.io/erpnext/supplier)

### Raise a material request
- **Path:** https://your-site/app → **Home > Stock > Stock Transactions > Material Request**
- **Record type:** Material Request
- **Documented steps:**
  1. Go to the Material Request list, click on Add Material Request
  2. Enter the Required By date
  3. Select the appropriate purpose from the list
  4. You can fetch Items from a BOM, Sales Order, or Product Bundle
  5. Select the Item and set the quantity
  6. Select the Warehouse for which Items are required
  7. You can change the Required By date for individual Items in this table
  8. Save and Submit
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__material-request.md`  (https://docs.frappe.io/erpnext/material-request)

### Send a request for quotation
- **Path:** open https://your-site/app (the Desk) and search the awesomebar for **Request for Quotation**
- **Record type:** Request for Quotation
- **Documented steps:**
  1. Go to the Request For Quotation list and click on "+ Add Request for Quotation"
  2. Enter the *Required Date*, by which you'll need the requested materials
  3. Fill the "Suppliers" list with possible suppliers
  4. In the next table, enter the required items along with UOM and quantity, as well as the target warehouse
  5. The *Warehouse* can be left blank if *Maintain Stock* is not enabled for the item
  6. If you want to send the Request for Quotation to your suppliers as an email, you can create an Email Template and select it here. In the template, you can use special variables for supplier specific data:
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__request-for-quotation.md`  (https://docs.frappe.io/erpnext/request-for-quotation)

### Record a supplier quotation
- **Path:** https://your-site/app → **Home > Buying > Purchasing > Supplier Quotation**
- **Record type:** Supplier Quotation
- **Documented steps:**
  1. You can also make a Supplier Quotation directly from
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__supplier-quotation.md`  (https://docs.frappe.io/erpnext/supplier-quotation)

### Place a purchase order
- **Path:** https://your-site/app → **Home > Buying > Purchasing > Purchase Order**
- **Record type:** Purchase Order
- **Documented steps:**
  1. Go to the Purchase Order list, click on New
  2. Select the Supplier, required by date
  3. In the items table, select the item by code, you can change the required by date for each item
  4. Set the quantity and the price will be fetched automatically if set in the Item master
  5. Set taxes
  6. Save and Submit
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__purchase-order.md`  (https://docs.frappe.io/erpnext/purchase-order)

### Receive goods
- **Path:** https://your-site/app → **Home > Stock > Stock Transactions > Purchase Receipt**
- **Record type:** Purchase Receipt
- **Documented steps:**
  1. Go to the Purchase Receipt list, click on New
  2. The Supplier name and the Items can be fetched from the Purchase Order by clicking on 'Get Items from > Purchase Order'
  3. You can set the Accepted Warehouse for all items in this Purchase Receipt. This is fetched if set in Purchase Order
  4. In case any Items are defective, set the Rejected Warehouse where those Items will be stored
  5. Select the Item and enter the quantity in the Items table
  6. The rate will be fetched and the amount will be calculated automatically
  7. You can expand the item row to change the Accepted Warehouse for an Item
  8. Save and submit
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__purchase-receipt.md`  (https://docs.frappe.io/erpnext/purchase-receipt)

### Return goods to a supplier
- **Path:** open https://your-site/app (the Desk) and find *Purchase Return* — the documentation page below shows the screen
- **Documented steps:**
  1. First open the original Purchase Receipt, against which supplier delivered the Items
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__purchase-return.md`  (https://docs.frappe.io/erpnext/purchase-return)

### Add landed costs
- **Path:** open https://your-site/app (the Desk) and find *Landed cost Voucher* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__landed-cost-voucher.md`  (https://docs.frappe.io/erpnext/landed-cost-voucher)

### Run subcontracting
- **Path:** open https://your-site/app (the Desk) and find *Subcontracting* — the documentation page below shows the screen
- **Documented steps:**
  1. Create a Service Item (Non-stock Item). It represents the service cost of the subcontracted operation
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__subcontracting.md`  (https://docs.frappe.io/erpnext/subcontracting)

### Score suppliers
- **Path:** https://your-site/app → **Home > Buying > Supplier Scorecard > Supplier Scorecard**
- **Record type:** Supplier Scorecard
- **Documented steps:**
  1. Go to the Supplier Scorecard list, click on New
  2. Select a Supplier to score
  3. Select the evaluating period whether weekly, monthly, or yearly
  4. Setup the scoring function (details in next section)
  5. A supplier scorecard is created for each supplier individually. Only one supplier scorecard can be created for each supplier
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__supplier-scorecard.md`  (https://docs.frappe.io/erpnext/supplier-scorecard)

### Agree a blanket order
- **Path:** https://your-site/app → **Selling > Sales > Blanket Order**
- **Record type:** Blanket Order
- **Documented steps:**
  1. Go to Selling > Sales > Blanket Order and select Add Blanket Order
  2. Set Order Type to Selling for a customer agreement or Purchasing for a supplier agreement
  3. Select the Customer or Supplier
  4. Enter the From Date and To Date
  5. Add each Item, committed Quantity, Rate, and item-specific Terms and Conditions
  6. Save and submit the Blanket Order
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__blanket-order.md`  (https://docs.frappe.io/erpnext/blanket-order)

