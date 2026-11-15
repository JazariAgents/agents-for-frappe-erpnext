<!-- Frappe documentation: erpnext, part 31 of 69. Index: docs/INDEX.md -->

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

![A Sales Order with Incoterm and Named Place highlighted.](https://novacompanies.m.frappe.cloud/files/incoterm-sales-order.png)

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

 ![Installation Note](/files/installation-note.png)

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

![The internal Customer with Is Internal Customer enabled and Nova Industries selected as Represents Company.](/files/internal-customer-company-link.webp)

For the selling Company, create or open the Supplier used by the buying Company and set **Represents Company** to the selling Company.

![The internal Supplier with Is Internal Supplier enabled and Nova Electronics Trading selected as Represents Company.](/files/internal-supplier-company-link.webp)

Use distinct party records for each legal entity, even when the Companies share ownership. Confirm the tax identifiers, addresses, payment terms, and receivable or payable accounts that apply to each entity.

## Create a Purchase Invoice from a Sales Invoice

1. Create and submit a [Sales Invoice](/erpnext/sales-invoice) in the selling Company for the Customer that represents the buying Company.
2. Confirm the items, quantities, rates, taxes, Company, and posting date.
3. From the submitted Sales Invoice, select **Create > Inter Company Purchase Invoice**.
4. Review the mapped document in the buying Company.
5. Select the correct expense or asset accounts, warehouses, taxes, and cost centers.
6. Save and submit the Purchase Invoice.

![The Sales Invoice showing Nova Electronics Trading as Company and Nova Industries Intercompany as Customer.](/files/inter-company-sales-invoice.webp)

![The highlighted Inter Company Purchase Invoice action in the submitted Sales Invoice Create menu.](/files/create-purchase-invoice-action.webp)

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

<!-- page: erpnext/erpnext__inter-company-journal-entry.md -->
---
title: "Inter Company Journal Entry | ERPNext Documentation"
description: "Create linked Inter Company Journal Entries in ERPNext, record both companies' debit and credit treatment, and verify each company's separate ledger posting."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/inter-company-journal-entry"
updated: "2026-08-14"
---

Nova Industries pays a shared software bill on behalf of Nova Electronics Distribution, another company in the same group. One bank account paid the money, but each legal entity needs its own balanced books and a clear inter-company balance showing who owes whom.



An Inter Company Journal Entry records the two sides as separate linked Journal Entries. The first entry posts only in the first Company; ERPNext then helps you create the corresponding entry for the second Company with opposite totals.



Use this workflow for shared costs, fund transfers, and adjustments between related entities when the event does not originate from an inter-company invoice. The event is complete across the group only after both linked entries are reviewed and submitted.



DIAGRAM\_PLACEHOLDER

## Before you begin

Confirm that:

1. At least two non-group companies exist in ERPNext.
2. Each company has its own [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts), default currency, fiscal year, and Cost Center.
3. The required due-from, due-to, bank, income, and expense accounts exist in the appropriate company.
4. You know the debit and credit treatment required in both companies.
5. Users creating the pair have permission to access both companies and their accounts.
6. If the companies use different currencies, [multi-currency accounting](https://docs.frappe.io/erpnext/multi-currency-accounting) and exchange rates are configured.

For routine trade between group companies, consider [Inter Company Invoices](https://docs.frappe.io/erpnext/inter-company-invoices). Use Inter Company Journal Entry for a deliberate accounting adjustment where invoices are not the appropriate business documents.

## Understand the example

Nova Electronics Trading pays a $1,200 trade show expense on behalf of Nova Electronics Distribution. The first company records the cash outflow and a receivable from the related company. The second company records the expense and an amount payable to the first company.


| Company                       | Account                                | Debit  | Credit | Meaning                                         |
| ----------------------------- | -------------------------------------- | ------: | ------: | ----------------------------------------------- |
| Nova Electronics Trading      | Due from Nova Electronics Distribution | $1,200 |        | The related company owes this amount.           |
| Nova Electronics Trading      | Nova Operating Bank                    |        | $1,200 | Cash leaves the paying company.                 |
| Nova Electronics Distribution | Trade Show Expenses                    | $1,200 |        | The benefiting company recognizes the expense.  |
| Nova Electronics Distribution | Due to Nova Electronics Trading        |        | $1,200 | The benefiting company owes the paying company. |


Each company’s entry balances independently. The linked second entry also reverses the first entry’s total sides: the second entry’s total credit must equal the first entry’s total debit, and its total debit must equal the first entry’s total credit when both companies use the same currency.

## Create the first company’s entry

From the Journal Entry list, select **Add Journal Entry**.

Set **Entry Type** to **Inter Company Journal Entry** and select the company that records the first side. In this example, select **Nova Electronics Trading**.



![The first submitted Inter Company Journal Entry with Company and Entry Type highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-inter-company-journal-entry-inter-company-source-entry.png)

In **Accounting Entries**, add the accounts and amounts for that company. Add a Cost Center or another [Accounting Dimension](https://docs.frappe.io/erpnext/accounting-dimensions) when required.

For the example:

1. Debit **Due from Nova Electronics Distribution** by $1,200.
2. Credit **Nova Operating Bank** by $1,200.

Select the pencil icon to open a child row when you need to enter a Cost Center, Project, party, currency, reference, or another row-level field.



![The first company's account rows with the row edit pencil highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-inter-company-journal-entry-inter-company-source-accounts.png)

Confirm that **Total Debit** equals **Total Credit**, add a clear remark, then save and submit the first Journal Entry. Submission posts the first company’s [General Ledger](https://docs.frappe.io/erpnext/general-ledger) entries. It does not yet post the other company’s side.

## Create the linked entry for the second company

Open the submitted first entry. Select **Make**, then select **Create Inter Company Journal Entry**.



![Create Inter Company Journal Entry highlighted in the Make menu](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-inter-company-journal-entry-inter-company-create-action.png)

Select the company that should receive the other side, then select **Create**.



![Nova Electronics Distribution selected in the Select Company dialog](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-inter-company-journal-entry-inter-company-select-company.png)

ERPNext opens a new draft and carries forward the following context:


| Field                                 | What ERPNext carries forward                              |
| ------------------------------------- | --------------------------------------------------------- |
| Entry Type                            | Inter Company Journal Entry                               |
| Company                               | The company selected in the dialog                        |
| Posting Date                          | The current date used by the linked-entry creation action |
| Inter Company Journal Entry Reference | The submitted first Journal Entry                         |


ERPNext does not copy the first company’s account rows because account names belong to different company ledgers. The draft starts with an empty **Accounting Entries** table. This is intentional.



![The second company's linked draft with an empty Accounting Entries table](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-inter-company-journal-entry-inter-company-counterpart-draft.png)

## Enter the second company’s accounts

Add the second company’s accounting treatment. In this example:

1. Debit **Trade Show Expenses** by $1,200.
2. Credit **Due to Nova Electronics Trading** by $1,200.
3. Use the second company’s Cost Center.

![The second company's opposite account rows with the row edit pencil highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-inter-company-journal-entry-inter-company-counterpart-accounts.png)

The individual accounts do not need to have the same names as the first company’s accounts. What must agree is the economic treatment and, for companies using the same currency, the reversed debit and credit totals.

Review the entry, confirm that it balances, and submit it. ERPNext then stores the link on both Journal Entries.

## Verify the linked pair

On either submitted entry, open **More Info**, then expand **Reference**. **Inter Company Journal Entry Reference** links to the other Journal Entry.



![The linked Inter Company Journal Entry Reference highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-inter-company-journal-entry-inter-company-linked-reference.png)

You can also review both entries from the Journal Entry list.



![The two linked Inter Company Journal Entries in the list](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-inter-company-journal-entry-inter-company-journal-list.png)

Use **View &gt; Ledger** on each entry to confirm the separate [GL Entries](https://docs.frappe.io/erpnext/accounting-entries). If consolidated group reporting is used, review the due-from and due-to balances and apply the organization’s elimination process outside the operating entries where required.

## Important fields and what they mean


| Field                                 | What it means                                                         | Guidance                                                                                                  |
| ------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Company                               | The company whose ledger receives this entry                          | Every account row must belong to this company.                                                            |
| Entry Type                            | Enables the linked inter-company workflow                             | Select Inter Company Journal Entry on the first entry. ERPNext carries it to the linked draft.            |
| Posting Date                          | The accounting date for that company’s entry                          | Review the date on both entries, especially near a period end.                                            |
| Multi Currency                        | Allows account currencies different from the company currency         | Review exchange rates and company-currency totals before submission.                                      |
| Accounting Entries                    | The accounts, parties, dimensions, and amounts posted in this company | The linked draft requires its own rows.                                                                   |
| Inter Company Journal Entry Reference | Links the two submitted Journal Entries                               | ERPNext sets this through the creation workflow and updates the first entry when the second is submitted. |
| Total Debit and Total Credit          | The balanced totals for one company                                   | Both must match within each entry. Same-currency linked entries must also have opposite totals.           |


## When a party is required

If a row uses a Receivable or Payable account, ERPNext requires **Party Type** and **Party**. Select the internal Customer or Supplier that represents the related company. For a dedicated due-from or due-to account that is not configured as a Receivable or Payable account type, a party is not mandatory, but your accounting policy may still require a separate account for each related company.

The earlier ERPNext restriction that exposed only accounts marked specifically for inter-company use was removed. Current versions filter account choices by the selected company and whether the account is a ledger account. Choose accounts that reflect the real accounting treatment instead of duplicating every normal bank or expense account solely for this entry type.

## Cancel or correct a linked pair

The two Journal Entries are separate submitted accounting documents. Cancelling one entry reverses its own ledger effect and removes the inter-company reference from the linked pair. It does not replace the need to review and correct the other company’s entry.

If both sides are wrong, correct both companies using the organization’s cancellation, amendment, or Reverse Journal Entry procedure. Keep the posting dates and explanations aligned so the audit trail remains clear.

## Troubleshooting

### Create Inter Company Journal Entry is not available

Confirm that the first Journal Entry is submitted, its Entry Type is Inter Company Journal Entry, and it does not already have an Inter Company Journal Entry Reference. The action is available only on the first submitted entry before a counterpart is linked.

### The linked draft has no account rows

This is expected in the current workflow. ERPNext cannot reuse accounts from another company’s Chart of Accounts. Add the second company’s own accounts and opposite totals.

### ERPNext says the linked debit and credit amounts do not match

For companies with the same default currency, the second entry’s total debit must equal the first entry’s total credit, and the second entry’s total credit must equal the first entry’s total debit. Check the amounts, precision, and exchange-rate treatment.

### A Receivable or Payable row asks for a party

Select the relevant Customer or Supplier in **Party Type** and **Party**. These fields are mandatory for Receivable and Payable account types unless the transaction is created through a special workflow that explicitly bypasses the requirement.

### I created both entries separately and they are not linked

Use **Make &gt; Create Inter Company Journal Entry** from the first submitted entry. Manually creating two unrelated Journal Entries does not populate the inter-company reference automatically.

## FAQs

### Does one Inter Company Journal Entry post to both companies?

No, The first entry posts only to its selected company. The linked second entry must be completed and submitted to post the other company’s side.

### Does ERPNext create the second entry automatically?

ERPNext creates the linked draft and prefills its company, entry type, posting date, and reference. You must choose the second company’s accounts, enter the amounts, review the entry, and submit it.

### Must the same accounts be used in both companies?

No, Each entry uses accounts from its own company. The accounts should express opposite sides of the same economic event, and the linked totals must agree according to the currency rules.

### Should I use an Inter Company Journal Entry or inter-company invoices?

Use invoices when one entity is selling goods or services to another and the transaction needs commercial documents, taxes, items, and receivable or payable workflow. Use this Journal Entry workflow for a direct accounting adjustment without an invoice.

### Is there a separate inter-company ledger report?

ERPNext posts the entries to the normal General Ledger. Use dedicated due-from and due-to accounts, Company filters, and consolidated reports to analyze inter-company balances.

### What happens if one linked entry is cancelled?

Its own ledger entries are reversed under ERPNext’s cancellation rules, and the reference between the pair is removed. Review the other company’s entry separately and correct it when necessary.

## Related topics

- [Journal Entry Template](https://docs.frappe.io/erpnext/journal-entry-template)
- [Finance Book](https://docs.frappe.io/erpnext/finance-book)
- [Consolidated Financial Statement](https://docs.frappe.io/erpnext/consolidated-financial-statement)

/mermaidTESTCURSOR/mermaid

<!-- page: erpnext/erpnext__introduction.md -->
---
title: "Introduction"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/introduction"
updated: "2026-04-27"
---

## What is ERPNext?

ERPNext is business management software that helps companies stay on top of their operations, whether it's tracking inventory, managing finances, handling projects, or keeping customers happy. Think of it as the central nervous system for your business, bringing everything together in one place.

Most ERPs are clunky, expensive, and a headache to customize. ERPNext is different. It is open-source, cloud-ready, and built to be flexible. You get the power of an enterprise system without the usual complications.

![ERPNext](/files/erpnext-hero-image.png)

## Why ERPNext?

Because running a business is already hard enough. Your ERP should not make it harder.

With ERPNext, you get a complete set of tools for all your business needs, built in and ready to use. With ERPNext, you get:

1. A complete suite of tools : From Assets to Accounting to Inventory, everything you need is built-in.
2. No vendor lock-in : Open-source means you own your data and have the freedom to customize.
3. Easy to use : A clean, modern interface that doesn't feel like it was built in the '90s.
4. Cost-effective : No sky-high licensing fees. Just powerful software that works.

Whether you are a small business or a growing enterprise, ERPNext helps you stay organized, automate the boring stuff, and focus on what really matters - running your business.

## Key features

ERPNext will help you:

1. Keep track of the financial indicators of the organization.
2. Track all invoices and payments.
3. Know what quantity of product is available in stock.
4. Identify and track your key performance indicators (KPIs).
5. Identify open customer queries.
6. Manage employee payroll.
7. Assign tasks and follow up on them.
8. Maintain a database of all your customers, suppliers, and contacts.
9. Prepare quotations.
10. Track your budgets and spending.
11. Determine effective selling price based on the actual raw material, machinery, and effort cost.
12. Get reminders on maintenance schedules.
13. Publish your website.

And a ton more.

## **Under the Hood**

- [Frappe Framework](https://github.com/frappe/frappe): A full-stack web application framework written in Python and Javascript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.
- [Frappe UI](https://github.com/frappe/frappe-ui): A Vue-based UI library, to provide a modern user interface. The Frappe UI library provides a variety of components that can be used to build single-page applications on top of the Frappe Framework.

## Installation

To install/setup the app, follow the [guidelines here](https://github.com/frappe/erpnext/#production-setup).

## Learning and community

1. [Frappe School](https://frappe.school/) - Learn Frappe Framework and ERPNext from various courses by the maintainers or from the community.
2. [Documentation](https://docs.frappe.io/erpnext) - Extensive documentation for ERPNext.
3. [User Forum](https://discuss.frappe.io/c/erpnext/6) - Engage with the community of ERPNext users and service providers.
4. [Telegram Group](https://t.me/erpnext_public) - Get instant help from the community of users.

<!-- page: erpnext/erpnext__inventory-account.md -->
---
title: "Inventory Account"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/inventory-account"
updated: "2026-02-25"
---

In ERPNext, users can either set up a Warehouse-wise Inventory Account or use the default Inventory Account from the Company master, which is 'Stock In Hand.'


![warehouse inventory account](/files/warehouse-inventory-account.png)

From the Version 16, users can also able to set the Item-wise Inventory Account. To do this, they need to enable the option 'Enable Item-wise Inventory Account' in the Company master.


![company configuration](/files/company-configuration.png)

After enabling it, users can define the Default Inventory Account in the Item master. Alternatively, they can set a Default Inventory Account at the Item Group or Brand level if they do not wish to define it for each item individually. 



![item inventory account](/files/item-inventory-account.png)


Users can choose to use either item-wise or warehouse-wise inventory accounts, but not both.
