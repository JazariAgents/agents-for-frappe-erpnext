# Interface adapter — Manufacturing and production

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

### Build a bill of materials
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Manufacturing > BOM**, or type *BOM* in the search bar at the top
- **Record type:** BOM
- **Documented steps:**
  1. Go to the Bill of Materials list, click on New
  2. Select the Item to be manufactured. The Item name, UoM, company, and currency will be fetched automatically
  3. Enter the quantity of the Item that will be manufactured from this Bill of Materials
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-09.md` lines 610–802  (https://docs.frappe.io/erpnext/bill-of-materials)

### Design a BOM with the BOM creator
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Manufacturing > Tools > BOM Creator**, or type *BOM Creator* in the search bar at the top
- **Record type:** BOM Creator
- **Two screens exist. Look before you click.** ERPNext 16.53 rebuilt this tool. If the form has a **Design File** field and the tabs Design, Costing and Details, it is the new one and the steps below apply. If it shows only a tree with an item dialog, the site is older: follow `docs/erpnext/erpnext-10.md` lines 683–728 instead.
- **Documented steps (new screen):**
  1. Go to the BOM Creator list and click Add BOM Creator
  2. In Finished Good, select the item that the design makes, and check that Company is correct
  3. Optional: attach a design file — a STEP file, or a CSV with the columns Level, Part Number and Quantity. Without one, build the tree by hand with **+** on each row
  4. Map each part to an item with Map Item, or create the missing items
  5. Change quantities, add materials that are not in the design (glue, paint, packing), remove parts that do not belong
  6. Choose how materials are costed on the Costing tab
  7. Submit, then click **Create BOMs**
- **What Create BOMs does:** in the background it makes and **submits** one BOM for every assembly in the tree, lowest level first. The line under the tree says how many. Tell the user that number and get a yes before clicking; submitted BOMs are cancelled, never edited.
- **Producing an item at each operation:** the tick box is labelled *Produce Item per Operation* or *Produce an Item at Each Operation* depending on the patch. Tick it only when each operation makes an item the user keeps in stock. It needs Operation and Workstation Type records, and creates a single BOM that lists the operations and what each one makes.
- **If it fails:** the status turns Failed, the reason is in Error Log on the Details tab, and no BOM from that run is kept. Fix the cause and click Create BOMs again.
- **Snapshot first** — reversibility: reversible until Create BOMs is clicked, irreversible after (the BOMs are submitted)
- **Full page, bundled offline:** `docs/erpnext/erpnext-10.md` lines 292–681  (https://docs.frappe.io/erpnext/bom-creator-new) — older screen: `docs/erpnext/erpnext-10.md` lines 683–728

### Update BOMs in bulk
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Manufacturing > Tools > BOM Update Tool**, or type *BOM Update Tool* in the search bar at the top
- **Record type:** BOM Update Tool
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-10.md` lines 827–887  (https://docs.frappe.io/erpnext/bom-update-tool)

### Run a work order
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Manufacturing > Work Order**, or type *Work Order* in the search bar at the top
- **Record type:** Work Order
- **Documented steps:**
  1. Go to the Work Order list, click on New
  2. Select the Item to be manufactured
  3. The default BOM for that item will be fetched by the system. You can also change the BOM
  4. Enter the quantity to manufacture. Raw material Items will be fetched only when this is set
  5. If the selected BOM has Operations mentioned in it, the system will fetch all Operations from BOM, these values can be changed. Refer section 3.2 to know more
  6. Set the Planned Start Date (an Estimated Date at which you want the Production to begin)
  7. Use Multi-Level BOM: This is enabled by default. If you want to plan materials for sub-assemblies of the Item you're manufacturing leave this enabled. If you plan and manufacture the sub-assemblies separately, you can disable this checkbox. To know more, visit this page
  8. Select Warehouses:
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-69.md` lines 147–379  (https://docs.frappe.io/erpnext/work-order)

### Record work on a job card
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Manufacturing > Job Card**, or type *Job Card* in the search bar at the top
- **Record type:** Job Card
- **Documented steps:**
  1. Click on the Start Job button, then on Complete Job when you're done
  2. Alternatively, you can also fill the From Time and To Time in the Time Logs table
  3. Select the Employee to whom the Job Card was assigned
  4. Enter the Completed Quantity. This is the number of Items on which the Operation was performed for the selected time interval
  5. Add more rows in the Time Logs table and record time using the Start/Completed buttons
  6. Click on Submit
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-34.md` lines 55–213  (https://docs.frappe.io/erpnext/job-card)

### Plan production
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Manufacturing > Production Plan**, or type *Production Plan* in the search bar at the top
- **Record type:** Production Plan
- **Documented steps:**
  1. Go to the Production Plan list, click on New
  2. Select whether to get items from a Sales Order or a Material Request
  3. Click on 'Get Items for Work Order' to fetch the items from the above Sales Orders. Items only for which a BOM is present will be fetched. !Get items for Production Plan
  4. On expanding a row in the Items to Manufacture table, you'll see an option to 'Include Exploded Items'. Ticking this includes raw materials of the sub-assembly items in the production process
  5. If "Consolidate Items" is ticked and saved, items with the same BOM are combined into a single item with the combined total planned quantity
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-45.md` lines 201–398  (https://docs.frappe.io/erpnext/production-plan)

### Set up workstations
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Manufacturing > Setup > Workstation**, or type *Workstation* in the search bar at the top
- **Documented steps:**
  1. Go to the Workstation list, click on New
  2. Enter a name for the Workstation
  3. Under Operating Costs, enter operating component with the cost
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-69.md` lines 729–858  (https://docs.frappe.io/erpnext/workstation)

### Define operations and routing
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Manufacturing > Setup > Routing**, or type *Routing* in the search bar at the top
- **Documented steps:**
  1. Go to the Routing list, click on New
  2. Enter a name for the Routing
  3. Enter the Operations in the BOM Operation table
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-51.md` lines 717–768  (https://docs.frappe.io/erpnext/routing)

### Watch the plant floor
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Manufacturing > Setup > Plant Floor**, or type *Plant Floor* in the search bar at the top
- **Full page, bundled offline:** `docs/erpnext/erpnext-43.md` lines 57–91  (https://docs.frappe.io/erpnext/plant-floor)

### Handle scrap and disassembly
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Manufacturing > BOM**, or type *BOM* in the search bar at the top
- **On this screen:** Scrap items are a table on the BOM; whether scrap is taken from the BOM is set in **Manufacturing Settings**.
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-55.md` lines 180–209  (https://docs.frappe.io/erpnext/scrap-management)

### Configure manufacturing settings
- **Path (checked on v16.55):** https://your-site/desk → **ERPNext > Manufacturing > Setup > Settings**, or type *Manufacturing Settings* in the search bar at the top
- **Record type:** Manufacturing Settings
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext-36.md` lines 807–962  (https://docs.frappe.io/erpnext/manufacturing-settings)

## What cannot be done in the interface

- Plan material requirements — an explanation, not an action (guide.md)
- Plan capacity — an explanation, not an action (guide.md)
