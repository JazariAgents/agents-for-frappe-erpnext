---
title: "Notification Configuration"
space: "Cloud"
url: "https://docs.frappe.io/cloud/server-notification-configuration"
updated: "2026-02-16"
---

You can configure multiple notifications at the server level to ensure that alerts are delivered through the right channels.

### Accessing Notification Settings

- Go to Server Overview → Application Server Actions.
- Under Notification Settings, click `Manage` to open the configuration screen.


![](/files/Screenshot%202025-10-06%20at%2015-51-41%20Settings%20-%20Profile.png)

### Configuring Notifications

The Notification Configuration screen allows you to set up how and where notifications are sent.


![](/files/Screenshot%202025-10-06%20at%2015-52-53%20Settings%20-%20Profile.png)

### Notification Flow Logic

The notification delivery follows a top-down hierarchy:

- Check if a specific notification type (e.g., Billing, Incident) is configured.
- If not found, use the General notification configuration.
- If General is also not configured, fallback to the Team-level configuration.


![](/files/shapes%20at%2025-10-06%2015.57.22.png)