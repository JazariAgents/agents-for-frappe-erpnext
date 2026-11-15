# Guide adapter — Manufacturing and production

## Contents

- what guided means here
- the topics, and what to check with the user

These are not buttons. They are decisions and concepts where Frappe's behaviour depends on a choice the
user has to make — and the wrong choice is expensive to reverse later. Claude explains the options from
the documentation, asks which case applies, and then acts through `api.md` or `browser.md` on the records
that follow from the answer.

## Topics

### Plan material requirements
- **What the page says:** The ERPNext currently have the MRP inside the production plan which is difficult for new users to understand and also it only uses sales order or material request data to generate the MRP.
- **It covers:** Purpose, Demand Planning, Sales Forecast, Delivery Schedules, Master Production Schedule, Material Requirements Planning Report, Item Lead Time
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/erpnext/erpnext__material-requirements-planning-mrp.md`  (https://docs.frappe.io/erpnext/material-requirements-planning-mrp)

### Plan capacity
- **What the page says:** Capacity Planning functionality helps you in tracking production jobs allocated on each Workstation.
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/erpnext/erpnext__capacity-planning.md`  (https://docs.frappe.io/erpnext/capacity-planning)

