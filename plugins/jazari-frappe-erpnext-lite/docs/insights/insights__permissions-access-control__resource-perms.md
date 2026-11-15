---
title: "Resource Permissions"
space: "Insights"
url: "https://docs.frappe.io/https://docs.frappe.io/insights/permissions-access-control/resource-perms"
updated: "2026-01-06"
---

### What are Resources?

Resources that can be shared with teams:
- **Data Sources**: Database connections
- **Tables**: Individual tables within data sources
- **Dashboards**: Dashboard access
- **Charts**: Chart access
- **Workbooks**: Workbook access (through sharing)

### Granting Access to Data


![access-data](/files/SCR-20251027-dzex.png)

1. Click on a team
2. Go to the **Access** tab
3. Select data sources and/or specific tables
4. Click **Done** to save

### Access Patterns

#### Pattern 1: Full Data Source Access
Grant access to entire data source:
- User can query all tables in that data source
- Best for admins or broad access needs

#### Pattern 2: Specific Table Access
Grant access to individual tables:
- User can only query selected tables
- More granular control
- Better for restricted access

**Example:**
```
Sales Team West has access to:
  ✓ Data Source: Production Database
    ✓ Table: customers
    ✓ Table: orders
    ✓ Table: invoices
    ✗ Table: employee_salaries (not accessible)
```

---