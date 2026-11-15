<!-- Frappe documentation: erpnext, part 27 of 69. Index: docs/INDEX.md -->

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

[Screenshot on the live page: Company Accounts Closing tab with Roles Allowed to Set and Edit Frozen Account Entries highlighted]

Grant this role sparingly. A user with it can bypass the restriction when posting to a frozen Account. In older ERPNext documentation, this control may be described as an Accounts Settings field. On the current develop interface it appears in the Company's **Accounts Closing** tab.

## Freeze an Account

1. Open **Accounting &gt; Chart of Accounts**.
2. Select the Company.
3. Open the ledger Account that should stop receiving transactions.
4. Set **Frozen** to **Yes**.
5. Save the Account.

[Screenshot on the live page: Ledger Account with Frozen set to No before the change]



[Screenshot on the live page: Ledger Account with Frozen set to Yes and Save highlighted]

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

[Screenshot on the live page: Company Accounts Closing tab showing the frozen date and authorized role]



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

[Screenshot on the live page: General Ledger filters showing Nova Industries and the selected reporting period]

## Follow a Sales Invoice through the ledger

For the selected period, Nova Industries has $395,762 in total debits and $395,762 in total credits. Equal totals show that the selected entries are mathematically balanced. They do not prove that every transaction used the correct account, so the finance manager opens the rows behind the $20,000 sale.

[Screenshot on the live page: Populated General Ledger for Nova Industries with balanced debit and credit totals]


| Posting             | Debit                      | Credit                | What it means                                               |
| ------------------- | -------------------------- | --------------------- | ----------------------------------------------------------- |
| Customer balance    | Debtors $20,000            |                       | The customer now owes Nova Industries.                      |
| Sales income        |                            | Sales $20,000         | The sale increases income for the period.                   |
| Inventory reduction |                            | Stock In Hand $14,500 | The inventory asset decreases by the delivered stock value. |
| Cost recognition    | Cost of Goods Sold $14,500 |                       | The cost of the sold goods becomes an expense.              |


The receivable and income rows explain the commercial sale. The stock and cost rows explain the inventory leaving the business. This is why one [Sales Invoice](/erpnext/sales-invoice) can produce more than two ledger rows when stock is updated.

## Open the source voucher

Select the Voucher No in the report to open the submitted transaction. Compare the customer, posting date, items, income account, taxes, stock settings, and totals with the ledger rows. The voucher explains the business event, while the General Ledger explains its accounting effect.

[Screenshot on the live page: Submitted Sales Invoice opened from its General Ledger voucher link]

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

[Screenshot on the live page: geolocation field]  

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

[Screenshot on the live page: Default Company in ERPNext Global Defaults]


| Setting               | What it controls                                                   | Nova example                                                                                |
| --------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| Default Company       | Company suggested on new records                                   | Nova Industries is suggested for routine operating transactions.                            |
| Default Country       | Country suggested on addresses and regional fields                 | United States is proposed for a new customer address, but users can select another country. |
| Default Currency      | Currency used when no company or transaction rule is more specific | USD is the normal working currency. A EUR customer invoice can still use EUR.               |
| Default Distance Unit | Unit used for distance fields                                      | Mile suits Nova's United States operations; kilometre may suit another site.                |
| Demo Company          | Company identified for demonstration behaviour where supported     | Use only on a genuine demo or training site, not to label a live Company as fictional.      |


[Screenshot on the live page: Default Country in ERPNext Global Defaults]

[Screenshot on the live page: Default Currency in ERPNext Global Defaults]

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

[Screenshot on the live page: GoCardless Settings]

On enabling service, the system will create a Payment Gateway record and an Account head in chart of account with account type as Bank.

[Screenshot on the live page: GoCardless COA]

It will also create a payment gateway account. You can change the default bank account if needed and create a template for the payment request.

[Screenshot on the live page: Payment Gateway Account]

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
 [Screenshot on the live page]
- Deleting an Event in ERPNext
 [Screenshot on the live page]

### Syncing Events from Google Calendar
- Once Google Calendar Integration is succesful, all the events in Google Calendar will be synced if `Pull from Google Calendar` is checked.
- Syncing Events from Google Calendar to ERPNext
 [Screenshot on the live page]

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
[Screenshot on the live page]

It will be shown in Google Contacts:
[Screenshot on the live page]

### Syncing Contacts from Google Contacts
- Once Google Contacts Integration is succesful, all the contacts in Google Contacts will be synced if `Pull from Google Contacts` is checked.
 [Screenshot on the live page]

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
* To backup data to Google Drive, click on **Take Backup**. Backup process will run in the background and you will be notified regarding the backup status. [Screenshot on the live page]

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
 [Screenshot on the live page]

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

1. Create a new project on Google Cloud Platform and generate new OAuth 2.0 credentials. [Screenshot on the live page]
* Enable API Access in API Library for the Integration you wish to integrate.


	+ Google Calendar: **Calendar API**
	+ Google Contacts: **People API**
	+ Google Drive: **Drive API**
	+ Google Indexing: **Indexing API**[Screenshot on the live page]
* In **API & Services > Credentials** create a new Credential and select **Create OAuth client ID**
* Select Application Type **Web Application**
* Add `https://{yoursite}` to Authorized JavaScript origins.
* Add `https://{yoursite}?cmd=frappe.integrations.doctype.google_calendar.google_calendar.google_callback` as an authorized redirect URI for Google Calendar.
* Add `https://{yoursite}/api/method/frappe.integrations.google_oauth.callback` as an authorized redirect URI for rest of the services.

[Screenshot on the live page]
* Add your Client ID and Client Secret in the Google Settings in **Home > Integrations > Google Services > Google Settings**

### For Google Maps


> Setting the *API Key* is only required if you want to use the Directions API, for example in ERPNext's **Delivery Trip**. For the other features, this is not required.
> 
> 

In order to allow a synchronization with Google Maps you need to generate an API key as Google Maps doesn't need access to data from Google.

1. Create a new project on Google Cloud Platform and generate new API Key.
* Enable API Access in API Library for the Directions API and then add the API Key in the Google Settings in **Home > Integrations > Google Services > Google Settings**. [Screenshot on the live page]

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

  


[Screenshot on the live page]

﻿

Now, make sure that your Customer's and Supplier's addresses have *GST State* and *Party GSTIN* configured properly.

  


﻿[Screenshot on the live page]

### 

### ﻿Step 2 - Configure State-wise GST Accounts ***(Optional)***

  


To configure, go to Chart of Accounts, create a state-wise set of GST accounts *(CGST, SGST & IGST)* as seen in the screenshot below.

﻿

﻿[Screenshot on the live page]

  


  


Add these newly created accounts in *GST Accounts* table from **GST Settings**, to include this in all GST Reports.

  


[Screenshot on the live page]

 

### Step 3 - Item-wise GST setup

  


a. Create **Item Tax Template** for different rates and add all the *GST Accounts* we have created in previous step.

b. Define the rates.

This helps system know which GST Accounts and Tax Rates to apply in the Invoices.

  


Your Item Tax Template should look like this: 

[Screenshot on the live page]

  


**The same way you can create different Item Tax Templates for different GST Rates.** 

  


After the creation of Item Tax Templates, you can start with assigning these templates to their respective Items from the Item Master.

  


[Screenshot on the live page]

 

### Step 4 - Classification of Inter-State and Intra-State Taxes

  


We are nearly there.

Create two **Tax Categories**, for each of our branches in different State. The **Source State** on each *Tax Category* will correspond to each of our company’s branches.

Each state will have two Tax Categories, one for Inter State and other for Out State transactions. 

  


**For ‘Out State’ Tax Categories, mark ‘Is Inter State’ checkbox as enabled.** 

  


*IN State Tax Category for Delhi:* 

[Screenshot on the live page]

  


*﻿OUT State Tax Category for Delhi:* 

[Screenshot on the live page]

 

**Create for other States the same way as shown above.**

  


### Step 5 - Configuring our Invoice Templates

  


Finally, configure a set of two **Sales Taxes and Charges Templates**, and two **Purchase Taxes and Charges Templates, for each Tax Categories created.** 

**﻿**

Go to Sales Taxes and Charges Template, and define a set of two templates for each state (as seen in the screenshot below for Maharashtra)

  


*For IN State template, choose the IN State Tax Category and appropriate CGST & SGST account in* ***Account Head.*** 

  


[Screenshot on the live page]

  


*For OUT State template, choose the OUT State Tax Category and appropriate IGST account in* ***Account Head.*** 

[Screenshot on the live page]

  


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

  


[Screenshot on the live page]

  


It auto-fetched the following Taxes and Charges Template:

[Screenshot on the live page]

  


### Example 2:

Here I have selected a **Customer from Maharashtra and Company's Address as Delhi**, it should fetch the OUT State template we created above.

  


[Screenshot on the live page]

  


It auto-fetched the following Taxes and Charges Template:

[Screenshot on the live page]
