<!-- Frappe documentation: erpnext, part 33 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__item-tax-template.md -->
---
title: "Item Tax Template\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-tax-template"
updated: "2026-08-14"
---

An Item Tax Template changes the tax rate for a particular item without replacing the tax structure of the transaction. Use it when most items follow the standard rate but selected goods or services are reduced-rated, zero-rated, exempt, or outside a particular tax component.



The Sales or Purchase Taxes and Charges Template still supplies the tax account and calculation row. ERPNext then uses the Item Tax Template rate for the net amount of the matching item.



At Nova Industries, an electronics manufacturer and distributor, one Sales Invoice can contain:


| Item                 | Net amount  | Applicable rate | Tax        |
| -------------------- | -----------: | ---------------: | ----------: |
| NovaPhone X1         | $699.00     | 8%              | $55.92     |
| Device Setup Service | $149.00     | 4%              | $5.96      |
| Extended Warranty    | $99.00      | 0%              | $0.00      |
| **Total**            | **$947.00** |                 | **$61.88** |


The standard transaction template remains at 8%, while item templates override that rate for the second and third lines.

## Before you begin

Create the required tax account in the [Chart of Accounts](/erpnext/chart-of-accounts). Then create the relevant [Sales Taxes and Charges Template](/erpnext/sales-taxes-and-charges-template) or [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template).

The tax account in the transaction template must match the account in the Item Tax Template. An item rate cannot calculate against an account row that is absent from the transaction.

In [Accounts Settings](/erpnext/accounts-settings), enable **Automatically Add Taxes and Charges from Item Tax Template** when ERPNext should add a missing tax row from an item's template. Even with this enabled, test the complete transaction because company, category, and template configuration still determine the final result.



![Automatically add Taxes and Charges from Item Tax Template](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-item-tax-template-enable-item-tax-template.png)

Decide whether the item is reduced-rated, zero-rated, exempt, or not applicable under your local rules. These classifications can have different reporting consequences, so confirm the intended treatment with your tax adviser.

## Create an Item Tax Template

Go to **Accounting &gt; Taxes &gt; Item Tax Template** and select **Add Item Tax Template**.

1. Enter a descriptive **Title**, such as `Nova Reduced Item Tax 4%`.
2. Select the **Company**.
3. In **Tax Rates**, add a row.
4. Select the tax account and enter the overriding rate.
5. Save the template.

Use the pencil icon to open the child-table row and review all its fields.



![Open an Item Tax Template rate row](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-item-tax-template-reduced-template-row.png)



![Tax account and rate in the Item Tax Template row](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-item-tax-template-reduced-template-fields.png)

You can add multiple rows when more than one tax component applies to the item. Each row must use the account that the corresponding transaction tax row uses.

## Important fields and what they mean


| Field          | What it controls                                                                                       |
| -------------- | ------------------------------------------------------------------------------------------------------ |
| Title          | A reusable name that helps users identify the intended rate or treatment                               |
| Company        | Restricts the template to transactions for that company                                                |
| Tax            | The ledger account and tax component whose rate is overridden                                          |
| Tax Rate       | The rate used for the matching item's net amount                                                       |
| Not Applicable | Indicates that this tax component does not apply to the item, which is distinct from applying it at 0% |
| Disabled       | Prevents the template from being selected without deleting its history                                 |


Use a 0% rate when the supply is reported as taxable at zero percent. Use **Not Applicable** when the tax component does not apply to the item. Do not treat these as interchangeable unless that is correct for your jurisdiction and reporting setup.

## Assign the template to an Item

Open the [Item](/erpnext/item) and go to the **Tax** tab. In the **Taxes** table, add a row and use the pencil icon to open it.



![Open the Item Tax assignment row](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-item-tax-template-item-tax-assignment-row.png)

Set the Item Tax Template and, when relevant, its Tax Category and validity conditions.



![Item Tax Template assignment, Tax Category, and Valid From](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-item-tax-template-item-tax-assignment-fields.png)


| Assignment field             | What it controls                                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Item Tax Template            | The rate or treatment available for the item                                                                  |
| Tax Category                 | Restricts the assignment to transactions using that category; a blank category acts as the default assignment |
| Valid From                   | The first date on which ERPNext can use this assignment                                                       |
| Minimum and Maximum Net Rate | Restricts the assignment by the item's transaction net rate when configured                                   |


You can add multiple assignments for different Tax Categories or validity periods. Keep their conditions mutually clear so the intended row is easy to predict.

## How ERPNext chooses an item template

ERPNext first considers the Tax Category and transaction date. It uses the first valid matching assignment for the item. When no category-specific row matches, a valid row with a blank Tax Category can act as the default.

For most transactions, the posting or transaction date determines validity. On a [Purchase Invoice](/erpnext/purchase-invoice), ERPNext considers the Supplier Invoice Date before falling back to Posting Date. This matters when a supplier invoice arrives after a rate change but carries an earlier invoice date.

If more than one assignment is valid for the same category and date, ERPNext can use the first matching row. Avoid overlapping validity periods. Give the earlier assignment a clear end in your migration or change-control process, and verify a draft transaction on both sides of the rate-change date.

## Assign a template to an Item Group

Use an [Item Group](/erpnext/item-group) assignment when every item in a group shares the treatment. This reduces repeated setup for large catalogs.

An assignment on the Item is more specific and takes precedence over a group-level default. Use the group for the common rate and item-level rows for genuine exceptions. Test an item with its own assignment and another that inherits the group assignment before relying on the setup in production.

## Use the template in a transaction

Create a draft Sales Invoice, Purchase Invoice, Quotation, Sales Order, Purchase Order, Delivery Note, or Purchase Receipt that supports item tax calculation.

1. Select the company and party.
2. Confirm the [Tax Category](/erpnext/tax-category), when used.
3. Select the transaction Taxes and Charges Template.
4. Add the items.
5. Review the Item Tax Template on each applicable row.
6. Check the item-wise tax calculation, total tax, and Grand Total before submission.

The mixed-rate invoice below contains standard, reduced, and zero-rated lines. Open a row with the pencil icon when you need to inspect or change the Item Tax Template selected for that transaction line.



![Mixed-rate items on one Sales Invoice](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-item-tax-template-mixed-rate-invoice-items.png)



![Item Tax Template selected on a transaction row](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-item-tax-template-transaction-item-tax-template.png)

ERPNext calculates $55.92 on the $699 phone, $5.96 on the $149 service, and $0 on the $99 warranty. Total tax is therefore $61.88 and the Grand Total is $1,008.88.



![Mixed-rate tax and Grand Total result](https://novacompanies.m.frappe.cloud/files/docs-tax-compliance-20260803-taxes-compliance-item-tax-template-mixed-rate-tax-result.png)

## Select a different template on a transaction line

The Item master supplies the normal default. A user can select another eligible Item Tax Template directly in a draft transaction row when the specific transaction needs a different supported treatment.

Use manual selection as a controlled exception, not as a substitute for maintaining the Item master. The chosen template must belong to the correct company, match the transaction Tax Category when one is set, be valid for the transaction date, and use tax accounts present in the transaction tax table.

After changing a category, date, item, or item template, review the full Taxes and Charges table again. Re-add the affected item row when stale tax context does not refresh as expected.

## Use different rates on one invoice

Current ERPNext can calculate different item rates against the same tax account by maintaining an item-wise breakdown behind the transaction tax row. Separate tax accounts are still appropriate when the tax components must post or report separately, but different rates alone do not always require different ledger accounts.

If only templated items should be taxed, the standard transaction row can use a 0% rate while the Item Tax Templates supply the applicable rates. Test non-templated items carefully because they will inherit the transaction row's rate.

## Troubleshooting

### The Item Tax Template is marked invalid

Compare its company, Tax Category, validity date, and account with the transaction. Confirm that the matching account exists in the selected Sales or Purchase Taxes and Charges Template. Recheck the item row after changing the transaction category or date.

### The standard rate is applied to every item

Open the affected item row and confirm its Item Tax Template. Check the Item or Item Group assignment, Valid From date, Tax Category, and the transaction date. Verify that item-wise tax values are present before submission.

### Tax from one template appears on unrelated items

Review every tax account row and item assignment. Ensure templates use the intended account and category, and remove overlapping default assignments. Recreate a small draft with one item per treatment to isolate the configuration.

### A zero-rated item still appears in the tax breakdown

A 0% item can still belong to the tax component and appear in reporting with zero tax. If the component should not apply at all, evaluate the **Not Applicable** option and confirm the legal and reporting treatment before changing the setup.

## Frequently asked questions

### Does an Item Tax Template replace the transaction tax template?

1. It overrides the rate for matching item amounts. The transaction template still provides the tax row, account, charge type, and ledger destination.

### Can one invoice contain items taxed at several rates?

Y

es. Assign the appropriate item templates and keep the matching tax account in the transaction tax table. Review the item-wise breakdown and calculated total before submission.

### Should a tax-exempt item use 0% or Not Applicable?

That depends on how the supply must be classified and reported. A 0% rate generally means the tax applies at zero percent, while Not Applicable means the tax component does not apply. Confirm the correct treatment for your jurisdiction.

### Why does a template work on one transaction date but not another?

Check the assignment's Valid From value and any overlapping rows. For Purchase Invoices, also inspect Supplier Invoice Date because it can determine which assignment is valid.

### Can I set the template on an Item Group instead of every Item?

Y

es. Use an Item Group assignment for a shared default and Item-level assignments for exceptions. The more specific Item assignment takes precedence.

## Related topics

- [Taxes](/erpnext/taxes)
- [Tax Category](/erpnext/tax-category)
- [Tax Rule](/erpnext/tax-rule)
- [Sales Taxes and Charges Template](/erpnext/sales-taxes-and-charges-template)
- [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template)
- [Sales Invoice](/erpnext/sales-invoice)
- [Purchase Invoice](/erpnext/purchase-invoice)

<!-- page: erpnext/erpnext__item-valuation-transactions.md -->
---
title: "Item Valuation Setup and Transactions"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-valuation-transactions"
updated: "2026-03-02"
---


In ERPNext, Item's stock valuation is updated on the creation of one of the following transaction.

1. Purchase Receipt
2. Stock Entry of type Material Receipt
3. Stock Reconciliation made for updating stock opening balance

You can select valuation method based on which item's value will be calculated. Valuation Method can be set globally for all the items from the Stock Settings.

![Download Backup](/files/item-valuation-1.png)

You can also set Valuation Method in the item master, especially when a valuation method for an item is different from the default Method as seen in the following screenshot.

![Download Backup](/files/item-valuation-2.png)

Note that once ledger entries are made for an item, this option will no longer be visible in the Item form.

[Click here to learn about the valuation methods available in the ERPNext, and how it works.](https://frappe.io/blog/erpnext-features/inventory-valuation-method-fifo-vs-moving-average)


### New in v16

In ERPNext v16, users can now select Valuation Method per company basis and a new field in the `Company` DocType has been added for the same. The old field in `Stock Settings` single DocType still remains and will only be used in certain cases where the reference document does not have a reference to any company (such as `Batch`). The valuation method will be fetched in the following order:

1. `Item` level
2. `Company` level
3. `Manufacturing Settings` (global) level

Please set the valuation method in all the above levels accordingly to prevent incorrect stock valuations.

<!-- page: erpnext/erpnext__item-variants.md -->
---
title: "Item Variants\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-variants"
updated: "2026-03-12"
---

**An Item Variant is a version of an Item with different attributes like sizes or colors.**

Eg: Suppose t-shirt is an Item and it comes in different sizes and colors like small, medium, large and red, blue, green. In ERPNext the t-shirt will be considered as an Item template and each of the variations will be an Item Variant.

A blue t-shirt in size small rather than just a t-shirt. Item variants let you treat the small, medium, and large versions of a t-shirt as variations of one Item 't-shirt'.

Without Item variants, you would have to treat the small, medium and large versions of a t-shirt as three separate Items.

## 1. Using Item Variants

Variants can be based on two things:

1. Item Attributes
2. Manufacturers

&gt; Tip: Once an item template is created, when you update this template, all the variants are also updated accordingly.

### 1.1 Creating the Item Variant Template

1. To use Item Variants in ERPNext, create an Item and tick 'Has Variants' under Variants.
2. The Item then shall be referred to as a so-called 'Template'. Such a Template is not identical to a regular 'Item' any longer. For example, it (the Template) cannot be used directly in any transaction (Sales Order, Delivery Note, Purchase Invoice) itself.
3. Only the Variants of the Item (blue t-shirt in size small) can be practically used. Therefore it would be ideal to decide whether an item 'Has Variants' or not directly when creating it.
  [Has Variants](/files/item-has-variants.png)
4. On selecting 'Has Variants' a table will appear. Specify the variant attributes for the Item in the table. In case the attribute has Numeric Values, you can specify the range and create intervals based on the increment values.
  [Valid Attributes](/files/item-attributes.png)

&gt; Note: You cannot make Transactions against a 'Template'.

### 1.2 Creating the Item Variants Based on Item Attributes

To create 'Item Variants' against a 'Template' click on 'Create'. From there, choose whether to create a single variant or multiple. Single is simple where you create just one or more attributes and one Item will be created. When choosing multiple variants, tick the attributes and multiple items will be created. For example, if you choose Color: Red, Green and Size: Small, Medium, Large, 6 variants will be created.

Creating multiple variants in ERPNext:

![](/files/item-variants.png)

To learn more about setting attributes, check out [Item Attributes](/erpnext/item-attribute)

### 1.3 Item Variants Based on Manufacturers

To set up variants based on Manufacturers, in your Item template, set "Variants Based On" as "Manufacturers"  
In this case, to create variants, click on Create &gt; Make Variant. The system will prompt you to select a Manufacturer. You can also optionally put in a Manufacturer Part Number.

![](/files/variant-manufacturer.png)

The naming of the variant will be based on the name (ID) of the template Item with a number suffix. e.g. "Screwdriver" will have variant "Screwdriver-1".

## 2. Update Item Variants Based on Template

Go to: **Home > Stock > Items and Pricing > Item Variant Settings**. The fields displayed here will be copied over to the variants as well. By default, all fields are shown, delete any rows you don't want to be updated from the item template to the variants.

### 3. Related Topics

1. [Item Attribute](/erpnext/item-attribute)

<!-- page: erpnext/erpnext__item-where-used-report.md -->
---
title: "Item Where Used Report"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-where-used-report"
updated: "2026-06-08"
---

# Item Where Used Report

The **Item Where Used** report shows master-data and product-structure references for an Item. It is intended for answering questions like “which BOMs or Product Bundles use this item?” without mixing in transactional documents such as Sales Orders, Purchase Invoices, Stock Ledger Entries, or Stock Entries.

## Filters


| Filter  | Required | Description                                                    |
| ------- | -------- | -------------------------------------------------------------- |
| Item    | Yes      | The Item to search for.                                        |
| Company | No       | Filters BOM-backed rows by Company.                            |
| Section | No       | Choose `Where Used` or `References`; leave blank to show both. |


## Sections

### Where Used

This section shows places where the selected Item is used inside another product or manufacturing structure.


| Reference Type               | Source                             |
| ---------------------------- | ---------------------------------- |
| BOM Component                | `BOM Item.item_code`               |
| Product Bundle Component     | `Product Bundle Item.item_code`    |
| BOM Secondary Item           | `BOM Secondary Item.item_code`     |
| Subcontracting Service Item  | `Subcontracting BOM.service_item`  |
| Subcontracting Finished Good | `Subcontracting BOM.finished_good` |


### References

This section shows related master references where the Item is the output, parent, template, or alternate item.


| Reference Type        | Source                                   |
| --------------------- | ---------------------------------------- |
| BOM Output            | `BOM.item`                               |
| Product Bundle Parent | `Product Bundle.new_item_code`           |
| Item Variant          | `Item.variant_of`                        |
| Item Alternative      | `Item Alternative.item_code`             |
| Alternative For Item  | `Item Alternative.alternative_item_code` |


## Report Columns


| Column                      | Description                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| Section                     | `Where Used` or `References`.                                        |
| Reference Type              | The type of usage or relationship found.                             |
| Document Type               | The linked DocType, such as BOM or Product Bundle.                   |
| Document                    | The linked document where the Item is referenced.                    |
| Related Item                | The parent, output, alternate, or related Item.                      |
| Matched Field               | The exact field that matched the selected Item.                      |
| Row                         | Child table row index, where applicable.                             |
| Qty / UOM                   | Quantity and UOM from the source row, where available.               |
| Stock Qty / Stock UOM       | Stock quantity and stock UOM from BOM rows, where available.         |
| Company                     | Company from the BOM, where applicable.                              |
| Default / Active / Disabled | Status metadata from the source document, where applicable.          |
| Details                     | Additional context such as secondary item type or linked BOM number. |


## Notes

- The report is master-data focused and intentionally excludes transactional usage.
- The Company filter applies to BOM-backed rows.
- Use the `Where Used` section for product-structure traceability.
- Use the `References` section to find related definitions such as default/output BOMs, parent bundles, variants, and alternatives.

<!-- page: erpnext/erpnext__item.md -->
---
title: "Item"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item"
updated: "2026-03-12"
---

**An Item is a product or a service offered by your company.**

The term Item is also applicable to raw materials or components of products yet to be produced (before they can be sold to customers). ERPNext allows you to manage all sorts of items like raw-materials, sub-assemblies, finished goods, item variants, and service items.

ERPNext is optimized for itemized management of your sales and purchase. If you are in services, you can create an Item for each service that you offer. Completing the Item Master is very essential for the successful implementation of ERPNext.

To access the Item list, go to: > Home > Stock > Items and Pricing > Item

1. Prerequisites

---

Before creating and using an Item, it is advised that you create the following first:

- [Item Group](/erpnext/item-group)
- [Warehouse](/erpnext/warehouse)
- A Unit of Measure if required

2. How to create an Item

---

1. Go to the Item list, click on new.
2. Enter an Item Code, the name will be auto-filled the same as Item Code on clicking inside the Item Name field.
3. Select an Item Group.
4. Enter the opening stock units and standard selling rate.
5. Save

![](/files/item_master.png)

**2.1 Item Properties**

- **Item Name:** Item name is the actual name of your product or service.
- **Item Code:** Item Code is a short-form to denote your Item. If you have very few Items, it is advisable to keep the Item Name and the Item Code same. This helps new users to recognise and update Item details in all transactions. In case you have a lot of Items with long names and the list runs into hundreds, it is advisable to code. To understand naming Item codes, see [Item Codification](/erpnext/item-codification). You can also generate an Item Code based on a [Naming Series](/erpnext/naming-series) by enabling this feature in [Stock Settings](/erpnext/stock-settings#1-item-naming-by).
- **Item Group:** Item Group is used to categorise an Item under various criteria like products, raw materials, services, sub-assemblies, consumables or all Item groups. Create your default Item Group list under Setup > Item Group and pre-select the option while filling your New Item details under [Item Group](/erpnext/item-group). Item groups can be sub-assemblies, raw materials, etc, or based on your business use case.
- **Default Unit of Measure:** This is the default measuring unit that you will use for your product. It could be Nos, Kgs, Meters, etc. You can store all the UOMs that your product will require under Set Up> Master Data > UOM. These can be preselected while filling New Item by using % sign to get a pop up of the UOM list. Visit the [UoM](/erpnext/uom) page for more details

### 2.2 Options when creating an item

- **Disabled**: If you disable an Item, it cannot be selected in any transaction.
- **Allow Alternative Item**: Sometimes, when manufacturing a finished good, a specific material may not be available. If you tick this, you can create and select an alternative item from the Item Alternative list. To know more, visit the [Item Alternative](/erpnext/item-alternative) page.
- **Maintain Stock:** If you are maintaining stock of this Item in your Inventory, ERPNext will make a stock ledger entry for each transaction of this item. Ensure to keep this option unchecked when creating a non-stock Item (make to order/engineer) or a service.
- **Include Item in Manufacturing**: This is for raw material Items that'll be used to create finished goods. If the Item is an additional service like 'washing' that'll be used in the BOM, keep this unchecked.
- **Valuation Rate**: There are two options to maintain the valuation of the stock. FIFO (first in - first out) and Moving Average. To understand this topic in detail, please visit [Item Valuation, FIFO and Moving Average](/erpnext/calculation-of-valuation-rate-in-fifo-and-moving-average).
- **Standard Selling Rate**: When *creating* an Item, entering a value for this field will automatically create an [Item Price](/erpnext/item-price) at the backend. Entering a value after the Item has been saved will not work. In this case, the Item Price is created from any transactions with the Item. The rate at which you'll sell the item. This will be fetched in Sales Orders and Sales Invoices.
- **Is Fixed Asset**: Tick this checkbox if this item is a company Asset. Check out the [Asset Module](/erpnext/asset) to know more.
- **Auto Create Assets on Purchase**: If Item is a Company Asset, tick this checkbox if you want to auto-create assets while purchasing this item through [Purchase Cycle](/erpnext/purchase-order). Check out the [Asset Page](/erpnext/asset) to know more.
- **Allowance Percentage**: This option will be available only when you create and save the item. This is the percent by which you will be allowed to over-bill or over-deliver this Item. If not set, it will select from [Stock Settings](/erpnext/stock-settings#3-limit-percent).
- **Uploading an Image**: To upload an image for your icon that will appear in all transactions, save the partially filled form. Only after your file is saved the 'Change' button will appear on the Image icon. Click on Change, then click on Upload, and upload the image.

For India:

- **HSN/SAC**: Harmonized System of Nomenclature (HSN) and Service Accounting Code (SAC) for GST. These numbers are defined by the government and different Items fall under different codes. New HSN codes can be added if not present in the list.
- **Is nil rated or exempted**: For an Item that is under GST, but no tax is applied to it. Eg: Cereals.
- **Is Non GST**: For an item that is not covered under GST. Eg: petrol.

---

### 3.1 Brand and Description

- **Brand**: If you have more than one brand, save them under Selling > Brand and pre-select them while filling a New Item.
- **Description**: Description of the item. The text from the Item Code will be fetched by default.

![](/files/item_desc.png)

### 3.2 Barcodes

Barcodes can be recorded in Items to quickly scan and add them in transactions. In the Barcodes table, you can add an Item's [barcode for scanning](/erpnext/track-items-using-barcode). There are two types of barcodes in ERPNext:

- **EAN**: The European Article Number is a 13-digit number. EAN is used internationally and recognised by more POS systems.
- **UPC**: The Universal Product Code is a 12-digit number. UPC is generally used only in the USA and Canada.

### 3.3 Inventory

- **Shelf Life In Days**: This is for a product [Batch](/erpnext/batch). The number of days after which the product batch will be unusable. For example, medicines.
- **End of Life**: For a single item/product, the date after which it'll be completely unusable. That is, the item will be unusable in transactions and manufacturing. For example, you're using plastic crystals for manufacturing Items for the next 5 years, after which you want to use plastic beads.
- **Warranty**: To track a warranty period, it is necessary that the Item is serialised. When this Item is delivered, the delivery date and the expiry period is saved in the Serial Number master. Through the serial number master, you can track the warranty status.

A warranty period is a time period in which a purchased product may be returned or exchanged.

![](/files/item_inv.png)

- **Weight UOM:** The Unit of Measure for the item. This can be Nos, Kilo, etc. The Weight UoM which you use internally can be different from the purchase UoM.
- **Weight Per Unit**: The actual weight per unit of the item. Eg: 1 kilo of biscuits or 10 biscuits per pack.
- **Default Material Request Type**: When you create a new Material Request for this item, the field set here will be selected by default in the new Material Request. This is also known as an 'indent'.
- **Valuation Method**: Select the Valuation Method, whether FIFO or Moving Average. Read [Item Valuation methods](/erpnext/calculation-of-valuation-rate-in-fifo-and-moving-average) to know more.
- **Allow negative stock**: When checked, the item will be allowed to go negative even if negative stock is disabled from Stock Settings. This is useful if you don't want to enable negative stock on high-value items, but a few select low-value items are allowed to go negative for a few days.

### 3.4 Automatic Reordering

When the stock of an item dips under a certain quantity, you can set an automatic reorder under 'Auto Reorder' section. This should be enabled in [Stock Settings](/erpnext/stock-settings#9-automatic-material-request). This will raise a [Material Request](/erpnext/material-request) for the Item. The user with roles Purchase Manager and Stock Manager will be **notified** when the Material Request is created.

- **Check in (group)**: In which group of warehouses to check the quantity of the item?
- **Request for**: Which warehouse to stock the item reorder.
- **Re-order Level**: When this quantity is reached, the reorder will be triggered. The reorder level can be determined based on the lead time and the average daily consumption. For example, you can set the reorder level of Motherboard at 10. When only 10 Motherboards are remaining in stock, the system will either automatically create a Material Request in your ERPNext account.
- **Re-order Qty**: The number of units to be reordered so that the sum of ordering cost and holding cost is at its minimum. The re-order quantity is based on the 'Minimum Order Qty' specified by the supplier and many other factors.

For example, If reorder level is 100 items, your reorder quantity may not necessarily be 100 items. The Reorder quantity can be greater than or equal to the reorder level. It may depend upon lead time, discount, transportation and average daily consumption.

- **Material Request Type**: The [Material Request](/erpnext/material-request) type with which the stock will be reordered. This depends on whether you buy the Item, manufacture it yourself or transfer it between Warehouses.

![](/files/item_reorder.png)

> **Note**: The Material Request is created at 12 midnight depending on the set reorder level.

### 3.5 Multiple Units of Measure

You can add alternate UoMs for an Item. If the default UoM in which you sell is numbers (NoS) but you receive it in Kilos, you can set an additional UoM with an appropriate conversion factor. For example, 500 Nos of screws = 1 Kilogram, so select Kilogram/Litre as UOM and set the conversion factor as 500. To know more about selling in different UoM, visit [this page](/erpnext/Selling-in-different-UOM).

### 3.6 Serial Numbers

> Allow Negative Stock has removed for Serial / Batch Items from version 15. So from version 15 users won't be able to make negative stock transactions for serial /batch items even though Allow Negative Stock has enabled in the Stock Settings.

With Serial Numbers, you can track warranty and returns. In case any individual Item is recalled by the supplier, the number system helps track that Item. The numbering system also manages expiry dates.

Please note that if you sell your items in thousands and they are very small, such as pens or erasers, you do not need to serialise them.

In ERPNext, you will have to mention the Serial Number in some accounting entries. If your product is not a major consumer durable Item, has no warranty, and has no chance of being recalled, avoid providing serial numbers.

### 3.7 Batches

> Allow Negative Stock has removed for Serial / Batch Items from version 15. So from version 15 users won't be able to make negative stock transactions for serial /batch items even though Allow Negative Stock has enabled in the Stock Settings.

A set of Items can be manufactured in batches. This is useful for moving the batch and associating an expiry date with a certain batch.

- **Has Batch No**: Options for batch number, expiry date, and retaining sample stock will be revealed on ticking this checkbox. You cannot activate this if there is any pre-existing transaction for this item. If this is disabled, you'll have to enter the serial numbers manually for every transaction.
- **Batch Number Series**: Prefix that'll be applied to batch numbers. If you set 5x1SCR, then the first batch will be named like 5x1SCR00001 on the first transaction/manufacture.
- **Automatically Create New Batch**: If the batch number is not specified in transactions, it will be automatically created in a format like AAAA.00001. If you always want to manually create a batch number for this item, leave this field blank. This setting will override 'Naming Series Prefix' in Stock Settings. Batch numbers can be set to be generated automatically if you manufacture the items, or can be entered manually if they come from an external manufacturer.
- **Has Expiry Date**: If you tick this, the batch number will be created according to the expiry date. The expiry dates can be set in the 'Batch' master.
- **Retain Sample**: To retain a minimum number of sample stock of the item. You need to set a Sample Retention Warehouse in Stock Settings for this. To know more, [click here](/erpnext/retain-sample-stock).
- **Has Serial No**: This is similar to the Batch Number Series; it'll be created when you make transactions/manufacture. If you set Serial Number Series as AA, then on the first transaction, a serial number like AA00001 will be created.

> Tip: While entering an Item Code in an Items table, if the table requires inventory details, then depending on whether the entered item is batched or serialized, you can enter serial or batch numbers right away in a pop-up dialog.

![](/files/item_bat_ser.png)

> **Note**: Once you mark an item as serialized or batched or neither, you cannot change it after you have made a Stock Entry.

To know more, visit the [Stock Reconciliation](/erpnext/stock-reconciliation) page.

### 3.8 Variants

An Item Variant is a different version of an Item. To learn more about managing variants, see [Item Variants](/erpnext/item-variants).

### 3.9 Item Defaults

In this section, you can define Company-wide transaction-related defaults for this Item.

- **Default Warehouse:** This is the Warehouse that is automatically selected in your transactions with this item.
- **Default Price List:** Whether Standard Selling or Standard Buying. Likewise, you can also set the purchasing and selling default accounts
- **Supplier**: If a default supplier is set, this supplier will be selected for new purchase transactions.
- **Default Expense Account:** It is the account in which cost of the Item will be debited.
- **Default Income Account:** It is the account in which income from selling the Item will be credited.
- **Default Cost Center:** It is used for tracking expense for this Item.

> Tip: You can add more rows for multiple companies.

![](/files/item_def.png)

### 3.10 Purchase, Replenishment Details

- **Default Purchase Unit of Measure**: The default UoM that will be used in Purchase transactions.
- **Minimum Order Qty**: The minimum quantity required for purchase transactions like Purchase Orders. If set, the system will not let you proceed with the purchase transaction if the item quantity in the purchase transaction is lesser than the quantity set in this field.
- **Safety Stock**: “Safety Stock” is used in the report “Itemwise Recommended Reorder Level”. Based on Safety Stock, average daily consumption and the lead time, the system suggests Reorder Level of an item.

Reorder Level = Safety Stock + (Average Daily Consumption * Lead Time)

- **Last Purchase Rate**: The rate at which you last purchased this item using a [Purchase Invoice](/erpnext/purchase-invoice) will be displayed here.
- **Is Purchase Item:** If unticked, you won't be able to use this item in purchase transactions.
- **Is Customer Provided Item:** Checked if Item is provided by a customer and received through **Stock Entry > Material Receipt**. If Checked, **Customer** field is Mandatory as the default customer for **Material Request**. To know more visit [this page](/erpnext/customer-provided-items).
- **Lead time days:** Lead time days are the number of days between ordering the Item and it to reach the Warehouse.

### 3.11 Supplier Details

- **Delivered by Supplier (Drop Ship)**: If the item is delivered directly by the supplier to the customer, tick this checkbox. Read more [here](/erpnext/drop-shipping-in-erpnext).
- **Supplier Codes:** Track Item Code defined by the Suppliers for this Item. In the Purchase transactions, on selecting an Item, a Supplier Part No. will be fetched as well for the Supplier's reference. You can read more about it [here](/erpnext/maintaining-suppliers-part-no-in-item).

![](/files/itmepur.png)

![](/files/item_supp.png)

### 3.12 Foreign Trade Details

If you're sourcing the item from another country, you can set the details here.

- **Country of Origin**: The country from which you're sourcing the item.
- **Customs Tariff Number**: You can create a customs tariff number with a description and use it for reference here to share with custom agencies. Later it can be used to add in Delivery Notes.

### 3.13 Sales Details

- **Grant Commission**: Grant a commission to [Sales Person](/erpnext/sales-person) and [Sales Partner](/erpnext/sales-partner) when this item is sold. If disabled, the sales generated by this item will be ignored in the calculation of commission.
- **Default Sales Unit of Measure**: The default UoM that'll be fetched for sales transactions.
- **Max Discount (%)**: You can define the maximum discount in % to be applied to an item. Eg: if you set 20%, you cannot sell this item with a discount greater than 20%.
- **Is Sales Item**: If unticked, you won't be able to use this item in sales transactions.

![](/files/item_sales.png)

### 3.14 Deferred Revenue and Deferred Expense

You can enable deferred revenue or expense from the item. Once you tick the checkbox, you'll see options to set the Deferred Expense Account and the number of months through which the revenue/expense is deferred.

For example, consider a yearly gym membership, you pay the money upfront at once but the service is given throughout the year. For the gym owner, this is deferred revenue and for the customer, it is a deferred expense.

![](/files/item_defe.png)

Check out the pages on [Deferred Revenue](/erpnext/deferred-revenue) for more details.

### 3.15 Customer Details

The Customer may identify an Item with a different Item Code. this is Similar to [Supplier Code](/erpnext/item#311-supplier-details).

- **Customer Name**: Select a customer here.
- **Customer Group**: This will be fetched based on the Customer you selected in the previous field.
- **Ref Code:** A customer can identify this item with a different number. You can track Item Code assigned by the Customer for this Item. When you create a Sales Order, the Customer's Reference Code for this Item will be shown.

### 3.16 Item Tax

These settings are required only if a particular Item has a different tax rate than the rate defined in the standard tax Account.

You need to create a new 'Item Tax Template' or choose an existing one. For example, if you have a tax Account, “VAT 14%” and this particular Item is exempted from tax, then you select “VAT 14%” in the first column, and set “0” as the tax rate in the second column. Visit the [Item Tax Template](/erpnext/item-tax-template) page for more details.

![](/files/item_tax.png)

You can also set a [Tax Category](/erpnext/tax-category) for this Item.

### 3.17 Inspection Criteria

- **Inspection Required before Purchase**: If an inspection is mandatory before the item is purchased, i.e., before you generate Purchase Receipt, tick this checkbox.
- **Inspection Required before Delivery**: If an inspection is required at the time of delivery from your Supplier is mandatory for this Item, tick this checkbox. That is, before you generate a Delivery Note.
- **Quality Inspection Template**: If a Quality Inspection is prepared for this Item, then this template of criteria will automatically be updated in the Quality Inspection table of the Quality Inspection. Examples of Criteria are: Weight, Length, Finish, etc.

Quality Inspection can be done with Quick View and you need not go to a different page to update the details inspection in ERPNext.

Read [Quality Inspection](/erpnext/quality-inspection) to know more.

### 3.18 Manufacturing

- **Default BOM**: The default [Bill of Materials](/erpnext/bill-of-materials) used to manufacture this Item.
- **Supply Raw Materials for Purchase**: If you're subcontracting to a vendor, you can choose to provide them with the raw materials to manufacture the item using the default BOM.
- **Manufacturer:** Select the Manufacturer who manufactured this item.
- **Manufacturer Part Number:** Enter the manufacturer's assigned part number for this item.

![](/files/item_man.png)

### 3.19 Publishing Item on Website

> From Version 16 onwards, the Webshop app has been separated from the core ERPNext. To use the functionality of publishing items on a website generated from your ERPNext account, ensure that Frappe’s Webshop app is installed on the site.

**Show on Website**: Choose whether to show this Item on your website; click Action and choose "Publish in Website".

![](/files/Screenshot 2026-03-04 at 4.23.37 PM.png)

A new record called Website Item is created, containing additional details about the items, and is also published on the web view of the item.

![](/files/Screenshot 2026-03-04 at 4.23.45 PM.png)

The following fields will be found in the Website Item master.

*Weightage**: Items with higher weight will be displayed first on the website. The limit for the number you can enter here is very high.

- **Slideshow**: A slideshow can be displayed at the top of the page. Visit the [Homepage](/erpnext/homepage) page in the Website module to know more.
- **Image**: You can attach an image instead of a Slideshow.
- **Website Warehouse**: Select an existing warehouse or create a new one for transactions on your website. This Warehouse will be different from your offline Warehouses. Stock for any online transactions will be deducted from the Warehouse set under Website Warehouse.
- **Website Item Groups**: In this table, you can select existing or create new [Item Groups](/erpnext/item-group) to classify items on your website.
- **Set Meta Tags**: Meta tags help with SEO. See [Web Page](/erpnext/web-page) to know how to add them.

Visit [Manufacturing](/erpnext/manufacturing) and [Website](/erpnext/website) to understand these topics in detail.

### 3.20 Website Specifications

This section is for configuring other details about the item.

- **Copy from Item Group:** The 'Website Specifications' details will be fetched as set in a specific Item Group chosen on the previous section (2.17).
- **Website Specifications**: Label and its description for the item. For example, 'Warranty: 1 year'.
- **Website Description**: This will appear on the item page.
- **Website Content**: (*Introduced in v12*) You can create additional styling, etc., use Bootstrap 4 markup to display on the item page.

### 3.21 Hub Publishing Details

The hub is a free online marketplace where Suppliers and Customers can transact. If both parties are on ERPNext, the transactions happen seamlessly. You can visit the hub at: [https://hubmarket.org](https://hubmarket.org).

- **Publish in Hub**: Choose if you want to publish your item on [https://hubmarket.org/](https://hubmarket.org/). It is a free marketplace. If your supplier/customer is also on ERPNext, the transactions will be seamless. For example, on creating a Purchase Order from your end, a Sales Order will be created on the Supplier's end.
- **Hub Warehouse**: This is a separate Warehouse to maintain the stock for your hub transactions.
- **Synced With Hub**: Sync item and other details with the hub when transactions take place.

4. Video

---

### 5. Related Topics

1. [Item Price](/erpnext/item-price)
2. [Item Codification](/erpnext/item-codification)
3. [Item Variants](/erpnext/item-variants)
4. [Item Group](/erpnext/item-group)
5. [Item Attribute](/erpnext/item-attribute)
6. [Item Valuation FIFO And Moving Average](/erpnext/calculation-of-valuation-rate-in-fifo-and-moving-average)
