<!-- Frappe documentation: erpnext, part 25 of 69. Index: docs/INDEX.md -->

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



[Screenshot on the live page: Company accounts for exchange gains and losses]

Create an eligible closing-date rate in [Currency Exchange](/erpnext/currency-exchange) or verify the active provider in [Currency Exchange Settings](/erpnext/currency-exchange-settings). Confirm that the [Accounting Period](/erpnext/accounting-period) is open and the user can submit revaluations and Journal Entries.

Review the currency controls in [Accounts Settings](/erpnext/accounts-settings) before closing so the stored-rate age policy matches finance's approved procedure.

## Create an Exchange Rate Revaluation

1. Open Accounting &gt; Multi Currency &gt; Exchange Rate Revaluation.
2. Select **Add Exchange Rate Revaluation**.
3. Enter the Posting Date and Company.
4. Set Rounding Loss Allowance only when a small balance should be treated as zero. The allowed value is from 0 inclusive to less than 1.
5. Select **Get Entries**.

[Screenshot on the live page: Company and posting date on the revaluation]

ERPNext fetches eligible foreign-currency accounts, their account and base balances, the current carrying rate, the new rate for the posting date, the new base balance, and the calculated gain or loss.

## Review the fetched accounts

Do not submit immediately. Review each account against the General Ledger, the approved closing rate, and the underlying bank, receivable, payable, or other balance.



[Screenshot on the live page: Revaluation account row and calculated gain]

Select the highlighted pencil to open the full child-row editor.



[Screenshot on the live page: Current foreign and base balances]



[Screenshot on the live page: New rate, new base balance, and gain]


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



[Screenshot on the live page: Revaluation totals]


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



[Screenshot on the live page: Automatic revaluation setting]

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

[Screenshot on the live page: Connect Applet]
[Screenshot on the live page: Call Popup Section]

> **Note:** Replace `<your-site>` in URL with your site name. For example, if the site name is **frappe.erpnext.com** then the URL will be:
`https://frappe.erpnext.com/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`

- After that add a Passthru applet under "After Call Conversation ends" and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_end_call`

[Screenshot on the live page: After Conversation Ends Section]

[Screenshot on the live page: After call ends section]

> **Note:** Make sure to check "Make Passthru Async".

- Similary, add a Passthru applet under "If nobody answers..." section and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_missed_call`

[Screenshot on the live page: No Response Section]

[Screenshot on the live page: After call ends section]

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

[Screenshot on the live page: Open the Sales Invoice Item row to review deferred accounting fields]



[Screenshot on the live page: Deferred revenue account and service period on a Sales Invoice Item]



1. Open the Deferred Revenue and Expense Report.
2. Select Nova Industries and the reporting period.
3. Choose the revenue view or filter for Sales Invoices.
4. Review the invoice, item, service dates, expected recognition, actual posting, and remaining amount.
5. Open the invoice or generated Journal Entry when a line needs explanation.

[Screenshot on the live page: Loaded Deferred Revenue and Expense Report for Nova annual service revenue]

## Review deferred expense

[Screenshot on the live page: Deferred expense account and service period on a Purchase Invoice Item]





Use the expense view for prepaid costs from Purchase Invoices. The same report logic shows the portion already recognised as expense and the amount that remains in the deferred asset account.

[Screenshot on the live page: Loaded Deferred Revenue and Expense Report for Nova prepaid service expense]

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

[Screenshot on the live page]



**Report View**

[Screenshot on the live page]

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

[Screenshot on the live page: ERPnext keycloak Settings]

## Setup fairlogin

To enable fairlogin as an ERPNext login option, you need to configure the following parameters:

- Base URL https://id.fairkom.net/auth/realms/fairlogin/
- Authorize URL https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/auth
- Redirect URL /api/method/frappe.integrations.oauth2_logins.login_via_fairlogin
- Access Token URL https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/token
- API Endpoint https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/userinfo

[Screenshot on the live page: ERPnext fairlogin Settings]

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
[Screenshot on the live page]  
1. In the first fields, list a DocTypes for which you want to collect a rating
2. In the Document Name field, just enter the name of first field "document", so that it becomes a [Dynamic Link](https://docs.erpnext.com/docs/v14/user/manual/en/customize-erpnext/articles/dynamic-link-fields) field.
3. Enter a Rating field. You can also choose other data or select field, if you wish to take rating on those lines.

  
**Web Form for Feedback Form**  
Once a DocType is created, simply create a Web Form by fetching all the standard fields from Feedback doctype.  
[Screenshot on the live page]  
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

  
[Screenshot on the live page]  
  
**Quick Demo:**  
Here is the demo of how link would be generated, Web Form would be filled and capture in ERPNext.  
[Screenshot on the live page]

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

[Screenshot on the live page]

We will also require the variable names of all the fields inside the child table which need to be referenced. This can be obtained from the 'Customize Form' section of the corresponding child table as shown below

[Screenshot on the live page]

 

[Screenshot on the live page]

 

[Screenshot on the live page]

 

[Screenshot on the live page]

**Method 1. Displaying rows of a Child Table on an unordered list**



{% for row in doc.items %}

* Item Code: {{ row.get_formatted("item_code", doc) }}

Quantity: {{ row.get_formatted("qty", doc) }}

Rate: {{ row.get_formatted("rate", doc) }}

Amount: {{ row.get_formatted("amount", doc) }}


{% endfor %}




 

The output on a print format would be as follows

[Screenshot on the live page]

 

 

**Method 2. Displaying rows of a Child Table as a table**

 



  

   

  

  

 

 

| Item Code | Quantity | Rate | Amount |
| --- | --- | --- | --- |
| {{item.item_code }} | {{item.qty}} | {{item.rate}} | {{item.amount}} |



 

The output on a print format would be as follows

 

[Screenshot on the live page]

 

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





[Screenshot on the live page]





For information on creating custom fields on a DocType you can refer to the following link - [Custom Fields in ERPNext](https://docs.erpnext.com/docs/v13/user/manual/en/customize-erpnext/custom-field)





Once this step is done you should have two new fields on the selected DocType, as illustrated below:-





[Screenshot on the live page]











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





[Screenshot on the live page]





**Step 3. Save, enable and test the Client Script**





Once the Client Script is amended as per your use case, we can Save it and enable it by clicking the 'Enabled' checkbox.

Go to the required DocType and refresh the page for the changes to take effect.





Now when an address is selected on our custom link field, the entire address will be fetched on our custom read only field, as illustrated below:-





[Screenshot on the live page]

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

[Screenshot on the live page: Standard fields in Sales Order]

Sales Invoice (custom fields)

[Screenshot on the live page: Custom Field in Sales Invoice]

Since names for the Customer's PO related fields are same in the Sales Order and Sales Invoice, when creating Sales Invoice from the Sales Order, values in these fields are auto-fetched.

[Screenshot on the live page: Values fetching from Sales Order to Sales Invoice]
[Screenshot on the live page: Values fetching from Sales Order to Sales Invoice]

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

[Screenshot on the live page: Check Field TYpe]  


#### Select

Select will be a drop-down field. You can add multiple results in the Option field, separated by row.

[Screenshot on the live page: Select Field Type]  


#### Table

A table will be a kind of Link field which renders another DocType within the current form. For example, the Item Table in the Sales Order is a Table field, which is linked to Sales Order Item DocType.

[Screenshot on the live page: Table Field Type]  


#### Attach

Attach field allows you to browse a field from the File Manager and attach the same herein.

[Screenshot on the live page: Attach Field Type]  


#### Attach Image

Attach Image is a field wherein you will be allowed to attach Images of the format jpeg, png, etc. This becomes the Image representing that particular DocType. For e.g., you would want the image of an Item in its DocType, you can choose your field to be an Attach Image Field.

[Screenshot on the live page: Field Type Image]  


#### Text Editor

Text Editor is a text field. It has text-formatting options. In ERPNext, this field is generally used for defining Terms and Conditions.

[Screenshot on the live page: Field Type Text Editor]  


#### Date

This field will enable you to enter the Date in this field.

[Screenshot on the live page: Field Type Date]  


#### Date and Time

This field will give you a date and time picker. The current date and time (as provided by your computer) are set by default.

[Screenshot on the live page: Field Type Date and Time]  


#### Barcode

In this field, you can specify the field as Barcode which will allow you to enter a Barcode number. Oce you do that, the Barcode would automatically get generated against the number.

[Screenshot on the live page: Field Type Barcode]  


#### Button

This kind of field will be an action button, like Save, Submit, etc.

[Screenshot on the live page: Field Type Button]  


#### Code

If the Field Type is selected as code, you will be able to enter a Code to the field.

[Screenshot on the live page: Field Type Code]  


#### Color

You will have the option of specifying the color for this Form.

[Screenshot on the live page: Field Type Colour]  


#### Column Break

Since ERPNext has multiple column layouts, using Column Breaks, you can divide a set of fields into a maximum of two columns.

[Screenshot on the live page: Field Type Column Break]  


#### Currency

Currency field holds numeric value, like Item Price, Amount, etc. Currency field can have value up to six decimal places. Also, you can have a currency symbol being shown for the currency field.

[Screenshot on the live page: Field Type Currency]  


#### Data

The data field will be a simple text field. It allows you to enter a value of up to 140 characters, making this the most generic field type. To enable validations for Email, Name, or Phone Number inputs, set options to "Email", "Name", "Phone" in Settings > DocType.

[Screenshot on the live page: Field Type Data]  


#### Float

Float field carries numeric value, up to nine decimal places. Precision for the float field is set via [Set Precision](/erpnext/set-precision)

> Setup > Settings > System Settings

The setting will be applicable on all the float field.

[Screenshot on the live page: Field Type Float]  


#### Geolocation

Use Geolocation field to store GeoJSON [feature_collection](https://tools.ietf.org/html/rfc7946#section-3.3). Stores polygons, lines, and points. Internally it uses the following custom properties for identifying a circle.

Read [Geolocation field](/erpnext/geolocation-field) for more understanding.

[Screenshot on the live page: Field Type Geolocation]  


#### HTML

You can select the field to be an HTML field when you want the data to be entered in HTML format.

[Screenshot on the live page: Field Type HTML]  


#### Image

Image field will render an image file selected in another attach field.

For the Image field, under Option (in Doctype), a field name should be provided where the image file is attached. By referring to the value in that field, the image will be a reference in the Image field.

[Screenshot on the live page: Field Type Image]  


#### Int (Integer)

The integer field holds numeric value, without decimal place.

[Screenshot on the live page: Field Type Integer]  


#### Small Text

Small Text field carries text content and has more character limit than the Data field.

[Screenshot on the live page: Field Type Small Text]  


#### Long Text

You can define your field to a Long Text Field when you would want to enter data with an unlimited character limit.

[Screenshot on the live page: Field Type Long Text]  


#### Text

This field type would allow you to add text in the field. The character limit in Small text, Long text and Text fields shall be determined based on the Relational Database Management System.

[Screenshot on the live page: Field Type Text]  


#### Markdown Editor

This field will allow you to add the text in Markup language.

[Screenshot on the live page: Field Type Markdown Editor]  


#### Password

The password field will have decoded value in it.

[Screenshot on the live page: Field Type Password]  


#### Percent

You can define the field as a Percentage field which in the background will be calculated as a percentage.

[Screenshot on the live page: Field Type Percent]  


#### Rating

You can define the field as a Rate field which in the background will be calculated as Rating.

[Screenshot on the live page: Field Type Rating]  


#### Read Only

Read Only field will carry data fetched from another form which will be non-editable. You should set Read Only as field type if its source for value is predetermined.

[Screenshot on the live page: Field Type Read Only]  


#### Section Break

Section Break is used to divide the form into multiple sections.

[Screenshot on the live page: Field Type Section Break]  


#### Signature

You can define the field to be a Signature field wherein you can add the Digital Signature in this field.

[Screenshot on the live page: Screenshot 2024-08-28 at 3.01.56 PM]  


#### Table MultiSelect

This is a combination of 'Link' type and 'Table' type fields. Instead of a child table with 'Add Row' button, in one field multiple values can be selected.

[Screenshot on the live page: Field Type Table MultiSelect]  


#### Time

This is a Time field where you can define the Time in the field.

[Screenshot on the live page: Field Type Time]  


#### Duration

You can use the Duration field if you want to define a timespan.

[Screenshot on the live page: Field Type Duration]  


If you don't want to track duration in terms of days or seconds, you can enable "Hide Days" and "Hide Seconds" options respectively in your Form.

[Screenshot on the live page: Field Type Duration Options]  


This is how the duration field looks after the above changes.

[Screenshot on the live page: Field Type Duration]  
