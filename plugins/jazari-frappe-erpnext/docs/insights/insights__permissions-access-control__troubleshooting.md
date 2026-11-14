---
title: "Troubleshooting"
space: "Insights"
url: "https://docs.frappe.io/https://docs.frappe.io/insights/permissions-access-control/troubleshooting"
updated: "2026-01-06"
---

### Users can't see any data

**Check:**

1. Is permissions enabled? (Settings → Permissions)
2. Is user in a team?
3. Does team have access to the data source/table?
4. Are table restrictions too restrictive?
5. Test with admin account first

### Users see wrong data

**Check:**

1. Review table restriction expressions
2. Verify column names match database schema exactly
3. Check for typos in filter expressions
4. Test with SQL query directly


---

## Security Considerations

### What Permissions DON'T Protect

- **Direct database access**: Permissions only apply within Insights
- **API access**: If users can access backend APIs directly
- **Exported data**: Once data is exported (CSV, Excel), filters don't apply
- **Shared workbooks**: Sharing bypasses team permissions

### What Permissions DO Protect

- All queries created within Insights
- Dashboard and chart views
- Data exploration and query builder
- API calls through Insights frontend