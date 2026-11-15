# Interface adapter — Selling, delivery and point of sale

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

### Send a quotation
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Selling > Quotation**, or type *Quotation* in the search bar at the top
- **Record type:** Quotation
- **Documented steps:**
  1. Go to Selling > Sales > Quotation
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-49.md` lines 335–466  (https://docs.frappe.io/erpnext/quotation)

### Confirm a sales order
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Selling > Sales Order**, or type *Sales Order* in the search bar at the top
- **Record type:** Sales Order
- **Documented steps:**
  1. Open Sales Order from the Selling workspace
  2. Select Add Sales Order
  3. Select the Company and Customer
  4. Keep Order Type as Sales for a standard customer order
  5. Set the transaction Date and promised Delivery Date
  6. Under Items, optionally set Set Source Warehouse to apply one warehouse to all stock items
  7. Add each Item and enter its Quantity. Review the delivery date, rate, and amount for every row
  8. Review taxes, totals, addresses, and commercial terms
  9. Save the document. ERPNext keeps it in Draft status
  10. Select Submit when the order is confirmed
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-53.md` lines 3–244  (https://docs.frappe.io/erpnext/sales-order)

### Ship goods with a delivery note
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Selling > Delivery Note**, or type *Delivery Note* in the search bar at the top
- **Record type:** Delivery Note
- **Documented steps:**
  1. Go to the Delivery Note list, click on New
  2. The Customer and Item details can be fetched by clicking on 'Get Items from > Sales Order'
  3. The UOM and Rates will be fetched automatically
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-20.md` lines 476–739  (https://docs.frappe.io/erpnext/delivery-note)

### Pick stock for an order
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Stock > Tools > Pick List**, or type *Pick List* in the search bar at the top
- **Record type:** Pick List
- **Documented steps:**
  1. Go to the Pick List list, click on New. !Unsaved Pick List
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-42.md` lines 792–906  (https://docs.frappe.io/erpnext/pick-list)

### Pack an order
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Stock > Tools > Packing Slip**, or type *Packing Slip* in the search bar at the top
- **Record type:** Packing Slip
- **Documented steps:**
  1. Go to the Packing Slip list, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-39.md` lines 976–1041  (https://docs.frappe.io/erpnext/packing-slip)

### Book a shipment
- **Path (checked on v16.55):** https://your-site/desk → type *Shipment* in the search bar at the top and open the doctype
- **Record type:** Shipment
- **Documented steps:**
  1. Go to the Shipment list, click on New
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-58.md` lines 274–355  (https://docs.frappe.io/erpnext/shipment)

### Plan a delivery trip
- **Path (checked on v16.55):** https://your-site/desk → type *Delivery Trip* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Select the Driver and Vehicle, create both if not present
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-20.md` lines 741–778  (https://docs.frappe.io/erpnext/delivery-trip)

### Process a sales return
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Selling > Delivery Note**, or type *Delivery Note* in the search bar at the top
- **Documented steps:**
  1. Open the original submitted Delivery Note
  2. Select Create > Sales Return
  3. Review the Customer, return warehouse, posting date, items, and rates fetched from the original document
  4. Keep only the returned lines. Enter the returned quantity for each Item. ERPNext represents return quantities as negative values
  5. For serialized or batched Items, select the returned Serial Numbers or Batch Numbers
  6. Save and submit the return Delivery Note
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-54.md` lines 315–508  (https://docs.frappe.io/erpnext/sales-return)

### Create and manage customers
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > CRM > Customer**, or type *Customer* in the search bar at the top
- **Record type:** Customer
- **Documented steps:**
  1. Open the Customer list from Selling > Customer
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-17.md` lines 549–721  (https://docs.frappe.io/erpnext/customer)

### Group customers
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > CRM > Setup > Customer Group**, or type *Customer Group* in the search bar at the top
- **Documented steps:**
  1. Open Selling > Customer Group
  2. In Tree view, select the parent group
  3. Select Add Child or New
  4. Enter the Customer Group Name
  5. Select Is Group when this node should contain child groups rather than Customers
  6. Save the Customer Group
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-17.md` lines 273–427  (https://docs.frappe.io/erpnext/customer-group)

### Organise territories
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > CRM > Setup > Territory**, or type *Territory* in the search bar at the top
- **Record type:** Territory
- **Documented steps:**
  1. Go to Selling > Settings > Territory
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-65.md` lines 3–173  (https://docs.frappe.io/erpnext/territory)

### Maintain price lists
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Buying > Items > Price List**, or type *Price List* in the search bar at the top
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-43.md` lines 621–660  (https://docs.frappe.io/erpnext/price-lists)

### Set item prices
- **Path (checked on v16.55):** https://your-site/desk → type *Item Price* in the search bar at the top and open the doctype
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-32.md` lines 858–932  (https://docs.frappe.io/erpnext/item-price)

### Apply a pricing rule
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Selling > Items > Pricing Rule**, or type *Pricing Rule* in the search bar at the top
- **Documented steps:**
  1. Click Add Pricing Rule
  2. Enter a clear Title that identifies the audience and offer
  3. In Apply On, select Item Code, Item Group, Brand, or Transaction
  4. Select Price for a rate, discount, or margin. Select Product for a free-item offer
  5. Add the Item Codes, Item Groups, or Brands covered by the rule. Select the highlighted pencil icon to edit all fields in a child-table row
  6. Under Party Information, enable Selling or Buying and, if required, limit the rule to a Customer, Customer Group, Territory, Sales Partner, Campaign, Supplier, or Supplier Group
  7. Set quantity, amount, validity, company, and currency conditions
  8. Enter the rate, discount, margin, or free-product result
  9. Save the Pricing Rule
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-43.md` lines 662–809  (https://docs.frappe.io/erpnext/pricing-rule)

### Run a promotional scheme
- **Path (checked on v16.55):** https://your-site/desk → type *Promotional Scheme* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Open the Promotional Scheme list and select Add Promotional Scheme
  2. Enter a descriptive title
  3. Select what the scheme applies on: Item Code, Item Group, Brand, or Transaction
  4. Add the eligible values in the table
  5. Select Selling, Buying, or both
  6. Add party conditions when the scheme is restricted
  7. Add Price Discount or Product Discount slabs
  8. Set validity, currency, warehouse, and priority when applicable
  9. Save
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-46.md` lines 462–575  (https://docs.frappe.io/erpnext/promotional-scheme)

### Issue coupon codes
- **Path (checked on v16.55):** https://your-site/desk → type *Coupon Code* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Open Pricing Rule and select Add Pricing Rule
  2. Configure the eligible Items, Item Groups, transaction conditions, quantity or amount limits, and validity
  3. Choose Price Discount or Product Discount
  4. Enable Coupon Code Based
  5. Save the rule
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-15.md` lines 306–429  (https://docs.frappe.io/erpnext/coupon-code)

### Run a loyalty program
- **Path (checked on v16.55):** https://your-site/desk → type *Loyalty Program* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Open the Loyalty Program list and select Add Loyalty Program
  2. Enter the Program Name
  3. Select Single Tier or Multiple Tier
  4. Set From Date and To Date
  5. Restrict the Customer Group and Territory when required
  6. Enable Auto Opt In only when all eligible Customers should join automatically
  7. Add the tier rows
  8. Configure redemption and expiry
  9. Save
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-35.md` lines 493–621  (https://docs.frappe.io/erpnext/loyalty-program)

### Track sales people and commission
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > CRM > Setup > Sales Person**, or type *Sales Person* in the search bar at the top
- **Documented steps:**
  1. Open Sales Person in the Selling or CRM workspace
  2. Review the hierarchy and select New, as highlighted
  3. Enter the Sales Person Name
  4. Select the Parent Sales Person
  5. Link an Employee when the salesperson is also maintained in Frappe HR
  6. Enter a Commission Rate if your process uses it as a default reference
  7. Select Is Group only when the record will contain child Sales Persons
  8. Keep Enabled selected for an active salesperson
  9. Save
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-54.md` lines 3–152  (https://docs.frappe.io/erpnext/sales-person)

### Enforce a customer credit limit
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > CRM > Setup > Customer Group**, or type *Customer Group* in the search bar at the top
- **Documented steps:**
  1. Go to Selling > Settings > Customer Group
  2. Open the required group
  3. In Credit & Overdue Limits, select Add row
  4. Select the Company and enter the Credit Limit
  5. Enter the approved Credit Limit
  6. Choose whether to enable Bypass credit limit check at sales order
  7. Save the Customer
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-15.md` lines 529–713  (https://docs.frappe.io/erpnext/credit-limit)

### Sell at the point of sale
- **Path (checked on v16.55):** https://your-site/desk → type *Point Of Sale* in the search bar at the top and open the page
- **On this screen:** Set up a **POS Profile** first; the Point of Sale screen asks for one.
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-43.md` lines 93–114  (https://docs.frappe.io/erpnext/point-of-sale)
- **Also read:** `docs/erpnext/erpnext-43.md` lines 116–131 — the step-by-step page for this
- **Also read:** `docs/erpnext/erpnext-43.md` lines 313–363 — the step-by-step page for this

### Configure a POS profile
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Selling > POS > POS Profile**, or type *POS Profile* in the search bar at the top
- **Record type:** POS Profile
- **Documented steps:**
  1. Go to POS Profile List, click on “Add POS Profile”
  2. Select the Company and Warehouse
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-43.md` lines 176–311  (https://docs.frappe.io/erpnext/pos-profile)

### Consolidate POS invoices
- **Path (checked on v16.55):** https://your-site/desk → type *POS Invoice Merge Log* in the search bar at the top and open the doctype
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-43.md` lines 145–174  (https://docs.frappe.io/erpnext/pos-invoice-consolidation)

