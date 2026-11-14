---
title: "Table Restrictions"
space: "Insights"
url: "https://docs.frappe.io/https://docs.frappe.io/insights/permissions-access-control/table-restrictions"
updated: "2026-01-06"
---

## Row-Level Security (Table Restrictions)

### What are Table Restrictions?

Table restrictions are **filter expressions** that automatically limit which rows users can see in a table. This is the key feature for implementing "users can only see their own data" scenarios.

### How to Set Table Restrictions


![india-team](/files/SCR-20251027-dzbt.png)

1. Click on a team → **Access** tab
2. Select a data source to expand it
3. Check the tables you want to grant access to
4. Click **"Set Filters"** next to a table name
5. Enter a filter expression
6. Click **Done** to save

### Filter Expression Syntax

Expressions use Python-like syntax with table column names:

```python
# Basic equality
column_name == 'value'

# Multiple conditions
region == 'West' AND active == 1

# Comparisons
revenue > 100000

# String operations
customer_name.startswith('A')

# NULL checks
manager IS NOT NULL
```

---