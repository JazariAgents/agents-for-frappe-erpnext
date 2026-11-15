<!-- Frappe documentation: erpnext, part 8 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__automate_lead_capturing.md -->
---
title: "Automate Lead Creation | ERPNext Documentation"
description: "Learn how ERPNext can create Leads from email, Web Forms, ecommerce activity, and data imports."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/automate_lead_capturing"
updated: "2026-07-23"
---

Leads come from many different sources. It is important that all leads are recorded, assigned to sales executives and followed up.

## Create Leads From Emails

You may have an email address like '[sales@yourcompany.com](mailto:sales@yourcompany.com)' which is probably displayed on your website. People may send emails asking information about your products and services. You can enable [Email Account](/erpnext/email-account) to pull these emails and create a lead for each email.

## Create Leads From Webforms

You can also map the Lead form to a [Web Form](/erpnext/web-form) and publish it on your website. When visitors of your website fill the form, it will be automatically added as a Lead.

## Create Leads From Incomplete Orders in E-Commerce Module

You can publish an e-commerce website and allow users to place an order for your products. If a user selects items but doesn't complete the process you can pursue that user as a lead.

## Create Leads By Importing Spreadsheet

If you have a spreadsheet with details of the leads, you can use the [Data Import](/erpnext/data-import) feature to import the leads.

<!-- page: erpnext/erpnext__automating-issue-assignments-to-support-team-in-erpnext.md -->
---
title: "Automating Issue Assignments in ERPNext"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/automating-issue-assignments-to-support-team-in-erpnext"
updated: "2026-02-27"
---

Modern support automation tools demonstrably improve customer service. Automating the assignment of support issues ensure that every issue ticket has been assigned a product expert and the customer seeks resolution to their queries faster. Assignment Rule has been introduced in v12 and here's how you can automate your support team's troubles away.  
First, we need to setup an email account that appends the incoming emails received there into the "Issue" DocType of ERPNext.**1) Create an Email Account:**You need to update email domain and setup your support email address in ERPNext's Email Account. To learn about email setup, please check out [this link](https://www.youtube.com/watch?v=ChsFbIuG06g&t=122s)  
![](/files/NPp14kS.png)  
**2) Append to Issue:**The checkbox, "Enable Incoming" has to be selected to allow emails sent on this email address to be received here. We need to capture them in a DocType, which is mentioned under "Appends To". In this case, we want to append all incoming emails to Issue  
![](/files/STAm8ko.png)  
This is a one-time configuration and you won't have to worry about it unless you require to change the password of that email address via third party apps. The Issue List will get populated with the emails that are sent here. With the use of Assignment Rules, we can organise the customer support team's schedule and ensure timely resolution for all open support tickets.  
**3) Setting an Assignment Rule:**  
![](/files/5q4HvOT.gif)  
**4) Based on the rule defined in step (3), the assignments will be done automatically**These are done as in when an Issue is created or updated. Check out below GIF to see automation in action when an issue ticket's status is *updated*:  
![](/files/Qb0kAzo.gif)  
Note: If needed, the rule can also be disabled/updated:  
![](/files/PZbCDuu.png)  
Similarly, you can automate the Sales process in ERPNext for assigning leads to your Sales team and ensure more conversion rates!! Thanks for reading this article! If you need further assistance with this, please reach our community [here](https://discuss.erpnext.com/)

<!-- page: erpnext/erpnext__automation.md -->
---
title: "Automation "
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/automation"
updated: "2026-03-02"
---

Automation in ERPNext is a game-changer, especially when it comes to streamlining complex processes like milestone tracking, task assignments, repetitive tasks, and event monitoring. These automation features in ERPNext not only save time and effort but also enhance overall efficiency and productivity across the organisation.

* [Assignment Rule](/erpnext/user/manual/en/assignment-rule)
* [Auto Repeat](/erpnext/user/manual/en/auto-repeat)
* [Milestone Tracking](/erpnext/user/manual/en/milestone-tracker)

<!-- page: erpnext/erpnext__awesomebar-global-search.md -->
---
title: "Awesomebar Global Search"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/awesomebar-global-search"
updated: "2026-08-14"
---

The Awesomebar is the fastest way to open a DocType, report, page, workspace, or new record from anywhere in Desk. It reduces menu navigation when you already know what you need.



For example, a billing user can type **Sales Invoice** and choose the list, report, or new-document action directly from the same search.

## Open and use the Awesomebar

1. Select the Search field at the top of Desk, or use the keyboard shortcut shown beside it.
2. Type a DocType, report, page, or action.
3. Use the arrow keys to move through results and press Enter to open the selected result.

![ERPNext Awesomebar showing list, report, and new-document results for Sales Invoice](https://novacompanies.m.frappe.cloud/files/setup-20260814-awesomebar-search.png)



## Understand the results


| Result            | Use it to                                         |
| ----------------- | ------------------------------------------------- |
| List              | Open all records of a DocType.                    |
| New               | Create a new record directly.                     |
| Report            | Open a matching report.                           |
| Page or Workspace | Navigate to a feature or module.                  |
| Search for        | Run a broader global search for matching records. |


## Use global record search

When the direct results do not contain the record you need, choose the broader search action. Search availability depends on the DocType, indexed content, and your permissions. A user will not receive results for records they cannot access.

## Troubleshooting

### A DocType or report is missing

Confirm that the user has the required role and permission. Also check whether the module or workspace is hidden.

### The expected record is not found

Try a distinctive part of its name or identifier. Open the DocType list and apply filters when the record is not included in global search.

## Frequently asked questions

### Does Awesomebar search bypass permissions?

Results respect the current user’s access.

### Can I create a document from the search?

Y

es. Select the **New** result when it is available and you have create permission.

## Related topics

- [Desk](/erpnext/desk)
- [Adding Users](/erpnext/adding-users)
- [Role Based Permissions](/erpnext/role-based-permissions)
- [Show or Hide Modules](/erpnext/show-hide-modules)

<!-- page: erpnext/erpnext__aws_s3.md -->
---
title: "Upload Backups to Amazon S3"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/aws_s3"
updated: "2026-04-15"
---

> Note: If you are Frappe Cloud user, onsite and offsite backups are automatically created for you: [https://frappecloud.com/docs/sites/backups](https://frappecloud.com/docs/sites/backups)

## Prerequisites

- [Email Account](/erpnext/email-account)

To receive emails for failed and successful backups, please create an **Email Account** first.

## Create S3 bucket and set up access

1. Create a new s3 bucket.

In the bucket settings, enable "Block all public access" to keep your data private. Feel free to enable encryption, versioning or object lock as per your requirements (please refer to [Amazon's documentation](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)).  
2. Open Identity and Access Management (IAM).  
3. Create a new policy for the Service "S3", allowing the Actions "ListBucket" and "PutObject".

![Screenshot of "Create Policy" in AWS](/files/s3-backup-policy.png)



Or, using the JSON editor:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::*/*",
                "arn:aws:s3:::YOUR TARGET BUCKET"
            ],
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": "YOUR SERVER IP"
                }
            }
        }
    ]
}
  

```

4. Create a new user for programmatic access.

![Screenshot of "Add User" in AWS](/files/s3_backup_add_user.png)

5. Attach the policy you created to the new user.
6. Copy the user's access key and secret.

To automatically delete old backups or move them to a cheaper storage class, have a look at [lifecycle management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html).



## Create a Hetzner Bucket with Minio

> Capital letters are variables you can choose freely. In this example, we use region nbg1 (Nuremburg).

1. In the Hetzner Console at `https://console.hetzner.com/projects/YOUR_PROJECT/security/s3-credentials` , create some S3 access credentials: key and secret.
2. [Install Minio](https://github.com/minio/minio)
3. Configure Minio to access your Hetzner buckets: `mc alias set MY_ALIAS https://nbg1.your-objectstorage.com YOUR_S3_KEY YOUR_S3_SECRET`
4. Create a bucket with Object Locking enabled: `mc mb MY_ALIAS/BUCKET_NAME --with-lock --region nbg1` . This ensures you cannot accidentally delete your backups.
5. Set Object Locking period to 90 days: `mc retention set GOVERNANCE 90d --default MY_ALIAS/BUCKET_NAME`
6. Check if everything is configured correctly: `mc retention info --json --default MY_ALIAS/BUCKET_NAME`
7. Enter configuration in **S3 Backup Settings**:
  1. *Endpoint URL*: [https://nbg1.your-objectstorage.com/](https://nbg1.your-objectstorage.com/)
  2. *Bucket Name:* `BUCKET_NAME`
  3. *Access Key ID*: `YOUR_S3_KEY`
  4. *Access Key Secret*: `YOUR_S3_SECRET`

## Set up ERPNext

- Open **S3 Backup Settings**.
- Check "Enable Automatic Backup".
- Paste the access key and secret from AWS.
- Set an email address to receive a notification when a backup fails. If you would like an email for successful backups as well, enable "Send Email for Successful Backup".
- Specify the name of the bucket that you created in step 1.
- Choose how often you want to take and upload backups. This can range from monthly to daily. If you only want to take manual backups, set the frequency to "None".

![S3 Backup Settings in ERPNext](/files/s3_backup_settings.png)

## Restore deleted files from versioned bucket

- List all file versions: `mc ls -r --versions MY_ALIAS/BUCKET_NAME/` 
- Download a specific version: `mc get --vid TARGET_VERSION_ID MY_ALIAS/BUCKET_NAME/20260415_162402/20260415_162402-company_frappe_cloud-database.sql.gz ~/Downloads`

<!-- page: erpnext/erpnext__balance-in-temporary-account.md -->
---
title: "Balance in Temporary Account"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/balance-in-temporary-account"
updated: "2026-07-31"
---

**Question:**

We used Temporary Opening Account for updating opening balance. After having update balance in all the Balance Sheet account, there is still some balance in Temporary Account? What is the cause of this balance, and how to make balance in this account to zero?

 

**Answer:**

When updating an opening balances in ERPNext, you have to first ensure that Balance Sheet in the previous system is tallying (Asset = Liability).

Then you start updating the opening balances for above statement, using Temporary Opening as an account to balance the entry. In the end, when opening is updated for all Asset and Liability accounts, the Temporary account's balance becomes zero automatically.

If you still have balance in the Temporary Account, it could be for one of the two (or both) the reasons.

1. The Balance Sheet followed for updating opening balance was not closed properly and it's Asset and Liability value was not tallying.
2. When updated opening balance in ERPNext, the Temporary Opening Account was not used consistently.

 

Kindly review the above points as they could be the cause of balance left in the Temporary Opening Account.

<!-- page: erpnext/erpnext__balance-sheet.md -->
---
title: "Balance Sheet"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/balance-sheet"
updated: "2026-08-14"
---

Nova Industries ends 2026 with $293,745 of assets, $184,305 of liabilities, and $109,440 of provisional profit. The owner wants to know what the business controls, what it owes, and why its bank balance is negative even though the company is profitable.



The Balance Sheet shows financial position at a point in time. Assets describe resources controlled by the business. Liabilities describe obligations. Equity and current profit explain the owners' residual interest. Use the [Profit and Loss Report](/erpnext/profit-and-loss-report) to explain how profit was earned during a period and [Cash Flow](/erpnext/cash-flow-report) to explain cash movement.

## Before you begin

Submit all relevant [Sales Invoices](/erpnext/sales-invoice), [Purchase Invoices](/erpnext/purchase-invoice), payments, stock transactions, assets, loans, payroll, depreciation, taxes, and approved [Journal Entries](/erpnext/journal-entry). Confirm that accounts have the correct Asset, Liability, or Equity root in the [Chart of Accounts](/erpnext/chart-of-accounts).

## Run the Balance Sheet

1. Open **Accounting** and select **Balance Sheet**.
2. Select **Nova Industries**.
3. Choose Fiscal Year or Date Range and the comparison periodicity.
4. Apply Finance Book, Cost Center, Project, Department, or another [Accounting Dimension](/erpnext/accounting-dimensions) only when required.
5. Refresh and wait for totals, chart, and account rows to load.

![Loaded Nova Industries Balance Sheet with assets liabilities and provisional profit](https://novacompanies.m.frappe.cloud/files/docs-20260814-nova-industries-balance-sheet-loaded.png)

## Interpret the Nova Industries result


| Section            | Value    | Meaning                                                           |
| ------------------ | -------- | ----------------------------------------------------------------- |
| Total Assets       | $293,745 | Resources controlled at the reporting date.                       |
| Total Liabilities  | $184,305 | Amounts owed to suppliers and other parties.                      |
| Equity             | $0       | Posted equity balances visible in the selected scope.             |
| Provisional Profit | $109,440 | Current-period profit not yet transferred through period closing. |


Assets equal liabilities plus equity and provisional profit: $293,745 equals $184,305 plus $109,440. This proves the statement balances mathematically. It does not prove that every account is correctly classified.

## Understand the account groups

Current Assets include balances expected to turn into cash or be used soon, such as receivables, bank, cash, and inventory. Fixed Assets support longer-term operations. Current Liabilities include obligations such as supplier payables and taxes. Longer-term loans belong in non-current liabilities. Equity contains owner capital, reserves, retained results, and period-closing transfers according to the organisation's account design.



Nova shows $316,212 in Accounts Receivable and a negative $118,104 Bank Accounts balance. The large receivable explains why the company can own net assets while still facing immediate cash pressure. Open [Accounts Receivable](/erpnext/accounts-receivable) to identify customers to collect from.

## Drill into a balance

Select an account amount to open its [General Ledger](/erpnext/general-ledger) entries. Keep Company, date, Finance Book, currency, and dimensions aligned with the Balance Sheet before comparing values.

![General Ledger drill-down opened from a Balance Sheet account](https://novacompanies.m.frappe.cloud/files/docs-20260814-nova-industries-balance-sheet-loaded-drilldown.png)

## Important filters


| Filter                        | Effect                                                                                             |
| ----------------------------- | -------------------------------------------------------------------------------------------------- |
| Reporting date or fiscal year | Sets the point in time and comparison columns.                                                     |
| Accumulated Values            | Shows balances accumulated through each displayed period.                                          |
| Finance Book                  | Restricts entries to a selected accounting book.                                                   |
| Dimensions                    | Shows the financial position for a selected operational segment when entries carry that dimension. |
| Currency                      | Changes presentation without changing ledger postings.                                             |
| Report Template               | Uses a configured [Financial Report Template](/erpnext/financial-report-template).                 |


## Troubleshooting

### The Balance Sheet does not balance

Check provisional profit, opening balances, account roots, period-closing entries, and identical report filters. Trace the difference through Trial Balance and General Ledger.

### An account appears in the wrong section

Review its Root Type and Report Type in Chart of Accounts. Correcting an account can affect reporting and should follow your accounting controls.

### A segment report looks incomplete

Transactions without the selected dimension are excluded. Verify dimension values on source entries before treating the filtered statement as a full-company balance sheet.

## Frequently asked questions

### Why is current profit shown separately from equity?

Profit remains provisional until the period is closed and transferred according to the configured closing process.

### Can a company be profitable but have a negative bank balance?

Profit includes income recognized before collection. Receivables, inventory, debt repayment, and other timing differences can consume cash.

### Does the Balance Sheet show market value?

The statement shows accounting balances produced by recorded transactions and valuation rules, not an automatic market valuation of the business.

## Related topics

- [Accounting Reports](/erpnext/accounting-reports)
- [Profit and Loss Report](/erpnext/profit-and-loss-report)
- [Cash Flow](/erpnext/cash-flow-report)
- [Trial Balance](/erpnext/trial-balance)
- [General Ledger](/erpnext/general-ledger)
- [Period Closing Voucher](/erpnext/period-closing-voucher)

<!-- page: erpnext/erpnext__bank-account.md -->
---
title: "Bank Account | ERPNext Documentation"
description: "Create ERPNext Company and party Bank Accounts and connect them to the correct bank ledger."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bank-account"
updated: "2026-07-31"
---

A **Bank Account** represents a real bank or card account held by a Company, Customer, or Supplier. For a Company account, it connects the Bank master to a Bank-type General Ledger account used by payments, statement imports, and reconciliation.

## Before you begin

Create the [Bank](/erpnext/bank) and, for a Company account, a ledger under Bank Accounts in the [Chart of Accounts](/erpnext/chart-of-accounts). Set the ledger's **Account Type** to **Bank** and use the correct Company and currency.

Do not confuse these records:

- the **Bank** is the financial institution;
- the **Bank Account** stores the real account identity and ownership;
- the **Account** is the General Ledger where the Company balance is posted.

## Create a Bank Account

1. Go to **Accounting &gt; Banking &gt; Bank Account**.
2. Select **Add Bank Account**.

![Bank Account list with Add Bank Account highlighted](https://novacompanies.m.frappe.cloud/files/banking-04-bank-account-list.png)

3. Enter an **Account Name** that users can identify, such as `Operating Account` or `Payroll Account`.
4. Select the **Bank**.
5. Select **Is Company Account** when the account belongs to one of your Companies.

![Bank Account ownership and Bank fields](https://novacompanies.m.frappe.cloud/files/banking-05-bank-account-ownership.png)

6. For a Company account, select the **Company** and **Company Account** ledger.
7. Select **Is Default Account** only when this should be the default Bank Account for the Company.

![Company ledger and default Bank Account setting](https://novacompanies.m.frappe.cloud/files/banking-06-bank-account-ledger.png)

8. Enter the account number, routing or branch code, IBAN when applicable, and other non-secret identifiers.
9. Save the Bank Account.

## Create a Customer or Supplier Bank Account

Leave **Is Company Account** clear, then select the **Party Type** and **Party**. Use this for payment instructions, refunds, or other workflows that need the counterparty's banking details.

A party Bank Account does not become a Company ledger and should not be selected as the account that posts Company cash movement.

## Important fields and what they mean


| Field                | What it controls                                                                                                     |
| -------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Account Name         | Human-readable identifier for the real account.                                                                      |
| Bank                 | Financial institution that holds the account.                                                                        |
| Is Company Account   | Shows Company and ledger fields and marks the account as belonging to your organization.                             |
| Company              | Company that owns the account. It must match the linked General Ledger account.                                      |
| Company Account      | Bank-type General Ledger account used for accounting entries.                                                        |
| Is Default Account   | Makes the Bank Account the default where that workflow uses a Company default. Maintain only one intended default.   |
| Is Credit Card       | Identifies a credit-card account where supported by the workflow.                                                    |
| Party Type and Party | Owner of a Customer, Supplier, Employee, or other party Bank Account.                                                |
| IBAN                 | International account identifier used in participating countries. Leave it empty when the country does not use IBAN. |
| Branch Code          | Routing, sort, transit, or other branch identifier used in your banking system.                                      |
| Bank Account No      | Account number supplied by the institution. Avoid exposing it in public screenshots or broad exports.                |
| Integration ID       | Identifier used by a supported bank integration.                                                                     |
| Disabled             | Prevents the account from being selected for new activity while preserving history.                                  |


## Use the Bank Account

The Company Bank Account is used by:

- [Payment Entry](/erpnext/payment-entry) and payment requests;
- statement synchronization or import;
- [Bank Transaction](/erpnext/bank-transaction) records;
- [Bank Reconciliation](/erpnext/bank-reconciliation);
- [Bank Guarantee](/erpnext/bank-guarantee);
- other banking integrations and reports.

Configure [Mode of Payment](/erpnext/mode-of-payment) Company defaults so cash, check, card, and wire payments use the intended ledger.

## Data protection

Limit access to full bank account numbers and integration identifiers. Documentation and support screenshots should use fictional or masked numbers. Do not store online-banking passwords in the account number, Statement PDF Password, comments, or attachments.

Use **Statement PDF Password** only for the supported encrypted-statement workflow and restrict who can read or modify it.

## Troubleshooting

### The Company Account cannot be selected

Confirm that it belongs to the selected Company, is not a group, is enabled, uses the correct currency, and has **Account Type: Bank**.

### Payments use a different ledger

Check the Mode of Payment Company default, the selected Bank Account, the Company's default Bank Account, and any account filled directly on the transaction.

### Bank Transactions are assigned to the wrong Company

Review the Bank Account ownership and linked ledger. Correct the master before importing more statement lines.

### The IBAN is rejected

Enter an officially valid IBAN without inventing a country prefix. Leave the field empty for accounts in countries that do not use IBAN.

### The account should no longer be used

Disable it instead of deleting it. Historical payments, Bank Transactions, and reconciliation records may still reference it.

## Frequently asked questions

### Can one Bank Account link to several ledgers?

It cannot. Create a separate Bank Account for each real account and Company ledger relationship.

### Can two Companies use accounts at the same Bank?

They can. Use one Bank master and separate Company Bank Accounts and ledgers for each Company.

### Is a credit card a bank or liability account?

The accounting ledger classification depends on your Chart of Accounts and local accounting policy. Mark the Bank Account as a credit card where appropriate and confirm the linked ledger treatment with finance.

## Related topics

- [Bank](/erpnext/bank)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Mode of Payment](/erpnext/mode-of-payment)
- [Payment Entry](/erpnext/payment-entry)
- [Bank Transaction](/erpnext/bank-transaction)
- [Bank Reconciliation](/erpnext/bank-reconciliation)

<!-- page: erpnext/erpnext__bank-accounts-and-modes-of-payment.md -->
---
title: "Bank Accounts and Modes of Payment | ERPNext Documentation"
description: "Configure banks, company bank accounts, ledger accounts, and Modes of Payment in ERPNext for accurate payment processing and reconciliation."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bank-accounts-and-modes-of-payment"
updated: "2026-08-14"
---

ERPNext needs two related pieces of information to record money correctly: where the money moved and how it moved. A Bank Account represents the real account held with a bank, while a Mode of Payment describes the channel, such as bank transfer, card, cash, or cheque.



Nova Industries may receive a card payment into one clearing account, a wire transfer into its operating bank, and cash at a showroom counter. Mapping each payment method to the right ledger account reduces manual selection and makes bank reconciliation easier later.



This page explains the relationship between Bank, Bank Account, ledger account, and Mode of Payment, then shows how to configure defaults that lead users to the correct account without hiding the accounting trail.

## Understand the records


| Record          | Purpose                                                                              |
| --------------- | ------------------------------------------------------------------------------------ |
| Bank            | Identifies the financial institution                                                 |
| Bank Account    | Stores an account held by a company, Customer, or Supplier                           |
| Account         | The Bank-type ledger in the Chart of Accounts                                        |
| Mode of Payment | Describes how money is paid or received, such as Cash, Check, Card, or Wire Transfer |


## Create a Bank

Go to **Home &gt; Accounting &gt; Bank Statement &gt; Bank** and add the institution.

![Bank master](/files/bank-master.webp)

Add integration details only when you use a supported bank integration.

## Create the company bank account

1. Create a ledger account under Bank Accounts in the company’s [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts). Set **Account Type** to **Bank**.
2. Open **Bank Account** and click **Add Bank Account**.
3. Select the Bank and enter the account name or number.
4. Select **Company** as the party type when it is the company’s own account.
5. Link the corresponding ledger account.
6. Mark it as the company default only when appropriate.

Store only the information required for operations and reconciliation. Restrict access to sensitive bank details.

## Configure Modes of Payment

Open **Mode of Payment**, select the type, and add a default account for each company.

![Mode of Payment default account](/files/mode-of-payment-defaults.webp)

For example, Cash should normally use a Cash-type ledger. A wire transfer or card settlement should use the relevant Bank or clearing account.

## How ERPNext selects the payment account

ERPNext first uses a transaction-specific value when supplied. It can otherwise fetch a company default or the account mapped to the selected Mode of Payment. Always verify the paid-from and paid-to accounts before submitting a Payment Entry.

## Bank statements and reconciliation

Use [Bank Transaction](https://docs.frappe.io/erpnext/bank-transaction) records to import or synchronize statement lines. Then use [Bank Reconciliation](https://docs.frappe.io/erpnext/bank-reconciliation) to match them with Payment Entries and Journal Entries.

## Troubleshooting

**A bank ledger is not selectable**

Confirm it belongs to the same company, is not a group, is enabled, and has Account Type Bank.

**A Mode of Payment selects the wrong account**

Review its company-wise default accounts and the transaction’s company.

## Related topics

- [Payment Entry](https://docs.frappe.io/erpnext/payment-entry)
- [Bank Reconciliation](https://docs.frappe.io/erpnext/bank-reconciliation)
- [Bank Statement Import](https://docs.frappe.io/erpnext/bank-statement-import)
- [Company accounting defaults](https://docs.frappe.io/erpnext/company-accounting-defaults)

<!-- page: erpnext/erpnext__bank-guarantee.md -->
---
title: "Bank Guarantee | ERPNext Documentation"
description: "Track guarantees received or provided, their validity, beneficiary, margin, charges, and references in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bank-guarantee"
updated: "2026-08-14"
---

Northstar Retail, a customer of Nova Industries, places a large electronics order but wants protection if Nova Industries does not meet the contract. A bank may guarantee Nova Industries' obligation, giving the customer confidence without requiring an immediate payment between the two companies.



A Bank Guarantee records the bank's commitment, its beneficiary, amount, validity, and linked transaction. ERPNext can track guarantees received from customers and guarantees issued on your company's behalf.



Use it to monitor contractual security and expiry dates. The record is operational evidence and does not automatically post accounting entries.



## Before you begin

Collect the guarantee document and confirm:

- whether the guarantee is **Receiving** or **Providing**;
- the underlying Sales Order, Purchase Order, Project, or contract;
- beneficiary and applicant details;
- guaranteed amount, start date, expiry, and claim terms;
- issuing Bank and Bank Account;
- margin money, charges, fixed deposit, and related accounting entries.

Create the [Bank](/erpnext/bank) and [Bank Account](/erpnext/bank-account) first. Confirm with finance how margin money and charges will be recorded through a [Payment Entry](/erpnext/payment-entry) or [Journal Entry](/erpnext/journal-entry).

## Create a Bank Guarantee

1. Go to **Accounting &gt; Banking &gt; Bank Guarantee**.
2. Select **Add Bank Guarantee**.

![Bank Guarantee list with Add Bank Guarantee highlighted](https://novacompanies.m.frappe.cloud/files/banking-07-bank-guarantee-list.png)

3. Choose the **Bank Guarantee Type**:
  - **Receiving** when another party provides the guarantee for your benefit;
  - **Providing** when your Bank issues it for a Customer, Supplier, or other beneficiary.
4. Enter the amount, start date, validity, and end date. Verify the expiry against the issued document.

![Bank Guarantee type, amount, and validity fields](https://novacompanies.m.frappe.cloud/files/banking-08-bank-guarantee-purpose.png)

5. Select the Bank, Bank Account, and related General Ledger account when applicable.

![Bank and Bank Account on the guarantee](https://novacompanies.m.frappe.cloud/files/banking-09-bank-guarantee-bank-details.png)

6. Enter the Bank's guarantee number and the beneficiary name exactly as shown on the issued instrument.

![Guarantee number and beneficiary](https://novacompanies.m.frappe.cloud/files/banking-09b-bank-guarantee-reference.png)

7. Add the reference document, Customer or Supplier, and Project when they identify the underlying obligation.
8. Record margin money, charges, fixed deposit number, clauses, and conditions.
9. Attach the issued guarantee and save the record.

## Important fields and what they mean


| Field                            | What it controls                                                                                                       |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Bank Guarantee Type              | Distinguishes guarantees received from guarantees provided.                                                            |
| Reference Document Type and Name | Links the guarantee to a Sales Order, Purchase Order, or other supported record.                                       |
| Customer or Supplier             | Party connected to the selected sales or purchase reference.                                                           |
| Project                          | Project or contract supported by the guarantee.                                                                        |
| Amount                           | Maximum guaranteed value. Use the currency and amount shown in the instrument.                                         |
| Start Date                       | Date from which the guarantee is effective.                                                                            |
| Validity in Days                 | Duration used to derive or check the end date.                                                                         |
| End Date                         | Expiry date. Monitor this date before renewal, release, or claim deadlines.                                            |
| Bank and Bank Account            | Institution and account through which the guarantee is issued or tracked.                                              |
| Bank Guarantee Number            | Unique reference assigned by the Bank.                                                                                 |
| Name of Beneficiary              | Party entitled to claim under the guarantee.                                                                           |
| Margin Money                     | Cash or deposit blocked as security. Record its accounting separately.                                                 |
| Charges Incurred                 | Bank fees associated with issuing or maintaining the guarantee.                                                        |
| Clauses and Conditions           | Operational summary of claim, expiry, renewal, and release terms. The attachment remains the authoritative instrument. |


## Receiving versus providing

When **Receiving**, monitor whether the counterparty maintains the guarantee through the required contractual period. Store the original or verified copy and set reminders before expiry.

When **Providing**, monitor the exposure, margin, fees, beneficiary, release documentation, and whether the guarantee should be renewed. A provided guarantee may create a contingent liability even when no payable is posted automatically.

## Accounting and controls

The Bank Guarantee record does not automatically debit margin money or expense charges. Record those movements using the correct accounting voucher:

- transfer blocked cash to a margin or deposit account;
- expense Bank charges to the approved account and Cost Center;
- release margin money when the Bank confirms release;
- recognize a claim only through the approved legal and accounting process.

Reconcile the guarantee register with Bank confirmations and the General Ledger. Restrict access to attachments containing account details, signatures, or confidential contract terms.

## Review and next steps

Review guarantees by expiry date at least monthly. For each guarantee, determine whether to:

- allow it to expire;
- obtain formal release;
- renew or extend it;
- reduce the amount;
- replace it with another instrument;
- prepare for or respond to a claim.

Use assignment, comments, or a workflow to identify the responsible owner. An expiry date without an owner or reminder is easy to miss.

## Troubleshooting

### The Customer or Supplier field does not appear

Select the relevant reference document type first. Customer is shown for supported sales references and Supplier for supported purchase references.

### End date does not match the instrument

Check the start date, validity calculation, inclusivity of dates, and any wording that specifies a fixed calendar expiry. Use the issued instrument as the authoritative source.

### Margin money is missing from the General Ledger

The Bank Guarantee is not an accounting voucher. Create the appropriate Payment Entry or Journal Entry and link it through references or attachments.

### The guarantee has expired but remains active operationally

Obtain the renewal or extension from the Bank, update the tracked dates with supporting evidence, and retain the prior instrument for the audit trail.

## Frequently asked questions

### Does a Bank Guarantee reduce the Bank balance automatically?

It does not. Record margin, deposit, and fee movements through accounting transactions.

### Can one guarantee cover several orders?

It may contractually, but the ERPNext reference field points to one document. Explain the broader coverage in conditions and attachments, or use a Project as the common reference.

### Should the guarantee document be attached?

It should, subject to your access and confidentiality policy. The structured fields support tracking, while the issued document contains the legal terms.

## Related topics

- [Bank](/erpnext/bank)
- [Bank Account](/erpnext/bank-account)
- [Payment Entry](/erpnext/payment-entry)
- [Journal Entry](/erpnext/journal-entry)
- [Sales Order](/erpnext/sales-order)
- [Purchase Order](/erpnext/purchase-order)

<!-- page: erpnext/erpnext__bank-reconciliation.md -->
---
title: "Bank Reconciliation | ERPNext Documentation"
description: "Match ERPNext accounting vouchers with bank statement transactions and balances."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/bank-reconciliation"
updated: "2026-08-01"
---

Bank Reconciliation compares the bank statement with entries in ERPNext. Match existing vouchers first, create missing accounting entries only when necessary, and finish by explaining every difference between the statement and ledger balances.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Bank Reconciliation

1. Select the Company Bank Account and statement date range.
2. Import or synchronize Bank Transactions.
3. Match each statement line with the correct Payment Entry, Journal Entry, or other supported voucher.
4. Create a missing voucher only after checking that it does not already exist.
5. Record bank fees, interest, and timing differences explicitly.
6. Confirm that the closing balance agrees with the bank statement.

![Bank Reconciliation in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-12-bank-reconciliation.png)

![Bank Reconciliation details](https://novacompanies.m.frappe.cloud/files/payments-13-bank-transactions-for-reconciliation.png)

## Important fields and what they mean


| Field                          | What it controls                           |
| ------------------------------ | ------------------------------------------ |
| Bank Account                   | Company account being reconciled.          |
| Bank Statement Closing Balance | Closing balance from the source statement. |
| Bank Transactions              | Imported statement lines.                  |
| Vouchers                       | Accounting entries available for matching. |
| Unreconciled Amount            | Difference still requiring action.         |
| Clearance Date                 | Date on which a voucher cleared the bank.  |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### A Payment Entry does not appear for reconciliation

Check that it posts to the selected bank account, falls within the date range, is submitted, and has not already been cleared. Also review the banking settings and the Payment Entry's Paid From and Paid To accounts.

### The bank statement balance does not match ERPNext

Confirm the statement opening and closing dates, opening balance, uncleared cheques, bank fees, interest, transfers, and duplicate imports. Do not force the difference into the reconciliation date without identifying it.

### An imported Bank Transaction has no suggested match

Verify the amount, date, currency, reference number, and bank account. Expand the matching date range when settlement dates differ, then select the correct voucher manually if necessary.

### The clearance date changed, but the General Ledger posting date did not

This is expected. Reconciliation records when the bank cleared the transaction; it does not move the original accounting posting date.

## Frequently asked questions

### What is the difference between Payment Reconciliation and Bank Reconciliation?

Payment Reconciliation links party payments to invoices. Bank Reconciliation matches accounting transactions to the bank statement and records clearance.

### Should reconciliation be done daily or monthly?

Use a frequency appropriate to transaction volume and control requirements. High-volume accounts often benefit from daily or weekly work, with a formal month-end completion.

### Can one bank transaction be matched to several Payment Entries?

Use the supported multi-allocation behavior when the bank combined several accounting payments into one statement line. The selected entries must explain the statement amount completely.

### Should unmatched bank fees be entered during reconciliation?

Create the appropriate accounting transaction for the fee, using the bank charges account, and then reconcile it. Reconciliation should not replace the accounting entry.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)
