---
title: "How to install a custom app"
space: "Cloud"
url: "https://docs.frappe.io/cloud/benches/custom-app"
updated: "2026-07-24"
---

You can use your custom version/fork of the vanilla Frappe Framework.

:::caution
We do not provide support for modified versions of the framework.
:::



You can do so by simply following the add app flow inside your Bench.

![Screenshot 2024-11-20 112324](/files/Screenshot 2024-11-20 112324.png "Screenshot 2024-11-20 112324.png")

This will replace the Vanilla Frappe Framework with your custom fork / version.

## Note

Please ensure, that the app being added, has a valid `pyproject.toml` file along with a key advertising the frappe version, like such:



`[tool.bench.frappe-dependencies]`  
`frappe = ">=16.0.0-dev,<17.0.0"`