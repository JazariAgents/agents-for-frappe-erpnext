# Interface adapter — Inventory and stock

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

### Create and manage items
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Buying > Items > Item**, or type *Item* in the search bar at the top
- **Record type:** Item
- **Documented steps:**
  1. Go to the Item list, click on new
  2. Enter an Item Code, the name will be auto-filled the same as Item Code on clicking inside the Item Name field
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-33.md` lines 396–700  (https://docs.frappe.io/erpnext/item)

### Group items
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Buying > Items > Item Group**, or type *Item Group* in the search bar at the top
- **Record type:** Item Group
- **Documented steps:**
  1. Go to the Item Group list, click on New
  2. Select a group node under which you wish to create the Item Group, the default root is 'All Item Groups'
  3. Select 'Add Child' or click on the New button
  4. To make this child a category/group node, tick on Group Node
  5. Click on Create New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-32.md` lines 786–856  (https://docs.frappe.io/erpnext/item-group)

### Create item variants
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Buying > Items > Item**, or type *Item* in the search bar at the top
- **On this screen:** Variants are made from a template Item: tick **Has Variants**, add the attributes, then **Create > Variant**.
- **Documented steps:**
  1. To use Item Variants in ERPNext, create an Item and tick 'Has Variants' under Variants
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-33.md` lines 255–316  (https://docs.frappe.io/erpnext/item-variants)

### Define item attributes
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Stock > Setup > Item Attribute**, or type *Item Attribute* in the search bar at the top
- **Record type:** Item Attribute
- **Documented steps:**
  1. Go to the Item Attribute list, click on 'Add Item Attribute'
  2. Enter a name for the Attribute
  3. Enter the attribute values in the table
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-32.md` lines 573–612  (https://docs.frappe.io/erpnext/item-attribute)

### Sell a product bundle
- **Path (checked on v16.55):** https://your-site/desk → type *Product Bundle* in the search bar at the top and open the doctype
- **Record type:** Product Bundle
- **Documented steps:**
  1. Go to the Product Bundle list, click on Add Product Bundle
  2. Select a Parent Item, create one if not already created. Make sure Maintain Stock unchecked when creating a Parent Item. eg: Dinner Set
  3. Enter a price for the parent item, this will be fetched when making a transaction
  4. You can enter a description for internal use
  5. Enter the products to be bundled in the Items table and enter their quantities
  6. Save
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-44.md` lines 717–794  (https://docs.frappe.io/erpnext/product-bundle)

### Manage units of measure
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Stock > Setup > Unit of Measure (UOM)**, or type *UOM* in the search bar at the top
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-66.md` lines 918–935  (https://docs.frappe.io/erpnext/uom)

### Set up warehouses
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Stock > Warehouse**, or type *Warehouse* in the search bar at the top
- **Record type:** Warehouse
- **Documented steps:**
  1. Go to the Warehouse list, click on New
  2. Enter a name for the Warehouse
  3. Set/check the Parent Warehouse. If you tick on 'Is Group', you can create sub-Warehouses under this group Warehouse
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-67.md` lines 667–745  (https://docs.frappe.io/erpnext/warehouse)

### Make a stock entry
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Manufacturing > Stock Entry**, or type *Stock Entry* in the search bar at the top
- **Record type:** Stock Entry
- **Documented steps:**
  1. Go to the Stock Entry list, click on New
  2. Select the Stock Entry Purpose from the ones listed above
  3. If you set the Default Source or Target Warehouses, they'll be automatically filled for the rows in the Items table
  4. Source/Target Warehouses will be available as per the Stock Entry Purpose you selected
  5. Select Items and enter a quantity
  6. The basic rate will be fetched and the amount will be calculated automatically
  7. Save and Submit
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-59.md` lines 568–752  (https://docs.frappe.io/erpnext/stock-entry)

### Reconcile physical stock
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Stock > Stock Reconciliation**, or type *Stock Reconciliation* in the search bar at the top
- **Record type:** Stock Reconciliation
- **Documented steps:**
  1. Go to the Stock Reconciliation list, click on New
  2. Select the Purpose as 'Opening Stock'. You can edit the posting Date and Time
  3. Select Item Code, Warehouse, Quantity, and Valuation Rate. If there is a Serial / Batch No involved, add it
  4. If you want to auto-generate Serial No / Batch No. then keep those fields blank
  5. The Difference Account will be set as 'Temporary Opening'
  6. Save and Submit
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-60.md` lines 39–164  (https://docs.frappe.io/erpnext/stock-reconciliation)

### Load opening stock
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Stock > Stock Reconciliation**, or type *Stock Reconciliation* in the search bar at the top
- **Documented steps:**
  1. Go to Stock > Stock Transactions > Stock Entry > New
  2. Select 'Material Receipt' in 'Stock Entry Type'
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-39.md` lines 683–723  (https://docs.frappe.io/erpnext/opening-stock)

### Track batches
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Stock > Serial & Batch > Batch No**, or type *Batch* in the search bar at the top
- **Record type:** Batch
- **Documented steps:**
  1. Go to the Batch list, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-09.md` lines 522–608  (https://docs.frappe.io/erpnext/batch)

### Track serial numbers
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Stock > Serial & Batch > Serial No**, or type *Serial No* in the search bar at the top
- **Record type:** Serial No
- **Documented steps:**
  1. Go to the Serial Number list, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-57.md` lines 48–144  (https://docs.frappe.io/erpnext/serial-no)

### Use the serial and batch bundle
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Stock > Serial & Batch > Serial and Batch Bundle**, or type *Serial and Batch Bundle* in the search bar at the top
- **Documented steps:**
  1. User has enabled *Use Serial / Batch Fields* in Stock Settings
  2. User wants to create the Serial and Batch Bundle per single batch
  3. User has set the auto-create batch in the Item master
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-56.md` lines 504–635  (https://docs.frappe.io/erpnext/serial-and-batch-bundle)

### Reserve stock for an order
- **Path (checked on v16.55):** https://your-site/desk → type *Stock Reservation Entry* in the search bar at the top and open the doctype
- **Documented steps:**
  1. Stock Unreservation from Sales Order or Pick List
  2. Unreserve the stock from the Stock Reservation Entry DocType
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-60.md` lines 380–437  (https://docs.frappe.io/erpnext/stock-reservation)

### Set putaway rules
- **Path (checked on v16.55):** https://your-site/desk → type *Putaway Rule* in the search bar at the top and open the doctype
- **Record type:** Putaway Rule
- **Documented steps:**
  1. Go to the Putaway Rule list, click on New
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-48.md` lines 418–520  (https://docs.frappe.io/erpnext/putaway-rule)

### Inspect incoming quality
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Quality > Quality Inspection**, or type *Quality Inspection* in the search bar at the top
- **Record type:** Quality Inspection
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-48.md` lines 566–701  (https://docs.frappe.io/erpnext/quality-inspection)

### Configure stock settings
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Setup > Settings > Stock**, or type *Stock Settings* in the search bar at the top
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-60.md` lines 439–643  (https://docs.frappe.io/erpnext/stock-settings)

### Read the stock ledger
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Stock > Reports > Stock Ledger**, or type *Stock Ledger* in the search bar at the top
- **Full page, bundled offline:** `docs/erpnext/erpnext-59.md` lines 773–815  (https://docs.frappe.io/erpnext/stock-ledger)

### Check stock levels
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Stock > Reports > Stock Projected Qty**, or type *Stock Projected Qty* in the search bar at the top
- **On this screen:** Stock Balance and Warehouse Wise Stock Balance are the other stock-level reports on v16.
- **Full page, bundled offline:** `docs/erpnext/erpnext-59.md` lines 817–844  (https://docs.frappe.io/erpnext/stock-level-report)

### Close a stock period
- **Path (checked on v16.55):** https://your-site/desk → type *Stock Closing Entry* in the search bar at the top and open the doctype
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-59.md` lines 490–512  (https://docs.frappe.io/erpnext/stock-closing-entry)

## What cannot be done in the interface

- Choose a valuation method — an explanation, not an action (guide.md)
- Run perpetual inventory — an explanation, not an action (guide.md)
