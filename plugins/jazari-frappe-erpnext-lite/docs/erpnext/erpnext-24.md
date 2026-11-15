<!-- Frappe documentation: erpnext, part 24 of 69. Index: docs/INDEX.md -->

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

[Screenshot on the live page: The Item form configured for a service by disabling Maintain Stock.]

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

[Screenshot on the live page: Sendcloud API]  


### 1.2 LetMeShip

1. Register on [LetMeShip](https://www.letmeship.com/en/).
2. Follow [these steps](https://www.letmeship.com/en-de/shipping-api/) to generate an **API ID** and **API Password**.
3. Search for **LetMeShip** in the awesomebar.
4. Add the **API ID** and **API Password** to the LetMeShip DocType. Check the **Enabled** field.
5. Save.

[Screenshot on the live page: LetMeShip API]  


2. Features
-----------

### 2.1 Comparison of Shipping Rates

Once a [Shipment](/erpnext/shipment) is submitted, if the app is installed, the button **Fetch Shipping Rates** will appear. On clicking, you will get a list of services along with their service providers and rates.

[Screenshot on the live page: Fetch Rates]  


You can also add frequently used services to your **Preferred Services** using **Parcel Service Type**:

1. Assuming the highlighted service is our frequently used service, let us add it to our **Preferred Services**

[Screenshot on the live page: Highlight Service]
2. Go to **Parcel Service Type** > **New**. Create a new **Parcel Service**. In our case, it is 'TNT'.
3. Add a **Parcel Service Type**. In our case, it will be 'Economy'.
4. Add 'Economy' to the **Parcel Service Type Alias** table as well.
5. Add a description (optional).
6. Enable the **Show in Preferred Services List** field. Save.

Now when you click on the **Fetch Shipping Rates** button, you will always see the previously highlighted service under **Preferred Services**.

[Screenshot on the live page: Preferred Service]  


### 2.2 Creation of Shipment

After comparing rates, you can proceed with any one of the services by clicking **Select** against the appropriate service row. On clicking, a Shipment is automatically created on your service provider's platform.

You will notice that the **Shipment Information** section is updated automatically, based on the Shipment created.

[Screenshot on the live page: Shipment Creation]  


You can also search for your transaction on your service provider's platform using the **Shipment ID** field.

### 2.3 Printing Labels

To avail the **Print Shipping Label** button, the **Shipment ID** must be generated in the current record.

[Screenshot on the live page: Print Label Button]  


You can then click on it and generate your shipping label.

[Screenshot on the live page: Dummy Shipping Label]  


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



[Screenshot on the live page: Allow Stale Exchange Rates in Accounts Settings]

The current behavior is best understood as a rate-selection policy:


| Setting                             | Lookup behavior                                                                                                            |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Allow Stale Exchange Rates enabled  | The latest matching stored rate may be used without an age limit. This supports rates that remain valid until replaced.    |
| Allow Stale Exchange Rates disabled | ERPNext limits stored-rate age using Stale Days, then tries the configured provider when no eligible manual record exists. |


The existing documentation associates this setting with whether the Exchange Rate field is editable. Because field behavior has changed across releases and can vary by document, verify the Draft page after changing the setting instead of relying only on the word “stale.” In current develop, users can often override a fetched rate on a Draft when permissions and document logic allow it.

## If you need a controlled fixed rate

Create a dated Currency Exchange record with the approved value and the correct buying or selling flag. Then decide whether the record may remain valid until another is entered.



[Screenshot on the live page: Approved EUR to USD rate]

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

[Screenshot on the live page: Exchange Rate on a Draft EUR Sales Invoice]

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
