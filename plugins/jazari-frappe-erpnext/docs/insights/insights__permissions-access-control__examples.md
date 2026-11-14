---
title: "Examples"
space: "Insights"
url: "https://docs.frappe.io/https://docs.frappe.io/insights/permissions-access-control/examples"
updated: "2026-01-06"
---

## Use Cases & Examples

### Use Case 1: Sales Team - Territory-Based Access

**Scenario**: Sales reps should only see customers in their assigned territory.

**Setup:**
1. Create team: "Sales Team North"
2. Add team members: northern sales reps
3. Grant access to `customers` table
4. Set table restriction:
   ```python
   territory == 'North'
   ```

**Result**: Team members only see customers where `territory = 'North'`

---

### Use Case 2: Sales Rep - Individual Assignment

**Scenario**: Each sales rep should only see their assigned customers and their sales data.

**Setup:**
1. Create team: "Sales Representatives"
2. Add all sales reps as members
3. Grant access to tables:
   - `customers`
   - `sales_orders`
4. Set table restrictions:

   For `customers` table:
   ```python
   sales_person == frappe.session.user
   ```

   For `sales_orders` table:
   ```python
   sales_person == frappe.session.user
   ```

**Result**:
- John (john@company.com) only sees customers/orders where `sales_person = 'john@company.com'`
- Jane (jane@company.com) only sees customers/orders where `sales_person = 'jane@company.com'`

---

### Use Case 3: Manager - Team View

**Scenario**: Sales managers should see all data for their team members.

**Setup:**
1. Create team: "Sales Managers West"
2. Add managers as members
3. Grant access to same tables as reps
4. Set table restrictions:

   For `customers` table:
   ```python
   sales_person_region == 'West'
   ```

   Or if you have a manager column:
   ```python
   manager == frappe.session.user
   ```

**Result**: Managers see all their team's data, reps see only their own.

---

### Use Case 4: Finance Team - AR Visibility

**Scenario**: AR team should see all invoices, but only for active customers.

**Setup:**
1. Create team: "Accounts Receivable"
2. Add AR team members
3. Grant access to:
   - `customers`
   - `sales_invoices`
   - `payments`
4. Set table restrictions:

   For `customers` table:
   ```python
   status == 'Active' AND outstanding_amount > 0
   ```

   For `sales_invoices` table:
   ```python
   status != 'Paid' AND due_date IS NOT NULL
   ```

**Result**: AR team sees all unpaid invoices for active customers.

---

### Use Case 5: Multi-Company Access

**Scenario**: Users should only see data for their assigned company/branch.

**Setup:**
1. Create teams per company: "Company A Team", "Company B Team"
2. Grant access to shared tables
3. Set table restrictions:

   ```python
   company == 'Company A'
   ```

**Result**: Users in "Company A Team" only see Company A data across all tables.

---

### Use Case 6: Time-Based Access

**Scenario**: Analysts should only see recent data.

**Setup:**
1. Create team: "Junior Analysts"
2. Grant access to transaction tables
3. Set table restrictions:

   ```python
   transaction_date >= '2024-01-01'
   ```

**Result**: Analysts can't see historical data older than specified date.
