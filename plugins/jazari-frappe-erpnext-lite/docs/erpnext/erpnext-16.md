<!-- Frappe documentation: erpnext, part 16 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__CRM.md -->
---
title: "Introduction to CRM | ERPNext Documentation"
description: "Learn how ERPNext CRM manages leads, opportunities, customers, activities, campaigns, and pipeline reporting, plus the planned version 17 transition."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/CRM"
updated: "2026-07-23"
---

Customer relationship management (CRM) in ERPNext helps sales teams organize prospects, qualify potential business, record follow-ups, and move an enquiry toward a sale. The records are connected, so a salesperson can begin with a [Lead](/erpnext/lead), create an [Opportunity](/erpnext/opportunity), prepare a [Quotation](/erpnext/quotation), and continue into the selling cycle without entering the same information again.

ERPNext CRM is useful when your organization wants customer context and sales transactions in one system. It connects pre-sales activity with the [Customer](/erpnext/customer), Sales Order, delivery, billing, and reporting records maintained by other ERPNext teams.

## Important: ERPNext CRM is scheduled for removal

On the develop version, the CRM workspace states that this module is scheduled for deprecation and will be completely removed in version 17. Frappe recommends using [Frappe CRM](https://frappe.io/crm) instead.

If you are starting a new CRM implementation, evaluate Frappe CRM before configuring a long-term workflow in the ERPNext CRM module. If you already use the module, inventory your leads, opportunities, activities, reports, integrations, and custom fields, then plan the transition with your implementation team. The transactional selling records in ERPNext remain relevant, but do not assume that custom CRM behavior will move automatically.

The CRM workspace brings together pipeline records, customer masters, campaigns, settings, and reports. The notice at the top identifies the planned version 17 change.

## How the CRM and selling cycle fits together


| Stage                 | Record                              | What happens                                                                                                             |
| --------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Capture interest      | Lead                                | Store an unqualified person or organization that may become a customer.                                                  |
| Qualify demand        | Opportunity                         | Record the potential requirement, expected value, probability, sales stage, and next action.                             |
| Make an offer         | Quotation                           | Share proposed items, quantities, prices, taxes, validity, and commercial terms.                                         |
| Establish the account | Customer                            | Create the party used for transactions and accounting. Add Contacts and Addresses to keep people and locations reusable. |
| Confirm the sale      | [Sales Order](/erpnext/sales-order) | Record the accepted order and drive delivery, billing, procurement, or production.                                       |


This sequence is a common path, not a mandatory one. You can create an Opportunity for an existing Customer, prepare a Quotation from a Lead, or create a Customer before a Quotation when your process requires it. The correct path depends on when your team qualifies a prospect and when it needs a formal customer account.

## What ERPNext CRM covers

### Lead management

A Lead represents a person or organization that has shown interest but has not yet been qualified as a customer. Capture the lead name, organization, contact details, source, territory, industry, and notes. Assign an owner and record each call, email, or meeting so another team member can understand the history.

Use clear qualification criteria. For example, confirm the requirement, approximate budget, decision process, and expected timing before converting a Lead into an Opportunity. Keeping low-quality enquiries at the Lead stage makes the active pipeline more meaningful.

### Opportunity tracking

An Opportunity represents potential revenue being actively pursued. It can be linked to a Lead, Customer, or Prospect. Add the requested items or services, expected closing date, probability, opportunity amount, source, and sales stage. The [Sales Stage](/erpnext/sales-stage) helps teams distinguish early discovery from evaluation, negotiation, and other defined stages.

[Screenshot on the live page: ERPNext Opportunity list with realistic demo opportunities and their current statuses]

The Opportunity list provides a shared view of active deals and their status. Filters, assignments, and saved views can help each salesperson focus on the records that need attention.

### Customer, contact, and address management

A Customer is the organization or individual you sell to. A [Contact](/erpnext/contact) stores a person and their communication details, while an [Address](/erpnext/address) stores a billing, shipping, office, or other location. Linking Contacts and Addresses to the Customer lets ERPNext reuse them in Quotations, Sales Orders, deliveries, and invoices.

Avoid creating a new Customer for every contact or branch unless the branch must be treated as a separate commercial or accounting party. Use Contacts and Addresses to model people and locations beneath the correct customer account.

### Activities and communication history

Calls, emails, meetings, comments, assignments, and other interactions provide the context behind a deal. Use the timeline on the relevant record and link communication to the correct Lead, Opportunity, or Customer. An [Appointment](/erpnext/appointment) can support scheduled interactions, while assignments and due dates make ownership visible.

Record the outcome and next action, not only that contact occurred. A useful note tells the next user what was discussed, what the prospect agreed to, and when the team should follow up.

### Campaigns and outreach

A [Campaign](/erpnext/campaign) groups marketing activity so leads and opportunities can be traced to an initiative. An [Email Campaign](/erpnext/email-campaign) can send a scheduled sequence using Email Templates. Use Lead Source, Campaign, and consistent naming to compare which channels generate qualified opportunities rather than only raw enquiries.

### Reports and analytics

The CRM workspace includes pipeline and efficiency reports. [Sales Pipeline](/erpnext/sales-pipeline) helps teams review opportunities by stage or status, and CRM Analytics can summarize activity and conversion information. Report quality depends on disciplined data entry, especially owners, stages, probabilities, expected closing dates, sources, and loss reasons.

## Before you begin

- Decide whether the ERPNext CRM module or Frappe CRM is the right long-term system for your version and roadmap.
- Define what qualifies a Lead and when users should create an Opportunity or Customer.
- Create a small, controlled list of Lead Sources, Opportunity Types, Sales Stages, Territories, and Campaign naming rules.
- Assign record ownership and agree on how quickly new leads must receive a first response.
- Configure [CRM Settings](/erpnext/crm-settings) only after the team agrees on conversion and naming behavior.
- Review roles and permissions so users can access the customers and opportunities they are responsible for.

## A typical CRM workflow

1. Create a Lead from an enquiry, website form, email, event, referral, or manual entry.
2. Assign the Lead to a salesperson and record the next follow-up.
3. Qualify the requirement. Update the status and capture the source, territory, organization, and communication details.
4. Create an Opportunity when the enquiry becomes a genuine potential deal.
5. Add the expected value, probability, sales stage, closing date, requested items, and next action.
6. Create and send a Quotation when the solution and commercial proposal are ready.
7. Create or select the Customer before the transaction requires a customer account.
8. Convert the accepted proposal into a Sales Order and continue with fulfilment and billing.

Review the pipeline regularly. Close or mark lost opportunities that are no longer active and record a meaningful loss reason. An accurate smaller pipeline is more useful than a large pipeline filled with stale records.

## Important records and what they mean


| Record or field       | What it means                                                                                                           |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Lead                  | An unqualified prospect. Use it before your organization is ready to treat the party as an active customer or deal.     |
| Opportunity           | A qualified potential sale being pursued, with value, probability, timing, items, and ownership.                        |
| Opportunity From      | Identifies whether the Opportunity is linked to a Lead, Customer, or Prospect.                                          |
| Source                | The channel or origin that generated the Lead or Opportunity, such as referral, website, or event.                      |
| Sales Stage           | The current step in your qualification and sales process.                                                               |
| Probability           | Your estimated likelihood that the Opportunity will convert. Use a consistent team rule rather than personal guesswork. |
| Expected Closing Date | The date the team currently expects the decision or conversion to occur.                                                |
| Next Contact Date     | The planned date for the next follow-up with the prospect or customer.                                                  |
| Campaign              | The marketing initiative associated with the enquiry or opportunity.                                                    |
| Lost Reason           | The reason an Opportunity did not proceed. Consistent reasons support useful analysis.                                  |


## Good practices

- Keep one clear owner for every active Lead and Opportunity.
- Record the next action and due date after every meaningful interaction.
- Use stages, sources, and loss reasons consistently across the team.
- Update expected values and closing dates when circumstances change.
- Do not convert every enquiry immediately. Keep the pipeline reserved for qualified work.
- Review duplicate Customers, Contacts, and Leads before creating new records.
- Close stale opportunities so forecasts reflect current reality.

## Frequently asked questions

### What is the difference between a Lead, Contact, and Customer?

A Lead is an unqualified prospect. A Contact is a person linked to one or more parties. A Customer is the commercial party used in sales and accounting transactions. See [Difference between Lead, Contact, and Customer](/erpnext/difference-between-lead-contact-and-customer) for a focused comparison.

### Do I need to create a Lead before every Opportunity?

No. An Opportunity can be created for a Lead, Customer, or Prospect. Use a Lead when qualification is still needed and create an Opportunity directly for an existing Customer when the potential deal is already known.

### When should I create a Customer?

Create the Customer when the party is qualified and your process needs a reusable customer account for a Quotation, Sales Order, invoice, address, contact, pricing, or accounting control. Avoid creating Customers for spam or early unqualified enquiries.

### Can ERPNext create Leads automatically?

Yes. Leads can be created through supported email and web workflows or integrations. See [Automate Lead Creation](/erpnext/automate-lead-creation) and test the source, assignment, duplicate-handling, and consent behavior before enabling automation.

### Should a new implementation use ERPNext CRM?

Because the develop version announces removal of the module in version 17, evaluate Frappe CRM first. Confirm the supported integration and migration approach for the exact versions you plan to deploy.

## Video tutorials

For guided learning, see the existing course: [Lead, Opportunity and Quotation](https://school.frappe.io/lms/courses/erpnext-sales-crm).

You can also use [Newsletter](/erpnext/newsletter) for email outreach to subscribed recipients.

## Related topics

- [CRM Masters](/erpnext/crm-masters)
- [Opportunity Type](/erpnext/opportunity-type)
- [Lead Source](/erpnext/lead-source)
- [CRM Reports](/erpnext/crm-reports)
- [CRM Analytics](/erpnext/crm-analytics)

<!-- page: erpnext/erpnext__crm_reports.md -->
---
title: "CRM Reports | ERPNext Documentation"
description: "Use ERPNext CRM Reports to review leads, opportunities, sales activity, conversions, and pipeline performance."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/crm_reports"
updated: "2026-07-23"
---

CRM reports in ERPNext offer valuable insights into lead management. They help businesses track key metrics, evaluate the success of various campaigns, and understand customer behaviour. 

By analyzing these reports, companies can make informed decisions, streamline their sales processes, and enhance customer relationships, leading to improved overall efficiency and growth.

> Home > CRM > Reports

### Lead Details

It typically provides an overview of the leads you are managing, including key details and metrics related to lead status, source, conversion, and more.

[Screenshot on the live page: Screenshot 2024-08-29 at 4.29.26 PM]

### Sales Funnel

The Sales Funnel Report provides a visual and analytical view of your sales pipeline, helping you understand the status and progression of leads and opportunities through various stages of your sales process.

For more details check [Sales Funnel](/erpnext/sales_funnel).

[Screenshot on the live page: Screenshot 2024-08-29 at 4.31.20 PM]

### Prospects Engaged But Not Converted

It helps you identify and analyze leads or opportunities that were engaged but did not result in a conversion.

[Screenshot on the live page: Prospects Engaged But Not Converted]

### Minutes to First Response for Opportunity

In this internet era, we all expect a quicker response time to any of our queries. This report gives you the details about time taken by sales executives for response to an opportunity. Lesser the average time for first response the better.

You can input the date range for which you would like to analyse the minutes to first response. The line graph is shown on the top and date wise details at the bottom.

### Inactive Customers

This report shows the list of customers who have not purchased since specific number of days. You can mention the number of days in 'Days Since Last Order' filter. Also you can mention if Sales Order or Sales Invoice is to be considered in DocType filter.

[Screenshot on the live page: Screenshot 2024-08-29 at 4.34.35 PM]

### Lost Opportunity

This report provides Lost Opportunity details like opportunity from, party, customer name, lost reasons, sales stage, territory, and other details.

[Screenshot on the live page: Lost Opportunity]

### Campaign Efficiency

This report evaluates the effectiveness of your marketing campaigns by analyzing various performance metrics. This report helps you understand how well your campaigns are performing, the return on investment (ROI), and areas where improvements can be made.

[Screenshot on the live page: Screenshot 2024-08-29 at 4.39.12 PM]

<!-- page: erpnext/erpnext__crm_settings.md -->
---
title: "CRM Settings | ERPNext Documentation"
description: "Configure ERPNext CRM Settings for lead naming, conversion, contact handling, and opportunity behavior."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/crm_settings"
updated: "2026-07-23"
---

> Introduced in Version 14.

CRM Settings allow you to configure your leads, opportunities, quotations and communication as per the business tules..

To access CRM Settings, go to:

> Home > CRM > Settings > CRM Settings

## Lead

[Screenshot on the live page: Screenshot 2024-06-03 at 12.48.00 PM]

### Campaign Naming By

It ensures consistency in the naming convention used by the organisation by automatically generating names for new campaigns based on predefined rules or patterns. It helps users create and maintain unique campaigns and track their effectiveness.

### Allow Lead Duplication based on Emails

If this is enabled, the system will allow users to create multiple leads with the same email address at the same time.

### Auto Creation of Contact

The system will automatically create a new Contact on creation of a Lead.

## Opportunity

[Screenshot on the live page: Screenshot 2024-06-03 at 12.54.38 PM]

### Close Replied Opportunity After Days

If there are many Opportunities having a status other than Open, then they will be auto-closed after the no. of days mentioned in this field if there is no action.

## Quotation

[Screenshot on the live page: Screenshot 2024-06-03 at 12.56.40 PM]

### Default Quotation Validity Days

You can configure quotations to the customer to be valid only for certain days. In the Quotation, you can update Valid Till Date manually. By default, the Valid Till date is auto-set as 30 days from the Quotation's Posting Date. You can change the no. of days in this field as per your business case.

## Other Settings

[Screenshot on the live page: Screenshot 2024-06-03 at 12.58.09 PM]

### Carry Forward Communication and Comments

If this is enabled, When converting a Lead into Opportunity and Opportunity to Quotation, the system will auto copy the emails and comments from the source document.

<!-- page: erpnext/erpnext__currency-exchange-settings.md -->
---
title: "Currency Exchange Settings | ERPNext Documentation"
description: "Configure the exchange-rate provider ERPNext uses when no eligible manual Currency Exchange record is available."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/currency-exchange-settings"
updated: "2026-08-14"
---

International transactions at Nova Industries sometimes need a market rate when finance has not stored one manually.



A Nova sales user creates a EUR invoice, but finance has not entered a manual rate for that date. ERPNext can either stop the user or ask an online exchange-rate service for a rate. Currency Exchange Settings controls that fallback through the provider, endpoint, request parameters, credentials, and result mapping.



The setting is global, so one incorrect configuration can affect transactions and period-end revaluation across several Companies. Use it when market rates are acceptable, or disable it when finance requires only approved [Currency Exchange](/erpnext/currency-exchange) records. This page helps you configure and test the provider before users depend on it.

## Before you begin

List the required currency pairs, transaction dates, and rate types. Confirm whether the provider covers historical dates as well as current rates. Decide who owns provider credentials, rate-source approval, outage handling, and manual fallback.

Enable the required [Currency](/erpnext/currency) records. Review the stale-rate controls in [Accounts Settings](/erpnext/accounts-settings), because a valid manual record is preferred before the provider is called. If **Allow Stale Exchange Rates** is enabled, an old manual rate can continue to win indefinitely.

## Review the configured provider

1. Open Currency Exchange Settings.
2. Confirm that **Disabled** is clear when provider fallback is required.
3. Select the Service Provider.
4. Review the API Endpoint and protocol.
5. Enter an Access Key only for a provider that requires one.
6. Review request Parameters and Result Key mappings.
7. Save, then test from a draft foreign-currency transaction.

[Screenshot on the live page: Frankfurter v2 provider configuration]

The current develop options include `frankfurter.dev`, `frankfurter.dev - v2`, `exchangerate.host`, and `Custom`. Frankfurter v2 supports more currencies than the older v1 configuration. Exchangerate.host requires an access key. Provider coverage and commercial terms can change, so validate them directly with the provider before rollout.

## Important fields and what they mean


| Field             | Meaning                                                                                                                       |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Disabled          | Stops provider requests. ERPNext can still use eligible stored Currency Exchange records.                                     |
| Service Provider  | Loads a predefined provider mapping or allows a Custom configuration.                                                         |
| API Endpoint      | URL template called by ERPNext. It can use placeholders such as `{transaction_date}`, `{from_currency}`, and `{to_currency}`. |
| Use HTTP Protocol | Uses HTTP instead of HTTPS. Leave this clear unless a trusted internal service specifically requires HTTP.                    |
| Access Key        | Credential required by some providers. Protect it like any external API secret.                                               |
| Parameters        | Key-value pairs sent with the request. Values can contain the supported placeholders.                                         |
| Result Key        | Path used to extract the numeric rate from the provider response.                                                             |
| Example URL       | A preview that helps validate the resulting request format.                                                                   |


Do not paste a secret into documentation, screenshots, support posts, or client scripts. Restrict write permission to this setting.

Use [Role Based Permissions](/erpnext/role-based-permissions) to limit who can alter the provider or its credentials. A rate source is an accounting control, not merely a technical preference. Record the owner, renewal date, approved providers, supported currency pairs, and manual fallback in the finance operating procedure.

## Provider choices

### Frankfurter v2

Use the v2 predefined configuration for a keyless, centrally sourced rate when its supported currencies and historical coverage match your need. The configured endpoint on the demo site requests a rate for the From Currency, To Currency, and transaction date.

### Frankfurter v1

The older endpoint covers fewer currencies. Keep it only when an existing integration has been tested against its supported list. New setups should evaluate v2 first.

### Exchangerate.host

This provider supports a broader commercial service but requires an access key in the current predefined setup. Review its free or paid plan, rate limits, historical coverage, licensing, and uptime before use.

### Custom

Use Custom for an approved treasury service or internal rate endpoint. Configure the URL, parameters, and result path carefully. The response must provide a numeric rate in the direction ERPNext requests.

## Understand lookup priority

When ERPNext requests a rate for a direction, date, and buying or selling context, it first searches stored Currency Exchange records. If none is eligible, the provider is called. If the provider fails or returns no usable value, ERPNext asks for a manual record.

This priority matters when users report that the system is not using the market rate. The cause may be an eligible stored record, not the provider. Review [Freeze Exchange Rate](/erpnext/exchange-rate-field-frozen) and stale-rate settings before changing the API configuration.

## Test the configuration

Create a Draft [Sales Invoice](/erpnext/sales-invoice) or [Purchase Invoice](/erpnext/purchase-invoice) dated on a known business day. Select a supported foreign currency and verify:

- the Exchange Rate populates;
- the direction in the field label is correct;
- the Company-currency total matches the rate;
- a historical date returns a plausible historical rate;
- a deliberately unsupported pair produces a clear fallback process;
- no API key or response detail is exposed to ordinary users.

Also test a [Payment Entry](/erpnext/payment-entry), because its source and target account currencies can request a different direction. Test [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation) separately for a closing date.

Repeat the test after application upgrades or provider configuration changes. Compare the returned value with an independently approved reference on a known date, and confirm that the same request is not unexpectedly using an older manual master.

## Disable provider fallback

Select **Disabled** when every rate must come from a manually approved master or another controlled process. Before doing so, create the required directional and dated records and test the behavior when a rate is missing. Disabling the provider does not create a warning-based approval workflow by itself.

If finance imports rates, use [Data Import](/erpnext/data-import) with a controlled template and validation process. Do not allow duplicate or incorrectly directed records to accumulate unnoticed.

## Troubleshooting

### ERPNext cannot find a rate for one currency

Confirm that the provider supports both currencies and the requested historical date. A provider can cover USD and EUR but not a regional currency. Try an approved alternative provider or create a manual record.

### The provider is configured but a different rate appears

Search Currency Exchange for a matching manual record. Check the transaction date, direction, buying or selling flag, Allow Stale Exchange Rates, and Stale Days.

### A custom provider returns data but ERPNext reads zero

Review the Result Key path and verify that the extracted value is numeric. Compare the request URL and response structure without exposing credentials.

### Historical rates fail while current rates work

The provider or plan may not support historical dates. Use a provider with suitable coverage or import approved historical Currency Exchange records.

## FAQs

### Does ERPNext always call the configured provider?

No, an eligible manual Currency Exchange record is preferred.

### Which provider should I choose?

Choose based on currency coverage, historical support, accuracy policy, licensing, rate limits, reliability, and security. There is no universal best provider.

### Are provider rates automatically posted to the ledger?

No, the fetched rate populates a document. The ledger changes only when a submittable accounting transaction or resulting Journal Entry is submitted.

### Can each Company use a different provider?

Currency Exchange Settings is a site-level singleton. Use controlled manual records or customization if Companies require separate approved sources.

### Should I enable HTTP for an external provider?

No, use HTTPS for external services. HTTP should be limited to a deliberately secured internal architecture.

## Related topics

- [Currency Exchange](/erpnext/currency-exchange)
- [Multi Currency Setup](/erpnext/multi-currency-setup)
- [Accounts Settings](/erpnext/accounts-settings)
- [Managing Transactions in Multiple Currency](/erpnext/managing-transactions-in-multiple-currencies)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)

<!-- page: erpnext/erpnext__currency-exchange.md -->
---
title: "Currency Exchange | ERPNext Documentation"
description: "Store dated buying and selling exchange rates in ERPNext and understand when a transaction uses them."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/currency-exchange"
updated: "2026-08-14"
---

When Nova Industries sells electronics in EUR but reports in USD, finance needs a controlled conversion rate.



Nova agrees to invoice a customer in EUR while maintaining its books in USD. Finance approves `1 EUR = 1.15 USD` for 3 August 2026, so users should not look up or retype the rate on every transaction. A Currency Exchange record stores the approved rate, its effective date, and the direction in which it applies.



ERPNext checks eligible stored records before asking the configured online provider. This gives finance control when a contract fixes the rate, historical entries need a known rate, or a provider does not cover the pair. Use this page to make transactions apply the correct dated rate consistently.

## Before you begin

Enable both currencies in the [Currency](/erpnext/currency) list. Confirm the intended direction and rate convention. `EUR to USD = 1.15` means one euro equals 1.15 US dollars. The inverse is not automatically the same number, so create `USD to EUR` separately when that direction is needed.

Review [Accounts Settings](/erpnext/accounts-settings), especially **Allow Stale Exchange Rates** and **Stale Days**. These settings decide how old a stored record may be when ERPNext searches for a rate. Also review the active [Currency Exchange Settings](/erpnext/currency-exchange-settings) provider, which is used when no eligible manual record is found.

## Create a Currency Exchange record

1. Open Accounting &gt; Multi Currency &gt; Currency Exchange.
2. Select **Add Currency Exchange**.
3. Enter the date from which the rate applies.
4. Select the From Currency and To Currency.
5. Enter the rate using the relationship shown in the field label.
6. Select **For Buying**, **For Selling**, or both.
7. Save.

The list can contain multiple dated records for the same pair. ERPNext searches by transaction date and chooses the latest eligible matching record.



[Screenshot on the live page: Dated Currency Exchange records]



[Screenshot on the live page: EUR to USD exchange rate for buying and selling]

## Important fields and what they mean


| Field         | Meaning                                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------- |
| Date          | The key date used when ERPNext searches for the latest eligible rate on or before a transaction date.               |
| From Currency | The currency representing one unit in the field's relationship.                                                     |
| To Currency   | The currency calculated from the From Currency.                                                                     |
| Exchange Rate | The number of To Currency units equal to one From Currency unit. Read the generated field label before entering it. |
| For Buying    | Makes the record eligible for buying transactions that request a buying rate.                                       |
| For Selling   | Makes the record eligible for selling transactions that request a selling rate.                                     |


If both boxes are selected, the same rate can be used for buying and selling. Use separate records when your approved buying and selling rates differ.

## How ERPNext chooses a rate

For a requested direction, date, and transaction type, current develop behavior follows this pattern:

1. Search Currency Exchange for the latest matching record on or before the transaction date.
2. Apply the stale-rate rule from Accounts Settings.
3. If no eligible stored record exists and the provider is enabled, request the rate from the configured service.
4. If ERPNext still cannot find a rate, ask the user to create a manual Currency Exchange record.

The direction and buying or selling flag matter. A record for EUR to USD does not necessarily satisfy a request for USD to EUR. A record marked only For Buying does not satisfy a selling-rate request.

## Understand stale rates

When **Allow Stale Exchange Rates** is enabled, ERPNext may use the latest matching stored record without an age limit. This is useful for contract rates or finance-approved rates that remain valid until replaced. It can also preserve an old rate longer than intended, so establish a review process.

When the option is disabled, **Stale Days** limits how far back ERPNext searches. If no eligible manual rate remains, ERPNext tries the configured provider. The setting does not create an approval workflow and does not guarantee that a transaction stops when a manual rate expires, because the provider may return a market rate.

See [Freeze Exchange Rate](/erpnext/exchange-rate-field-frozen) if a transaction's Exchange Rate field appears read-only or behaves differently from what the page title suggests.

## Use the rate in a transaction

On a draft [Sales Invoice](/erpnext/sales-invoice), [Purchase Invoice](/erpnext/purchase-invoice), [Quotation](/erpnext/quotation), or order, select the foreign currency and confirm the Exchange Rate. ERPNext calculates Company-currency totals using that rate. If the Price List uses a different currency, **Price List Exchange Rate** converts item prices separately.

The same check applies when a [Sales Order](/erpnext/sales-order) becomes the commercial source for a later invoice. A mapped document may carry forward currency and rate context, so verify the new document rather than assuming it refreshed to the latest master.

On a [Payment Entry](/erpnext/payment-entry), the currencies come from the paid-from and paid-to accounts. The source or target exchange rate converts between the account amounts and Company currency. A payment made at a different rate from its invoice can create a realized exchange gain or loss.

## Correct or supersede a rate

If a saved record is wrong and has not been relied on operationally, correct it with appropriate permission. If a new rate becomes valid later, create a new record with the later date rather than overwriting the historical record. Submitted transactions retain their own exchange-rate values; changing the master does not silently revalue old documents.

Use [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation) to update the Company-currency carrying value of eligible open foreign-currency accounts at a reporting date. Do not alter historical Currency Exchange records merely to force a current closing balance.

## Troubleshooting

### ERPNext says it cannot find an exchange rate

Check that both currencies are enabled, the direction matches, the date is on or before the transaction date, and the buying or selling flag matches. Then verify stale-rate settings and whether the provider supports the pair.

### ERPNext uses an older manual rate instead of the market rate

An eligible Currency Exchange record is preferred. Review **Allow Stale Exchange Rates**, the latest dated record, and its flags. Create a new dated record or change the stale-rate policy according to your finance process.

### The transaction shows two exchange-rate fields

**Exchange Rate** converts the transaction currency to Company currency. **Price List Exchange Rate** converts the Price List currency for item prices. They can be different when the transaction and Price List use different currencies.

## FAQs

### Must I create a Currency Exchange record every day?

No, if no eligible manual record exists, ERPNext can use the configured provider. Create manual records only when you need controlled, historical, unsupported, or contract rates.

### Does the latest record override submitted invoices?

No, a submitted invoice retains the rate saved on that document. The new master affects later rate lookups.

### Can I store different buying and selling rates?

Yes, create records with the appropriate flags and rates. Do not select both flags if finance uses different rates for purchases and sales.

### Why does the inverse direction use another rate?

The system searches the exact From and To direction. Store the inverse record when that direction is needed, using the approved reciprocal or independently supplied rate.

### Can I type over the fetched rate?

The field may be editable depending on document state, permissions, and stale-rate behavior. Always verify the saved value and Company-currency total before submission.

## Related topics

- [Currency](/erpnext/currency)
- [Multi Currency Setup](/erpnext/multi-currency-setup)
- [Currency Exchange Settings](/erpnext/currency-exchange-settings)
- [Manage Foreign Exchange Difference](/erpnext/manage-foreign-exchange-difference)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)

<!-- page: erpnext/erpnext__currency.md -->
---
title: "Currency | ERPNext Documentation"
description: "Configure currency symbols, fractions, and number formats in ERPNext before using a currency in transactions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/currency"
updated: "2026-08-14"
---

For Nova Industries, an electronics manufacturer and distributor, enabling EUR is the first step toward invoicing European customers.



Nova keeps its books in USD, but a European customer expects an invoice in EUR. Before EUR can appear correctly, ERPNext needs to know its code, symbol, fractional unit, and number format. The Currency record stores these display rules.



Enabling EUR makes it available for selection. It does not convert money, create a EUR ledger, or change the Company currency. Those decisions belong to the [Company](/erpnext/company-setup), foreign-currency [Account](/erpnext/chart-of-accounts), Customer, Price List, transaction, and Currency Exchange records. Use this page to enable a currency and verify how its values will appear throughout ERPNext.

## Before you begin

Confirm the currency's official code, symbol, fractional unit, and display convention. Use the standard three-letter code when it already exists. Changing a widely used Currency record affects how values appear across forms, reports, and print formats, so test presentation before changing a standard definition.

You also need permission to read or update Currency masters. If the purpose is to enter a conversion rate, use [Currency Exchange](/erpnext/currency-exchange) instead. If the purpose is to change a Company's base currency, review the Company and existing ledger entries first. A Currency record does not convert historical accounting data.

## Enable and review a currency

1. Open the Currency list from Accounting &gt; Multi Currency &gt; Currency.
2. Search for the standard code, such as EUR.
3. Open the record and select **Enabled**.
4. Review the fraction, symbol, and number format.
5. Save the record.

[Screenshot on the live page: EUR currency settings in ERPNext]

Enabling a currency makes it available for selection. It does not make it the default currency of any Company, party, account, [Price List](/erpnext/price-lists), or document.

Confirm the saved symbol and separators with a realistic amount, including thousands and decimals, before using the currency in customer-facing documents.

After saving, reload the record and test the formatted value on a Draft transaction and its print preview. This confirms that both Desk and the party-facing output use the expected symbol position, separators, and fraction wording.

## Important fields and what they mean


| Field                              | Meaning                                                                                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Currency Name                      | The standard currency code used as the record name, such as EUR, USD, or GBP.                                                                                |
| Enabled                            | Makes the currency available in Link fields. Disable an unused currency only after confirming that no current process requires it.                           |
| Fraction                           | The singular name used for the sub-currency when amounts are converted to words, such as Cent or Penny.                                                      |
| Fraction Units                     | The number of fractional units in one currency unit. EUR uses 100 because one euro equals 100 cents.                                                         |
| Smallest Currency Fraction Value   | The smallest circulating denomination, entered as a decimal value. For EUR, 0.01 represents one cent. This is not the same setting as calculation precision. |
| Symbol                             | The display symbol, such as €, $, or £.                                                                                                                      |
| Show Currency Symbol on Right Side | Places the symbol after the number where that is the accepted convention.                                                                                    |
| Number Format                      | Defines grouping and decimal separators. For example, `#,###.##` displays 12345.67 as 12,345.67.                                                             |


The system-wide [System Settings](/erpnext/system-settings) and field precision still affect how many decimal places ERPNext calculates or displays. A number format changes presentation; it does not necessarily round the underlying General Ledger value. Test reports if you use a currency with no minor unit or unusually high precision.

## Where currency is selected

Currency has several distinct roles in ERPNext:


| Record                        | What the currency controls                                                                                                                                |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Company                       | The base currency used for the Company's accounting books and base-currency values.                                                                       |
| Account                       | The fixed account currency used for that ledger. One bank or cash account should represent one currency.                                                  |
| Customer or Supplier          | The default billing currency and, when configured, the matching receivable or payable account. See [Multi Currency Setup](/erpnext/multi-currency-setup). |
| Price List                    | The currency in which [Item Prices](/erpnext/item-price) are maintained.                                                                                  |
| Sales or Purchase transaction | The currency shown to the party and used for document totals. ERPNext also records the Company-currency equivalent through an exchange rate.              |


Do not assume that enabling EUR automatically creates a EUR bank account or EUR receivable account. Create those ledgers deliberately in the Chart of Accounts, then connect them to the relevant Customer or Supplier.

## Number format and precision

Number format answers how a number is shown. Precision answers how many decimal places are retained or displayed. For example, a format containing two decimal placeholders cannot by itself guarantee that every posting is rounded to two decimals. Review currency precision and the precision of the relevant fields if a report appears to contain unexpected decimals.

Use a format familiar to the people reading the document. `#,###.##` uses a comma for thousands and a period for decimals. `#.###,##` uses a period for thousands and a comma for decimals. Users should enter values according to the locale and input behavior configured for the site, then verify the parsed value before saving a transaction.

## After enabling a currency

Configure the rest of the workflow in this order:

1. Create the required foreign-currency ledger accounts.
2. Set the party's Billing Currency and default account when the party normally uses that currency.
3. Create a matching Price List if prices are maintained in the foreign currency.
4. Add a manual rate in Currency Exchange or verify the configured [exchange-rate provider](/erpnext/currency-exchange-settings).
5. Test a draft [Sales Invoice](/erpnext/sales-invoice), [Purchase Invoice](/erpnext/purchase-invoice), or [Payment Entry](/erpnext/payment-entry) and compare the transaction and Company-currency totals.

## Troubleshooting

### The currency does not appear in a transaction

Open the Currency record and confirm that **Enabled** is selected. Then check whether the party account or Price List restricts the transaction to another currency. A foreign-currency party account normally requires the transaction currency to match that account.

### The symbol or separators look wrong

Review the Currency symbol, symbol position, and Number Format. Also check the site's number format and currency precision. Clear the browser cache or reload the document after saving a master change.

### A whole-number currency still has decimals in a report

Hiding decimal places is not the same as changing stored precision. Review System Settings, report behavior, tax rounding, stock valuation, and the relevant field precision before relying on a visually rounded report for statutory output.

## FAQs

### Do I need to create every currency my business may use?

No, most standard currencies already exist. Enable only those required by your Companies, parties, accounts, price lists, transactions, or reports.

### Can I change a Currency code after transactions exist?

Treat the code as a stable identifier. Create or enable the correct standard currency rather than renaming a code used by existing records.

### Does disabling a currency change old transactions?

No, it removes the currency from normal selection but does not translate or delete historical values. Confirm that reports, recurring documents, integrations, and imports no longer need it before disabling it.

### Is Smallest Currency Fraction Value the same as Currency Precision?

No, the smallest fraction describes the circulating denomination. Precision controls numeric calculation or display detail elsewhere in the system.

### Where do I enter the exchange rate?

Use Currency Exchange for a stored rate, or let ERPNext use the active provider when no eligible manual rate exists. The Currency master itself contains no rate.

## Related topics

- [Currency Exchange](/erpnext/currency-exchange)
- [Multi Currency Accounting](/erpnext/multi-currency-accounting)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [Currency Exchange Settings](/erpnext/currency-exchange-settings)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)
