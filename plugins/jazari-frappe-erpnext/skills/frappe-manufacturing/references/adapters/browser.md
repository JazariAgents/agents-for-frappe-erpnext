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
- **Path:** https://your-site/app → **Home > Manufacturing > Bill of Materials > Bill of Materials**
- **Record type:** BOM
- **Documented steps:**
  1. Go to the Bill of Materials list, click on New
  2. Select the Item to be manufactured. The Item name, UoM, company, and currency will be fetched automatically
  3. Enter the quantity of the Item that will be manufactured from this Bill of Materials
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__bill-of-materials.md`  (https://docs.frappe.io/erpnext/bill-of-materials)

### Design a BOM with the BOM creator
- **Path:** open https://your-site/app (the Desk) and find *Multi-level BOM Creator* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__bom-creator.md`  (https://docs.frappe.io/erpnext/bom-creator)

### Update BOMs in bulk
- **Path:** https://your-site/app → **Home > Manufacturing > Tools > BOM Update Tool**
- **Record type:** BOM Update Tool
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__bom-update-tool.md`  (https://docs.frappe.io/erpnext/bom-update-tool)

### Run a work order
- **Path:** https://your-site/app → **Home > Manufacturing > Production > Work Order**
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
- **Full page, bundled offline:** `docs/erpnext/erpnext__work-order.md`  (https://docs.frappe.io/erpnext/work-order)

### Record work on a job card
- **Path:** https://your-site/app → **Home > Manufacturing > Production > Job Card**
- **Record type:** Job Card
- **Documented steps:**
  1. Click on the Start Job button, then on Complete Job when you're done
  2. Alternatively, you can also fill the From Time and To Time in the Time Logs table
  3. Select the Employee to whom the Job Card was assigned
  4. Enter the Completed Quantity. This is the number of Items on which the Operation was performed for the selected time interval
  5. Add more rows in the Time Logs table and record time using the Start/Completed buttons
  6. Click on Submit
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__job-card.md`  (https://docs.frappe.io/erpnext/job-card)

### Plan production
- **Path:** https://your-site/app → **Home > Manufacturing > Production > Production Plan**
- **Record type:** Production Plan
- **Documented steps:**
  1. Go to the Production Plan list, click on New
  2. Select whether to get items from a Sales Order or a Material Request
  3. Click on 'Get Items for Work Order' to fetch the items from the above Sales Orders. Items only for which a BOM is present will be fetched. !Get items for Production Plan
  4. On expanding a row in the Items to Manufacture table, you'll see an option to 'Include Exploded Items'. Ticking this includes raw materials of the sub-assembly items in the production process
  5. If "Consolidate Items" is ticked and saved, items with the same BOM are combined into a single item with the combined total planned quantity
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__production-plan.md`  (https://docs.frappe.io/erpnext/production-plan)

### Set up workstations
- **Path:** open https://your-site/app (the Desk) and find *Workstation* — the documentation page below shows the screen
- **Documented steps:**
  1. Go to the Workstation list, click on New
  2. Enter a name for the Workstation
  3. Under Operating Costs, enter operating component with the cost
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__workstation.md`  (https://docs.frappe.io/erpnext/workstation)

### Define operations and routing
- **Path:** open https://your-site/app (the Desk) and find *Routing* — the documentation page below shows the screen
- **Documented steps:**
  1. Go to the Routing list, click on New
  2. Enter a name for the Routing
  3. Enter the Operations in the BOM Operation table
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__routing.md`  (https://docs.frappe.io/erpnext/routing)

### Watch the plant floor
- **Path:** open https://your-site/app (the Desk) and find *Plant Floor* — the documentation page below shows the screen
- **Full page, bundled offline:** `docs/erpnext/erpnext__plant-floor.md`  (https://docs.frappe.io/erpnext/plant-floor)

### Handle scrap and disassembly
- **Path:** open https://your-site/app (the Desk) and find *Production Scrap Management* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__scrap-management.md`  (https://docs.frappe.io/erpnext/scrap-management)

### Configure manufacturing settings
- **Path:** https://your-site/app → **Home > Manufacturing > Settings > Manufacturing Settings**
- **Record type:** Manufacturing Settings
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/erpnext/erpnext__manufacturing-settings.md`  (https://docs.frappe.io/erpnext/manufacturing-settings)

## What cannot be done in the interface

- Plan material requirements — an explanation, not an action (guide.md)
- Plan capacity — an explanation, not an action (guide.md)
