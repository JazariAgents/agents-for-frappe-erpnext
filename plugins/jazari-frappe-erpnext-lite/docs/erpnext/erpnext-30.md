<!-- Frappe documentation: erpnext, part 30 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__import-accounting-masters.md -->
---
title: "Import Accounting Masters | ERPNext Documentation"
description: "Import ERPNext accounting masters in dependency order using Data Import, test representative records, correct failures, and validate links and defaults."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/import-accounting-masters"
updated: "2026-07-30"
---

Import masters before opening transactions and balances. Use ERPNext’s Data Import tool for records that do not have a specialized importer.

## Import order

1. Groups and parent records
2. Company-independent masters
3. Company-specific masters
4. Parties and addresses
5. Items and Warehouses
6. Banks, payments, taxes, and terms

For example, import Customer Groups and Territories before Customers, and Item Groups and UOMs before Items.

## Download the ERPNext template

1. Go to **Home &gt; Data Import and Settings &gt; Import Data**.
2. Create a new Data Import.
3. Select the DocType.
4. Choose **Insert New Records**.
5. Download the template.
6. Include only the columns needed for the approved mapping.

[Screenshot on the live page: Data Import configured for a migration master]

Do not build a template from memory. Current mandatory and dependent fields may differ from an older version.

## Fill the template

Keep column headers unchanged. Use exact ERPNext names for Link fields.

For tree masters, import parents first and set **Is Group** correctly. For child tables, use the importer’s row structure and test with one record before loading the full file.

## Test a small batch

Import two to five representative records:

- one simple record;
- one record with every optional link;
- one record with a child table;
- one foreign-currency party, if applicable;
- one disabled or historical record.

Open each imported record and test it in a draft transaction.

## Run the full import

1. Upload the approved file.
2. Start the import.
3. Download or copy the failure log.
4. Correct the source working file, not only the failed ERPNext row.
5. Re-import rejected records.
6. Record imported and rejected counts in the control workbook.

## Addresses and Contacts

Import Address and Contact only after parties exist. Add the Links child table so each record is connected to its Customer, Supplier, or other party.

For primary records, set the appropriate billing, shipping, or primary flags and verify the party form shows the correct defaults.

## Items and accounting defaults

For Items, verify:

- Maintain Stock;
- stock UOM;
- Item Group;
- default Warehouse;
- income and expense accounts;
- Cost Center;
- tax template;
- valuation method where relevant.

A successful import does not prove that accounting defaults are correct.

## Correcting master imports

Use **Update Existing Records** for approved corrections. Do not create a second record because the first import had a spelling error. If a duplicate has already been used in a transaction, follow the supported rename or merge process.

## Validation checklist

- source count equals imported plus rejected count;
- no unexpected duplicates;
- parent trees are correct;
- party and Item defaults are correct;
- addresses and contacts are linked;
- disabled records remain disabled;
- draft sales, purchase, payment, and stock transactions fetch expected values.

## Related topics

- [Data Import](https://docs.frappe.io/erpnext/data-import)
- [Accounting Masters for Migration](https://docs.frappe.io/erpnext/accounting-masters)
- [Prepare and Map Legacy Data](https://docs.frappe.io/erpnext/prepare-and-map-legacy-data)
- [Import Chart of Accounts](https://docs.frappe.io/erpnext/import-chart-of-accounts)

<!-- page: erpnext/erpnext__import-advances-unallocated-payments-bank-stock-and-asset-balances.md -->
---
title: "Import Special Opening Balances | ERPNext Documentation"
description: "Import ERPNext opening advances, unallocated payments, bank and cash, stock, fixed assets, deferred amounts, and foreign-currency balances safely."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/import-advances-unallocated-payments-bank-stock-and-asset-balances"
updated: "2026-07-31"
---

These balances need specialized opening documents. Import them before the residual opening Journal Entry so their control-account balances are not duplicated.

## Customer and Supplier advances

Prepare one row per advance with:

- party;
- receipt or payment date;
- currency and exchange rate;
- amount;
- bank or cash account;
- party account;
- legacy reference;
- order reference, if the allocation must be retained.

Create opening Payment Entries or use the approved opening-journal method for your version and process. Mark entries as opening where supported. Leave genuinely unallocated amounts unallocated so they can be reconciled against future invoices.

After posting, compare party-wise advances with the source schedule and check the General Ledger.

## Unallocated receipts and payments

Do not convert unallocated money into an invoice simply to make ageing agree. Import the payment against the correct party and leave the unallocated amount available.

Use the Payment Reconciliation Tool after the related opening invoices exist if legacy allocations must be recreated.

## Bank and cash balances

Create the Bank, Bank Account, ledger account, and Mode of Payment before import.

The General Ledger bank balance at cutover should match the reconciled legacy book balance, not necessarily the statement closing balance. Carry unreconciled deposits, withdrawals, checks, and fees in the reconciliation schedule.

Import each cash account separately and obtain a signed cash count where applicable.

## Stock quantities and values

Use Stock Reconciliation with an opening purpose:

1. Select the cutover date and Company.
2. Add each Item and Warehouse.
3. Enter opening quantity.
4. Enter valuation rate.
5. Verify the total stock value.
6. Submit after quantity and value totals match the approved stock report.

[Screenshot on the live page: Stock Reconciliation configured for opening stock]

Do not import stock value again through the opening Journal Entry when perpetual inventory creates the accounting balance.

Test serial numbers, batches, negative stock, alternative UOMs, and multiple Warehouses before the final import.

## Fixed assets

Import each active asset with:

- Asset Category;
- Company;
- gross purchase amount;
- purchase and available-for-use dates;
- accumulated depreciation;
- opening number of booked depreciations;
- remaining useful life or depreciation periods;
- location and custodian;
- finance book;
- asset and accumulated depreciation accounts.

Verify:

`Gross cost - accumulated depreciation = opening net book value`

After import, inspect the depreciation schedule. The next depreciation date and remaining amount must agree with the source asset register.

## Loans, deposits, accruals, and prepayments

Use the supported operational record when future schedules or allocations are required. Otherwise include the approved balance in the opening Journal Entry with the correct party, Cost Center, Project, and dimensions.

For deferred revenue and expense, decide whether to recreate the remaining schedule or bring only the cutover balance. Test automatic future recognition.

## Foreign-currency balances

Retain foreign amount and company-currency amount. Use the approved cutover rate. Reconcile both values and keep exchange differences separate from operating balances.

## Reconciliation


| Balance                           | ERPNext report                          |
| --------------------------------- | --------------------------------------- |
| Advances and unallocated payments | Party ledger and Payment Reconciliation |
| Bank                              | Bank Reconciliation and General Ledger  |
| Cash                              | General Ledger and cash count           |
| Stock                             | Stock Balance and Stock Ledger          |
| Assets                            | Fixed Asset Register and General Ledger |


## Related topics

- [Payment Entry](https://docs.frappe.io/erpnext/payment-entry)
- [Bank Reconciliation](https://docs.frappe.io/erpnext/bank-reconciliation)
- [Stock Reconciliation](https://docs.frappe.io/erpnext/stock-reconciliation)
- [Asset](https://docs.frappe.io/erpnext/asset)
- [Opening Balance in Accounts](https://docs.frappe.io/erpnext/opening-balance)

<!-- page: erpnext/erpnext__import-e-invoice.md -->
---
title: "Importing e-Invoice from Supplier\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/import-e-invoice"
updated: "2026-02-26"
---


> Introduced in Version 13

As of January 1, 2019, electronic Invoicing is mandatory for domestic businesses operating with domestic B2B and B2C transactions in Italy. ERPNext has a feature to import supplier invoices from XML files provided by suppliers to the government.

ERPNext has a feature to import supplier invoices from XML files provided by suppliers to the government. Using this you can import Supplier e-invoices into ERPNext. The supplier details like supplier names, addresses and purchase invoices will get created automatically in the system from the XML files.

## 1. Prerequisites
- Default Stock UOM should be specified in the Stock Settings Doctype.
- Enable Check Supplier Invoice Uniqueness in the Accounts Settings Doctype.
- Create a Zip file with all your supplier invoice XML files.

### 2. How to use Import Supplier Invoice

1. Navigate to Import Supplier Invoice doctype from the global search bar and enter the Invoice Series, Company, Supplier Group, Tax Account, Item Code and Default Buying Price List.
 [Screenshot on the live page]

 - Invoice Series - The series with which the new Purchase Invoices will be created.
 - Company - The company for which the new Purchase Invoices will be created.
 - Supplier Group - The supplier group under which the new suppliers will be created.
 - Tax Account - The account under which the taxes would be entered for the Purchase Invoices created.
 - Item Code - The item code which would be used for Purchase Invoice creation.
 - Default Buying Price list - The default buying price list to be used for the Purchase Invoice.

2. After entering the above details click on Save.

3. Attach the zip file with XML invoices.

4. Click on Import invoices and the Purchase Invoices will be created. Suppliers would be created if they do not exist in the system already.
 [Screenshot on the live page]

5. If the file import completes successfully you would see a status of File Import Completed. If there are any errors you can view them from the Error Log.
 [Screenshot on the live page]

<!-- page: erpnext/erpnext__include-document-link-in-notification-email.md -->
---
title: "Include Document Link in Notification Email"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/include-document-link-in-notification-email"
updated: "2026-03-04"
---

While sending an email notification in ERPNext, many a times, we need the document ID to be a part of the email message as a link. For example, if we have set a reminder (notification) for every new Material Request, then we would want the link of the new Material Request to be also sent in email to us. To set that up, following the below steps:  
1) Go to Notification list, click on New.  
2) Create a new Notification for any DocType. In this case, we have taken an example of sending an Email Notification on creation of every new Material Request as shown below.  
[Screenshot on the live page]  
  
3) To send the document ID of the associated record as a link, copy the below snippet in the email message: 
    
    `<a href="{{frappe.utils.get_url_to_form(doc.doctype, doc.name)}}">{{doc.name}}</a>`  
    [Screenshot on the live page]  
4) Now on creation of a new Material Request, following email will be received because of the above set Notification.  
[Screenshot on the live page]  
On clicking the link, you will be taken to the new Material Request.  
[Screenshot on the live page]   

<!-- page: erpnext/erpnext__incoterm-and-named-place.md -->
---
title: "Record Incoterms and Named Places | ERPNext Documentation"
description: "Record an Incoterm and its named place on ERPNext sales and purchase transactions so delivery responsibilities are captured consistently."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/incoterm-and-named-place"
updated: "2026-07-25"
---

Use **Incoterm** and **Named Place** to record the agreed trade term and location on sales and purchase transactions. Together they provide commercial context about delivery responsibilities, costs, and risk transfer.

ERPNext records the agreement. It does not interpret the legal obligations, calculate every freight or insurance charge, or replace the complete contract.

## Before you begin

Confirm:

- The Incoterm edition and term agreed with the counterparty.
- The exact named port, terminal, warehouse, city, or other place.
- Currency, freight, insurance, taxes, and delivery terms.
- Whether the term is appropriate for the transport mode.

Seek qualified trade or legal advice when choosing the term. A short code without a named place is incomplete for many practical uses.

## Add an Incoterm to a transaction

The fields are available on supported documents such as a [Quotation](/erpnext/quotation), [Sales Order](/erpnext/sales-order), [Delivery Note](/erpnext/delivery-note), [Sales Invoice](/erpnext/sales-invoice), [Purchase Order](/erpnext/purchase-order), and [Purchase Invoice](/erpnext/purchase-invoice).

1. Open or create the transaction.
2. Find the shipping or terms section.
3. Select the agreed **Incoterm**.
4. Enter the complete **Named Place**.
5. Confirm that freight, taxes, shipping address, and Terms and Conditions are consistent.
6. Save.

[Screenshot on the live page: A Sales Order with Incoterm and Named Place highlighted.]

Example: **CIP, Seattle-Tacoma International Airport, Seattle, WA, USA, Incoterms 2020**.

Use the location detail your contract requires. Avoid a vague value such as only “USA” or “Port”.

## Understand the two fields


| Field       | What to record                                 |
| ----------- | ---------------------------------------------- |
| Incoterm    | Standard trade-term code agreed by the parties |
| Named Place | Exact agreed location associated with the term |


The meaning of the named place depends on the selected term. For one term it may identify the place of delivery; for another it may identify a destination to which specified costs are paid. Do not infer all obligations from the location alone.

## Keep the sales cycle consistent

When creating downstream documents, verify that the Incoterm and Named Place remain aligned with the latest agreement.

If the agreement changes after a Sales Order is submitted:

- Use the supported amendment or after-submit update workflow.
- Retain approval evidence.
- Update downstream documents that have not yet been submitted.
- Use a revised commercial document when required.

Do not overwrite a completed historical agreement merely to show the latest terms.

## Freight, insurance, and accounting

Incoterm fields do not automatically create every related charge or accounting entry. Configure freight through shipping charges, taxes, landed costs, or supplier invoices according to the transaction and accounting policy.

For stock purchases, [Landed Cost Voucher](/erpnext/landed-cost-voucher) may be relevant when additional costs need to be included in inventory valuation.

## Terms and printed documents

Use [Terms and Conditions](/erpnext/terms-and-conditions) to state the complete commercial wording, Incoterm edition, responsibilities, exclusions, and documentary requirements.

Check the Print Format to ensure Incoterm and Named Place appear on the document sent to the Customer or Supplier.

## Troubleshooting


| Problem                               | What to check                                               |
| ------------------------------------- | ----------------------------------------------------------- |
| Named Place is hidden                 | Select the Incoterm first                                   |
| Downstream document has old terms     | Review mapped values and whether the source was amended     |
| Freight is not calculated             | Configure charges separately; Incoterm is descriptive       |
| The printed document omits the fields | Update the Print Format                                     |
| Users select inconsistent terms       | Add approval, training, or a Workflow for commercial review |


## Frequently asked questions

### Does ERPNext choose the correct Incoterm?

No. Users must select the term agreed by the parties.

### Is the Named Place always the delivery destination?

No. Its role depends on the selected Incoterm.

### Do Incoterm fields calculate freight or insurance?

Not by themselves. Configure the relevant charges and accounting separately.

### Should the Incoterm edition be recorded?

Yes. Include the agreed edition in Terms and Conditions or another controlled field or print format.

## Related topics

- [Terms and Conditions](/erpnext/terms-and-conditions)
- [Sales Order](/erpnext/sales-order)
- [Purchase Order](/erpnext/purchase-order)
- [Shipping Rule](/erpnext/shipping-rule)
- [Landed Cost Voucher](/erpnext/landed-cost-voucher)

<!-- page: erpnext/erpnext__india-compliance-app.md -->
---
title: "India Compliance"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/india-compliance-app"
updated: "2026-07-02"
---

Any ERPNext user who needs India-specific statutory features can install the India Compliance app to unlock the capabilities inside ERPNext. After installation and setup, the app adds the workflows, fields, reports, and validations required for operating ERPNext in India.

Official documentation: [https://docs.indiacompliance.app/docs/getting-started/introduction](https://docs.indiacompliance.app/docs/getting-started/introduction)

## What the India Compliance app provides

The India Compliance app extends ERPNext for Indian tax and regulatory needs. It is especially useful for companies that need to manage GST, e-Invoicing, e-Way Bills, TDS, TCS, and India-specific reporting from within ERPNext.

Broadly, the app helps with:

- GST setup and GST-aware transactions
- GSTIN and party tax details
- HSN/SAC handling for items and services
- GST tax templates and tax treatment
- GST returns and statutory reports
- e-Invoice generation and management
- e-Way Bill generation and management
- TDS and TCS compliance
- India-specific validations on transactions
- Regional fields and workflows needed by Indian businesses

The exact features available may depend on the installed app version, ERPNext version, and the configuration enabled for the company.

## Why it is separate from ERPNext

ERPNext serves users across many countries. Keeping India-specific compliance in a separate app makes the core product cleaner while still allowing Indian companies to get the workflows they need.

This means a company that does not need Indian compliance can continue using standard ERPNext, while an Indian company can install the India Compliance app and enable the additional features required for local operations.

## Typical usage flow

```
Install ERPNext
      |
      v
Install India Compliance app
      |
      v
Configure company and GST settings
      |
      v
Set up masters such as GSTIN, HSN/SAC, tax templates
      |
      v
Create transactions in ERPNext
      |
      v
Generate India-specific compliance outputs
```

## Common areas affected

### Masters

The app can add or use India-specific details in masters such as Company, Customer, Supplier, Address, Item, and tax templates. These details help ERPNext understand how GST and other rules should apply during transactions.

### Transactions

Sales Invoices, Purchase Invoices, Delivery Notes, and other documents can include India-specific tax information. The app helps validate and process these transactions according to Indian compliance needs.

### Reporting

The app provides reports and outputs needed for Indian statutory compliance, including GST-related reporting and other tax summaries.

### Electronic compliance

For businesses that need e-Invoicing or e-Way Bill workflows, the India Compliance app provides the required integration and document handling experience inside ERPNext.

## When should you install it?

Install the India Compliance app if your ERPNext site is used by an Indian company or by a company that must comply with Indian tax and invoicing rules.

You may not need it if your company does not operate in India and does not need Indian statutory reporting.

## Learn more

Read the official India Compliance documentation here:

[https://docs.indiacompliance.app/docs/getting-started/introduction](https://docs.indiacompliance.app/docs/getting-started/introduction)

<!-- page: erpnext/erpnext__installation-note.md -->
---
title: "Installation Note\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/installation-note"
updated: "2026-02-27"
---


**An Installation Note can be created when a product/item is being installed or set up at the Customer's place.**

For example, if you sell an Air Conditioner, a service person generally accompanies the delivery to install the Air Conditioner at the Customer’s place. The service person can create an “Installation Note”, to track the date and details of the installation.

To access the Installation Note list, go to:
> Home > Stock > Serial No and Batch > Installation Note

## 1. How to create an Installation Note
An Installation Note is usually created from a Delivery Note. You can also create it manually and click on the 'From Delivery Note' button to fetch details from a selected Delivery Note.

1. Go to the Installation Note list, click on New.
1. The Customer, Item, and quantity will be fetched from the Delivery Note.
1. The date and time are set to when the note is created.
1. Save and submit.

 [Screenshot on the live page: Installation Note]

Any additional remarks about the installation can be added. If the Item is serialized, the serial numbers can be added in Items table.

### 2. Related Topics
1. [Delivery Note](/erpnext/delivery-note)
1. [Delivery Trip](/erpnext/delivery-trip)

<!-- page: erpnext/erpnext__installing_redisearch_to_enable_super_fast_e_commerce_search.md -->
---
title: "Installing RediSearch to enable fast E-commerce Search"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/installing_redisearch_to_enable_super_fast_e_commerce_search"
updated: "2026-03-02"
---


> **Experimental**
> 
> 

The E-Commerce module of ERPNext optionally uses RediSearch to enable search functionality which is configurable via **E Commerce Settings**.

Once installed and configured, RediSearch will be used to charge the search functionality of the E-Commerce website. This includes features like fuzzy-word searching, autocomplete, results ranking and customizable field indexing.

### Pre-requisites

1. Frappe Framework + ERPNext Setup
2. Redis 6+

### Installation Instructions


```
$ git clone --recursive https://github.com/RediSearch/RediSearch.git
$ cd RediSearch
$ sudo make setup # Remove `sudo` on macOS
$ make build
  

```

> Please Note: the latest version of RediSearch requires Redis 7.1+, while the stable redis as on 01-Aug-2023 available in snap repos is 7.0. Therefore, Redis need to be compiled from source for Redissearch to be compatible with Redis.
> 
> Also note ERPNext requires Redis 6+, therefore using Redis 7.1+ might break thinks. Use Redis 7.1+ with caution.
> 
> 

On successful completion of the above instructions, a `redisearch.so` binary file will be generated in the `RediSearch/build` directory.

Move this binary to the `/etc` directory and restart your Frappe Server:


```
sudo mv build/redisearch.so /etc/
  

```
Now, open the `redis_cache.conf` file located in the `config` directory (inside the bench directory). Add the following line before the `save ""` line and then restart bench server:


```
loadmodule /etc/redisearch.so
  

```
This will load the redisearch module at startup. You can check if the module was loaded successfully by running the following command in the `redis-cli -p 13000` (assuming port as 13000 default port for redis in frappe config):


```
> MODULE LIST
  

```
and `search` should be one of the modules.

You can also load the module on a running redis instance by running the following command in the `redis-cli`:


```
> MODULE LOAD /etc/redisearch.so
  

```

> We placed the `redisearch.so` module in the `/etc` directory, but it can be placed anywhere in the file system. We have used this directory because in the future the `loadmodule` line will be populated in the config file automatically and it will assume the binary is in the `/etc` directory.
> 
> 


> More detailed instructions can be found [here](https://github.com/RediSearch/redisearch-getting-started/blob/master/docs/002-install-redisearch.md).
> 
> 

<!-- page: erpnext/erpnext__integrating-erpnext-with-other-applications.md -->
---
title: "Integrating ERPNext with other Applications"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/integrating-erpnext-with-other-applications"
updated: "2026-07-04"
---

ERPNext is designed to be integrated with other applications. Because ERPNext is built on Frappe Framework, business records are exposed through a consistent REST API. This makes it straightforward to connect ERPNext with external systems such as CRM platforms, logistics providers, order management systems, recommerce platforms, Google services, banking systems, payment gateways, and internal business applications.

## Why ERPNext Is Easy To Integrate

Most ERPNext business objects are DocTypes. Customers, Items, Sales Orders, Purchase Orders, Sales Invoices, Delivery Notes, Payment Entries, Stock Entries, Projects, and many other records follow the same document model. Frappe automatically provides REST API access for DocTypes, so integrations can read, create, update, and delete records using predictable endpoints.

This means a third-party application does not need a separate custom API for every ERPNext module. Once the external system knows the DocType and field names, it can exchange data with ERPNext using standard HTTPS requests and JSON payloads.

Custom fields added in ERPNext become part of the DocType metadata and are available to integrations immediately. For example, if a business adds a custom field such as `marketplace_order_id` on Sales Order or `courier_tracking_id` on Delivery Note, third-party applications can send and receive those values through the same REST API used for standard fields.

This is especially useful when ERPNext is connected to external systems that need their own identifiers, statuses, references, or operational data. Custom fields let teams extend ERPNext without breaking the standard data model.

## How REST APIs Work

Frappe provides REST API endpoints for DocTypes. A third-party application can authenticate with an API key and API secret, then call endpoints to list documents, fetch a specific document, create a new record, update an existing record, or delete a record where permissions allow it.

Common integration patterns include:

- **Read from ERPNext:** Fetch customers, items, prices, stock levels, invoices, or payment status.
- **Write to ERPNext:** Create leads, customers, sales orders, purchase orders, delivery notes, payment entries, or support tickets.
- **Update ERPNext:** Send shipping updates, reconciliation references, bank transaction IDs, marketplace order IDs, or fulfillment statuses.
- **React to ERPNext events:** Use webhooks to notify another application when a document is created, updated, submitted, or cancelled.

## Examples Of Integrations

- **CRM:** Sync leads, opportunities, customers, quotations, and follow-up status between ERPNext and a sales CRM.
- **Logistics:** Send delivery notes or shipment requests to a courier platform and receive tracking numbers back into ERPNext.
- **Order Management:** Push orders from an order management system into ERPNext as Sales Orders, then send fulfillment and invoice status back.
- **Recommerce Platforms:** Sync product catalog, customer orders, stock availability, returns, refurbishment status, and payouts.
- **Google Services:** Connect ERPNext with Google Workspace, Google Calendar, Google Sheets, or reporting workflows.
- **Banks And Payment Systems:** Import bank transactions, update payment references, reconcile payments, or connect payment collection workflows.

## Typical Integration Flow

1. Identify the ERPNext DocTypes involved, such as Customer, Item, Sales Order, Delivery Note, Sales Invoice, Payment Entry, or a custom DocType.
2. Map the fields between ERPNext and the external application, including any custom fields required by the business process.
3. Create an integration user in ERPNext with only the roles and permissions required for the integration.
4. Generate API credentials for that user and authenticate API calls securely.
5. Use REST API endpoints to create, fetch, update, or delete records as needed.
6. Use webhooks or background jobs for event-driven sync, retries, and asynchronous processing.

## Good Practices

- Use a dedicated integration user instead of an administrator account.
- Apply role-based permissions so the integration can access only the records it needs.
- Store external IDs in custom fields to make reconciliation and troubleshooting easier.
- Design integrations to be idempotent, so retrying a request does not create duplicate records.
- Use webhooks or queues for high-volume workflows instead of making everything synchronous.
- Log request IDs, external references, and error messages so failures can be traced quickly.

## Related Topics

- [Frappe REST API](https://docs.frappe.io/framework/user/en/api/rest)
- [Token Based Authentication](https://docs.frappe.io/framework/user/en/guides/integration/token_based_authentication)
- [Webhooks](https://docs.frappe.io/framework/user/en/guides/integration/webhooks)
- [Insert A Document Via API](https://docs.frappe.io/framework/user/en/guides/app-development/insert-a-document-via-api)
- [Custom Field](https://docs.frappe.io/erpnext/custom-field)

<!-- page: erpnext/erpnext__inter-company-invoices.md -->
---
title: "Inter Company Invoices | ERPNext Documentation"
description: "Create linked Sales and Purchase Invoices between companies in ERPNext and verify parties, accounts, taxes, stock, and balances."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/inter-company-invoices"
updated: "2026-07-23"
---

Inter Company Invoices in ERPNext create the matching receivable and payable transactions when one Company sells goods or services to another Company in the same ERPNext site. A submitted Sales Invoice can create a linked Purchase Invoice for the buying Company, reducing duplicate entry while preserving separate ledgers.

## Before you begin

- Create both Companies and their charts of accounts.
- Create a Customer that represents the buying Company.
- Create a Supplier that represents the selling Company.
- In the Customer and Supplier records, set the corresponding **Represents Company** value.
- Make sure both Companies can transact in the required Currency.
- Create matching Items, UOMs, taxes, warehouses, and accounts for both Companies.

The Customer and Supplier links are essential. They tell ERPNext which legal entity is on the other side of the transaction.

## Configure the inter-company parties

For the buying Company, create or open the Customer used by the selling Company and set **Represents Company** to the buying Company.

[Screenshot on the live page: The internal Customer with Is Internal Customer enabled and Nova Industries selected as Represents Company.]

For the selling Company, create or open the Supplier used by the buying Company and set **Represents Company** to the selling Company.

[Screenshot on the live page: The internal Supplier with Is Internal Supplier enabled and Nova Electronics Trading selected as Represents Company.]

Use distinct party records for each legal entity, even when the Companies share ownership. Confirm the tax identifiers, addresses, payment terms, and receivable or payable accounts that apply to each entity.

## Create a Purchase Invoice from a Sales Invoice

1. Create and submit a [Sales Invoice](/erpnext/sales-invoice) in the selling Company for the Customer that represents the buying Company.
2. Confirm the items, quantities, rates, taxes, Company, and posting date.
3. From the submitted Sales Invoice, select **Create > Inter Company Purchase Invoice**.
4. Review the mapped document in the buying Company.
5. Select the correct expense or asset accounts, warehouses, taxes, and cost centers.
6. Save and submit the Purchase Invoice.

[Screenshot on the live page: The Sales Invoice showing Nova Electronics Trading as Company and Nova Industries Intercompany as Customer.]

[Screenshot on the live page: The highlighted Inter Company Purchase Invoice action in the submitted Sales Invoice Create menu.]

The Purchase Invoice is a separate accounting transaction. ERPNext maps source values, but the user must verify the accounts and taxes appropriate to the buying Company.

## Create a Sales Invoice from a Purchase Invoice

The flow can also begin with a submitted Purchase Invoice in the buying Company. Use **Create > Inter Company Sales Invoice** to create the corresponding Sales Invoice in the selling Company, then review and submit it.

Choose one direction for each transaction. Do not create both counterparts independently, or the same trade may be recorded twice.

## Important fields and what they mean


| Field                   | What it means                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------- |
| Company                 | The legal entity whose books receive the transaction.                                   |
| Customer                | The inter-company Customer used on the Sales Invoice.                                   |
| Supplier                | The inter-company Supplier used on the Purchase Invoice.                                |
| Represents Company      | Links a Customer or Supplier to the other Company in the same site.                     |
| Inter Company Reference | Identifies the linked source transaction where available.                               |
| Currency                | The transaction currency. Conversion rates apply when it differs from Company currency. |
| Debit To                | The receivable account used by the selling Company.                                     |
| Credit To               | The payable account used by the buying Company.                                         |
| Income Account          | The revenue account for the selling Company.                                            |
| Expense Account         | The expense or asset account for the buying Company.                                    |
| Cost Center             | The organizational unit to which income or expense is assigned.                         |


## Items, warehouses, and taxes

Item Codes should exist and be usable in both Companies. Accounts and warehouses remain Company-specific, so review every mapped row. Open a child-table row with the pencil icon when you need to verify hidden item fields.

Tax treatment can differ between the selling and buying entities. Do not assume the tax rows on the source document are correct for the target Company. Check tax templates, accounts, rates, addresses, and regional compliance before submission.

For stock items, the invoice pair does not by itself replace the required stock movement. Use the approved Delivery Note, Purchase Receipt, or inter-company stock process so physical inventory agrees with accounting.

## Cancel or amend linked invoices

The two invoices remain separate submitted documents. If one must be cancelled or amended, review the effect on its counterpart and any linked payments, returns, or stock transactions. Follow your accounting period and audit controls. Do not leave one Company with a valid invoice while the corresponding document in the other Company is incorrect.

## Reconcile inter-company balances

Run receivable, payable, and general ledger reports for both Companies. The balances should agree after accounting for timing differences, currency conversion, taxes, credit notes, and payments. Use a consistent reference or naming practice so finance users can match the two sides quickly.

## Frequently asked questions

### Why is the inter-company create option missing?

Check that the source invoice is submitted, the party has **Represents Company** set, the represented Company is different from the source Company, and a counterpart has not already been created.

### Are both invoices submitted automatically?

No. Review and submit the mapped target invoice separately.

### Can the Companies use different currencies?

Yes, when the required currencies and conversion rates are configured. Review exchange rates and Company-currency totals on both documents.

### Does this consolidate the Companies?

No. It records transactions in separate Company ledgers. Consolidated reporting and elimination entries are separate accounting activities.

### Can I create inter-company credit notes?

Use the applicable return or credit-note process for both Companies and link the transactions according to your controls.

## Related topics

- [Sales Invoice](/erpnext/sales-invoice)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Company](/erpnext/company)
- [Customer](/erpnext/customer)
- [Supplier](/erpnext/supplier)
- [Inter Company Journal Entry](/erpnext/inter-company-journal-entry)
- [Drop Ship Between Subsidiary Companies](/erpnext/drop-ship-between-subsidiary-companies)
