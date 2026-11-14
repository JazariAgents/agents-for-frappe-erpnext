---
title: "In-Place Site Migration"
space: "Cloud"
url: "https://docs.frappe.io/cloud/site/site-migrations/in-place-site-migration"
updated: "2026-03-06"
---

In certain situations, you may need to manually run the `bench migrate` command for your site.

> **[Note]** This operation **does not create a backup** before running the migration. Proceed with caution and ensure you have a backup if required.

To run the migration:

1. Open your **Site** page.
2. Go to the **Migrations** tab.
3. Click **Trigger Migration**.
4. Select **In-Place Migrate Site** as the migration type.

Once triggered, that will run the equivalent of the `bench migrate` command on your site.

![](/files/image525c9e.png)

