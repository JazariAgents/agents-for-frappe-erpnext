<!-- Frappe documentation: erpnext, part 34 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__journal-entry.md -->
---
title: "Journal Entry | ERPNext Documentation"
description: "Create balanced Journal Entries in ERPNext, understand account rows and references, verify General Ledger postings, and reverse an incorrect entry safely."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/journal-entry"
updated: "2026-08-14"
---

A Journal Entry records a balanced debit and credit directly in the [General Ledger](/erpnext/general-ledger). Use it for accounting adjustments, accruals, transfers, opening balances, write-offs, revaluations, and other postings that do not belong in a normal sales, purchase, or payment workflow.



For routine money received from Customers or paid to Suppliers, prefer a [Payment Entry](/erpnext/payment-entry). It selects the expected bank, cash, party, currency, and invoice-allocation fields for you. Use a Journal Entry when you need deliberate control over the accounts and understand the accounting effect.



This guide uses a simple example: Nova Industries pays $845 of office-maintenance expense from its operating bank account.


| Account                           | Debit | Credit | Meaning                  |
| --------------------------------- | -----: | ------: | ------------------------ |
| Office Maintenance Expenses - NET | $845  | $0     | Recognizes the expense   |
| Nova Operating Bank - NET         | $0    | $845   | Reduces the bank balance |


## Before you begin

Confirm that the Company, [Chart of Accounts](/erpnext/chart-of-accounts), Fiscal Year, and Posting Date are correct. The accounts must be non-group accounts belonging to the selected Company. Configure a Cost Center, Project, or other [Accounting Dimension](/erpnext/accounting-dimensions) before using it on an account row.

If the entry records a Customer or Supplier balance, use the correct receivable or payable account and select the Party Type and Party. Add a document reference when the entry should change an invoice, order, expense claim, employee advance, asset, or another supported outstanding balance.

## Create a Journal Entry

1. Open the Journal Entry list and select **Add Journal Entry**.  
[Screenshot on the live page: Journal Entry list showing the submitted office-maintenance example]
2. Select the **Company**, **Entry Type**, and **Posting Date**. For a general adjustment, keep **Entry Type** as **Journal Entry**.  
[Screenshot on the live page: Company and Entry Type selected on a new Journal Entry]
3. In **Accounting Entries**, add the account to debit and enter the debit amount. Add the offsetting account and enter the credit amount. Total Debit and Total Credit must be equal before submission.

  The grid shows the main columns. Select the highlighted pencil icon to open the complete row editor when you need Party, reference, currency, Cost Center, Project, or other row-level fields.
  [Screenshot on the live page: Balanced Accounting Entries with the first row pencil icon highlighted]
4. In the row editor, confirm the **Account** and enter either a debit or a credit, never both on the same row. In the example, Office Maintenance Expenses is debited by $845.  
[Screenshot on the live page: Account and debit fields in the Journal Entry row editor]
5. Add a clear **User Remark** and, when applicable, a Reference Number, Reference Date, Bill Number, Bill Date, and Due Date. These supporting fields do not replace a formal link to an ERPNext document.
6. Save, review the accounts and dimensions, then submit. Submission posts the debit and credit to the General Ledger.  
[Screenshot on the live page: Submitted Journal Entry with balanced account rows]

## Create a Journal Entry with Quick Entry

Use **Quick Entry** for a straightforward two-account posting. Enter the amount, debit account, credit account, date, and remark. ERPNext fills the Accounting Entries table and saves the draft. Open the full form before submission when you need a Party, document reference, multiple rows, dimensions, or multiple currencies.



[Screenshot on the live page: Quick Journal Entry dialog with amount, debit account, and credit account highlighted]

You can also select a reusable [Journal Entry Template](/erpnext/journal-entry-template). Loading a template replaces the current account rows and brings in its Entry Type, Company, naming series, opening-entry setting, multi-currency setting, and accounts. You can add or edit rows after loading it.

## Important fields and what they mean


| Field                                | What it controls                                                                                                                                                                                                     |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Entry Type                           | Classifies the posting and can enable type-specific behavior, such as Inter Company Journal Entry or Opening Entry.                                                                                                  |
| Finance Book                         | Limits the posting to a specific [Finance Book](/erpnext/finance-book). Leave it blank when the entry should appear in every Finance Book.                                                                           |
| Multi Currency                       | Shows account currency, exchange rate, and debit or credit in account currency. The selected accounts determine which currencies are available. See [Multi Currency Accounting](/erpnext/multi-currency-accounting). |
| Party Type and Party                 | Identifies the Customer, Supplier, Employee, or other party represented by a receivable or payable row.                                                                                                              |
| Reference Type and Reference Name    | Links a row to a submitted transaction and can change its outstanding or advance position. Do not select an unrelated document merely as a note.                                                                     |
| Is Advance                           | Identifies an advance against a supported order or party. Prefer the supported advance-payment workflow where available so the amount remains reconcilable.                                                          |
| Cost Center, Project, and dimensions | Attribute income, expense, asset, or liability movement for reporting. These values are stored on each account row.                                                                                                  |
| Mode of Payment and Bank Account     | Add payment context and can fetch configured bank information. For routine payments, a Payment Entry is usually safer.                                                                                               |
| Pay To / Recd From                   | Supplies the name used by applicable print formats, including cheque-oriented formats.                                                                                                                               |
| Is Opening                           | Marks a migrated opening posting. Use the documented [Opening Balance](/erpnext/opening-balance) process and validate the temporary opening account.                                                                 |


Supported references can include Sales Invoice, Purchase Invoice, Journal Entry, Sales Order, Purchase Order, Expense Claim, Asset, Loan, Payroll Entry, Employee Advance, Exchange Rate Revaluation, and Invoice Discounting. Availability depends on the selected account, party, document status, and current outstanding amount.

Do not manually set **Payment Entry** as a Journal Entry row reference. Current ERPNext blocks this because payment-allocation relationships must be created through the supported payment and reconciliation workflow.

## Entry types


| Entry type                                                    | Typical use                                                                                                                                                                 |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Journal Entry                                                 | General accrual, adjustment, direct expense, or multi-account posting                                                                                                       |
| Inter Company Journal Entry                                   | Mirrored posting between related Companies. Follow the [Inter Company Journal Entry](/erpnext/inter-company-journal-entry) workflow.                                        |
| Bank Entry, Cash Entry, Credit Card Entry                     | Classification for account movements using the corresponding account type                                                                                                   |
| Contra Entry                                                  | Cash-to-bank, bank-to-cash, bank-to-bank, or cash-to-cash transfer inside the Company                                                                                       |
| Debit Note and Credit Note                                    | Accounting classification for an adjustment. For invoice returns, use the supported [Debit Note](/erpnext/debit-note) or [Credit Note](/erpnext/credit-note) workflow.      |
| Write Off Entry                                               | Writes off a receivable or payable against an appropriate expense or income account. Review [Accounting for Bad Debts](/erpnext/accounting-for-bad-debts) where applicable. |
| Opening Entry                                                 | Migrates balance-sheet balances and outstanding positions                                                                                                                   |
| Depreciation Entry and Asset Disposal                         | System or controlled postings connected to [Asset Depreciation](/erpnext/asset-depreciation) and disposal                                                                   |
| Exchange Rate Revaluation, Exchange Gain Or Loss              | Currency revaluation and realized or unrealized exchange differences                                                                                                        |
| Deferred Revenue, Deferred Expense, Periodic Accounting Entry | System-supported recognition or periodic stock-accounting postings                                                                                                          |
| Excise Entry                                                  | Legacy or regional classification. Confirm applicability with the relevant localization and tax adviser before use.                                                         |


## Verify the General Ledger impact

On the submitted Journal Entry, open **View &gt; Ledger**.



[Screenshot on the live page: Ledger action highlighted in the View menu of a submitted Journal Entry]

The report should show the same total debit and credit under the Journal Entry voucher. In this example, Office Maintenance Expenses is debited by $845 and Nova Operating Bank is credited by $845.



[Screenshot on the live page: General Ledger filtered to the submitted Journal Entry]

For very large entries with more than 100 account rows, current ERPNext can queue submission or cancellation in the background. Wait for processing to finish before relying on the ledger or financial reports.

## Correct or reverse a Journal Entry

Do not edit a submitted posting. If the original should be cancelled and corrected, follow the permitted cancellation and amendment process, subject to linked documents, frozen periods, and [Immutable Ledger](/erpnext/immutable-ledger-in-erpnext) rules.

Use **Actions &gt; Reverse Journal Entry** when the accounting correction should be recorded as a new posting with the debit and credit sides exchanged. Review the generated draft and its Posting Date before submission. On current develop versions, reversal entries are linked to their originals and protected from casual field changes.



[Screenshot on the live page: Reverse Journal Entry action highlighted on a submitted entry]

## Troubleshooting

### Total debit and credit do not match

Review each row and confirm that an amount was entered on only one side. Add the intended offsetting account. The difference must be zero; do not use a miscellaneous account merely to force balance without understanding the cause.

### A Customer or Supplier cannot be selected

Select the correct receivable or payable account first. Confirm the account belongs to the Company and that the Party Type is valid for that account.

### A document is missing from Reference Name

The document normally must be submitted, belong to the relevant party and account, and have a compatible outstanding or unbilled position. Confirm the row's Account, Party Type, Party, Reference Type, and Cost Center.

### A foreign-currency account is unavailable

Enable **Multi Currency** and confirm that the account was created with the required currency. ERPNext does not let a transaction arbitrarily override an account's currency.

## Frequently asked questions

### Should I use a Journal Entry for normal Customer receipts and Supplier payments?

Usually no. Use Payment Entry because it handles party accounts, bank or cash accounts, invoice allocations, advances, exchange rates, references, and later reconciliation more explicitly. Use Journal Entry for a deliberate accounting adjustment or a workflow that specifically requires it.

### Does saving a draft affect the General Ledger?

No, The General Ledger is posted when the Journal Entry is submitted. Cancelling or reversing it creates the corresponding accounting effect according to the current ledger rules.

### Can one Journal Entry contain more than two accounts?

Yes, It may contain several debit and credit rows as long as the total debit equals the total credit and every row passes account, party, reference, currency, and dimension validation.

### Can I use a Journal Entry to settle an invoice?

ERPNext can update an invoice's outstanding position when the correct receivable or payable row is linked to the invoice. For an actual receipt or payment, Payment Entry and [Payment Reconciliation](/erpnext/payment-reconciliation) normally provide a clearer audit trail.

### What is the difference between reversing and cancelling?

Cancellation reverses the submitted document under ERPNext's cancellation rules. **Reverse Journal Entry** creates a separate draft with exchanged debit and credit sides so the correction can be reviewed and posted as its own voucher.

## Related topics

- [Journal Entry Template](/erpnext/journal-entry-template)
- [Accounting Entries](/erpnext/accounting-entries)
- [Inter Company Journal Entry](/erpnext/inter-company-journal-entry)
- [General Ledger](/erpnext/general-ledger)
- [Payment Entry](/erpnext/payment-entry)
- [Repost Accounting Ledger](/erpnext/repost-accounting-ledger)
- [Finance Book](/erpnext/finance-book)

<!-- page: erpnext/erpnext__landed-cost-voucher.md -->
---
title: "Landed cost Voucher"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/landed-cost-voucher"
updated: "2026-02-26"
---

For creating a **Landed cost voucher** in ERPNext: You have to create it against a **Purchase Receipt** and **Purchase Invoice.**  
While creating against **Purchase Invoice**: In the Purchase Invoice --> **Update Stock** should be checked.  
[Screenshot on the live page]  
 If this field is unchecked, the Purchase Invoices will not be fetched in the Landed Cost Voucher  
While creating against **Purchase Receipt**: The Item selected should have **Maintain Stock** checked.  
[Screenshot on the live page]  
 If this field is not checked, the Items will not be displayed when you click **Get items from Purchase Receipt.**   
While creating a Landed cost Voucher, additional costs can be added for the items until they land in our Inventory.  
These additional charges once added, get added in the **Item Valuation rate** and update the Item Rate.  
You can trace this additional charge effect on the Accounting ledger in the **Purchase Receipt --> View --> Accounting Ledger**  
If the additional charges have to be paid against the Landed Cost Voucher, you can:1. You can create a **Payment Entry** directly to complete the payment for additional expenses for the Item and then create a **Purchase Invoice** with **Is Paid** checked --> [In this case, Purchase Invoice is not mandatory unless you want the accounting effect to be seen. ]
2. You can create a **Purchase Invoice** for a **Supplier** for which the **Additional Expenses** are incurred, this way you can see the Accounting effect for the expenses as per the Landed Cost Voucher, then create a Payment entry against it.

  

<!-- page: erpnext/erpnext__ldap-integration.md -->
---
title: "Setting up LDAP\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/ldap-integration"
updated: "2026-02-26"
---


Lightweight Directory Access Protocol (LDAP) is a centralized access control system used by many small and medium-scale organizations.

By settings up LDAP service, you able to login to ERPNext account by using LDAP credentials.

## 1. Prerequisites
To use LDAP, you will first need to install the `ldap3` Python module. To do this, open a terminal session on your server that hosts the ERPNext instance. Go to the `frappe-bench` directory.
run the command: `./env/pip install ldap3`

You are now ready to enable the LDAP service in ERPNext.

## 2. Setting up LDAP
To setup LDAP, go to
> Home > Integrations > LDAP Settings

Many parameters are mandatory to allow ERPNext to connect to LDAP. They are:

 * LDAP Server URL: This is the URL to your LDAP server. Must be in the form of `ldap://yourserver:port` or `ldaps://yourserver:port`

 * Base Distinguished Name (DN): This is the distinguished name of the user that has permissions to look up user details on your LDAP server. This should be a user that only has read-only permissions on your LDAP Server.

 * Password for Base DN: This is the password for the user above, that is used to look up user details on your LDAP server.

 * Organization Unit of Users: This is the DN of the Organizational Unit that all users in your LDAP server must be part of to be able to log into ERPNext.

 * Default Role on Creation: When the user is created in ERPNext, they will be assigned with this default role, the first time they log in.

 * LDAP Search String: This field allows ERPNext to match the user/email entered in the ERPNext login screen, with the LDAP Server. For example, you could use email address, or username depending on your preference.

 It must be entered in the format: `LDAPFIELD={0}`

 Active Directory username example: `sAMAccountName={0}`

 Open LDAP username example: `uid={0}`

 * LDAP Email Field: Specifies the LDAP field that contains the email address of the user.

 Active Directory and Open LDAP example: `mail`

 * LDAP Username Field: Specifies the LDAP field that contains the username of the user.

 Active Directory example : `sAMAccountName`

 Open LDAP example: `uid`

 * LDAP First Name Field: Specifies the LDAP field that contains the first name of the user.

 Active Directory example: `givenName`

 Open LDAP example: `sn`

There are many other non-mandatory fields that you can use to map your LDAP user fields to the ERPNext user fields. They are:

 * Middle Name
 * Phone
 * Mobile



Once your settings are correct, you can click the `Enabled` checkbox at the top. When attempting to enable LDAP, ERPNext will try and connect to the LDAP server to ensure the settings are correct. If it fails, you will not be able to enable LDAP and will receive an error message.

The error message will indicate the issue that needs to be resolved to continue.

After setting enabling LDAP, on the login screen, the system enables **Login Via LDAP** option.



### 2.1 LDAP Security

In the LDAP Security section, You have many options to connect securely to your LDAP server.

 * ##### SSL/TLS Mode
 Specifies whether you want to start a TLS session on initial connection to the LDAP server.

 * ##### Require Trusted Certificate
 Specifies if you require a trusted certificate to connect to the LDAP server


 If you are specifying a trusted certificate, you will need to specify the paths to your certificate files. These files are to be placed on your ERPNext server, and the following fields should be an absolute path to the files on your server.
 The certificate fields are:

 * Path to private Key File

 * Path to Server Certificate

 * Path to CA Certs File


### 2.2 LDAP Group Mappings
ERPNext also allows you to automatically map multiple LDAP groups to the appropriate ERPNext roles.
For example, you may want all of your Accounting employees, to automatically have the Accounts User Role.

Ensure that you fill out the LDAP Group Field to allow this. This is the LDAP field that is found on a user object in LDAP, that has all of the groups the user is a member of.

For Active Directory and Open LDAP, this field should be set to `memberOf`.

Open LDAP may need this field to be enabled on your LDAP server. Please see examples on the internet for more details.

> Note that all ERPNext roles will be checked each time a user logs on and will be removed or added to the user's permissions.



In the LDAP Settings area, there are two dropdowns.
1. SSL/TLS Mode - set this to **StartTLS** to connect to your LDAP server using StartTLS. If your LDAP server does not support StartTLS, setting this to StartTLS will result in an error `StartTLS is not supported`. Check the configuration on your LDAP server if you receive this error.
2. Require Trusted Certificate - if you change this to **Yes** then the certificate provided by the LDAP server must be trusted by the Frappe/ERPNext server. If you would rather use StartTLS with a self-signed (untrusted) certificate, set this to **No**. If you do not use StartTLS, this setting is ignored.

<!-- page: erpnext/erpnext__lead.md -->
---
title: "Lead | ERPNext Documentation"
description: "Learn how to create, qualify, assign, and convert Leads in ERPNext CRM."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/lead"
updated: "2026-07-23"
---

**A lead is a potential customer who might be interested in your products or services.**

To get the customer through the door, you may be doing all or any of the following:

- Listing your product on directories.
- Maintaining an updated and searchable website.
- Meeting people at trade events.
- Advertising your products or services.

When you send out the word that you are around and have something valuable to offer, people will come in to check out your products. These are your Leads.

They are called Leads because they may lead you to a sale. Sales executives usually work on leads by calling them, building a relationship and sending information about products or services. It is important to track all this conversation to enable another person who may have to follow-up on that contact. The new person is then able to know the history of that particular Lead.

To access the Lead list, go to:

> Home > CRM > Sales Pipeline > Lead

- How to Create a Lead
- Go to the Lead list and select New.
- If the person represents an organization, check the 'Lead is an Organization' checkbox. Notice that when you check, the 'Company Name ' field becomes mandatory. Enter the Company Name.
- If the person is an individual, leave the checkbox unchecked and enter Person Name and Gender.
- Enter the 'Email Address'.
- **Status is the important field** in the Lead. You can set the status manually and also it will be updated automatically based on your actions against the lead. Lead: This is the default status assigned when a Lead is created and it indicates an action is needed against this Lead.  
 Open: Sales executive needs to contact the Lead.  
 Replied: A sales executive has provided the information needed and response from Lead is awaited.  
 Opportunity: If an Opportunity is created against the Lead, the status is set to Opportunity. It indicates that the Lead is qualified and may lead to sales.  
 Quotation: If a quotation is created against a Lead, then the status is set to Quotation.  
 Lost Quotation: If the quotation given to the lead has been marked as lost, then the status is set to 'Lost Quotation'.  
 Interested: The lead is interested in the products or services.  
 Converted: If the quotation given to the Lead has resulted in confirmation of an order and if the Sales Order has been created against the quotation, then the status is set to Converted.  
 Do Not Contact: Lead is not interested and no further communication is needed.
- You can set the Lead Source in Source field.
- Enter email ID for communication.
- select 'Save'.

[Screenshot on the live page: Lead]

You can also record the details of the conversation in the NOTES section.

Further details like Lead Type, Market Segment, Industry can be added in the 'MORE INFORMATION' section.

If you have a healthy number of leads, all this information will help you prioritize the leads you can pursue.

You can assign the Lead to a user by clicking on 'Assign' button on left bar. You can also attach files/images by clicking on 'Attach File' button.

- Features

### Reminders to Follow Up on the Leads

It is important to reach out to leads from time to time and build the relationship. You can create a calendar event from the **Activities** tab for the user and a notification will be shown on that date.

### Adding Multiple Contacts and Addresses

In Busines-to-business(B2B) scenario, in order to close a sales deal, you will have to contact multiple people working in the prospective company. You can add the details of all such people in the same lead. Once you save a Lead, you will get the option to add [Contact](/erpnext/contact) details by clicking on 'New Contact' button. Similarly, you can add the [Address](/erpnext/address) details by clicking on 'New Address'.

[Screenshot on the live page: Multiple Contacts and Addresses in Lead]

### 3 Recording Comments, Emails and Events

- **Comments**: You can write your comment in 'Add a comment' box and select 'Comment'.
- **Emails**: You can send an email to the lead by clicking on the 'New Email' button and when the lead responds to your email, it will be appended to your email creating an email thread.
- **Events**: You can also records the Meetings, Calls etc you have had with the Lead by clicking on 'New Event'

### Creating Opportunity, Customer and Quotation

You can create an Opportunity, Customer or a Quotation from the Make dropdown. Relevant field values will be copied over.

### Auto-assigning the Leads to Sales Executives

> Introduced in Version 12

You can define [Assignment Rules](/erpnext/assignment-rule) to automatically assign the leads to sales executives.

[Screenshot on the live page: Lead Assignment Rule]

- Adding Custom Fields

You may need to add custom fields to capture additional details as per your needs.

You can customize the Lead DocType using [Customize Form](/erpnext/custom-field) tool.

- Related Topics
- [Opportunity](/erpnext/opportunity)
- [Customer](/erpnext/customer)
- [Difference between Lead, Contact, and Customer](/erpnext/difference_between_lead_contact_and_customer)

<!-- page: erpnext/erpnext__lead_source.md -->
---
title: "Lead Source | ERPNext Documentation"
description: "Learn how to configure Lead Sources in ERPNext and use them to track where leads and sales opportunities originate."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/lead_source"
updated: "2026-07-23"
---

**Lead Source is a channel through which the leads are generated.**

It is important to track the source from which you are getting the leads. This will help in measuring effectiveness of various marketing campaigns and allocate the budgets accordingly.

To access the Lead Source list, go to:

> Home > Selling > Settings > Lead Source

- How to Create a Lead Source
- Go to the Lead Source list, select New.
- Enter 'Source Name'.
- Enter 'Details' if you need to elaborate more on the source.

Typical lead sources are contact forms on your website, marketing campaigns, events, references, ads on social media etc.

[Screenshot on the live page: Screenshot 2023-12-28 at 10.30.48 AM]

The system will allow you to maintain a list of various lead sources leveraged by you.

[Screenshot on the live page: Screenshot 2023-12-28 at 10.35.00 AM]

<!-- page: erpnext/erpnext__legacy-controller-for-period-closing-voucher.md -->
---
title: "Legacy Controller for Period Closing Voucher"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/legacy-controller-for-period-closing-voucher"
updated: "2026-08-14"
---

A small company can close its Profit and Loss balances in one operation. A company with millions of General Ledger rows may time out when the same work is attempted as one large database transaction. The Period Closing Voucher controller lets ERPNext use either the legacy single-transaction process or newer batched background processing.



The name is technical, but the decision is operational: keep the familiar legacy process for modest ledgers, or use batched processing when volume and accounting dimensions make one large close unreliable.

## Find the setting

1. Open **Accounts Settings**.
2. Open the **Accounts Closing** or Period Closing section.
3. Find **Use legacy controller for Period Closing Voucher**.
4. Save the setting before creating the next closing voucher.

[Screenshot on the live page: Use legacy controller for Period Closing Voucher in Accounts Settings]



## Choose the controller


| Setting  | Processing                                                     | Best fit                                                                      |
| -------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Enabled  | Processes the voucher in one database transaction.             | Small and medium ledgers where closing completes reliably.                    |
| Disabled | Splits work into background batches, including date-wise jobs. | Large ledgers, timeouts, and closes that must preserve dimensional reversals. |


With the legacy controller, reversals are primarily account-based. Batched processing is designed to honour dimensional postings more fully. Test the result in a representative environment and reconcile the closing account before changing a live year-end process.

## Troubleshooting

### The voucher remains queued

Check background workers, failed jobs, error logs, and the voucher status. Do not submit duplicate closing vouchers until you know whether the queued job posted any entries.

### The closing totals differ after switching

Compare company, fiscal year, Finance Book, cost-center option, dimensions, and source ledger entries. Reconcile the General Ledger to the approved Profit and Loss before accepting the result.

## Frequently asked questions

### Should every company disable the legacy controller?

Change it only for a clear reason such as volume, timeout risk, or dimensional processing. A stable close does not need extra complexity.

### Can I switch after a voucher has started?

Do not change processing assumptions mid-run. First confirm the job state and whether entries were posted, then follow an approved recovery plan.

## Related topics

- [Accounting overview](/erpnext/accounting/introduction)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Fiscal Year](/erpnext/fiscal-year)

<!-- page: erpnext/erpnext__letter-head-in-the-report.md -->
---
title: "Letter Head in the Report\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/letter-head-in-the-report"
updated: "2026-03-04"
---


In the reports, Letter Head is fetched from the Company master.

To have the company's Letter Head fetched correctly in the report, please ensure that you have updated the default Letter Head in the Company master.

> Explore > Accounting > Company

[Screenshot on the live page: Letter Head]

In a Company master, if no Letter Head is set as default, then in the reports, Letter Head having Default field checked will be fetched.

[Screenshot on the live page: Letter Head]

If you are managing multiple companies in a single ERPNext account, then ensure that for each Company, default Letter Head is set in the Company master.

After updating Letter Head in the Company master, refresh your ERPNext account, and then check the print format of a report.

<!-- page: erpnext/erpnext__letter-head.md -->
---
title: "Letter Head\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/letter-head"
updated: "2026-03-02"
---


**A Letter Head contains your organization's name, logo, address, etc which appears at the top portion in documents.**

Every company has a default Letter Head. These Letter Head values are generally set as Header and Footer in the documents. In ERPNext, you can capture these details in the Letter Head master.

These details will appear in the Print Format of transactions like Sales Order, Sales Invoice, Salary Slip, Purchase Order, etc. In ERPNext, the Letter Head is only for setting up the top part of the document, other content is pre-formatted and can be configured via [Print Format](/erpnext/print-format) and [Print Headings](/erpnext/print-headings).

To access Letter Head, go to:
> Home > Settings > Letter Head

## 1. How to create a Letter Head
1. Go to the Letter Head list, click on New.
1. Enter a name for the Letter Head. You can create a separate Letter Head for different office locations.
1. Choose whether based on image or HTML.
1. You can enter details in a Letter Head by using:

 * Logo Image: Click on the Attach button to attach an image. Once the image is inserted, HTML for it will be generated automatically.
 * Other information (like Address, tax ID, etc.) that you want to put on your Letter Head.

 [Screenshot on the live page: Print Heading]

 > If you want to make this the default Letter Head, click on "Default Letter Head".

1. After entering values in the Header and Footer section, save the Letter Head.

You can set the Letter Head based on HTML to make changes to it:

[Screenshot on the live page: Letter Head based on]

This is how the Letter Head looks in a document's print.

[Screenshot on the live page: Print Heading]

> Note that Footer will be visible only when the document's print is seen in the PDF. Footer will not be visible in the HTML based print preview.

## 2. Video

<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/cKZHcx1znMc?end=58&amp;rel=0">
</iframe>



### 3. Related Topics
1. [Address Template](/erpnext/address-template)
1. [Terms and Conditions](/erpnext/terms-and-conditions)
1. [Cheque Print Template](/erpnext/cheque-print-template)
1. [Print Headings](/erpnext/print-headings)

<!-- page: erpnext/erpnext__linkedin-settings.md -->
---
title: "LinkedIn Settings | ERPNext Documentation"
description: "Configure the LinkedIn integration settings in ERPNext for publishing supported social posts."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/linkedin-settings"
updated: "2026-07-23"
---

> Note: This integration is deprecated and will be removed in v15. 

LinkedIn related settings like OAuth can be configured here. ERPNext needs access to the API through which the post is shared and achieved using OAuth 2.0 Authentication Protocol.

1. How to set up LinkedIn Developer App

---

You must have LinkedIn Developer App for your company. ERPNext interacts with this App for sharing the post.

### Create LinkedIn Developer App

Create App by link `https://www.linkedin.com/developers` fill all the details and verify it. And that App has the following products.

1. Share on LinkedIn
2. Sign In with LinkedIn
3. Marketing Developer Platform [Screenshot on the live page: LinkedIn Developer App Product]

### Configure Redirect URLs:

1. Goto your LinkedIn Developers App then **Auth** tab.
2. In **OAuth 2.0 settings** section add **Redirect URLs**: `https://{yoursite}/api/method/erpnext.crm.doctype.linkedin_settings.linkedin_settings.callback`
3. Click **Update** to make changes. [Screenshot on the live page: LinkedIn Redirect URL]
4. How to set up LinkedIn Settings

---

To access LinkedIn Settings, go to:

> Home > CRM > Settings > LinkedIn Settings

Current availability

This integration is deprecated. Confirm support in your ERPNext version and the current LinkedIn API requirements before configuring new credentials.



### Company ID

You get the Company ID from your LinkedIn Company URL. 

[Screenshot on the live page: LinkedIn Company ID]



### Consumer Key and Consumer Secret

You get **Consumer Key** and **Consumer Secret** from your LinkedIn Developer account go to:

> `https://www.linkedin.com/developers/` > My Apps > `{Your App}` > Auth

[Screenshot on the live page: LinkedIn Client]



Once you save the doc by filling **Company ID**, **Consumer Key**, and **Consumer Secret** it will redirect to LinkedIn's sign-in page by providing valid LinkedIn credentials and clicking Allow, the member approves your application's request to access their member data and interact with LinkedIn on their behalf. 

[Screenshot on the live page: Authorize LinkedIn]

<!-- page: erpnext/erpnext__linking-emails-to-document.md -->
---
title: "Linking Emails to Documents"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/linking-emails-to-document"
updated: "2026-03-02"
---


> Introduced in v12
> 
> 

**An email can be linked to multiple documents in ERPNext.**

This can be done in the following two ways:

* Email Aggregation in Contact, Customer, Supplier.
* Automatic Email Linking.

1. Email Aggregation for Customer and Supplier
----------------------------------------------

Email Aggregation takes place in Contact, Customer, and Supplier. All the Emails sent or received from a Contact can be viewed in that Contact's Timeline and as well as linked Customer's or Supplier's Timeline. To enable Email Aggregation, do the following:

1. In a Contact, add Links for the Customer or Supplier respectively.

[Screenshot on the live page: Add Customer/Supplier in Contact]
2. Now when an Email is sent to or received from the Contact associated with Customer or Supplier, that email is linked to the Customer or Supplier mentioned in the Links section of the Contact.

[Screenshot on the live page: With Filters]

2. Automatic Email Linking to a Document
----------------------------------------

Automatic Email Linking links an Email to the Document specified in the unique Email Address generated by the system for a document. If an Email is sent or received using the unique Email Address, the system will link that Email to the Document.

1. Enable Automatic Email Linking in Email Account. This feature can be used only with one Email Account at a time.

[Screenshot on the live page: Add Customer/Supplier in Contact]
2. Once this feature has been enabled, you will see a unique Email ID generated using the Email ID mentioned in the Email Account.
3. Now you can copy the Email ID by clicking on it and you can send or receive Emails using the unique Email ID. If an Email contains this unique Email ID either in the Recipients or Cc section, the system will link that Email to the specified Document.

[Screenshot on the live page: Add Customer/Supplier in Contact]


> Note: Email linking with BCC is not supported. You have to add unique email as receipient in TO or CC.
> 
> 

### 3. Related Topics

1. [Auto Email Reports](/erpnext/auto-email-reports)
2. [Sending Email from any Document](/erpnext/sending-email)
3. [Document Follow](/erpnext/document-follow)

<!-- page: erpnext/erpnext__local_overrides.md -->
---
title: "Sales and Payment Transactions\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/local_overrides"
updated: "2026-07-02"
---


In order to be compliant with the latest finance law applicable to POS software, ERPNext automatically registers all sales and payment transactions in a chained log.

If your country is set to "France", the deletion of sales and payment transactions will also not be permitted, even if the appropriate permissions are given to the user.

Please note that ERPNext is not yet fully compliant with the 2016 Finance Law.

# Chained log Report

A dedicated report called "Transaction Log Report" is available to verify that the logged chain has not been broken.

If the status of the column "Chain Integrity" is "True", the chain has not been broken.
It means that you can consult the full chain of events that occurred in your system.

If the status of the column "Chain Integrity" is "False", it means that there is a discrepancy in the chain.
In this case, the previous row has been removed or altered in the database. It is a probable effect of a fraudulent behavior.

<!-- page: erpnext/erpnext__lower-deduction-certificate.md -->
---
title: "Lower Deduction Certificate\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/lower-deduction-certificate"
updated: "2026-02-27"
---


According to the tax withholding category, a person responsible for making payments is required to deduct tax at source at prescribed rates. Instead of receiving tax on your income from you at a later date, the government wants the payers to deduct tax beforehand and deposit it with the government. However this scheme of deducting tax at source may cause issues to a few taxpayers who may not have taxable income for that fiscal year.

Therefore, for such taxpayers, the government provides an option to obtain a certificate confirming to either a lower rate or NIL rate of TDS compared to the rate specified in the tax withholding category.

## 1. Prerequisites
Before creating and using a Lower Deduction Certificate, it is advised to create and study the following first:

1. [Supplier](/erpnext/supplier)
1. [Tax Withholding Category](/erpnext/tax-withholding-category)

## 2. How to create a Lower Deduction Certificate
1. Go to the Lower Deduction Certificate list and click on New.
1. Enter the Certificate No.
1. Select the Section Code.
1. Enter the [Fiscal Year](/erpnext/fiscal-year).
1. Select the Supplier having a valid PAN number. PAN number will be auto fetched on the selection of Supplier.
1. Enter Valid From and Valid Up To dates.
1. Enter rate of TDS as per the certificate and the certificate limit.
1. Click on Save.

 [Screenshot on the live page: Lower Deduction Certificate]

## 3. Using Lower Deduction Certificate

### 3.1 Use in Purchase Invoice

In the following example, we have selected TDS category as 'TDS - 194D - Individual' which has a rate of 5%.

 [Screenshot on the live page: Tax Withholding Category]

1. Set the Tax Withholding Category for the Supplier in the supplier master. Then upon selecting that Supplier, a checkbox will become visible in the Purchase Invoice to select whether to apply tax or not and the TDS category will be auto-fetched.

 [Screenshot on the live page: Supplier With Tax Withholding Category]

1. Let's create an invoice for 20,000. Saving the invoice automatically calculates tax and appends it in the Purchase Taxes and Charges table. Although the tax category assigned to the supplier has a tax rate of 5%, the prevailing tax rate is 1% which is mentioned in the Lower Deduction Certificate.

 [Screenshot on the live page: Lower TDS in Purchase Invoice]

### 4. Related Topics
1. [Tax Withholding Category](/erpnext/tax-withholding-category)

<!-- page: erpnext/erpnext__loyalty-points-redemption-in-pos.md -->
---
title: "Loyalty points redemption in POS"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/loyalty-points-redemption-in-pos"
updated: "2026-03-02"
---

In ERPNext POS module, the invoices are auto generated. You can set your complete POS system right with the following configuration steps:   
* Create a Loyalty program in the doctype: You can set Single Tier or a Multiple Tier Program based on the slabs existing in the amount of Purchase that is done in ERPNext.

[Screenshot on the live page]* Once the loyalty program is set, you can create a Customer and link the Loyalty program to it.

[Screenshot on the live page]Once this Customer is linked to the Loyalty program, you can now setup your POS profile if it is not set yet:  
[Screenshot on the live page]  
Now, you can go to POS transaction:* Select Customer
* Add items
* Pay
* Check the field --> **Redeem Loyalty Points**

[Screenshot on the live page]
