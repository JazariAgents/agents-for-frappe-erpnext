<!-- Frappe documentation: erpnext, part 7 of 18. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__energy-point-system.md -->
---
title: "Energy Point System"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/energy-point-system"
updated: "2026-05-28"
---

**Energy Points System is a gamification of user engagement to recognize and incentivize users for their contributions and activities within ERPNext.**

 

This system can be used to track the performance of each user.

 

> To enable Energy Point System go to
>
> **Energy Point Settings** > **Enabled**

 

## How to use the Energy Point System?

---

 To start using this system you need to create some Energy Point Rules (see section 3. How to create Energy Point Rules?) so that users can get energy points based on their activities.

## What are Energy Point Rules?

---

Energy Point Rules store the information about the activity and the value of points to be allocated.

 

Energy Point Rule has the following fields: 


| Field                          | Description                                                                                                                                                                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reference DocType              | Document Type you want to apply the rule on eg. Task, ToDo, Issue, etc.                                                                                                                                                       |
| For Document Event             | Options: Save, Submit, Cancel, and Custom.**Note:** If "Custom" option is selected then the "Conditions" field becomes mandatory                                                                                              |
| Points                         | Points to be allocated.                                                                                                                                                                                                       |
| Allot Points To Assigned Users | If checked, users assigned to the reference document will get respective points. eg. If users Santosh and Albert are assigned to a particular task then both of them will get points when the document fulfills the condition |
| User Field                     | Field from which user will be selected eg. `Resolved By`, `Modified By`, `Owner`, etc. can be used. If `Modified By` is selected, the last person to satisfy the doc condition will get the points.                           |
| Multiplier Field               | Field which stores value for the multiplier. This field can take numeric and decimal values which will be multiplied with points defined in the rule. For example: 2 (multiplier) * 10 (points set in the rule) = 20 points   |
| Condition                      | Condition for the point allocation. eg. `doc.status == 'Closed'`The above condition will check whether the `status` field in the document is 'Closed' and if yes then the points will be allocated to the user.               |
| Apply Only Once                | The rule will be applied only once per document.                                                                                                                                                                              |
|                                |                                                                                                                                                                                                                               |


 

## How to create Energy Point Rules? 

---

 Search for **Energy Point Rule** > create new Energy Point Rule

 

Take a look at the following example rule:  

![](/files/image13b0d0.png)

The screenshot above is the rule for **Issue Closing**. So when any user closes the issue he/she will be rewarded with **10** points.

 

Other cases can be covered similarly.

 

Suppose, you want to create a rule where a user gets points on completing a task, you can do so by creating following rule   

![](/files/image1d19dd.png)

## Features 

---

### 4.1 Auto Point allocation

Based on energy point rules created, users will automatically get points when they complete activities which are tracked using the Energy Point System. 

### 4.2 Review System

Review system can be used to "Appreciate" or "Criticize" someone's work, check out the following GIF for the review process.

![](/files/review-system.gif)

   

For reviewing, the user needs to have review points which can be assigned by System Manager through **Energy Point Settings**.

 

You can also setup auto review point allocation from 'Energy Point Settings':   

![](/files/imaged9995e.png)

### 4.3 Leaderboard

> Go to Social Home > Leaderboard (side navigation bar)

The leaderboard shows the user's standing in the organization.

![](/files/leaderboard.png)

### 5. Related Topics

1. [Milestone Tracking](/erpnext/milestone-tracker)

<!-- page: erpnext/erpnext__erpnext-chat-with-raven.md -->
---
title: "ERPNext Chat with Raven"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/erpnext-chat-with-raven"
updated: "2026-07-05"
---

ERPNext Chat is deprecated and should not be used for new implementations. If your organization needs instant messaging, team channels, document sharing, and collaboration inside the Frappe ecosystem, use **Raven** instead.

Raven is a Frappe app for team messaging. It works as an open-source Slack alternative and can be installed on the same site as ERPNext and other Frappe apps. This makes it a good option for organizations that want internal communication to stay close to their business data and workflows.

## Why Use Raven

Raven helps teams communicate in real time without leaving the Frappe ecosystem. Teams can create channels, send direct messages, share files, mention users, react to messages, and search conversations.

It is especially useful for organizations using ERPNext because discussion can happen around actual work: customers, sales orders, invoices, issues, projects, tasks, and other business documents.

## Key Features

- **Channels and direct messages:** Create public or private channels for teams, departments, projects, or topics.
- **Rich messaging:** Send formatted messages, links, code blocks, emojis, mentions, replies, and reactions.
- **File sharing:** Share images, documents, PDFs, and other files directly in conversations.
- **Search:** Search messages, channels, files, and users.
- **Mobile-friendly:** Raven is designed for collaboration on desktop and mobile.
- **Dark mode:** Users can choose a comfortable interface for daily communication.

## ERPNext And Frappe Native Features

Raven is more than a standalone chat tool. Since it is built on Frappe, it can work closely with ERPNext and other Frappe apps.

Useful ERPNext-native capabilities include:

- Share ERPNext documents in Raven conversations.
- Send messages to channels from the Desk interface.
- Link messages to documents so the discussion context is available from the document timeline.
- Trigger notifications based on document events.
- Use document previews when sharing ERPNext records.
- Perform workflow-related actions from conversations where supported.
- Keep collaboration connected to business records instead of scattered across external chat tools.

This makes Raven useful for teams that want conversations to remain connected to actual ERPNext work instead of living separately in another system.

## When To Use Raven

Use Raven when your organization needs:

- Internal team messaging.
- Department or project channels.
- ERPNext-related discussions around documents and transactions.
- A Frappe-native alternative to Slack.
- A self-hostable or Frappe Cloud-hosted communication tool.
- Better context between chat, documents, and workflows.

## Installation And Source Code

You can install Raven from the Frappe Cloud Marketplace:

- [Raven on Frappe Cloud Marketplace](https://cloud.frappe.io/marketplace/apps/raven)

The source code is available on GitHub:

- [Raven GitHub Repository](https://github.com/The-Commit-Company/raven)

## Related Topics

- [ERPNext](https://docs.frappe.io/erpnext)
- [Frappe Framework](https://docs.frappe.io/framework)
- [Raven on Frappe Cloud Marketplace](https://cloud.frappe.io/marketplace/apps/raven)
- [Raven GitHub Repository](https://github.com/The-Commit-Company/raven)

<!-- page: erpnext/erpnext__erpnext-dashboards.md -->
---
title: "ERPNext Dashboards"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/erpnext-dashboards"
updated: "2026-07-05"
---

ERPNext includes dashboards, analytics pages, reports, and workspaces that help teams monitor business activity across modules. These views bring important information into one place so users can review trends, exceptions, transactions, and operational status without opening each document individually.

Dashboards are useful for day-to-day monitoring, while reports and analytics pages are useful for deeper review. In practice, most ERPNext teams use a combination of module workspaces, dashboards, and reports.

## Accounting Dashboard And Reports

The Accounting dashboard and reports help finance teams track receivables, payables, profitability, taxes, ledgers, and financial statements.

- [Accounting Reports](/erpnext/accounting-reports): Index of standard accounting reports.
- [Financial Report Template](/erpnext/financial-report-template): Configure custom financial report layouts.
- [Budget Variance Report](/erpnext/budget-variance-report): Compare budgets with actual values.
- [Deferred Revenue/Expense Report](/erpnext/expense_report): Review deferred revenue and expense schedules.
- [Customise Cash Flow Report](/erpnext/customise-cash-flow-report): Customize cash flow reporting.
- [VAT Audit Report](/erpnext/vat_audit_report): Review VAT audit reporting.
- [UAE VAT 201 Report](/erpnext/uae-vat-201-report): Review UAE VAT reporting.

## Selling Dashboard And Sales Analytics

Selling dashboards and reports help teams review sales performance, quotations, sales orders, invoices, customers, and sales trends.

- [Sales Reports](/erpnext/sales-analytics): Review sales analytics and sales reports.
- [Payment Terms Status Report](/erpnext/payment_terms_status_report): Track payment term status for transactions.
- [Brandwise Items and Profitability Report](/erpnext/brandwise-items-and-profitability-report): Analyze profitability by brand and item.
- [Setting Company Sales Goal](/erpnext/setting-company-sales-goal): Set and track company sales goals.

## Buying Dashboard And Purchase Reports

Buying dashboards and reports help procurement teams monitor purchase activity, suppliers, purchase orders, pending receipts, and procurement performance.

- [Buying Reports](/erpnext/buying_reports): Review buying and purchase-related reports.
- [Procurement Tracker Report](/erpnext/procurement-tracker-report): Track procurement progress.
- [Supplier Scorecard](/erpnext/supplier-scorecard): Evaluate supplier performance.

## Stock Dashboard And Inventory Reports

Stock dashboards and reports help inventory teams track stock levels, valuation, ledger movement, batches, serial numbers, and stock reconciliation.

- [Stock Level Report](/erpnext/stock-level-report): Review current stock levels.
- [Stock Ledger Report](/erpnext/stock-ledger): Review stock ledger entries and stock movement.
- [Stock Value and Account Value Comparison Report](/erpnext/stock-value-account-value-comparison): Compare stock value with accounting value.
- [Stock Ledger Variance Report](/erpnext/stock-reposting): Review stock ledger variance and reposting.
- [Serial No and Batch Traceability Report](/erpnext/serial-and-batch-traceability-report): Trace serial numbers and batches.
- [Negative Batch Report](/erpnext/stock/reports/negative-batch-report): Identify negative batch quantity issues.

## Manufacturing Dashboard And Reports

Manufacturing dashboards and reports help production teams monitor work orders, production planning, BOMs, operations, and material requirements.

- [Manufacturing Dashboard](/erpnext/manufacturing-dashboard): Review manufacturing activity in a dashboard-style view.
- [Manufacturing Reports](/erpnext/manufacturing-reports): Index of manufacturing reports.
- [Production Analytics](/erpnext/production-analytics): Analyze production trends.
- [Production Planning Report](/erpnext/production-planning-report): Review production planning data.
- [Open Work Order Report](/erpnext/open-work-orders): Track open work orders.
- [BOM Stock Report](/erpnext/bom-stock-report): Review BOM-related stock availability.
- [Item Where Used Report](/erpnext/item-where-used-report): Find where an item is used in BOMs.

## CRM Dashboard And Reports

CRM dashboards and analytics help sales teams monitor leads, opportunities, campaigns, pipeline movement, and customer interactions.

- [CRM Analytics](/erpnext/sales_funnel): Review sales funnel and CRM analytics.
- [CRM Reports](/erpnext/crm_reports): Index of CRM reports.
- [CRM Settings](/erpnext/crm_settings): Configure CRM behavior before using CRM dashboards and reports.

## Projects Dashboard And Reports

Project dashboards and reports help teams monitor project progress, profitability, tasks, timesheets, and billing.

- [Project Reports](/erpnext/project-reports): Review project-related reports.
- [Project Profitability Report](/hr/project-profitability-report): Analyze project profitability.
- [Project Settings](/erpnext/projects/project-settings): Configure project behavior before using project reports.

## Support Dashboard And Reports

Support dashboards and reports help service teams monitor issues, support workload, maintenance activity, and customer support performance.

- [Support Reports](/erpnext/support_reports): Review support-related reports.
- [Support Settings](/erpnext/support-settings): Configure support behavior before using support dashboards and reports.
- [Maintenance Visit](/erpnext/maintenance-visit): Track maintenance visits and service activity.

## Asset Dashboard And Reports

Asset dashboards and reports help finance and operations teams review fixed assets, depreciation, asset movement, and asset accounting.

- [Asset Reports](/erpnext/asset-reports): Review asset-related reports.
- [Using Finance Book for Asset Depreciation](/erpnext/using-finance-book-for-asset-depreciation): Understand depreciation reporting by finance book.

## HR And Payroll Dashboards

HR and payroll dashboards and reports help teams monitor employees, leave, attendance, appraisals, salary structures, payroll, and compliance.

- [Human Resources Reports](/hr/human-resources-reports): Review HR reports.
- [HR Reports](/hr/reports): Index of HR reports.
- [Appraisal Overview Report](/hr/appraisal-overview-report): Review appraisal progress and status.
- [Leave Ledger Report](/hr/leave-ledger-report): Review leave ledger entries.
- [Employee CTC Break-Up](/hr/reports/employee-ctc-break-up): Review employee cost-to-company details.
- [India Payroll Reports](/hr/india-payroll/reports): Review India payroll reports.

## Loan And Lending Dashboards

Lending dashboards and reports help teams monitor loan applications, disbursements, repayments, outstanding balances, securities, and cash flow.

- [Lending Reports](/lending/lending-reports): Index of lending reports.
- [Loan Outstanding Report](/lending/loan-outstanding-report): Review outstanding loan balances.
- [Future Cashflow Report](/lending/future-cashflow-report): Review expected future cash flows.
- [Past Cashflow Report](/lending/past-cashflow-report): Review past cash flows.
- [Loan Statement of Account](/lending/loan-management/lending-reports/loan-statement-of-account): Review statement of account for loans.
- [Loan Repayment and Closure](/lending/loan-management/lending-reports/loan-repayment-and-closure): Track repayment and closure details.
- [Loan Security Status](/lending/loan-management/lending-reports/loan-security-status): Review loan security status.
- [Loan Security Exposure](/lending/loan-management/lending-reports/loan-security-exposure): Review exposure against securities.
- [Credit Reporting](/lending/credit-reporting): Review credit reporting tools.

## Analytics And Custom Dashboards

ERPNext also works with reporting and dashboard tools in the Frappe ecosystem. These are useful when a standard report is not enough and a team needs custom charts, grouped metrics, or cross-module analysis.

- [ERPNext Analytics](/erpnext/analytics): Review analytics features in ERPNext.
- [Insights Dashboards](/insights/dashboards): Build dashboards using Frappe Insights.
- [Insights Dashboard Overview](/insights/dashboards/overview): Understand dashboard concepts in Insights.
- [Creating Your First Dashboard](/insights/dashboards/creating-your-first-dashboard): Create a custom dashboard in Insights.
- [Sharing and Access Control](/insights/dashboards/sharing-and-access-control): Control who can view dashboards.
- [Desk Reports](/framework/desk---reports): Understand report types in Frappe Desk.
- [Report Builder](/framework/user/en/desk/reports/report-builder): Create reports without code.
- [Query Report](/framework/user/en/desk/reports/query-report): Create SQL-based reports.
- [Script Report](/framework/user/en/desk/reports/script-report): Create script-based reports.
- [Workspace](/framework/user/en/desk/workspace): Use workspaces to organize module-level shortcuts, charts, and links.

## Choosing The Right Dashboard

Use a module dashboard or report when you want to monitor a specific area of ERPNext:

1. Use [Accounting Reports](/erpnext/accounting-reports) for financial review.
2. Use [Sales Reports](/erpnext/sales-analytics) for sales performance.
3. Use [Buying Reports](/erpnext/buying_reports) for procurement tracking.
4. Use [Stock Level Report](/erpnext/stock-level-report) and [Stock Ledger Report](/erpnext/stock-ledger) for inventory monitoring.
5. Use [Manufacturing Dashboard](/erpnext/manufacturing-dashboard) and [Production Analytics](/erpnext/production-analytics) for production review.
6. Use [Project Reports](/erpnext/project-reports) for project tracking.
7. Use [Support Reports](/erpnext/support_reports) for customer support review.
8. Use [Insights Dashboards](/insights/dashboards) when you need custom dashboards across modules.

## Related Topics

- [ERPNext Analytics](/erpnext/analytics)
- [Accounting Reports](/erpnext/accounting-reports)
- [Sales Reports](/erpnext/sales-analytics)
- [Buying Reports](/erpnext/buying_reports)
- [Manufacturing Dashboard](/erpnext/manufacturing-dashboard)
- [Project Reports](/erpnext/project-reports)
- [Support Reports](/erpnext/support_reports)
- [Desk Reports](/framework/desk---reports)
- [Workspace](/framework/user/en/desk/workspace)
- [Insights Dashboards](/insights/dashboards)

<!-- page: erpnext/erpnext__erpnext-for-services-organization.md -->
---
title: "ERPNext for Service Organization\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/erpnext-for-services-organization"
updated: "2026-07-23"
---

# ERPNext for Service Organization

ERPNext supports service organizations such as software companies, certification providers, agencies, professional-services firms, and independent consultants. You can use it to manage sales, accounting, projects, support, assets, and—when Frappe HR is installed—HR operations without running a warehouse-based fulfillment process for every sale.

The main difference from a trading or manufacturing setup is that services are normally configured as non-stock Items. A service Sales Order can then be invoiced without a Delivery Note and marked **Completed** after it is fully billed.

The original overview of how the ERPNext team used ERPNext for its own service-business operations is retained below:

<iframe src="https://www.youtube.com/embed/b6r7WxJMfFA" title="How ERPNext uses ERPNext for service-business operations" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0"></iframe>

## Before you begin

Set up the following records:

- a [Company](/erpnext/company) with its Chart of Accounts and default currency;
- a [Customer](/erpnext/customer) for each organization you serve;
- one or more non-stock service [Items](/erpnext/item);
- income accounts, taxes, payment terms, and Cost Centers required by your accounting process;
- [Projects](/erpnext/project) and [Timesheets](/erpnext/timesheet) when you bill or measure work by project or time.

Decide whether you will bill a fixed fee, recurring amount, milestone, or time and expenses. That decision affects the Items, Sales Orders, Projects, and invoicing process you configure.

## Create a service Item

Use a non-stock Item for consulting, implementation, support, subscriptions, or other work that does not move through a Warehouse.

1. Open **Item** and select **Add Item**.
2. Enter an Item Code and Item Name that describe the service.
3. Disable **Maintain Stock**.
4. Select an Item Group and the default unit of measure, such as **Nos** or **Hour**.
5. Under accounting defaults, select the appropriate income account when your setup requires one.
6. Save the Item.

![The Item form configured for a service by disabling Maintain Stock.](/files/service-item.png)

A non-stock service Item does not require a source Warehouse and does not create stock-ledger entries. You can still use quantities, rates, taxes, and accounting dimensions on sales transactions.

## Sell and invoice a service

The recommended flow for an agreed service is:

**[Quotation](/erpnext/quotation) → [Sales Order](/erpnext/sales-order) → [Sales Invoice](/erpnext/sales-invoice) → [Payment Entry](/erpnext/payment-entry)**

A Quotation is optional when the Customer has already confirmed the work.

### Complete a Sales Order without a Delivery Note

Use this flow when the service does not require a stock or delivery transaction:

1. Create a Sales Order and select the Customer.
2. Set **Order Type** to **Maintenance**.
3. Enable **Skip Delivery Note**.
4. Add the non-stock service Item, quantity, rate, taxes, payment terms, and commercial terms.
5. Save and submit the Sales Order.
6. From the submitted Sales Order, select **Create > Sales Invoice**.
7. Review and submit the Sales Invoice.

When **Skip Delivery Note** is enabled, delivery is not required for the order. After the Sales Invoice bills the full ordered quantity, ERPNext sets the Sales Order to **Completed**. If you invoice only part of the order, it remains open until the remaining quantity is billed or the order is closed.

Use a normal Delivery Note flow when the order includes physical goods that must leave a Warehouse. For an order containing both services and stock Items, choose the workflow that preserves the required stock movement and audit trail.

## Track delivery through Projects and Timesheets

Create a Project when the service has tasks, milestones, budgets, or a defined delivery period. Link the Sales Order and subsequent transactions to the Project so revenue and costs can be reviewed together.

Use Timesheets when employees record billable or non-billable hours. Depending on the commercial model, you can invoice time through the relevant project-and-timesheet billing workflow instead of using only a fixed-quantity service Item.

Service organizations can also use [Issues](/erpnext/issue) for customer support, Service Level Agreements for response commitments, and Maintenance Visits or Schedules when work is performed at planned intervals.

## Manage equipment and fixed assets

A service company may still purchase and track physical assets such as laptops, servers, furniture, or test equipment. Configure those purchases and [Assets](/erpnext/asset) separately from the non-stock Items sold to Customers.

Use stock Items only when you genuinely need inventory quantities and Warehouse movements. An office asset does not need to become a sales Item merely because the company owns it.

## Hide workspaces you do not use

Service organizations may not need Manufacturing, Stock, or other operational workspaces. Keep the interface focused by controlling workspace visibility and user roles:

- assign each user only the roles required for their work;
- remove Stock or Manufacturing roles from users who should not use those modules;
- configure workspace visibility or customize the workspace when your version supports it.

The older **Setup > Permissions > Show/Hide Modules** instruction may appear in legacy documentation. In current ERPNext versions, use role-based permissions and workspace configuration available on your site.

## Configure permissions

ERPNext is role- and permission-controlled. A hidden workspace is not a substitute for access control: use [Role Permissions Manager](/erpnext/role-permission-manager) to define which documents a role can read, create, submit, amend, or cancel.

Test permissions using a non-administrator account that has the same roles as the intended user. Confirm both what the user can see and what the user can do.

The existing permissions walkthrough is retained below:

<iframe src="https://www.youtube.com/embed/8Slw1hsTmUI" title="ERPNext user and permissions setup video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0"></iframe>

## Troubleshooting

### A Warehouse is required for a service Item

Open the Item and confirm that **Maintain Stock** is disabled. Also confirm that the Sales Order row contains the intended service Item rather than a stock Item with a similar name.

### Skip Delivery Note is not visible

Set the Sales Order **Order Type** to **Maintenance**. The checkbox is conditional and does not appear for every order type.

### The Sales Order is not Completed after invoicing

Confirm that **Skip Delivery Note** was enabled and that the Sales Invoice was submitted for the full ordered quantity. Review the Sales Order's billing percentage and linked invoices. A partial or draft invoice does not complete the order.

### A user can still access an unwanted module

Review the user's assigned roles and Role Permission Manager settings. Workspace visibility affects navigation, while document permissions control access.

## Frequently asked questions

### Do service organizations need Warehouses?

Not for non-stock services. Warehouses are still useful when the company buys, stores, or sells physical Items.

### Must every service sale use a Sales Order?

No. You can create a Sales Invoice directly when your process does not require a confirmed-order stage. Use a Sales Order when you need to record scope, value, terms, or progress before billing.

### Should every service Sales Order use Maintenance order type?

Use **Maintenance** with **Skip Delivery Note** for the delivery-free completion flow described here. If the transaction includes physical fulfillment, use the order type and delivery process appropriate to that sale.

## Related topics

- [Item](/erpnext/item)
- [Sales Order](/erpnext/sales-order)
- [Maintenance Sales Orders](/erpnext/maintenance-sales-orders)
- [Sales Invoice](/erpnext/sales-invoice)
- [Project](/erpnext/project)
- [Timesheet](/erpnext/timesheet)
- [Role Permission Manager](/erpnext/role-permission-manager)

<!-- page: erpnext/erpnext__erpnext_integration.md -->
---
title: "Integration Categories"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/erpnext_integration"
updated: "2026-02-26"
---

ERPNext provides a wide range of integration capabilities that allow businesses to seamlessly connect with various third-party applications and services to enhance operational efficiency and data flow. 

These integrations span across e-commerce platforms, payment gateways, shipping providers, Google services, e-commerce providers, etc. By integrating ERPNext with these systems, businesses can streamline their processes, reduce manual data entry, improve data accuracy, and gain deeper insights into their operations, which will eventually help in making informed business decisions.

To integrate ERPNext with other applications that aren't listed here, you can use Frappe's REST API. Visit this link to learn more about it:

[Frappe Rest API](https://frappeframework.com/docs/user/en/guides/integration/rest_api)

### Authentication Integrations

- [Setting up LDAP](/erpnext/user/manual/en/ldap-integration)
- [Setting up Fairlogin](/erpnext/user/manual/en/fairlogin-integration)

### Backup Integrations

- [Setting up Dropbox Backups](/erpnext/user/manual/en/dropbox-backup)
- [Google Drive Integration](/erpnext/user/manual/en/google_drive)
- [Upload Backups to Amazon S3](/erpnext/user/manual/en/aws_s3)

### Bank Integrations

- [Plaid Integration](/erpnext/user/manual/en/plaid_integration)

### E-commerce Integrations

- [Shopify Integration](/erpnext/user/manual/en/shopify_integration)
- [WooCommerce Integration](/erpnext/user/manual/en/woocommerce_integration)
- [Amazon SP-API Integration](/erpnext/user/manual/en/amazon_integration)
- [Unicommerce Integration](/erpnext/user/manual/en/unicommerce_integration)
- [Zenoti Integration](/erpnext/user/manual/en/zenoti_integration)

### Shipping Integrations

- [ERPNext Shipping](/erpnext/user/manual/en/erpnext_shipping)

### Payment Integrations

- [RazorPay Integration](/erpnext/user/manual/en/razorpay-integration)
- [GoCardless Integration](/erpnext/user/manual/en/gocardless-integration)
- [Stripe Integration](/erpnext/user/manual/en/stripe-integration)
- [Braintree Integration](/erpnext/user/manual/en/braintree-integration)
- [Paytm Integration](/erpnext/user/manual/en/paytm-integration)
- [M-pesa Integration](/erpnext/user/manual/en/mpesa-integration)

### Telephony Integrations

- [Exotel Integrations](/erpnext/user/manual/en/exotel_integration)

### Google Integrations

- [Google Settings](/erpnext/user/manual/en/google_settings)
- [Google Calendar Integration](/erpnext/user/manual/en/google_calendar)
- [Google Contact Integration](/erpnext/user/manual/en/google_contacts)
- [Google Maps Integration](/erpnext/user/manual/en/google_maps)

<!-- page: erpnext/erpnext__erpnext_shipping.md -->
---
title: "ERPNext Shipping"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/erpnext_shipping"
updated: "2026-03-02"
---

> Introduced in version 13

**The ERPNext Shipping app helps you compare shipping rates being offered by multiple service providers, generate labels, and track your shipments' status.**

Integration with the following service providers is available:

1. [LetMeShip](https://www.letmeship.com/en/)
2. [SendCloud](https://www.sendcloud.com)

> To avail these features, the **ERPNext Shipping** app will have to be installed on your site. You can the avail the app [on GitHub](https://github.com/frappe/erpnext-shipping/tree/master), [on Frappe Cloud Marketplace](https://cloud.frappe.io/marketplace/apps/erpnext_shipping) or you can contact your hosting platform.

1. Setting Up
-------------

For the app to work smoothly, you will have to generate an API key from **at least one** of the platforms listed above. Here is a guide to set them up:

### 1.1 SendCloud

1. Register on [SendCloud](https://panel.sendcloud.sc/accounts/signup/).
2. Follow [these steps](https://support.sendcloud.com/hc/en-us/articles/360024967612-Service-points-for-API-Integrations#step-1-) to generate a **Public Key** and a **Secret Key**.
3. Search for **SendCloud** in the awesomebar.
4. Add the **Public Key** in the 'API Key' field and the **Secret Key** in the 'API Secret' field of the SendCloud DocType.
5. Check the **Enabled** field.
6. Save.

![Sendcloud API](/files/sendcloud_api.png)  


### 1.2 LetMeShip

1. Register on [LetMeShip](https://www.letmeship.com/en/).
2. Follow [these steps](https://www.letmeship.com/en-de/shipping-api/) to generate an **API ID** and **API Password**.
3. Search for **LetMeShip** in the awesomebar.
4. Add the **API ID** and **API Password** to the LetMeShip DocType. Check the **Enabled** field.
5. Save.

![LetMeShip API](/files/letmeship_api.png)  


2. Features
-----------

### 2.1 Comparison of Shipping Rates

Once a [Shipment](/erpnext/shipment) is submitted, if the app is installed, the button **Fetch Shipping Rates** will appear. On clicking, you will get a list of services along with their service providers and rates.

![Fetch Rates](/files/fetch_rates.png)  


You can also add frequently used services to your **Preferred Services** using **Parcel Service Type**:

1. Assuming the highlighted service is our frequently used service, let us add it to our **Preferred Services**

![Highlight Service](/files/service_highlight.png)
2. Go to **Parcel Service Type** > **New**. Create a new **Parcel Service**. In our case, it is 'TNT'.
3. Add a **Parcel Service Type**. In our case, it will be 'Economy'.
4. Add 'Economy' to the **Parcel Service Type Alias** table as well.
5. Add a description (optional).
6. Enable the **Show in Preferred Services List** field. Save.

Now when you click on the **Fetch Shipping Rates** button, you will always see the previously highlighted service under **Preferred Services**.

![Preferred Service](/files/preferred_service.png)  


### 2.2 Creation of Shipment

After comparing rates, you can proceed with any one of the services by clicking **Select** against the appropriate service row. On clicking, a Shipment is automatically created on your service provider's platform.

You will notice that the **Shipment Information** section is updated automatically, based on the Shipment created.

![Shipment Creation](/files/create_shipment.gif)  


You can also search for your transaction on your service provider's platform using the **Shipment ID** field.

### 2.3 Printing Labels

To avail the **Print Shipping Label** button, the **Shipment ID** must be generated in the current record.

![Print Label Button](/files/print_label_button.png)  


You can then click on it and generate your shipping label.

![Dummy Shipping Label](/files/dummy_shipping_label.png)  


You can also track your shipment's status by clicking on **View** > **Track Status**.

> **Note** : The currently integrated platforms may not serve your region. Please visit the links attached against them to know more.

<!-- page: erpnext/erpnext__exchange-rate-field-frozen.md -->
---
title: "Freeze Exchange Rate | ERPNext Documentation"
description: "Understand why an ERPNext exchange-rate field may be read-only and how stale-rate settings affect manual and fetched rates."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/exchange-rate-field-frozen"
updated: "2026-08-14"
---

A Nova Industries sales user may find that an exchange rate cannot be edited on a foreign-currency invoice.



A Nova sales user opens a foreign-currency invoice, sees an unexpected Exchange Rate, and cannot edit it. The field may appear frozen because the document is submitted, the selected accounts determine the currencies, the user lacks permission, or ERPNext has applied a stored-rate policy from Accounts Settings.



This guide helps you identify the actual cause on a Draft before changing configuration. A submitted invoice is intentionally locked and should not be repriced to solve a setup problem. When a manual override is approved, record its source so finance can explain the rate later.

## Before you begin

Confirm that the document is Draft and that at least two currencies are involved. A Company-currency transaction with Company-currency accounts needs no conversion rate. Check the user's write permission for the transaction and [Accounts Settings](/erpnext/accounts-settings).

Read the rate label carefully. `1 EUR = 1.15 USD` is a direction, not a generic ratio. Verify the [Currency Exchange](/erpnext/currency-exchange) record for that exact direction and date.

## Review Allow Stale Exchange Rates

Open Accounting &gt; Settings &gt; Accounts Settings and locate Currency Exchange Settings.



![Allow Stale Exchange Rates in Accounts Settings](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-accounts-settings-allow-stale-rate.png)

The current behavior is best understood as a rate-selection policy:


| Setting                             | Lookup behavior                                                                                                            |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Allow Stale Exchange Rates enabled  | The latest matching stored rate may be used without an age limit. This supports rates that remain valid until replaced.    |
| Allow Stale Exchange Rates disabled | ERPNext limits stored-rate age using Stale Days, then tries the configured provider when no eligible manual record exists. |


The existing documentation associates this setting with whether the Exchange Rate field is editable. Because field behavior has changed across releases and can vary by document, verify the Draft page after changing the setting instead of relying only on the word “stale.” In current develop, users can often override a fetched rate on a Draft when permissions and document logic allow it.

## If you need a controlled fixed rate

Create a dated Currency Exchange record with the approved value and the correct buying or selling flag. Then decide whether the record may remain valid until another is entered.



![Approved EUR to USD rate](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-currency-exchange-rate.png)

For a contract rate, enabling stale rates can be appropriate because the latest manual record remains eligible. For daily treasury rates, disable stale rates and use a small Stale Days value or import a new approved rate regularly.

This is not a true record-level “freeze” that prevents authorized users from changing the master. Control update permission and establish an approval process if rates must be protected.

For a stronger control, assign rate maintenance to a small finance role and have another person review the Draft transaction before submission. Keep the approved source and effective date with the treasury workpaper. This separates rate approval from transaction entry without misusing the stale-rate setting as a security control.

## If you need the current provider rate

Disable stale rates or ensure there is no eligible manual record that should win. Review [Currency Exchange Settings](/erpnext/currency-exchange-settings) and verify that the provider covers the pair and historical date.

ERPNext first searches an eligible stored record. The provider is a fallback, so changing provider settings does not override a matching manual record.

## If you need to enter the rate manually on a transaction

1. Keep the transaction in Draft.
2. Select the correct foreign Currency.
3. Confirm the receivable, payable, bank, or cash [Account](/erpnext/chart-of-accounts) currencies.
4. Review the Exchange Rate field and its direction.
5. Enter the approved rate if the field is editable.
6. Compare the transaction and Company-currency totals.
7. Save and reload the Draft to confirm the value persisted.

![Exchange Rate on a Draft EUR Sales Invoice](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-sales-invoice-eur-currency-rate.png)

The **Price List Exchange Rate** is a different field. It converts [Price List](/erpnext/price-lists) currency to transaction currency. Do not change it when the issue concerns the accounting conversion between transaction and Company currency.

## Submitted transactions

A submitted [Sales Invoice](/erpnext/sales-invoice), [Purchase Invoice](/erpnext/purchase-invoice), or [Payment Entry](/erpnext/payment-entry) represents an accounting event. ERPNext locks material fields to preserve the audit trail. If the rate is materially wrong, follow the document's cancel and amend process, subject to permissions, linked records, [Immutable Ledger](/erpnext/immutable-ledger-in-erpnext) rules, and the open [Accounting Period](/erpnext/accounting-period).

Do not update Currency Exchange and expect old submitted documents to change. They retain their own saved rates.

Before cancelling, inspect downstream payments, returns, credit notes, stock consequences, and reconciliations. A correct amendment should reproduce the commercial facts with the approved rate and preserve a readable audit trail. Ask finance to confirm whether the difference is truly an invoice error or a legitimate exchange movement that belongs at settlement.

## Common causes of a read-only field


| Cause                                 | What to check                                                              |
| ------------------------------------- | -------------------------------------------------------------------------- |
| Document is submitted                 | Cancel and amend only when accounting policy and links permit it.          |
| No currency conversion is needed      | Company, transaction, and relevant account currencies are the same.        |
| Account currency determines the flow  | The selected party or bank account fixes the amount currency.              |
| Stored rate policy controls selection | Review Allow Stale Exchange Rates, Stale Days, date, direction, and flags. |
| Provider supplied the value           | Verify the provider and whether Draft override is permitted.               |
| User lacks permission                 | Review role permissions rather than weakening accounting controls.         |
| Custom script or customization        | Test in a clean role and inspect client or server customization.           |


## Troubleshooting

### The field remains read-only after changing Accounts Settings

Reload the transaction, confirm it is Draft, and check account currencies, permissions, and customizations. Test a new Draft instead of a document whose state was already submitted or mapped from another transaction.

### ERPNext keeps using the old rate

Search Currency Exchange for the latest eligible record. Check Allow Stale Exchange Rates and Stale Days. A later transaction date does not force a provider call while an eligible manual record still wins.

### ERPNext cannot fetch a rate after stale rates are disabled

The provider may not support the pair or historical date. Create a manual record or select an approved provider that covers it.

### Changing the rate also changes item prices

Separate Exchange Rate from Price List Exchange Rate. If the Price List currency differs, item rates can be converted independently.

## FAQs

### Does Allow Stale Exchange Rates literally freeze a rate?

No, it allows the latest matching manual record to remain eligible without an age limit. Permissions and transaction logic determine editability.

### Can I lock a rate after finance approves it?

Restrict Currency Exchange write permission and use an approval or import process. The stale-rate option alone is not a master-record lock.

### Why can I edit a Draft but not a submitted invoice?

Submission posts accounting consequences and locks material fields for audit integrity.

### Will a new Currency Exchange record update old Drafts?

Not necessarily. Reload or retrigger the currency and date logic, then verify the saved field. Submitted documents remain unchanged.

### Should I disable the provider to force manual rates?

You can, but first ensure all required directions and dates have manual records and define what users should do when a rate is missing.

## Related topics

- [Currency Exchange](/erpnext/currency-exchange)
- [Currency Exchange Settings](/erpnext/currency-exchange-settings)
- [Accounts Settings](/erpnext/accounts-settings)
- [Managing Transactions in Multiple Currency](/erpnext/managing-transactions-in-multiple-currencies)
- [Manage Foreign Exchange Difference](/erpnext/manage-foreign-exchange-difference)

<!-- page: erpnext/erpnext__exchange-rate-revaluation.md -->
---
title: "Exchange Rate Revaluation | ERPNext Documentation"
description: "Revalue open foreign-currency account balances in ERPNext and verify the unrealized gain or loss and resulting Journal Entries."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/exchange-rate-revaluation"
updated: "2026-08-14"
---

At month end, Nova Industries must restate its foreign-currency balances in the USD used for Company reporting.



At month end, Nova still holds EUR 1,000 in its Euro Bank account. The euros have not changed, but their value in Nova's USD books has. If the balance was recorded at `1 EUR = 1.10 USD` and the closing rate is 1.15, its USD value has risen from 1,100 to 1,150.



Exchange Rate Revaluation updates that Company-currency carrying value without changing the EUR 1,000 balance. It identifies the USD 50 unrealized gain so finance can review and post an accurate period-end adjustment.


| Measure                         | Before    | After revaluation calculation |
| ------------------------------- | ---------: | -----------------------------: |
| Account-currency balance        | EUR 1,000 | EUR 1,000                     |
| Exchange rate                   | 1.10      | 1.15                          |
| Company-currency carrying value | USD 1,100 | USD 1,150                     |
| Unrealized gain                 |           | USD 50                        |


## Before you begin

Complete [Multi Currency Setup](/erpnext/multi-currency-setup). The Company must have at least one non-stock balance-sheet [Account](/erpnext/chart-of-accounts) whose currency differs from the Company currency and whose General Ledger balance qualifies for revaluation.

In the [Company](/erpnext/company-setup), set **Unrealized Exchange Gain/Loss Account**. Also review the normal Exchange Gain/Loss account, which is used for realized differences in payment workflows.



![Company accounts for exchange gains and losses](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-company-exchange-gain-loss-accounts.png)

Create an eligible closing-date rate in [Currency Exchange](/erpnext/currency-exchange) or verify the active provider in [Currency Exchange Settings](/erpnext/currency-exchange-settings). Confirm that the [Accounting Period](/erpnext/accounting-period) is open and the user can submit revaluations and Journal Entries.

Review the currency controls in [Accounts Settings](/erpnext/accounts-settings) before closing so the stored-rate age policy matches finance's approved procedure.

## Create an Exchange Rate Revaluation

1. Open Accounting &gt; Multi Currency &gt; Exchange Rate Revaluation.
2. Select **Add Exchange Rate Revaluation**.
3. Enter the Posting Date and Company.
4. Set Rounding Loss Allowance only when a small balance should be treated as zero. The allowed value is from 0 inclusive to less than 1.
5. Select **Get Entries**.

![Company and posting date on the revaluation](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-exchange-rate-revaluation-header.png)

ERPNext fetches eligible foreign-currency accounts, their account and base balances, the current carrying rate, the new rate for the posting date, the new base balance, and the calculated gain or loss.

## Review the fetched accounts

Do not submit immediately. Review each account against the General Ledger, the approved closing rate, and the underlying bank, receivable, payable, or other balance.



![Revaluation account row and calculated gain](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-exchange-rate-revaluation-account-pencil.png)

Select the highlighted pencil to open the full child-row editor.



![Current foreign and base balances](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-exchange-rate-revaluation-current-balance.png)



![New rate, new base balance, and gain](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-exchange-rate-revaluation-new-balance.png)


| Field                           | Meaning                                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------------------ |
| Account                         | The foreign-currency balance-sheet ledger being revalued.                                  |
| Account Currency                | The fixed currency of that ledger.                                                         |
| Balance in Account Currency     | Net debit less credit in the foreign currency up to the Posting Date.                      |
| Balance in Base Currency        | Existing Company-currency carrying value.                                                  |
| Current Exchange Rate           | Existing base balance divided by the foreign balance when the foreign balance is non-zero. |
| New Exchange Rate               | Closing-date rate used for revaluation. Review it before submission.                       |
| New Balance in Account Currency | Normally unchanged from the existing foreign balance.                                      |
| New Balance in Base Currency    | Foreign balance multiplied by the new rate.                                                |
| Gain/Loss                       | Difference between new and existing base balance.                                          |
| Zero Balance                    | Identifies a case where either the base or account-currency balance is treated as zero.    |


The example retains EUR 1,000 but changes its USD value by USD 50.

## Review the totals

The parent document separates ordinary revaluation gain or loss from gain or loss already accumulated on zero-balance cases.



![Revaluation totals](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-exchange-rate-revaluation-totals.png)


| Total                      | Meaning                                                                    |
| -------------------------- | -------------------------------------------------------------------------- |
| Gain/Loss from Revaluation | Unbooked change calculated for ordinary non-zero foreign balances.         |
| Gain/Loss already booked   | Difference associated with accounts whose account or base balance is zero. |
| Total Gain/Loss            | Combined result for the document.                                          |


From ERPNext v14 onward, zero-balance cases are handled by a separate Exchange Gain/Loss Journal Entry in Draft. This addresses situations where a foreign balance is zero but a residual Company-currency balance remains, or the reverse.

## Submit and create Journal Entries

1. Save the revaluation and resolve any incorrect account or rate.
2. Submit it. Rows without a gain or loss are removed.
3. From **Create**, select **Journal Entries**.
4. Open the created Journal Entry and verify the account rows, Company-currency debit and credit, reference to the revaluation, and posting date.
5. Submit the Journal Entry only after review.

Submitting the revaluation calculates and locks the reviewed result, but the General Ledger is affected by the resulting submitted Journal Entry. If the Journal Entry remains Draft, reports do not yet include the revaluation posting.

Use [Journal Entry](/erpnext/journal-entry) permissions and period-close controls consistently. The unrealized account balances the adjustment to the foreign-currency ledger.

## Verify the result

Run the [General Ledger](/erpnext/general-ledger) for the foreign account and revaluation date. Confirm:

- the account-currency balance remains the same;
- the Company-currency carrying value changes by the expected gain or loss;
- the Journal Entry references the Exchange Rate Revaluation;
- the offset reaches the configured unrealized account;
- financial statements now use the updated Company-currency balance.

Also review [Accounts Receivable and Payable](/erpnext/accounts-receivable-and-payable) when party balances are involved. Its Revaluation Journals option affects how revaluation journals are considered in outstanding reporting.

## Automate creation carefully

The Company can automatically create Exchange Rate Revaluation records at a Daily, Weekly, or Monthly frequency. **Submit ERR Journals?** controls whether the resulting Journal Entries are submitted automatically.



![Automatic revaluation setting](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-company-auto-revaluation-setting.png)

Start with manual review. Automate only after finance trusts the provider, closing-date selection, account coverage, unrealized account, and reversal or closing procedure. Automatic submission reduces the opportunity to catch an unexpected rate or account balance.

## Reversal and later periods

Current develop supports creating reversal Journal Entries after revaluation journals are posted. Whether and when to reverse depends on your accounting policy and reporting cycle. Do not manually cancel or duplicate entries without checking the linked revaluation and subsequent periods.

A later revaluation should use the latest carrying value and the new closing rate. It should not rewrite the original invoice, payment, or historical Currency Exchange record.

## Troubleshooting

### Get Entries returns no accounts

Verify that the Account currency differs from Company currency, the account is a non-stock balance-sheet account, it has qualifying ledger balances by the Posting Date, and the selected Company is correct.

### The new exchange rate is zero or missing

Check the exact currency direction, transaction date, stale-rate rules, stored Currency Exchange record, and provider coverage. Create an approved manual rate if required.

### The revaluation is submitted but the ledger did not change

Open the linked Journal Entry. It must be created and submitted. A Draft Journal Entry has no General Ledger effect.

### The foreign balance is zero but Company currency remains

Review the Zero Balance row and the separate Exchange Gain/Loss journal behavior. Do not enter a fictional foreign amount merely to force the base balance to zero.

## FAQs

### Is revaluation the same as exchange gain or loss on payment?

No, revaluation records an unrealized reporting-date change on an open balance. Payment settlement records a realized difference.

### Does revaluation change the foreign-currency balance?

No, it changes the Company-currency carrying value while retaining the account-currency amount.

### Must I revalue every foreign-currency transaction?

No, revalue eligible open balance-sheet accounts according to your reporting policy, commonly at period end.

### Can I edit the New Exchange Rate?

Review and, where permitted, adjust it before submission using an approved rate. Record the source and approval outside the narrative if your controls require it.

### Should automatic Journal Entries be submitted automatically?

Only when the process has been tested and finance accepts the reduced review step. Draft creation is safer during rollout.

## Related topics

- [Multi Currency Accounting](/erpnext/multi-currency-accounting)
- [Currency Exchange](/erpnext/currency-exchange)
- [Manage Foreign Exchange Difference](/erpnext/manage-foreign-exchange-difference)
- [Journal Entry](/erpnext/journal-entry)
- [Accounting Reports](/erpnext/accounting-reports)

<!-- page: erpnext/erpnext__exotel_integration.md -->
---
title: "Exotel Integration\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/exotel_integration"
updated: "2026-02-26"
---


This integration allows you to integrate Exotel into your ERPNext account. Leads and their phone numbers captured via Exotel can be saved directly to your ERPNext.

## 1. Features

- Track incoming calls in your ERPNext account.
- Shows existing lead/customer information pop-up to employees when an incoming call is received.

## 2. How to setup

### 2.1 Setup your Exotel account

- Login to your Exotel account and go to App Bazar.
- Create a new App for a new flow.
- Setup the flow as you wish it to be.
- In your connect API under "Create popup..." and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`

![Connect Applet](/files/connect_applet.png)
![Call Popup Section](/files/create_popup_section.png)

> **Note:** Replace `<your-site>` in URL with your site name. For example, if the site name is **frappe.erpnext.com** then the URL will be:
`https://frappe.erpnext.com/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`

- After that add a Passthru applet under "After Call Conversation ends" and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_end_call`

![After Conversation Ends Section](/files/after_conversation_ends_section.png)

![After call ends section](/files/passthru_end_call.png)

> **Note:** Make sure to check "Make Passthru Async".

- Similary, add a Passthru applet under "If nobody answers..." section and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_missed_call`

![No Response Section](/files/no_response.png)

![After call ends section](/files/passthru_missed_call.png)

> **Note:** Make sure to check "Make Passthru Async".

- Save the flow.
- Now assign this newly created app to your ExoPhone from which you receive your business calls.

### 2.2 Setup in ERPNext

- From Awesome Bar, go to 'Exotel Settings'.
- Set your "Exotel SID" and "Exotel Token". You can find your Exotel API key and token on your [Exotel Dashboard](https://my.exotel.com/apisettings/site#api-credentials).
- Go to Communication Medium.
- Add your ExoPhone and schedule that number. Based on this schedule employees will receive the popup.

<!-- page: erpnext/erpnext__expense_report.md -->
---
title: "Deferred Revenue/Expense Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/expense_report"
updated: "2026-08-14"
---

Nova Industries sells a $1,200 annual warranty service and also prepays $1,200 for a year of software support. The invoices show the full contractual amounts, but finance should recognise only the portion earned or consumed in each accounting period.





The Deferred Revenue and Expense Report compares the expected recognition schedule with actual deferred-accounting postings. It helps finance identify what has already been recognised, what remains deferred, and which invoice or item requires investigation.

## Before you begin

Configure deferred accounts in [Accounts Settings](/erpnext/accounts-settings), enable deferred accounting on the relevant Item or invoice row, and enter valid service start and end dates. Submit the invoice and run [Process Deferred Accounting](/erpnext/process-deferred-accounting) according to the company's schedule.

## Review deferred revenue

![Open the Sales Invoice Item row to review deferred accounting fields](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-sales-invoice-item-pencil.png)



![Deferred revenue account and service period on a Sales Invoice Item](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-sales-invoice-service-period.png)



1. Open the Deferred Revenue and Expense Report.
2. Select Nova Industries and the reporting period.
3. Choose the revenue view or filter for Sales Invoices.
4. Review the invoice, item, service dates, expected recognition, actual posting, and remaining amount.
5. Open the invoice or generated Journal Entry when a line needs explanation.

![Loaded Deferred Revenue and Expense Report for Nova annual service revenue](https://novacompanies.m.frappe.cloud/files/docs-accounting-reports-20260814-deferred-revenue-report.png)

## Review deferred expense

![Deferred expense account and service period on a Purchase Invoice Item](https://novacompanies.m.frappe.cloud/files/docs-deferred-2026-purchase-invoice-service-period.png)





Use the expense view for prepaid costs from Purchase Invoices. The same report logic shows the portion already recognised as expense and the amount that remains in the deferred asset account.

![Loaded Deferred Revenue and Expense Report for Nova prepaid service expense](https://novacompanies.m.frappe.cloud/files/docs-accounting-reports-20260814-deferred-expense-report.png)

## Understand the result


| Value                        | What to check                                                 |
| ---------------------------- | ------------------------------------------------------------- |
| Invoice amount               | The original deferred item value and currency.                |
| Service period               | The dates over which revenue or expense should be recognised. |
| Expected amount              | The schedule amount calculated for the selected period.       |
| Actual amount                | The value already posted by deferred accounting entries.      |
| Upcoming or remaining amount | The portion still expected in future periods.                 |


## Verify the accounting

Open the generated Journal Entry and compare the deferred account with the income or expense account in the [General Ledger](/erpnext/general-ledger). Revenue recognition normally debits the deferred revenue liability and credits income. Expense recognition normally credits the deferred expense asset and debits expense.

## Troubleshooting

### An invoice does not appear

Confirm that it is submitted, its item row has deferred accounting enabled, deferred and income or expense accounts are set, and the service dates overlap the report period.

### Expected and actual values differ

Run Process Deferred Accounting for the missing period and inspect failed or draft entries. Also check the Accounts Settings basis and whether generated Journal Entries require submission.

### The same amount appears in the wrong period

Review posting date, service start and end dates, and the deferred-recognition basis. Correct the source through the approved amendment process rather than editing ledger rows.

## Frequently asked questions

### Does this report create accounting entries?

The report explains expected and actual recognition. Process Deferred Accounting creates the recognition entries.

### Can one invoice contain deferred and immediate items?

Deferred behavior is configured at item-row level, allowing other rows to post immediately when their settings and accounts require it.

### Why is the full invoice still visible as receivable or payable?

Deferral changes when income or expense is recognised. It does not normally change the customer's or supplier's contractual invoice balance.

## Related topics

- [Deferred Accounting](/erpnext/deferred-accounting)
- [Deferred Revenue](/erpnext/deferred-revenue)
- [Deferred Expense](/erpnext/deferred-expense)
- [Process Deferred Accounting](/erpnext/process-deferred-accounting)
- [General Ledger](/erpnext/general-ledger)

<!-- page: erpnext/erpnext__export-data-for-specific-year-or-filter.md -->
---
title: "Export Data for Specific Year or Filter"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/export-data-for-specific-year-or-filter"
updated: "2026-03-29"
---

**Question:** I need to export Sales Invoices for Particular Fiscal Year only.

**Answer:**

The system allows you to use any combination of filters including a Date Range to extract the data whether from the List view or from the Report View.

**List View**

![](/files/image36316a.png)



**Report View**

![](/files/imagebb9c64.png)

<!-- page: erpnext/erpnext__fairlogin-integration.md -->
---
title: "Setting up fairlogin\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fairlogin-integration"
updated: "2026-02-26"
---


fairlogin is an GDPR aware oAuth provider by fairkom.eu.

To setup fairlogin as an oAuth provider, go to:
> Home > Integrations > Social Login Key

## Setup keycloak

fairlogin is based on keycloak, so the parameters may be similar for any custom oAuth setting facilitating keycloak.

There you add a new client, select open-id as client protocol and enter the address of your ERPnext instance as the Root, Redirect and Base URL.

Adding your ERNext service as a client is being [offered as a service by fairkom](https://erp.fairkom.net/cloud/fairlogin-client).

![ERPnext keycloak Settings](/files/fairloginKeycloakERPnext.png)

## Setup fairlogin

To enable fairlogin as an ERPNext login option, you need to configure the following parameters:

- Base URL https://id.fairkom.net/auth/realms/fairlogin/
- Authorize URL https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/auth
- Redirect URL /api/method/frappe.integrations.oauth2_logins.login_via_fairlogin
- Access Token URL https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/token
- API Endpoint https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/userinfo

![ERPnext fairlogin Settings](/files/fairloginERPnextSettings.png)

On enabling service, the system will allow to login with any fairlogin account.

The default role of a new user is Blogger (currently hardcoded).

<!-- page: erpnext/erpnext__faqs.md -->
---
title: "Stock FAQs"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/faqs"
updated: "2026-07-02"
---

Is any integration required for using Barcode reader in ERPNext?  
How Valuation Rate is Calculated for an Item  
How to Update valuation after purchase transaction

<!-- page: erpnext/erpnext__feedback-request-using-web-form.md -->
---
title: "Feedback Request Using a Web Form"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/feedback-request-using-web-form"
updated: "2026-03-04"
---

In the ERPNext version 11, we have a feature which allowed collecting a Feedback from a Customer and users. In ERPNext, this feature is now manageable using built-in customisation tools like:  
* Custom DocType
* Web Form
* Notification

  
Following are the steps on how you should configure a feature and start collecting feedback.  
**Feedback as a DocType**  
Create a Custom DocType for Rating on these lines  
![](/files/oUDbd8e.png)  
1. In the first fields, list a DocTypes for which you want to collect a rating
2. In the Document Name field, just enter the name of first field "document", so that it becomes a [Dynamic Link](https://docs.erpnext.com/docs/v14/user/manual/en/customize-erpnext/articles/dynamic-link-fields) field.
3. Enter a Rating field. You can also choose other data or select field, if you wish to take rating on those lines.

  
**Web Form for Feedback Form**  
Once a DocType is created, simply create a Web Form by fetching all the standard fields from Feedback doctype.  
![](/files/eWKqJ50.png)  
**Create a Notification**  

A Notification should be created to send a link to a user following which they will submit a rating. You can define the conditions for triggering an email based on standard features of [Notification](/erpnext/notifications). Following is the help on how to define a message and link which would take user to a Web Form and allow submitting a rating.  

```
https://example.erpnext.com/feedback?new=1&document=Sales%20Order&document_name={{doc.name}}
```
  
Where:  
* **example.erpnext.com** will be URL of your ERPNext account
* **feedback** will be the name of custom doctype added for collecting a feedback
* **document=Sales%20Order&** will be a name of DocType for which you want to sent a notification
* document_name={{doc.name}} will pick-up specific document name and update in the Document Name field of Feedback form.

  
![](/files/UDBhIaK.png)  
  
**Quick Demo:**  
Here is the demo of how link would be generated, Web Form would be filled and capture in ERPNext.  
![](/files/hEbdh6c.gif)

<!-- page: erpnext/erpnext__fetch-child-table-values-using-jinja-tags.md -->
---
title: "Fetch child table values using Jinja tags"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fetch-child-table-values-using-jinja-tags"
updated: "2026-03-04"
---

Jinja templating can be used to reference any field on any DocType in ERPNext. This can simply be done by calling {{doc.field_name}} on a print format, where 'doc.name' is the variable name for a certain field.

 

However this approach does not work for Child Tables inside a DocType. This article will help you traverse and display all rows pertaining to a child table inside any DocType.

 

**Pre Requisites**

 

We would require the variable name of the child table on the corresponding DocType. This can be viewed from the 'Customize Form' section for the required DocType. The same is illustrated below

![](/files/f7Xxz1S.png)

We will also require the variable names of all the fields inside the child table which need to be referenced. This can be obtained from the 'Customize Form' section of the corresponding child table as shown below

![](/files/tzloEh2.png)

 

![](/files/wPB82f0.png)

 

![](/files/AV0308f.png)

 

![](/files/CW0oEUo.png)

**Method 1. Displaying rows of a Child Table on an unordered list**



{% for row in doc.items %}

* Item Code: {{ row.get_formatted("item_code", doc) }}

Quantity: {{ row.get_formatted("qty", doc) }}

Rate: {{ row.get_formatted("rate", doc) }}

Amount: {{ row.get_formatted("amount", doc) }}


{% endfor %}




 

The output on a print format would be as follows

![](/files/lgLjE7u.png)

 

 

**Method 2. Displaying rows of a Child Table as a table**

 



  

   

  

  

 

 

| Item Code | Quantity | Rate | Amount |
| --- | --- | --- | --- |
| {{item.item_code }} | {{item.qty}} | {{item.rate}} | {{item.amount}} |



 

The output on a print format would be as follows

 

![](/files/GS00WlC.png)

 

This template can be used for reference. Any additional fields on the child table field can be fetched in a similar manner, by amending the Jinja template.

<!-- page: erpnext/erpnext__fetch-the-entire-address-text-on-a-custom-field.md -->
---
title: "Fetch the entire address text on a custom field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fetch-the-entire-address-text-on-a-custom-field"
updated: "2026-03-02"
---

This article will help you to add a custom field for fetching full addresses on any DocType, using a 3 step approach.





**Step 1. Cosmetic customisations on the required DocType**





We would first need to add two new fields on the DocType for fetching addresses:-





a) A field of type 'Link' which points to our Address master

b) A field of type 'Read Only' which would display the full address





Take note of the variable names of the new fields you create. This information will be required later in the process.





![](/files/q90efZM.png)





For information on creating custom fields on a DocType you can refer to the following link - [Custom Fields in ERPNext](https://docs.erpnext.com/docs/v13/user/manual/en/customize-erpnext/custom-field)





Once this step is done you should have two new fields on the selected DocType, as illustrated below:-





![](/files/SabQi7A.png)











**Step 2. Adding a Client Script for fetching the full address from our Address master**





Search for 'Client Script' on the search bar, and create a new Client Script. Select the required DocType on which we need to fetch the address on.





In the section for the script paste the following Client Script:-







```
frappe.ui.form.on("DocType Name", "address_link_field", function(frm, cdt, cdn) {    if(frm.doc.address_link_field){     return frm.call({      method: "frappe.contacts.doctype.address.address.get_address_display",      args: {       "address_dict": frm.doc.address_link_field      },      callback: function(r) {       if(r.message)           frm.set_value("full_address_field", r.message);              }     });    }    else{        frm.set_value("full_address_field", "");    }});
```





Here we will need to replace the the following changes based on your use case:-

a) Replace 'DocType Name' with the Name of the DocType we need to fetch the address on. Eg. Sales Invoice, Purchase Order etc.

b) Replace 'addresslinkfield' with the variable name of the custom link field we created in Step 1

c) Replace 'fulladdressfield' with the variable name of the custom read only field we created in Step 1





Once this is done, you would have a Client Script which looks as below:-





![](/files/VukPzs4.png)





**Step 3. Save, enable and test the Client Script**





Once the Client Script is amended as per your use case, we can Save it and enable it by clicking the 'Enabled' checkbox.

Go to the required DocType and refresh the page for the changes to take effect.





Now when an address is selected on our custom link field, the entire address will be fetched on our custom read only field, as illustrated below:-





![](/files/W3kxhT2.gif)

<!-- page: erpnext/erpnext__fetch-values-from-master.md -->
---
title: "Fetching Values From Master"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fetch-values-from-master"
updated: "2026-03-02"
---


To pull a value of a link on selection, use the `add_fetch` method.

 
 
 add_fetch(link_fieldname, source_fieldname, target_fieldname)
 

### Example

Let' say you have created a Custom Field **VAT ID** (`vat_id`) in **Customer** and **Sales Invoice** and want to make sure that this value gets updated every time you select a Customer in a Sales Invoice.

To configure this, in the Sales Invoice Custom Script, you can add this line:

 
 
 cur_frm.add_fetch('customer','vat_id','vat_id')
 

<!-- page: erpnext/erpnext__fetching-data-from-a-document.md -->
---
title: "Fetching Data from a Document\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fetching-data-from-a-document"
updated: "2026-03-04"
---


**Question:** We track Customer's PO Number and PO Date field in the Sales Order. To have these values fetched into Sales Invoice as well, we have inserted Custom Field in the Sales Invoice. However, when we create Sales Invoice from the Sales Order, Customer's PO details are not being fetched.

**Answer:** When data is fetched from one transaction to the another, then mapping of the data is done based on the field names. If two transactions have fields with the exact same name, then it's values are mapped.

For example, if you want Customer's PO No. and PO Date to be fetched from Sales Order to Sales Invoice, then you should ensure that Custom Fields added in the Sales Invoice has an exact same field name as in the Sales Order.

Sales Order (standard fields)

![Standard fields in Sales Order](/files/customize-fetch-data-1.png)

Sales Invoice (custom fields)

![Custom Field in Sales Invoice](/files/customize-fetch-data-2.png)

Since names for the Customer's PO related fields are same in the Sales Order and Sales Invoice, when creating Sales Invoice from the Sales Order, values in these fields are auto-fetched.

![Values fetching from Sales Order to Sales Invoice](/files/customize-fetch-data-3.png)
![Values fetching from Sales Order to Sales Invoice](/files/customize-fetching-data.gif)

<!-- page: erpnext/erpnext__fichier_des_ecritures_comptables.md -->
---
title: "Le Fichier des \u00c9critures Comptables [FEC]\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fichier_des_ecritures_comptables"
updated: "2026-07-02"
---


Since 2014, a legal requirement makes it mandatory for companies operating in France to provide a file of their general accounting postings by fiscal year corresponding to an electronic accounting journal.

For ERPNext users this file can be generated using a report available if you system's country is France.


### Requirements

To generate the report correctly, your Chart of Account needs to be setup according to the french accounting rules.

All accounts need to have a number in line with the General Chart of Account (PCG) and a name.

The SIREN number of your company can be added in the "Company" doctype.


### CSV generation

You can generate the required CSV file by clicking on "Export" in the top right corner of the report.


### Testing Instructions

To test the validity of your file, the tax administration provides a testing tool at the following address: [Outil de test des fichiers des écritures comptables (FEC)](http://www.economie.gouv.fr/dgfip/outil-test-des-fichiers-des-ecritures-comptables-fec)

<!-- page: erpnext/erpnext__field-types.md -->
---
title: "Field Types"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/field-types"
updated: "2026-03-04"
---

The following are the types of fields you can define while creating new ones, or while amending standard ones.

#### Link

Link field is connected to another master from where it fetches data. For example, in the Quotation master, the Customer is a Link field. To know more, [click here](/erpnext/creating-custom-link-field).

#### Dynamic Link

Dynamic Link field is one which can search and hold value of any document/doctype. [Click here](/erpnext/dynamic-link-fields) to learn how Dynamic Link Field functions.

#### Check

This will enable you to have a checkbox here.

![Check Field TYpe](/files/field-type-check.png)  


#### Select

Select will be a drop-down field. You can add multiple results in the Option field, separated by row.

![Select Field Type](/files/field-type-select.png)  


#### Table

A table will be a kind of Link field which renders another DocType within the current form. For example, the Item Table in the Sales Order is a Table field, which is linked to Sales Order Item DocType.

![Table Field Type](/files/field-type-table.png)  


#### Attach

Attach field allows you to browse a field from the File Manager and attach the same herein.

![Attach Field Type](/files/field-type-attach.png)  


#### Attach Image

Attach Image is a field wherein you will be allowed to attach Images of the format jpeg, png, etc. This becomes the Image representing that particular DocType. For e.g., you would want the image of an Item in its DocType, you can choose your field to be an Attach Image Field.

![Field Type Image](/files/field-type-image.png)  


#### Text Editor

Text Editor is a text field. It has text-formatting options. In ERPNext, this field is generally used for defining Terms and Conditions.

![Field Type Text Editor](/files/field-type-text-editor.png)  


#### Date

This field will enable you to enter the Date in this field.

![Field Type Date](/files/field-type-date.png)  


#### Date and Time

This field will give you a date and time picker. The current date and time (as provided by your computer) are set by default.

![Field Type Date and Time](/files/field-type-date-and-time.png)  


#### Barcode

In this field, you can specify the field as Barcode which will allow you to enter a Barcode number. Oce you do that, the Barcode would automatically get generated against the number.

![Field Type Barcode](/files/field-type-barcode.png)  


#### Button

This kind of field will be an action button, like Save, Submit, etc.

![Field Type Button](/files/field-type-button.png)  


#### Code

If the Field Type is selected as code, you will be able to enter a Code to the field.

![Field Type Code](/files/field-type-code.png)  


#### Color

You will have the option of specifying the color for this Form.

![Field Type Colour](/files/field-type-colour.png)  


#### Column Break

Since ERPNext has multiple column layouts, using Column Breaks, you can divide a set of fields into a maximum of two columns.

![Field Type Column Break](/files/field-type-column-break.png)  


#### Currency

Currency field holds numeric value, like Item Price, Amount, etc. Currency field can have value up to six decimal places. Also, you can have a currency symbol being shown for the currency field.

![Field Type Currency](/files/field-type-currency.png)  


#### Data

The data field will be a simple text field. It allows you to enter a value of up to 140 characters, making this the most generic field type. To enable validations for Email, Name, or Phone Number inputs, set options to "Email", "Name", "Phone" in Settings > DocType.

![Field Type Data](/files/field-type-data.png)  


#### Float

Float field carries numeric value, up to nine decimal places. Precision for the float field is set via [Set Precision](/erpnext/set-precision)

> Setup > Settings > System Settings

The setting will be applicable on all the float field.

![Field Type Float](/files/field-type-float.png)  


#### Geolocation

Use Geolocation field to store GeoJSON [feature_collection](https://tools.ietf.org/html/rfc7946#section-3.3). Stores polygons, lines, and points. Internally it uses the following custom properties for identifying a circle.

Read [Geolocation field](/erpnext/geolocation-field) for more understanding.

![Field Type Geolocation](/files/field-type-geolocation.png)  


#### HTML

You can select the field to be an HTML field when you want the data to be entered in HTML format.

![Field Type HTML](/files/field-type-html.png)  


#### Image

Image field will render an image file selected in another attach field.

For the Image field, under Option (in Doctype), a field name should be provided where the image file is attached. By referring to the value in that field, the image will be a reference in the Image field.

![Field Type Image](/files/field-type-image2.png)  


#### Int (Integer)

The integer field holds numeric value, without decimal place.

![Field Type Integer](/files/field-type-integer.png)  


#### Small Text

Small Text field carries text content and has more character limit than the Data field.

![Field Type Small Text](/files/field-type-small-text.png)  


#### Long Text

You can define your field to a Long Text Field when you would want to enter data with an unlimited character limit.

![Field Type Long Text](/files/field-type-long-text.png)  


#### Text

This field type would allow you to add text in the field. The character limit in Small text, Long text and Text fields shall be determined based on the Relational Database Management System.

![Field Type Text](/files/field-type-text.png)  


#### Markdown Editor

This field will allow you to add the text in Markup language.

![Field Type Markdown Editor](/files/field-type-markdown-editor.png)  


#### Password

The password field will have decoded value in it.

![Field Type Password](/files/field-type-password.png)  


#### Percent

You can define the field as a Percentage field which in the background will be calculated as a percentage.

![Field Type Percent](/files/field-type-percent.png)  


#### Rating

You can define the field as a Rate field which in the background will be calculated as Rating.

![Field Type Rating](/files/field-type-rating.png)  


#### Read Only

Read Only field will carry data fetched from another form which will be non-editable. You should set Read Only as field type if its source for value is predetermined.

![Field Type Read Only](/files/field-type-read-only.png)  


#### Section Break

Section Break is used to divide the form into multiple sections.

![Field Type Section Break](/files/field-type-section-break.png)  


#### Signature

You can define the field to be a Signature field wherein you can add the Digital Signature in this field.

![Screenshot 2024-08-28 at 3.01.56 PM](/files/Screenshot 2024-08-28 at 3.01.56 PM.png)  


#### Table MultiSelect

This is a combination of 'Link' type and 'Table' type fields. Instead of a child table with 'Add Row' button, in one field multiple values can be selected.

![Field Type Table MultiSelect](/files/field-type-table-multiselect.png)  


#### Time

This is a Time field where you can define the Time in the field.

![Field Type Time](/files/field-type-time.png)  


#### Duration

You can use the Duration field if you want to define a timespan.

![Field Type Duration](/files/field-type-duration.png)  


If you don't want to track duration in terms of days or seconds, you can enable "Hide Days" and "Hide Seconds" options respectively in your Form.

![Field Type Duration Options](/files/field-type-duration-options.png)  


This is how the duration field looks after the above changes.

![Field Type Duration](/files/field-type-duration2.png)  

<!-- page: erpnext/erpnext__fifo-and-moving-average.md -->
---
title: "FIFO and Moving Average"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fifo-and-moving-average"
updated: "2026-06-28"
---

# FIFO & Moving Average Valuation Methods

## 1. Overview

ERPNext values stock **perpetually**: every stock movement (receipt, issue, transfer, manufacture) updates the item's quantity *and* its monetary value in real time through the **Stock Ledger**. The **Valuation Method** decides *how the value of each outgoing unit is calculated* and therefore what your remaining inventory is worth and what your Cost of Goods Sold (COGS) becomes.

ERPNext supports three valuation methods:

- **FIFO** (First In, First Out)
- **Moving Average**
- **Standard Cost** *(covered in a separate guide)*

This guide explains **FIFO** and **Moving Average** — how each works, the accounting they produce, their behavior with backdated entries and reposting, and the pros and cons of each so you can choose the right one per item.

> **Where to set it:** Valuation Method can be set per **Item** (Item master → *Valuation Method*), or defaulted at the **Company** level, or globally in **Stock Settings**. The most specific setting wins (Item → Company → Stock Settings).

---

## 2. FIFO (First In, First Out)

### 2.1 How it works

FIFO assumes the **oldest stock is consumed first**. ERPNext maintains a **FIFO queue** of `[quantity, rate]` layers for each item-warehouse. Every receipt adds a layer at its actual incoming rate; every issue consumes layers from the **front** (oldest) of the queue at *their original rates*.

The valuation rate reported at any moment is the **weighted average of the layers currently remaining** in the queue, but each outgoing unit is costed at the *specific* rate of the layer it is drawn from.

### 2.2 Worked example


| Step | Transaction      | Queue after              | Stock value |
| ---- | ---------------- | ------------------------ | ----------- |
| 1    | Receive 10 @ 100 | `[10 @ 100]`             | 1,000       |
| 2    | Receive 10 @ 120 | `[10 @ 100], [10 @ 120]` | 2,200       |
| 3    | Issue 15         | `[5 @ 120]`              | 600         |


At step 3, the 15 issued units are costed as **10 @ 100 + 5 @ 120 = 1,600** (oldest first). The remaining 5 units stay valued at their original 120.

### 2.3 Accounting impact

In a perpetual-inventory company, the issue posts COGS at the **actual layered cost** of the consumed units:

- COGS (step 3) = 1,600
- Inventory is credited 1,600; remaining inventory asset = 600.

Because outgoing cost reflects the **actual historical purchase price** of the specific units leaving stock, FIFO closely tracks real acquisition cost and is widely accepted for statutory/tax reporting.

### 2.4 Pros

- **Closely matches actual cost flow** — the cost of goods sold reflects the genuine price paid for the specific units consumed.
- **Realistic ending inventory value** — remaining stock is valued at the most **recent** purchase prices, so the balance sheet reflects current replacement-ish cost.
- **Widely accepted** for accounting standards and tax authorities; intuitive and auditable (you can trace which layers were consumed).
- **Good for items with shelf life / lot rotation** (food, pharma, perishables) where you physically issue oldest-first anyway.

### 2.5 Cons

- **Sensitive to backdated entries** — inserting or editing a past transaction changes which layers later issues consume, so **every subsequent ledger entry must be recomputed (reposted)**. On long, dense ledgers this reposting is slow and resource-intensive.
- **Volatile COGS in rising-price environments** — older, cheaper layers are expensed first, which can understate COGS and overstate profit during inflation.
- **More computation / storage** — the layer queue must be maintained and serialized for every item-warehouse.
- **Heavier reposting load** when corrections, cancellations, or landed-cost vouchers touch historical entries.

---

## 3. Moving Average

### 3.1 How it works

Moving Average maintains a **single blended average rate** per item-warehouse. On **every receipt**, the average is recomputed:

```
new average = (existing qty × existing avg rate + incoming qty × incoming rate)
              ──────────────────────────────────────────────────────────────
                             existing qty + incoming qty
```

Issues are costed at the **current average rate** and do **not** change the average; only receipts (and revaluations) move it.

### 3.2 Worked example


| Step | Transaction      | Qty on hand | Avg rate | Stock value |
| ---- | ---------------- | ----------- | -------- | ----------- |
| 1    | Receive 10 @ 100 | 10          | 100      | 1,000       |
| 2    | Receive 10 @ 120 | 20          | 110      | 2,200       |
| 3    | Issue 15         | 5           | 110      | 550         |


At step 2 the average becomes `(10×100 + 10×120) / 20 = 110`. The 15 issued units at step 3 are each costed at **110** → COGS = 1,650; remaining 5 units valued at 110 = 550.

### 3.3 Accounting impact

- COGS (step 3) = **1,650** (15 × average 110).
- Inventory credited 1,650; remaining inventory asset = 550.

Compared with FIFO on the same data, Moving Average **smooths** the cost: COGS is 1,650 vs FIFO's 1,600, and the difference flows into the value of remaining stock.

### 3.4 Pros

- **Smooths out price fluctuations** — a single blended rate dampens the impact of volatile purchase prices, giving steadier COGS and margins.
- **Simpler and lighter** — only one rate per item-warehouse to maintain; no layer queue to store or walk.
- **Easier to understand and reconcile** — "one item, one current cost" is intuitive for operations and reporting.
- **Good for homogeneous, fast-moving, commoditized items** where individual lots are indistinguishable (bulk fasteners, fuel, raw chemicals).

### 3.5 Cons

- **Still requires reposting on backdated entries** — because a past receipt changes the running average for **all later** transactions, ERPNext must recompute the forward chain. Like FIFO, this can be slow on long ledgers.
- **Does not track actual lot cost** — outgoing cost is a blend, so it can diverge from the real price paid for the specific units shipped; less precise for lot-traceable or high-value items.
- **Average can lag reality** — in fast-moving price environments the blended rate trails current market cost, which may misstate margins on individual sales.
- **Less granular audit trail** — you cannot point to "these specific units left at this specific cost," only to the average at that time.

---

## 4. FIFO vs Moving Average — at a glance


| Aspect                           | FIFO                                            | Moving Average                               |
| -------------------------------- | ----------------------------------------------- | -------------------------------------------- |
| **Outgoing cost basis**          | Actual rate of the oldest remaining layer       | Current blended average rate                 |
| **Tracks real lot cost?**        | Yes (layer-accurate)                            | No (blended)                                 |
| **COGS behavior**                | Reflects oldest prices first                    | Smoothed across all receipts                 |
| **Ending inventory value**       | At most recent purchase prices                  | At the blended average                       |
| **Data maintained**              | Queue of `[qty, rate]` layers                   | Single average rate                          |
| **Backdated entry → reposting?** | **Yes** (recompute forward chain)               | **Yes** (recompute forward chain)            |
| **Computation cost**             | Higher (layer walking)                          | Lower (single rate)                          |
| **Best for**                     | Perishables, lot-rotated, audit-sensitive items | Homogeneous, high-volume, commoditized items |
| **Statutory acceptance**         | Very widely accepted                            | Widely accepted                              |


---

## 5. The shared limitation: backdated entries trigger reposting

This is the most important operational characteristic both methods share — and the key contrast with **Standard Cost**.

With **both FIFO and Moving Average**, the value of any stock ledger entry depends on **the entries before it** (which layers exist, or what the running average is). So when you:

- insert a **backdated** transaction,
- **cancel** or **amend** a historical voucher,
- apply a **Landed Cost Voucher** to a past receipt, or
- change a past valuation rate,

…ERPNext must **repost** — recompute the quantity, rate, value, and GL impact of **every subsequent stock ledger entry** for that item-warehouse (a *Repost Item Valuation* job). On items with long, dense histories this is **slow, resource-heavy, and temporarily changes the value of stock you considered settled**.

> If your organization frequently records **backdated corrections** and this reposting cost is painful, consider the **Standard Cost** method (see the separate *Standard Valuation Rate* guide), where the rate is known by date and backdated entries do **not** trigger reposting.

---

## 6. Choosing a method — recommendations


| Your situation                                                     | Recommended method                   |
| ------------------------------------------------------------------ | ------------------------------------ |
| Perishable / shelf-life items, physically issued oldest-first      | **FIFO**                             |
| High-value or lot-traceable items needing precise cost             | **FIFO**                             |
| Statutory/tax regime that expects actual cost flow                 | **FIFO**                             |
| Homogeneous, commoditized, fast-moving items                       | **Moving Average**                   |
| You want smoother, more stable margins                             | **Moving Average**                   |
| You want minimal valuation maintenance overhead                    | **Moving Average**                   |
| You frequently post **backdated** entries and reposting hurts      | **Standard Cost** *(separate guide)* |
| You want predictable, fixed product cost & isolated price variance | **Standard Cost** *(separate guide)* |


### Best practices (both methods)

- **Set the method before the item transacts.** Changing an item's valuation method while stock exists is disruptive and may be blocked.
- **Enable perpetual inventory accounts** (warehouse/stock, stock-received-but-not-billed, COGS, stock adjustment) so valuation and GL stay in lock-step.
- **Batch your historical corrections** and run them in low-traffic windows, since they trigger reposting.
- **Use Landed Cost Vouchers promptly** after receipt to avoid large retroactive revaluations later.
- **Reconcile stock value vs. GL** periodically (Stock Ledger / Stock Balance vs. the inventory account) to catch drift early.
- **Be consistent per item category** so reporting and margins are comparable across similar items.

---

## 7. Summary

- **FIFO** costs outgoing stock at the **actual rate of the oldest remaining layer** — precise, audit-friendly, ideal for perishables and lot-traceable goods, but layer-heavy and reposting-sensitive.
- **Moving Average** costs outgoing stock at a **single blended rate** — simple, smooth, ideal for commoditized high-volume items, but less precise and still reposting-sensitive.
- **Both** recompute (repost) the forward ledger when the past changes. If that cost is the deciding factor, the **Standard Cost** method avoids it entirely — see the *Standard Valuation Rate* guide.

<!-- page: erpnext/erpnext__filter-options-in-select-field.md -->
---
title: "Filter Options in Select Field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/filter-options-in-select-field"
updated: "2026-03-02"
---

Let's say you have two drop-down fields named State and City. State has two values Karnataka and Maharashtra and City has four values, Bangalore, Mysore, Mumbai, and Pune. If you would like to filter options in City based on the value chosen in State, you can write custom script as shown below.

```
frappe.ui.form.on("Lead", "state", function(frm) {
  if(frm.doc.state == "Karnataka") {
    set_field_options("city", ["Bangalore","Mysore"])
  } else if(frm.doc.state == "Maharashtra") {
    set_field_options("city", ["Mumbai","Pune"])
  } else if(frm.doc.state == "") {
    set_field_options("city", ["","Bangalore","Mysore","Mumbai","Pune"])
  }
});
  

```

![Opening Account](/files/filter_dropdown.gif)



Here’s an example of a custom script that filters options in a Select field within a child table:

```
frappe.ui.form.on('Parent DocType', {
    refresh: function (frm) {
        // Trigger this function when the form is refreshed or reloaded
        frm.fields_dict['child_table_fieldname'].grid.get_field('select_fieldname').get_query = function(doc, cdt, cdn) {
            return {
                filters: [
                    ['Some Field', '=', 'Some Value'] // Replace with your filter criteria
                ]
            };
        };
    }
});
```

### Example Scenario

Suppose you have a parent DocType called **Sales Order** with a child table field called **items**. The child table has a Select field named **itemcode**, and you want to filter the options to show only items from a specific category.

Here’s how your script might look:

```
frappe.ui.form.on('Sales Order', {
    refresh: function (frm) {
        frm.fields_dict['items'].grid.get_field('item_code').get_query = function(doc, cdt, cdn) {
            return {
                filters: [
                    ['Item Group', '=', 'Specific Category'] // Adjust the filter criteria as needed
                ]
            };
        };
    }
});
  

```

<!-- page: erpnext/erpnext__finance-book.md -->
---
title: "Finance Book | ERPNext Documentation"
description: "Learn how to use Finance Books in ERPNext for alternate accounting views, company defaults, report filters, and separate fixed-asset depreciation schedules."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/finance-book"
updated: "2026-08-14"
---

A Finance Book lets the same [Company](https://docs.frappe.io/erpnext/company) maintain parallel accounting views when a transaction or depreciation schedule must belong to one reporting basis but not another. A business may keep one book for statutory reporting and another for management or shareholder reporting.



Finance Books are optional. Do not create several books merely to separate departments, branches, projects, or product lines. Use [Cost Centers](https://docs.frappe.io/erpnext/cost-center) or [Accounting Dimensions](https://docs.frappe.io/erpnext/accounting-dimensions) for those reporting segments. Use Finance Books only when the same company needs alternate accounting treatments or report views.



Typical uses include:

- statutory and management depreciation using different methods or useful lives;
- local accounting rules and a separate group-reporting basis;
- an alternate internal balance sheet without changing the company's primary ledger view.

## Before you begin

Agree the purpose and ownership of every book with your accountant. Decide which book is the company default, which entries must be common to all books, and which reports reviewers will run.

The example below uses **Statutory Reporting** as the default Finance Book for Nova Electronics Trading and **Management Reporting** as an alternate book.

## Create Finance Books

Open **Finance Book** and select **Add Finance Book**. Enter a clear name that describes the reporting basis, then save.

Create only the books your reporting policy requires. The Finance Book record itself contains a name; its effect comes from selecting it on accounting transactions, depreciation schedules, and reports.



![Finance Book list with Statutory Reporting and Management Reporting](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-finance-book-finance-book-list.png)

## Set the company default

Open the Company record and select the **Accounts** tab. Set **Default Finance Book** to the book that represents normal accounting for that company, then save.



![Default Finance Book on the Company record](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-finance-book-company-default-finance-book.png)

The default is important because the current [Journal Entry](https://docs.frappe.io/erpnext/journal-entry) Finance Book field is read-only. ERPNext carries the company's default book into new Journal Entries instead of asking users to choose it manually each time.

Do not change the default casually after transactions exist. Review the effect on reports and future entries with your accountant first.

## Record an entry in a Finance Book

Create the transaction using the normal workflow. In a Journal Entry, open **More Info** and review the **Finance Book** value before submission.



![Finance Book carried into a submitted Journal Entry](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-finance-book-journal-entry-finance-book.png)

The example posts a $450 maintenance adjustment to **Statutory Reporting**:


| Account                     | Debit | Credit | Finance Book effect            |
| --------------------------- | -----: | ------: | ------------------------------ |
| Office Maintenance Expenses | $450  |        | Appears in the statutory book. |
| Nova Operating Bank         |       | $450   | Appears in the statutory book. |


An entry with a specific Finance Book belongs to that book. An entry whose Finance Book is blank is treated as common and is included in Finance Book report views. This preserves the original ERPNext behavior for transactions that apply to every reporting basis.

## Review reports by Finance Book

Open the [General Ledger](https://docs.frappe.io/erpnext/general-ledger), [Trial Balance](https://docs.frappe.io/erpnext/trial-balance), [Balance Sheet](https://docs.frappe.io/erpnext/balance-sheet), or [Profit and Loss Statement](https://docs.frappe.io/erpnext/profit-and-loss-statement). Select the company, dates, and Finance Book, then refresh the report.



![General Ledger filtered by Statutory Reporting Finance Book](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-finance-book-general-ledger-finance-book-filter.png)

In General Ledger, **Include Default FB Entries** is enabled by default. When it is enabled, ERPNext uses the company's default Finance Book and includes common entries whose Finance Book is blank. If you select a book different from the company default, clear **Include Default FB Entries** first. ERPNext otherwise stops the report and asks you to clear it.

Use the same filters when comparing reports. A report filtered to one Finance Book cannot be compared reliably with an unfiltered report or a report using a different setting for default-book entries.

## Use Finance Books for depreciation

A company may depreciate the same [Asset](https://docs.frappe.io/erpnext/asset) differently for statutory and management reporting. For example, the statutory book may use Written Down Value while the management book uses Straight Line.

On the asset's Finance Books table, each row can hold its own:


| Field                         | What it controls                                                        |
| ----------------------------- | ----------------------------------------------------------------------- |
| Finance Book                  | Reporting book that receives the depreciation entries.                  |
| Depreciation Method           | Straight Line, Double Declining Balance, Written Down Value, or Manual. |
| Frequency of Depreciation     | Number of months between scheduled postings.                            |
| Total Number of Depreciations | Number of scheduled depreciation entries.                               |
| Depreciation Posting Date     | Date from which the schedule begins.                                    |
| Salvage Value                 | Expected value after the useful life.                                   |
| Rate of Depreciation          | Percentage used where the selected method requires it.                  |


ERPNext can generate a separate [depreciation schedule](https://docs.frappe.io/erpnext/asset-depreciation) for each Finance Book and post the resulting automatic depreciation entries to the corresponding book. This keeps alternate asset values separate without duplicating the asset master.

## Important fields and what they mean


| Field or control           | Where it appears                               | Meaning                                                                                                |
| -------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Name                       | Finance Book                                   | Identifies the reporting basis. Use a stable, policy-oriented name.                                    |
| Default Finance Book       | Company                                        | Default book carried into supported accounting transactions.                                           |
| Finance Book               | Journal Entry and supported accounting records | Book to which the resulting GL entries belong.                                                         |
| Finance Book               | Financial reports                              | Limits the report to the selected book plus common entries.                                            |
| Include Default FB Entries | General Ledger                                 | Includes the company's default book and common entries. Clear it before reporting on a different book. |


## Troubleshooting

### A depreciation entry does not appear in the Trial Balance

Open the report and select the Finance Book used by the asset's depreciation schedule. A Finance Book-specific entry may not appear in a report using another book or no matching book filter.

### ERPNext asks me to clear Include Default FB Entries

The report has a Finance Book different from the company's default while **Include Default FB Entries** is enabled. Clear the checkbox, keep the alternate book selected, and refresh.

### The Journal Entry Finance Book cannot be edited

This is expected in current ERPNext. The field is read-only and comes from the company's **Default Finance Book**. Review the Company setup before creating entries that require a different accounting basis.

### Two Finance Book reports do not reconcile

Confirm that both reports use the same company, date range, accounts, opening-entry settings, and **Include Default FB Entries** choice. Then identify entries assigned exclusively to one book and compare the related asset schedules or Journal Entries.

### An entry appears in more than one Finance Book

Check whether the transaction's Finance Book is blank. Blank entries are common entries and appear with Finance Book report views. Assign a book only when the transaction belongs exclusively to that reporting basis.

## FAQs

### Is a Finance Book mandatory?

No, A company with one accounting basis can operate without creating additional Finance Books.

### Should I create one Finance Book for each department?

No, Use Cost Centers or Accounting Dimensions for departments, branches, projects, and other operational segments. Finance Books are for alternate accounting treatments or reporting bases.

### Can the same asset use different depreciation methods?

Yes, Add separate Finance Book rows to the asset and configure a different depreciation method or schedule for each reporting basis.

### Why does a blank Finance Book entry appear in a filtered report?

A blank Finance Book means the entry is common. ERPNext includes common entries when it builds a Finance Book view so shared transactions are not lost.

### Can I change the default Finance Book after posting transactions?

Technically the Company setting can be changed, but treat it as an accounting-policy change. Review existing entries, future posting behavior, report filters, and audit requirements before changing it.

## Related topics

- [Journal Entry](https://docs.frappe.io/erpnext/journal-entry)
- [General Ledger](https://docs.frappe.io/erpnext/general-ledger)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Asset Depreciation](https://docs.frappe.io/erpnext/asset-depreciation)
- [Accounting Dimensions](https://docs.frappe.io/erpnext/accounting-dimensions)
- [Cost Center](https://docs.frappe.io/erpnext/cost-center)

<!-- page: erpnext/erpnext__financial-report-template.md -->
---
title: "Financial Report Template"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/financial-report-template"
updated: "2026-08-14"
---

Nova Industries prepares monthly reports for its managers, investors, and lenders. The finance team needs one concise Profit and Loss view for the board and an IFRS-style Cash Flow presentation for external readers. Rebuilding each version in a spreadsheet is slow, makes formulas difficult to govern, and creates uncertainty about whether every report still agrees with the ledger.



A Financial Report Template is a reusable blueprint that turns the same submitted accounting data into different report presentations. Nova can standardise headings across subsidiaries, reuse calculations such as Gross Profit and Operating Margin, hide zero or supporting rows, control signs and charts, and produce the same approved structure every month without changing its Chart of Accounts.



Separate templates can support board packs, investor updates, lender reporting, group reporting, and regional presentation requirements. A template controls grouping, labels, calculations, and layout. It does not by itself make the underlying books compliant with IFRS, US GAAP, or another country's rules because recognition, valuation, depreciation, tax, and disclosure requirements must also be configured and professionally reviewed.

## Before you begin

- Review the [Chart of Accounts](/erpnext/chart-of-accounts) and assign Account Categories where the template will filter by category.
- Decide the report's required lines, calculations, hierarchy, and sign presentation.
- Choose stable Line References that formulas can reuse.
- Test the template on a non-production company and period before relying on it for reporting.

## Start from a template

Open Financial Report Template. ERPNext may provide reusable templates that can be reviewed and adapted, or you can create a new template for a controlled reporting requirement.

![Financial Report Template list on the Nova develop demo site](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-list.png)

## Create the template

![Standard Cash Flow Statement Financial Report Template opened on the Nova Industries demo site](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-form.png)



1. Enter a descriptive Template Name and select the Report Type.
2. Add rows to the Report Line Items table in the order they should appear.
3. Select the Data Source for each row.
4. Give calculated or reusable rows a unique Line Reference.
5. Configure formatting, visibility, sign, and chart options.
6. Save, run the associated report, and reconcile the output with standard financial statements.

## Choose a row data source

![Report Line Items in the Standard Cash Flow Statement template](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-form.png)




| Data source       | Use it for                                                      | Example                                       |
| ----------------- | --------------------------------------------------------------- | --------------------------------------------- |
| Account Data      | Balances selected through account filters or categories         | All accounts in Revenue from Operations       |
| Calculated Amount | Arithmetic based on referenced rows                             | `REVENUE - COST_OF_GOODS_SOLD`                |
| Custom API        | Approved server-side logic unavailable through standard filters | A specialised regulatory or management metric |
| Visual row        | Headers, blank lines, or layout structure                       | OPERATING EXPENSES                            |


## Important row fields


| Field                     | Meaning                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Display Name              | The line label shown to report readers.                                                                          |
| Line Reference            | A unique code used by calculations and other rows. Start with a letter and use letters, numbers, or underscores. |
| Formula or Account Filter | The expression, filter, or API path used by the selected data source.                                            |
| Balance Type              | Opening balance, closing balance, or movement during the period.                                                 |
| Reverse Sign              | Changes presentation when a line should appear with the opposite sign.                                           |
| Hide If Zero              | Removes an empty line from the rendered report.                                                                  |
| Hidden Line               | Keeps a supporting calculation available without displaying it.                                                  |
| Include in Charts         | Makes the line eligible for the report chart where supported.                                                    |


## Build calculations safely

Nova can define `REVENUE` and `COGS` as account-data rows, then calculate `GROSS_PROFIT` with `REVENUE - COGS`. A margin row can use `(GROSS_PROFIT / REVENUE) * 100 if REVENUE != 0 else 0` to avoid division by zero.

## Validate coverage and output

Check that all intended accounts are included once, formulas reference valid rows, no circular dependency exists, and parentheses are balanced. Compare the template output with the standard [Balance Sheet or Profit and Loss Statement](/erpnext/accounting-reports) for the same company, period, Finance Book, and dimensions.

## See a template in the report

Nova selects the **Cash Flow Statement (IFRS)** template in the Cash Flow report. The report now uses the template's headings, ordering, visual rows, and calculations while continuing to read the same General Ledger entries.

![Cash Flow report for Nova Industries rendered with the Cash Flow Statement IFRS Financial Report Template](https://novacompanies.m.frappe.cloud/files/docs-20260814-financial-report-template-ifrs-output-v2.png)

The result separates cash flows from operating activities, presents supporting adjustments such as depreciation and finance costs, and retains calculated totals such as operating profit before working-capital changes. Finance can reuse this view for every period and still drill into the underlying accounting values when a number needs investigation.

## Troubleshooting

### A formula references an unknown line

Confirm that the source row has a Line Reference and that the formula uses the exact code. Keep references unique and create source rows before dependent calculations.

### An account is missing from the report

Review its Account Category and the row's account filter. Also check whether a parent or child account was selected and whether Hide If Zero suppresses the line.

### The report total differs from the standard statement

Align company, dates, Finance Book, cost center, dimensions, currency, period-closing treatment, and accumulation options. Then check for omitted or duplicated accounts.

## Frequently asked questions

### Should I edit a built-in template?

Use a controlled copy when the standard template must remain available as a baseline. Document every custom calculation and account category dependency.

### Can one template work across companies?

A category-based design can support comparable charts across companies, but each company must map accounts consistently and the output must be tested separately.

### Can a template replace statutory review?

The template controls presentation and calculations inside ERPNext. It does not determine whether the report meets local statutory, audit, or filing requirements.

## Related topics

- [Using Custom API Rows](/erpnext/using-custom-api-rows-in-financial-report-template)
- [Accounting Reports](/erpnext/accounting-reports)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Finance Book](/erpnext/finance-book)
- [Accounting Dimensions](/erpnext/accounting-dimensions)

<!-- page: erpnext/erpnext__fiscal-year-error.md -->
---
title: "Fixing Fiscal Year Error"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fiscal-year-error"
updated: "2026-08-14"
---

Nova Industries creates an invoice dated 2 January 2027, but ERPNext reports that the date is not in the selected fiscal year. The transaction date, the selected Fiscal Year, and the company’s defaults no longer agree. Create the missing year or correct the default instead of changing the document to an inaccurate date.

## Resolve the error

1. Open **Fiscal Year** and confirm a record covers the transaction date.
2. Check the start date, end date, and company assignment.
3. Set the new Fiscal Year as default when it should be used for new transactions.
4. Open Global Defaults and confirm the default Fiscal Year.
5. Reload ERPNext and reopen the transaction.

![Fiscal Year start and end dates highlighted](https://novacompanies.m.frappe.cloud/files/final-accounting-20260814-fiscal-year-dates.png)



## Troubleshooting

### The year exists but the error remains

Check whether the Fiscal Year is assigned to the transaction’s company, whether another field explicitly contains the old year, and whether the posting date falls exactly within the configured range.

### The date is intentionally in an older year

Select the appropriate fiscal year and confirm that the period is not frozen or closed. Obtain approval before entering a backdated accounting transaction.

## Frequently asked questions

### Should I change the date just to submit?

The posting date should reflect the real accounting event. Fix the year setup or obtain the required period access instead of using a false date.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__fiscal-year.md -->
---
title: "Fiscal Year | ERPNext Documentation"
description: "Create, assign, and manage fiscal years in ERPNext and understand how they differ from accounting periods and year-end closing."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/fiscal-year"
updated: "2026-08-14"
---

A financial report is meaningful only when ERPNext knows where one reporting year ends and the next begins. A Fiscal Year defines that period for transactions, budgets, opening balances, and year-end closing.



For Nova Industries, the finance team may report from January to December while another company on the same site follows April to March. Separate Fiscal Year records let both companies post and compare transactions using the periods required by their owners, auditors, and local regulations.



This page shows how to create the period, assign it to the right companies, control posting dates, and avoid gaps or overlaps that can make transactions fail validation.

## Create a Fiscal Year

1. Go to **Home &gt; Accounting &gt; Accounting Masters &gt; Fiscal Year**.
2. Click **Add Fiscal Year**.
3. Enter a name, start date, and end date.
4. Add the companies that use it.
5. Enable **Is Short Year** only for a genuine transition period shorter than twelve months.
6. Save.

![Fiscal Year dates and company](/files/fiscal-year-dates.webp)

## Set the default Fiscal Year

Open the Fiscal Year and use the action to set it as default. ERPNext uses the default year when it initializes posting dates and report filters.

The posting date still determines the actual fiscal year. A transaction cannot be posted outside a valid Fiscal Year for its company.

## Create the next year

ERPNext can create the next Fiscal Year shortly before the current year ends. Confirm the dates and company assignment before users begin posting in it.

## Fiscal Year, Accounting Period, and closing

These records serve different purposes:


| Record                 | Purpose                                               |
| ---------------------- | ----------------------------------------------------- |
| Fiscal Year            | Defines the accounting year and reporting period      |
| Accounting Period      | Restricts selected transaction types for a date range |
| Period Closing Voucher | Transfers profit or loss to a closing account         |


Creating a new Fiscal Year does not close the previous one. Complete reconciliation, adjustments, reporting, and the closing voucher as separate activities.

## Troubleshooting

**The posting date is outside the Fiscal Year**

Create or assign the correct Fiscal Year to the company. Do not alter historical dates to bypass the validation.

**A report opens in the wrong year**

Change the report filter or set the intended Fiscal Year as default.

## Related topics

- [Accounting Period](https://docs.frappe.io/erpnext/accounting-period)
- [Period Closing Voucher](https://docs.frappe.io/erpnext/period-closing-voucher)
- [Company accounting defaults](https://docs.frappe.io/erpnext/company-accounting-defaults)
- [Accounting Setup Checklist](https://docs.frappe.io/erpnext/accounting-setup-checklist)

<!-- page: erpnext/erpnext__france.md -->
---
title: "Requirements for France"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/france"
updated: "2026-07-02"
---


ERPNext aims to support local regulation for different regions in the world. In most cases, ERPNext is very flexible, so you can easily add custom fields and make custom reports to support the regulation of your region.

This section contains region specific features for France.

- [Le Fichier des Écritures Comptables (FEC)](/erpnext/fichier_des_ecritures_comptables)
- [Sales and Payment Transactions](/erpnext/local_overrides)

<!-- page: erpnext/erpnext__frappe-healthcare.md -->
---
title: "Healthcare Module in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/frappe-healthcare"
updated: "2026-07-04"
---

Frappe Healthcare was earlier available as the Healthcare module inside ERPNext. It has now been separated into a dedicated open-source app called Marley Health.

Marley Health is owned and maintained by earthians Health Informatics Private Limited. It can be installed alongside ERPNext when an organization wants to manage healthcare workflows such as patients, appointments, consultations, clinical records, laboratory tests, procedures, and billing.

Marley Health documentation: [https://marley.frappe.cloud/docs](https://marley.frappe.cloud/docs)

## Basic features

### Patient management

Marley Health helps maintain patient records, demographics, contact details, medical history, and related healthcare documents. The patient record becomes the central place from which appointments, consultations, lab tests, procedures, and billing can be tracked.

### Healthcare practitioners

Organizations can maintain doctors, consultants, therapists, and other healthcare practitioners. These records are used for appointments, schedules, consultations, and clinical documentation.

### Appointments and scheduling

The app supports appointment booking and scheduling so front-desk and clinical teams can manage patient visits. Appointments can be linked to patients, practitioners, departments, and service units.

### Patient encounters and consultations

Healthcare teams can record consultations using patient encounters. Encounters help capture symptoms, diagnosis, observations, notes, prescriptions, investigations, and follow-up advice.

### Clinical records

Marley Health helps maintain structured healthcare records such as vital signs, prescriptions, medical observations, and other clinical information. This gives practitioners a clearer view of the patient's treatment history.

### Laboratory tests and procedures

The app supports lab test and clinical procedure workflows. Tests and procedures can be ordered, recorded, and linked back to the patient record.

### Inpatient care

For facilities that admit patients, Marley Health can help manage inpatient records, admissions, service units, and patient movement inside the healthcare facility.

### Billing integration

Because Marley Health works with ERPNext, healthcare services can be connected to ERPNext billing documents such as Sales Invoices. This helps combine clinical operations with accounting and revenue tracking.

## Typical healthcare cycle

```
Patient Registration
        |
        v
Appointment Booking
        |
        v
Patient Encounter / Consultation
        |
        +-------------------+
        |                   |
        v                   v
Prescription          Lab Test / Procedure
        |                   |
        +---------+---------+
                  v
              Billing
                  |
                  v
              Follow-up
```

## When should you install Marley Health?

Install Marley Health if your ERPNext site is used by a clinic, hospital, diagnostic center, therapy center, or any healthcare organization that needs patient and clinical workflows.

Read the Marley Health documentation here:

[https://marley.frappe.cloud/docs](https://marley.frappe.cloud/docs)

<!-- page: erpnext/erpnext__freeze-account.md -->
---
title: "Freeze an Account | ERPNext Documentation"
description: "Learn how to freeze an Account in ERPNext, restrict new postings, authorize exception roles, preserve ledger history, verify defaults, and unfreeze it safely."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/freeze-account"
updated: "2026-08-03"
---

Freeze an individual ledger Account when users should be able to see its history but should no longer post new transactions to it. This is useful after replacing a bank, expense, income, receivable, or payable account without deleting the older ledger.



Freezing does not remove the Account or its existing [General Ledger](https://docs.frappe.io/erpnext/general-ledger) entries. It prevents ordinary users from using that Account in new accounting transactions. An explicitly authorized role can still set frozen Accounts and create or modify entries against them.

> Freeze only an Account that should no longer receive postings. If you need to prevent entries for a past date range instead, use [Freeze Accounting Entries](https://docs.frappe.io/erpnext/freeze-accounting-entries) or an [Accounting Period](https://docs.frappe.io/erpnext/accounting-period).

## Before you begin

Confirm that:

1. The Account is a ledger Account, not a group used to organize the [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts).
2. Users should retain access to its historical transactions and balances.
3. A replacement Account is available if future invoices, payments, or journals still need a ledger for the same purpose.
4. Defaults in the Company, Customer, Supplier, Item, tax templates, and [Mode of Payment](https://docs.frappe.io/erpnext/mode-of-payment) no longer point to the Account you plan to freeze.
5. The role permitted to manage frozen Accounts has been reviewed.

## Authorize a role to manage frozen Accounts

The permission is company-specific in the current ERPNext interface.

1. Open the required **Company**.
2. Select the **Accounts Closing** tab.
3. In **Roles Allowed to Set and Edit Frozen Account Entries**, select the role that may freeze Accounts and post or modify entries against them.
4. Save the Company.

![Company Accounts Closing tab with Roles Allowed to Set and Edit Frozen Account Entries highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-freeze-an-account-role-allowed-for-frozen-accounts.png)

Grant this role sparingly. A user with it can bypass the restriction when posting to a frozen Account. In older ERPNext documentation, this control may be described as an Accounts Settings field. On the current develop interface it appears in the Company's **Accounts Closing** tab.

## Freeze an Account

1. Open **Accounting &gt; Chart of Accounts**.
2. Select the Company.
3. Open the ledger Account that should stop receiving transactions.
4. Set **Frozen** to **Yes**.
5. Save the Account.

![Ledger Account with Frozen set to No before the change](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-freeze-an-account-account-not-frozen.png)



![Ledger Account with Frozen set to Yes and Save highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-refresh-20260803-freeze-an-account-freeze-account-before-save.png)

After saving, ordinary users cannot use the Account in accounting transactions. Existing [Journal Entries](https://docs.frappe.io/erpnext/journal-entry), invoices, payments, and reports remain connected to it.

## What freezing changes


| Area                                | Result                                                                                                                                 |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| New accounting transactions         | Ordinary users cannot post entries against the frozen Account.                                                                         |
| Authorized role                     | Users with the Company role configured for frozen Account entries can set the Account as frozen and post or modify entries against it. |
| Existing ledger history             | Remains available in the General Ledger and financial reports.                                                                         |
| Account master                      | Remains in the Chart of Accounts and can be unfrozen later.                                                                            |
| Defaults that reference the Account | Are not automatically replaced. Update them before users create new transactions.                                                      |
| Date-based locks                    | Are unchanged. Freezing one Account is separate from freezing entries through a date or closing an Accounting Period.                  |


## Verify the change

After saving:

1. Reopen the Account and confirm **Frozen** is **Yes**.
2. Check that active defaults now use the intended replacement ledger.
3. Open the [General Ledger report](https://docs.frappe.io/erpnext/general-ledger) and confirm the historical Account balance remains visible.
4. If your controls require a test, use a draft transaction with a test user who does not have the exception role. Do not submit an incorrect entry merely to test the restriction.

## Unfreeze an Account

An authorized user can reopen the Account, set **Frozen** to **No**, and save. Before unfreezing, confirm why postings need to resume and whether a newer Account has already replaced it. Allowing both Accounts to remain active can split transactions and make [financial statements](https://docs.frappe.io/erpnext/accounting-reports) harder to reconcile.

## Troubleshooting


| Issue                                           | What to check                                                                                                                               |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Frozen cannot be changed                        | Confirm that your user has the role selected in the Company's Accounts Closing settings.                                                    |
| A transaction still posts to the frozen Account | Check whether the user has the authorized role. Also confirm that the transaction used the Account you froze, not a similarly named ledger. |
| New transactions default to the frozen Account  | Replace the Account in Company and master defaults, tax templates, payment modes, and transaction templates.                                |
| A past period must be locked                    | Use Accounts Frozen Till Date or an Accounting Period. Freezing an Account controls a ledger, not a date range.                             |
| Reports still show the Account                  | This is expected. Freezing stops new postings and does not remove historical balances.                                                      |


## Frequently asked questions

### Does freezing an Account delete it?

No, The Account and its historical ledger entries remain available. The restriction applies to new or modified accounting entries.

### Is a frozen Account the same as a disabled Account?

No, **Frozen** is an accounting control that blocks ordinary postings while permitting a configured role to handle exceptions. **Disable** is a broader master-state control. Use the option that matches your control objective.

### Can an authorized user post to a frozen Account?

Yes, A user with the role configured in **Roles Allowed to Set and Edit Frozen Account Entries** can create or modify entries against it. Keep that role limited and review its assignments.

### Does freezing an Account affect its balance?

No, Existing debits, credits, and balances remain unchanged. The Account continues to appear in reports based on its historical postings.

### When should I use a date freeze instead?

Use **Accounts Frozen Till Date** when the restriction should apply to accounting entries before a cutoff date. Use an Accounting Period when selected transaction types must be closed for a completed period. Use **Frozen** on the Account when one specific ledger should stop receiving entries regardless of date.

## Related topics

- [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts)
- [Freeze Accounting Entries](https://docs.frappe.io/erpnext/freeze-accounting-entries)
- [Accounting Period](https://docs.frappe.io/erpnext/accounting-period)
- [Company](https://docs.frappe.io/erpnext/company-setup)
- [General Ledger](https://docs.frappe.io/erpnext/general-ledger)
- [Journal Entry](https://docs.frappe.io/erpnext/journal-entry)

<!-- page: erpnext/erpnext__freeze-accounting-entries.md -->
---
title: "Freeze Accounting Entries                                          "
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/freeze-accounting-entries"
updated: "2026-08-14"
---

Nova Industries went live on ERPNext on 1 January. If someone accidentally posts a transaction dated in December, the opening balances and signed-off legacy reports no longer agree. **Accounts Frozen Upto** gives finance a simple cut-off date: ordinary users cannot create or change accounting entries on or before that date.



Use this control for migration cutover dates, completed month-end closes, and audited periods. Unlike an [Accounting Period](/erpnext/accounting-period), it is a broad accounting freeze rather than a list of selected document types.

## Set the frozen date

1. Open the **Company** record.
2. Open the **Accounts Closing** tab.
3. Set **Accounts Frozen Till Date** to the last protected date.
4. Select **Roles Allowed to Set and Edit Frozen Account Entries**.
5. Save the Company and test with a non-privileged account before relying on the control.

![Company Accounts Closing tab showing the frozen date and authorized role](https://novacompanies.m.frappe.cloud/files/final-accounting-20260814-company-frozen-period.png)



## Use the exception role carefully

The role is for approved corrections, not a way to continue routine backdated posting. Keep membership small, require supporting evidence, and review the General Ledger and Version history after an exception.

## Troubleshooting

### A user can still post inside the frozen period

Check whether the user has the authorized frozen-entries role. Confirm the document actually posts accounting entries and that its posting date is on or before the configured date.

### The authorized user is still blocked

Check for a submitted Accounting Period, fiscal-year restriction, immutable-ledger rule, or stock reposting restriction. These are separate controls and the frozen-entries role does not override every validation.

## Frequently asked questions

### Does freezing delete or reverse anything?

It prevents new changes through the cut-off date. Existing ledger entries remain unchanged.

### Can I move the date forward every month?

That is a common month-end practice after reconciliations and approval. Record the close checklist and the person who approved each change.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__general-ledger.md -->
---
title: "General Ledger"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/general-ledger"
updated: "2026-08-14"
---

Nova Industries has finished its August review. The finance manager sees a $20,000 sale in the books and needs to confirm that the customer receivable, sales income, inventory value, and cost of goods sold were posted correctly. A financial statement shows the summarized result. The General Ledger shows the entries that created it.



The General Ledger is ERPNext's detailed accounting trail. It lists every debit and credit generated by submitted transactions and connects each row to its source voucher. Use it to explain an account balance, investigate an unexpected posting, or provide transaction-level evidence for an audit. It does not replace the [Accounts Receivable](/erpnext/accounts-receivable) and [Accounts Payable](/erpnext/accounts-payable) reports when the question is which invoices remain outstanding.

## Before you begin

Transactions must be submitted before they appear in the ledger. Confirm the correct [Company](/erpnext/company), fiscal period, and reporting currency. If your organisation uses [Finance Books](/erpnext/finance-book), [Cost Centers](/erpnext/cost-center), Projects, or other [Accounting Dimensions](/erpnext/accounting-dimensions), use the same filters when comparing reports.

## Run the General Ledger

1. Open **Accounting** and select **General Ledger**.
2. Select **Nova Industries** and the required date range.
3. Leave Account and Party blank to review all postings, or narrow the report to the balance you are investigating.
4. Use Voucher No when you already know the source transaction. Select a categorization option when you want entries arranged by Account, Voucher, or Party.
5. Refresh the report and confirm that the result has fully loaded before interpreting it.

![General Ledger filters showing Nova Industries and the selected reporting period](https://novacompanies.m.frappe.cloud/files/docs-20260814-nova-industries-general-ledger-filters.png)

## Follow a Sales Invoice through the ledger

For the selected period, Nova Industries has $395,762 in total debits and $395,762 in total credits. Equal totals show that the selected entries are mathematically balanced. They do not prove that every transaction used the correct account, so the finance manager opens the rows behind the $20,000 sale.

![Populated General Ledger for Nova Industries with balanced debit and credit totals](https://novacompanies.m.frappe.cloud/files/docs-20260814-nova-industries-general-ledger-voucher-postings.png)


| Posting             | Debit                      | Credit                | What it means                                               |
| ------------------- | -------------------------- | --------------------- | ----------------------------------------------------------- |
| Customer balance    | Debtors $20,000            |                       | The customer now owes Nova Industries.                      |
| Sales income        |                            | Sales $20,000         | The sale increases income for the period.                   |
| Inventory reduction |                            | Stock In Hand $14,500 | The inventory asset decreases by the delivered stock value. |
| Cost recognition    | Cost of Goods Sold $14,500 |                       | The cost of the sold goods becomes an expense.              |


The receivable and income rows explain the commercial sale. The stock and cost rows explain the inventory leaving the business. This is why one [Sales Invoice](/erpnext/sales-invoice) can produce more than two ledger rows when stock is updated.

## Open the source voucher

Select the Voucher No in the report to open the submitted transaction. Compare the customer, posting date, items, income account, taxes, stock settings, and totals with the ledger rows. The voucher explains the business event, while the General Ledger explains its accounting effect.

![Submitted Sales Invoice opened from its General Ledger voucher link](https://novacompanies.m.frappe.cloud/files/docs-20260814-nova-industries-general-ledger-source-sales-invoice.png)

Ledger rows cannot be edited directly. If an account or dimension is wrong, correct the source through its supported cancellation and amendment process or post an approved [Journal Entry](/erpnext/journal-entry). Review [Immutable Ledger](/erpnext/immutable-ledger) behavior before correcting backdated stock or accounting transactions.

## Understand the important columns


| Column                               | How to read it                                                                                |
| ------------------------------------ | --------------------------------------------------------------------------------------------- |
| Posting Date                         | The accounting date used by the source voucher. It determines the reporting period.           |
| Account                              | The ledger account affected by the row.                                                       |
| Debit and Credit                     | The two sides of the posting in the displayed currency.                                       |
| Balance                              | The running debit less credit balance for the current report arrangement.                     |
| Voucher Type and Voucher No          | The submitted source document that created the row.                                           |
| Against Account                      | The counterpart account or accounts from the same voucher.                                    |
| Party                                | The Customer, Supplier, Employee, Shareholder, or other party associated with a party ledger. |
| Cost Center, Project, and dimensions | The reporting segments copied from the transaction.                                           |


## Choose the right categorization


| View                                 | Use it when                                                                                                        |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| No categorization                    | You need each individual GL Entry in posting order.                                                                |
| Categorize by Account                | You need opening, movement, and closing values account by account.                                                 |
| Categorize by Voucher                | You want all rows created by each transaction together. ERPNext does not allow a Voucher No filter with this view. |
| Categorize by Voucher (Consolidated) | You want a compact voucher-level result instead of every underlying row.                                           |
| Categorize by Party                  | You are reviewing ledger movement for customers or suppliers.                                                      |


## General Ledger, Trial Balance, and Payment Ledger


| Report                                    | Question it answers                                                                              |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------ |
| General Ledger                            | Which debit and credit entries created this balance, and which vouchers produced them?           |
| [Trial Balance](/erpnext/trial-balance)   | What is the opening, period movement, and closing balance for every account?                     |
| [Payment Ledger](/erpnext/payment_ledger) | How were invoices, payments, credit notes, and advances linked to calculate outstanding amounts? |


Use the General Ledger for accounting evidence. Use Trial Balance for account-level closing balances. Use Payment Ledger and [Payment Reconciliation](/erpnext/payment-reconciliation) when an invoice remains outstanding because a payment or credit has not been allocated correctly.

## Troubleshooting

### A submitted voucher is missing

Check Company, posting dates, Account, Party, Finance Book, dimensions, and Voucher No. Draft documents have not posted ledger entries. Also confirm that the report is not excluding cancelled or period-closing entries needed for the investigation.

### General Ledger and Trial Balance appear different

Run both reports with the same Company, dates, Finance Book, dimensions, presentation currency, and period-closing options. Trial Balance separates opening, movement, and closing values, while General Ledger lists the underlying postings.

### The debit and credit totals do not match

Remove narrow Account and Party filters before concluding that the books are unbalanced. A filtered subset can display only one side of otherwise balanced vouchers. Compare the full company scope for the same period.

### The opening balance is unexpected

The opening value includes qualifying postings before the From Date. Extend the date range, inspect the account from the fiscal-year start, and verify opening entries and previous closing activity.

## Frequently asked questions

### Can a General Ledger row be edited?

ERPNext generates ledger rows from submitted source documents. Correct the voucher through its supported lifecycle or use an approved adjustment. Direct editing would break the audit trail.

### Why does one voucher create several rows?

A transaction can affect receivable, income, tax, stock, cost, discount, and dimension accounts. Each accounting effect appears as a separate row.

### Does cancelling a transaction remove its history?

ERPNext preserves the accounting history through reversal behavior where applicable. Review the original voucher, cancellation, and later amended voucher together.

### Why is account currency different from company currency?

A foreign-currency account retains amounts in its account currency while ERPNext also records company-currency values. Confirm the selected presentation currency before comparing reports.

## Related topics

- [Accounting Reports](/erpnext/accounting-reports)
- [Trial Balance](/erpnext/trial-balance)
- [Payment Ledger](/erpnext/payment_ledger)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Journal Entry](/erpnext/journal-entry)
- [Repost Accounting Ledger](/erpnext/repost-accounting-ledger)

<!-- page: erpnext/erpnext__generate-item-code-based-on-custom-logic.md -->
---
title: "Generate Item Code Based On Custom Logic\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/generate-item-code-based-on-custom-logic"
updated: "2026-03-02"
---

Add this Custom Script in the script of **Item**, so that the new Item Code is  
generated just before the Item gets saved.



```javascript
 cur_frm.cscript.customvalidate = function (doc) {
  // clear itemcode (name is from itemcode)
  doc.itemcode = "";

  // first 2 characters based on itemgroup
  switch (doc.itemgroup) {
    case "Test A":
      doc.itemcode = "TA";
      break;
    case "Test B":
      doc.itemcode = "TB";
      break;
    default:
      doc.itemcode = "XX";
  }

  // add next 2 characters based on brand
  switch (doc.brand) {
    case "Brand A":
      doc.itemcode += "BA";
      break;
    case "Brand B":
      doc.itemcode += "BB";
      break;
    default:
      doc.itemcode += "BX";
  }
};
```

<!-- page: erpnext/erpnext__geolocation-field.md -->
---
title: "Geolocation Field"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/geolocation-field"
updated: "2026-03-04"
---

**The "Geolocation" field is used to capture and store geographical coordinates, such as latitude and longitude.** 

This can be useful for various purposes, such as tracking the location of assets, employees, or events. The geolocation data can help in mapping and visualizing the geographical distribution of various entities within the ERP system.

Here are a few key points about the Geolocation field in ERPNext:

1. **Storing Coordinates**: The Geolocation field typically stores latitude and longitude values, which represent a specific point on the earth's surface.
2. **Usage in Modules**: This field can be used in different modules where location information is relevant. For example, it can be used in the Assets module to track the physical location of assets or in the Employee module to log the locations of employees.
3. **Integration with Maps**: The geolocation data can be integrated with map services (like Google Maps) to provide visual representations of locations. This can be helpful for route planning, site visits, and logistics management.
4. **Automated Capture**: Some implementations allow for automated capture of geolocation data using GPS-enabled devices, ensuring accurate and real-time location tracking.
5. **Customization**: ERPNext allows customization, so the Geolocation field can be added to custom forms and doctypes as per the specific needs of the organization.

![geolocation field](/files/geolocation-field.gif)  

<!-- page: erpnext/erpnext__getting-started-with-erpnext.md -->
---
title: "Getting Started with ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/getting-started-with-erpnext"
updated: "2026-08-14"
---

Getting started with ERPNext can seem overwhelming, but focusing on these steps will help you set up and integrate the system effectively. Here’s a streamlined approach to kickstart your ERPNext journey.



**1. Define Your Needs**

- **Identify Requirements**: Determine the key features you need (e.g., inventory management, accounting).
- **Set Goals**: Clarify what you aim to achieve with ERPNext.



**2. Choose Deployment**

- **Cloud Hosting**: Opt for an easy setup with minimal infrastructure by using [Frappe Cloud](https://frappe.io/cloud) or a third-party provider.
- **Self-Hosting**: Install ERPNext on your own server if you have the technical resources and prefer control over your setup.



**3. Setup ERPNext**

- **Cloud**: Sign-up and follow the setup instructions.
- **Self-Hosting**: Prepare your server, and follow the [installation guide](https://github.com/frappe/erpnext) to set up ERPNext.



**4. Configure Basic Settings**

- **Setup Admin Account**: Create your administrator profile.
- **Enter Company Details**: Input essential information like company name, address, and currency.
- **System Configuration**: Configure different modules and workflows to match your requirements.



**5. Train and Launch**

- **Train Users**: Provide training [sessions or resources](https://school.frappe.io/lms/courses) to help your team get familiar with ERPNext.
- **Go Live**: Transition to ERPNext for your daily operations and monitor the system for any issues.

<!-- page: erpnext/erpnext__global-defaults.md -->
---
title: "Global Defaults/ERPNext Settings | ERPNext Documentation"
description: "Set ERPNext defaults for company, country, currency, distance, and transaction presentation with clear examples and precedence guidance."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/global-defaults"
updated: "2026-08-15"
---

Nova Industries is a fictional electronics manufacturer and distributor. Its finance team creates dozens of quotations, invoices, payments, and stock transactions every day. Most of them belong to Nova Industries, use USD, and refer to United States addresses. Asking every user to select those same values repeatedly wastes time, while one accidental selection of the wrong company or currency can send a transaction into the wrong books.



Global Defaults supplies the values ERPNext should suggest when a more specific rule has not already provided one. It reduces repetitive entry but does not replace judgement. Users must still verify the Company, Currency, and other values before submitting a transaction, especially in a multi-company or multi-currency organisation.

## Configure the default business context

![Default Company in ERPNext Global Defaults](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-global-company.png)


| Setting               | What it controls                                                   | Nova example                                                                                |
| --------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| Default Company       | Company suggested on new records                                   | Nova Industries is suggested for routine operating transactions.                            |
| Default Country       | Country suggested on addresses and regional fields                 | United States is proposed for a new customer address, but users can select another country. |
| Default Currency      | Currency used when no company or transaction rule is more specific | USD is the normal working currency. A EUR customer invoice can still use EUR.               |
| Default Distance Unit | Unit used for distance fields                                      | Mile suits Nova's United States operations; kilometre may suit another site.                |
| Demo Company          | Company identified for demonstration behaviour where supported     | Use only on a genuine demo or training site, not to label a live Company as fictional.      |


![Default Country in ERPNext Global Defaults](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-global-country.png)

![Default Currency in ERPNext Global Defaults](https://novacompanies.m.frappe.cloud/files/setup-core-20260815-global-currency.png)

## General settings and real effects


| Setting                                   | What it changes                                                             | Nova example                                                                                                                              |
| ----------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Hide Currency Symbol                      | Hides symbols where the interface uses the currency code or context instead | A report may show USD values without repeating the dollar symbol in every cell. Verify printed documents before enabling.                 |
| Disable Rounded Total                     | Removes the separate rounded-total calculation                              | Nova keeps exact cent totals when its accounting policy does not use cash-style rounding.                                                 |
| Disable In Words                          | Hides the amount written in words                                           | Useful when print formats do not require “One thousand dollars only.”                                                                     |
| Use Posting Datetime for Naming Documents | Uses posting date and time when a naming rule depends on date values        | A backdated invoice can receive a series based on its posting date instead of the time it was created. Test naming rules before enabling. |


## Which default wins

A field may receive a value from Company configuration, a user default, a Session Default, a mapped source document, or transaction logic. The most specific valid source normally matters more than the global suggestion. For example, a Session Default of Nova Electronics Trading can be used for one accountant's current session even when the global Company is Nova Industries.



Treat Global Defaults as convenience, not access control. User Permissions and roles decide what a user may open. A default value does not grant permission to that Company.

## Troubleshooting

### A new document shows a different Company

Check the user's defaults, Session Defaults, the source document used to create the record, and company-specific logic. Clear the session value and reload before testing again.

### The currency symbol still appears

The print format, report, browser cache, or linked Currency may control the display. Verify the final printed document rather than relying only on the form.

### A backdated document has an unexpected name

Review the naming series and Use Posting Datetime for Naming Documents. Do not rename submitted accounting documents without following the supported correction process.

## Frequently asked questions

### Do Global Defaults change existing records?

They normally supply values to newly created records. Existing records retain their saved values unless a separate supported process changes them.

### Can every user have a different default Company?

Users can have personal or session defaults, subject to permission. Global Defaults remains the common fallback.

### Does Default Currency convert transactions automatically?

It supplies a default context. Multi-currency transactions still require the correct party currency, account currency, and exchange rate.

### Should a multi-company site leave Default Company blank?

A common default can still be useful, but users must understand precedence and permissions. Leave it blank when no company is a safe general choice.

## Related topics

- [System Settings](/erpnext/system-settings)
- [Session Defaults](/erpnext/session-defaults)
- [Company](/erpnext/company-setup)
- [Currency](/erpnext/currency)
- [Multi Currency Accounting](/erpnext/multi-currency-accounting)
- [Naming Series](/erpnext/document-naming-settings)
- [User Permissions](/erpnext/user-permissions)

<!-- page: erpnext/erpnext__gocardless-integration.md -->
---
title: "Setting up GoCardless\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/gocardless-integration"
updated: "2026-02-26"
---


To setup GoCardless, go to `Explore > Integrations > GoCardless Settings`

## Setup GoCardless

To enable GoCardless in your ERPNext account, you need to configure the following parameters and Access Token and optionally (but highly recommended), a Webhooks Secret key.


You can setup several GoCardless payment gateways if needed. The choice of payment gateway account will determine which GoCardless account is used for the payment.

![GoCardless Settings](/files/gocardless_account.png)

On enabling service, the system will create a Payment Gateway record and an Account head in chart of account with account type as Bank.

![GoCardless COA](/files/gocardless_coa.png)

It will also create a payment gateway account. You can change the default bank account if needed and create a template for the payment request.

![Payment Gateway Account](/files/payment_gateway_account_gocardless.png)

After configuring the Payment Gateway Account, your system is able to accept online payments through GoCardless.

## SEPA Payments Flow

When a new payment SEPA payment in initiated, the customer is asked to enter his IBAN (or local account number) and to validate a SEPA mandate.

Upon validation of the mandate, a payment request is sent to GoCardless and processed.

If the customer has already a valid SEPA mandate, when instead of sending a payment request to the customer, the payment request is directly sent to GoCardless without the need for the customer to validate it.
The customer will only receive a confirmation email from GoCardless informing him that a payment has been processed.


## Mandate cancellation

You can setup a Webhook in GoCardless to automatically disabled cancelled or expired mandates in ERPNext.

The Endpoint URL of your webhook should be:

`https://yoursite.com/api/method/erpnext.erpnext_integrations.doctype.gocardless_settings.webhooks`


In this case do not forget to configure your Webhooks Secret Key in your GoCardless account settings in ERPNext.


## Supported transaction currencies
 "EUR", "DKK", "GBP", "SEK"

<!-- page: erpnext/erpnext__google_calendar.md -->
---
title: "Google Calendar Integration\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/google_calendar"
updated: "2026-02-28"
---


ERPNext provides an integration with Google Calendar in order for all users to synchronize their Google Calendar Events with ERPNext.


## How to set up Google Calendar Integration

In order to allow a synchronization with Google Calendar, you need to authorize ERPNext to get Calendar Events data from Google. Google Calendar Integration is set up with the following steps:

- Create OAuth 2.0 Credentials via [Google Settings](/erpnext/google_settings).
- In the Google Calendar list, click on New. Enter Calendar Name and the User for whom you want to sync and then save it.
- Depending what data you want to sync, you can select following
 - Pull from Google Calendar - Syncs all event from Google Calendar to ERPNext.
 - Push to Google Calendar - Syncs all event from ERPNext to Google Calendar.
- Now click on **Authorize Calendar Access** to authorize ERPNext to get Calendar Events data from Google.
- Once Authorized, you can manually sync Google Calendar Event or let ERPNext sync Google Contacts daily.

## How to use Google Calendar Integration

### Creating an Event in ERPNext
- Once Google Calendar Integration is succesful, all the events created in ERPNext will be synced if `Push to Google Calendar` is checked.
- Creating an Event in ERPNext
 ![](/files/erpnext-gc.gif)
- Deleting an Event in ERPNext
 ![](/files/gc-erpnext.gif)

### Syncing Events from Google Calendar
- Once Google Calendar Integration is succesful, all the events in Google Calendar will be synced if `Pull from Google Calendar` is checked.
- Syncing Events from Google Calendar to ERPNext
 ![](/files/gc-sync.gif)

<!-- page: erpnext/erpnext__google_contacts.md -->
---
title: "Google Contacts Integration\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/google_contacts"
updated: "2026-02-28"
---


ERPNext provides an integration with Google Contacts in order for all users to synchronize their Google Contacts with ERPNext.

## How to set up Google Contacts Integration

In order to allow a synchronization with Google Contacts, you need to authorize ERPNext to get Contacts data from Google. Google Contacts Integration is set up with the following steps:

- Create OAuth 2.0 Credentials via [Google Settings](/erpnext/google_settings).
- In the Google Contacts list, click on New. Enter the Google Account Email you want to sync and then save it. Now click on **Authorize Contacts Access** to authorize ERPNext to get Contacts data from Google.

## How to use Google Contacts Integration

### Creating a Contacts in ERPNext
- Once Google Contacts Integration is succesful, all the contacts created in ERPNext will be synced if `Push to Google Contacts` is checked.

Creating a Contact in ERPNext:
![](/files/google_contacts_create_contact.gif)

It will be shown in Google Contacts:
![](/files/google_contacts_create_contact_!.gif)

### Syncing Contacts from Google Contacts
- Once Google Contacts Integration is succesful, all the contacts in Google Contacts will be synced if `Pull from Google Contacts` is checked.
 ![](/files/google_contacts_contact_sync.gif)

<!-- page: erpnext/erpnext__google_drive.md -->
---
title: "Google Drive Integration"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/google_drive"
updated: "2026-02-27"
---

ERPNext provides an integration with Google Drive in order for all users to backup their data to Google Drive.

How to set up Google Drive Integration
--------------------------------------

In order to allow a ERPNext to upload backups to Google Drive, you need to authorize ERPNext to upload files to Google Drive. Google Drive Integration is set up with the following steps:

* Create OAuth 2.0 Credentials via [Google Settings](/erpnext/google_settings).
* In the Google Drive list, click on New. Enter the Backup folder name to save backups to Google Drive, the backup frequency and the email of the person to whom email is sent notifying the status of the backup and then save it. Now click on **Authorize Drive Access** to authorize ERPNext to push files to Google Drive.
* Once Authorized, you can save your backup to Google Drive.

How to use Google Drive Integration
-----------------------------------


> Note: If you are Frappe Cloud user, onsite and offsite backups are automatically created for you: <https://frappecloud.com/docs/sites/backups>
> 
> 

### Uploading backup to Google Drive

* Once Google Drive Integration is successful, you can upload the system backup as well as all your public and private files to Google Drive.
* To backup data to Google Drive, click on **Take Backup**. Backup process will run in the background and you will be notified regarding the backup status. ![](/files/google_drive.gif)

> **Note**: If the compressed backup size exceeds 1GB (Gigabyte), the system will upload the latest available backup to Google Drive instead of generating a new backup file.

<!-- page: erpnext/erpnext__google_maps.md -->
---
title: "Google Maps Integration\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/google_maps"
updated: "2026-02-28"
---


ERPNext provides an integration with Google Maps to calculate and optimize time for Delivery Trips.


## How to set up Google Maps Integration

To setup Google Maps in order to allow a ERPNext to calculate and optimize time for Delivery Trip, follow the steps:

- Enable API access [Google Settings](/erpnext/google_settings#for-google-maps).

## How to use Google Maps Integration

### Calculating and optimizing Delivery Trips
- Once Google Maps Integration is succesful, you can calculate ETA for a delivery stop or optimize delivery stops
 ![](/files/google_maps.gif)

<!-- page: erpnext/erpnext__google_settings.md -->
---
title: "Google Settings"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/google_settings"
updated: "2026-02-26"
---

To enable Google Integrations, ERPNext needs access to the API through which the data will be synced which is achieved using OAuth 2.0 Authentication Protocol.

How to set up Google Settings
-----------------------------

### For Google Calendar, Google Contacts, Google Drive and Google Indexing

In order to allow a synchronization with any of the above mentioned services, you need to authorize ERPNext to get data from Google. Following is an example for setting up Google Contacts Integration

1. Create a new project on Google Cloud Platform and generate new OAuth 2.0 credentials. ![](/files/google_contacts_project_creation.gif)
* Enable API Access in API Library for the Integration you wish to integrate.


	+ Google Calendar: **Calendar API**
	+ Google Contacts: **People API**
	+ Google Drive: **Drive API**
	+ Google Indexing: **Indexing API**![](/files/api.gif)
* In **API & Services > Credentials** create a new Credential and select **Create OAuth client ID**
* Select Application Type **Web Application**
* Add `https://{yoursite}` to Authorized JavaScript origins.
* Add `https://{yoursite}?cmd=frappe.integrations.doctype.google_calendar.google_calendar.google_callback` as an authorized redirect URI for Google Calendar.
* Add `https://{yoursite}/api/method/frappe.integrations.google_oauth.callback` as an authorized redirect URI for rest of the services.

![](/files/google_contacts_oauth.gif)
* Add your Client ID and Client Secret in the Google Settings in **Home > Integrations > Google Services > Google Settings**

### For Google Maps


> Setting the *API Key* is only required if you want to use the Directions API, for example in ERPNext's **Delivery Trip**. For the other features, this is not required.
> 
> 

In order to allow a synchronization with Google Maps you need to generate an API key as Google Maps doesn't need access to data from Google.

1. Create a new project on Google Cloud Platform and generate new API Key.
* Enable API Access in API Library for the Directions API and then add the API Key in the Google Settings in **Home > Integrations > Google Services > Google Settings**. ![](/files/api_key.gif)

<!-- page: erpnext/erpnext__gst-for-multiple-branches.md -->
---
title: "GST for multiple branches"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/gst-for-multiple-branches"
updated: "2026-07-31"
---

This will help you automate GST calculation if your company has different branches with separate GSTIN. 

  


This is an extension to the blog: [5 Steps to automate Indian GST in ERPNext](https://erpnext.com/blog/erpnext-features/5-steps-to-automate-indian-gst-in-erpnext)

  


1. **Update your Company’s branch-wise addresses**
2. **Configure State-wise GST Accounts** ***(Optional)***
3. **Item-wise GST setup**
4. **Classification of Inter-State and Intra-State Taxes**
5. **Configuring Invoice Templates**

  


### Step 1- Update your Company’s branch-wise billing addresses

  


The very first step is to update your company’s branch wise Address with appropriate GSTIN as it will differ *(if in different states)* frombranch to branch. 

  


![](https://erpnext.com/files/RU29P7U.png)

﻿

Now, make sure that your Customer's and Supplier's addresses have *GST State* and *Party GSTIN* configured properly.

  


﻿![](https://erpnext.com/files/LdjEDNd.png)

### 

### ﻿Step 2 - Configure State-wise GST Accounts ***(Optional)***

  


To configure, go to Chart of Accounts, create a state-wise set of GST accounts *(CGST, SGST & IGST)* as seen in the screenshot below.

﻿

﻿![](https://erpnext.com/files/BVg9U1f.png)

  


  


Add these newly created accounts in *GST Accounts* table from **GST Settings**, to include this in all GST Reports.

  


![](https://erpnext.com/files/JBtVopQ.png)

 

### Step 3 - Item-wise GST setup

  


a. Create **Item Tax Template** for different rates and add all the *GST Accounts* we have created in previous step.

b. Define the rates.

This helps system know which GST Accounts and Tax Rates to apply in the Invoices.

  


Your Item Tax Template should look like this: 

![](https://erpnext.com/files/MuMGvEa.png)

  


**The same way you can create different Item Tax Templates for different GST Rates.** 

  


After the creation of Item Tax Templates, you can start with assigning these templates to their respective Items from the Item Master.

  


![](https://erpnext.com/files/qhXeg1d.png)

 

### Step 4 - Classification of Inter-State and Intra-State Taxes

  


We are nearly there.

Create two **Tax Categories**, for each of our branches in different State. The **Source State** on each *Tax Category* will correspond to each of our company’s branches.

Each state will have two Tax Categories, one for Inter State and other for Out State transactions. 

  


**For ‘Out State’ Tax Categories, mark ‘Is Inter State’ checkbox as enabled.** 

  


*IN State Tax Category for Delhi:* 

![](https://erpnext.com/files/qJiylOa.png)

  


*﻿OUT State Tax Category for Delhi:* 

![](https://erpnext.com/files/vL7KwMs.png)

 

**Create for other States the same way as shown above.**

  


### Step 5 - Configuring our Invoice Templates

  


Finally, configure a set of two **Sales Taxes and Charges Templates**, and two **Purchase Taxes and Charges Templates, for each Tax Categories created.** 

**﻿**

Go to Sales Taxes and Charges Template, and define a set of two templates for each state (as seen in the screenshot below for Maharashtra)

  


*For IN State template, choose the IN State Tax Category and appropriate CGST & SGST account in* ***Account Head.*** 

  


![](https://erpnext.com/files/Jv8R3fX.png)

  


*For OUT State template, choose the OUT State Tax Category and appropriate IGST account in* ***Account Head.*** 

![](https://erpnext.com/files/lwQVAOr.png)

  


**Note: Enter our *Tax Accounts* in *Account Heads* and leave *rest as '0'* - since the tax rates will be fetched from the Item Master.**

  


Repeat the same process to configure **Purchase Taxes and Charges Template** and for other **States** as well. 

  


### We enjoy the fruits of our labour:

  


Refresh your account now as we have completed the setup now.

  


To verify if everything works as expected, create an Invoice or an Order:

1. Select a Customer/Supplier.
2. Check Company's Address and reselect it to whichever Branch you want to create the Invoice/Order from.
3. Selecting Customer/Supplier will fetch the right template, check if the Taxes and Charges are fetched properly.

  


### Example 1:

Here I have selected a **Customer from Maharashtra and Company's Address as Maharashtra** too, it should fetch the IN State template we created above.

  


![](https://erpnext.com/files/KOv2bSi.png)

  


It auto-fetched the following Taxes and Charges Template:

![](https://erpnext.com/files/Kz3m5ux.png)

  


### Example 2:

Here I have selected a **Customer from Maharashtra and Company's Address as Delhi**, it should fetch the OUT State template we created above.

  


![](https://erpnext.com/files/edIsIvn.png)

  


It auto-fetched the following Taxes and Charges Template:

![](https://erpnext.com/files/0DvILkB.png)
