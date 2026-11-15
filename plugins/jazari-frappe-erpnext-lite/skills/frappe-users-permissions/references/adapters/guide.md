# Guide adapter — Users, roles and permissions

## Contents

- what guided means here
- the topics, and what to check with the user

These are not buttons. They are decisions and concepts where Frappe's behaviour depends on a choice the
user has to make — and the wrong choice is expensive to reverse later. Claude explains the options from
the documentation, asks which case applies, and then acts through `api.md` or `browser.md` on the records
that follow from the answer.

## Topics

### Understand permission types
- **What the page says:** Custom Permission Types let you create permission flags beyond the built-in ones `read`, `write`, `create`, `delete`, `submit`). Use them for action-specific permissions like "approve record", "download file", or "impersonate user".
- **It covers:** How it works, Example: Creating an "approve" permission on Invoice, Step 1: Create the permission type (Developer), Step 2: Add permission checks in your code (Developer), Step 3: Assign to roles (System Manager), How to check the permission
- **Documented detail:**
  1. Developer creates the permission type in dev mode for a DocType
  2. Developer adds permission checks in code where the action happens
  3. System Manager assigns the permission to roles in the Desk UI
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/framework/framework-01.md` lines 2738–2815  (https://docs.frappe.io/framework/permission-types)

