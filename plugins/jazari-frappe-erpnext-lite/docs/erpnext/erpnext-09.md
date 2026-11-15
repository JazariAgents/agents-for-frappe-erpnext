<!-- Frappe documentation: erpnext, part 9 of 18. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__item-creation-not-required-in-purchase-invoice.md -->
---
title: "Purchase invoice for Services"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-creation-not-required-in-purchase-invoice"
updated: "2026-03-02"
---

### **1. Set Up Supplier**

1. **Navigate to Suppliers:**


	* Go to **Buying > Supplier**.
2. **Create New Supplier (if not already created):**


	* Click on **New**.
	* Enter the supplier's details (name, contact information, address).
	* Save the supplier record.

### **2. Create a Service Item**

1. **Navigate to Item Master:**


	* Go to **Stock > Item**.
2. **Create New Item:**


	* Click on **New**.
	* Enter the item code and name.
	* Under the **Item Group** field, select or create a group for services.
	* Set the **Item Type** to **Service**.
	* Fill in other relevant details, such as unit of measure and description.
	* Save the item record.

### **3. Create a Purchase Invoice**

1. **Navigate to Purchase Invoice:**


	* Go to **Buying > Purchase Invoice**.
2. **Start a New Invoice:**


	* Click on **New**.
3. **Enter Basic Information:**


	* **Supplier:** Select the supplier from whom the service was received.
	* **Invoice Date:** Enter the date of the invoice.
	* **Reference Number:** Input any reference number provided by the supplier.
4. **Add Service Details:**


	* **Items Section:** Click on **Add Item**.
	* **Select Service Item:** Choose the service item you created earlier.
	* **Description:** Provide a detailed description of the service.
	* **Rate and Quantity:** Enter the rate and quantity for the service.
	* **Taxes and Charges:** If applicable, add any taxes or additional charges.
5. **Account Details:**


	* **Expense Account:** Ensure the service expense is recorded in the appropriate expense account. This can be configured under the **Accounts** section of the invoice.
6. **Review and Save:**


	* Verify all details for accuracy.
	* Click **Save** to save the draft of the invoice.

### **4. Submit**

1. **Submit Invoice:**


	* Once the details are confirmed, click **Submit** to finalize the invoice.

![](/files/PU1Sggx.gif)  

<!-- page: erpnext/erpnext__item-group.md -->
---
title: "Item Group"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-group"
updated: "2026-03-06"
---

**An Item Group is a way to classify items based on types.**

Depending on the type of product, you can categorize an item under its respective field. If the product is service-oriented, assign it under the Item Group - service. If the product is used as a raw-material, assign it under the Raw Material category. In case, an item is used only in trading, you can categorize it under an Item Group called Trading.

To access the Item Group list, go to: 

> Home > Stock > Items and Pricing > Item Group

This is what the Item Group tree looks like: 

![](/files/item_groups.png)

## How to create an Item Group

---

1. Go to the Item Group list, click on New.
2. Select a group node under which you wish to create the Item Group, the default root is 'All Item Groups'.
3. Select 'Add Child' or click on the New button.
4. To make this child a category/group node, tick on Group Node.
5. Click on Create New.

Note:

- Nodes in different parts of the tree cannot have the same name.
- The child notes get alphabetically arranged

![](/files/item-group-new2af55d.gif)

### 1.2 Delete an Item Group

1. Select the Item Group you want to delete.
2. Select 'Delete'.
3. Click on Yes.
4. Features

---

To see the following options, click on an Item Group, click on Edit.

### 2.1 Parent Item Group

You can change the parent Item Group of an item by choosing another one under General Settings.

### 2.2 Defaults

- **Default Price List**: A default price list that'll determine the Item Prices for this Item Group.
- **Default Warehouse**: The default Warehouse is set in transactions for the items that belong to this group.
- **Default Buying/Selling Cost Centre**: The default Buying/Selling Cost Centre to which items in this group will be billed against.
- **Default Expense/Income Account**: The default accounts for items that belong to this group.
- **Default Supplier**: On setting a Supplier here, this supplier will be chosen in purchase transactions by default for items in this group.

### 2.3 Item Tax

A default item tax template will be applied to all items belonging to this group. Similarly a Tax Category can also be selected, visit [Quotation](/erpnext/quotation) to know more about Tax Categories.

### 2.4 Website Settings

- **Show in Website**: Items belonging to this group will be shown on your website under the Item Group.
- **Weightage**: This is the weight for the Item Groups themselves, item groups with higher weights will be shown first.
- **Slideshow**: A slideshow for the Item Group, just like in an Item. Visit the [Homepage](/erpnext/homepage) page in Website module to know more.
- **Description**: This will appear on the Item Group page.
- **Website Specifications**: Label and its description for an item group.

<!-- page: erpnext/erpnext__item-price.md -->
---
title: "Item Price"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-price"
updated: "2026-03-06"
---

**Item Price is the record in which you can log the selling and buying rate of an item.**

---

There are two ways to reach a new Item Price form:

**Selling/Buying/Stock > Items and Pricing > Item Price > New**.

Or

**Stock > Item > Click on "+" next to Item Price**.  
2. Select the Item. The name, UoM and description will be fetched.  
3. Select the Price List, whether Selling/Buying price or any other price list you may have created.  
4. Enter the actual rate in the Rate field.  
5. Save. 

![](/files/item-price.png)

### 1.1 Selecting the Price List

You can create multiple Price Lists for one Item in ERPNext to track the Selling and Buying Price of an Item separately. Also, if the Item's selling prices change based on Territory or due to other criteria, you can create multiple Selling Price Lists for it.

On selection of Price List, its currency and applicability, whether for selling/buying or both, will be fetched as well. To have Item Price fetching in the sales or purchase transaction, you should have 'Price List' selected in the transaction under Currency and Price List.

To check all Item Prices together, go to:

**Stock > Stock Reports > Item Price Stock**

Visit the [Price Lists](/erpnext/price-lists) page to know more.

---

## 2. Features

### 2.1 Unit of Measurement (UOM)

A price is always specific to a certain UOM. For example, $1 *per KG* or $80 *per hour*. By default, the **Item Price** will fetch the item's *Default Unit of Measure*. You can change it to any UOM from the item's UOM table.

For example, if Rice is sold in 1 KG and 500-gram packets, then you can mention the UOM ("KG" or "grams") in the **Item Price**, and the correct price will be applied based on the UOM selected in the transaction.

### 2.2 Packing Unit

This is the quantity that must be bought or sold per unit of measure. For example, if the Packing Unit is two, and the UOM is one, two items in quantity will be transacted. The default is 0; you can use non-integer UoM like 1.5 kg oats for 1 Packing Unit. If you leave it as 0, it'll not affect any transaction.

### 2.3 Minimum quantity

This is the minimum quantity of items to be transacted for this price to be applicable and updated in the Item Price list.

### 2.4 Applying Price List to a specific Customer/Supplier

If you select a Selling Price list, a customer field will appear where you can assign this Item Price to a specific customer. Likewise, if you select a Buying Price List, a Supplier field will appear where you can select a specific Supplier

### 2.5 Applying Price List to a Specific Batch

You can also link a specific batch to an Item Price, and on the selection of that batch in the transaction, the item price for that specific batch will be applied.

### 2.6 Validity

There are two fields here, ' Valid From' and 'Valid Upto'. Valid from is set to the date you created the Item Price; you can also set the Valid Upto date on which the Item Price will expire.

### 2.7 Lead Time in days

The approximate number of days it takes the product to reach the warehouse. You can set different Item Prices based on how long it takes the same product to reach you from different vendors.

### 2.8 Note

You can add any note about the Item Price in this field.

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

<!-- page: erpnext/erpnext__item_group_wise_product_listing.md -->
---
title: "Item Group-wise Product Listing"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item_group_wise_product_listing"
updated: "2026-03-02"
---

Similar to the [Product Listing](/erpnext/product-listing) at `/all-products`, ERPNext offers Product Listings that are Item Group-wise as well. You can link these pages on your landing page to direct users easily.

### Setting Up an Item Group Page
To provide a Product Listing page for an Item Group (e.g. Products), go to:

> Item Group List > Products

- Enable **Show in Website**.
- Scroll down to the **Website Filters** section and add field and attribute filters similar to E Commerce Settings.
- You can also add a description in the RichText Editor that will show above the product list as a banner.

Now if you click on the **See on Website** link, on the top left, above the image in the current document, you will be redirected to the **Products** Item Group's listing page.

#### Product Visibility
Consider the Item Group **Products** has child Item Groups **Mobile Services** and **Mobiles**. 

Website Items that will be visible on the **Products** page are:

- Those having **Products** as their Item Group
- Those having **Products** in their **Website Item Groups** table.

Website Items having their Item Groups as **Mobile Services** or **Mobiles** will be visible on their respective pages. These pages will be linked in the **Products** page.

> Child Item Groups such as **Mobile Services** and **Mobiles** will be visible as pills above the search bar on the **Producst** page.

![Item Group-wise Product Listing](/files/item-group-page.png)

<!-- page: erpnext/erpnext__job-card-summary.md -->
---
title: "Job Card Summary\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/job-card-summary"
updated: "2026-02-26"
---


To access the Job Card Summary, go to:

> Home > Manufacturing > Reports > Job Card Summary

![Task](/files/job-card-summary.png)

This report will give information about the Job Card as well as their status. Using this report users can check the month's Open and Completed Job Cards for the selected periods.

<!-- page: erpnext/erpnext__job-card.md -->
---
title: "Job Card\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/job-card"
updated: "2026-05-20"
---

**A Job Card stores actual production information about a particular Operation performed on a particular Workstation.**

A Job Card is created from the Work Order and given to each of the Workstations in the manufacturing floor to start the production of an item with a certain quantity in each of the operations defined in the Work Order.

Job Card allows each Operation's workstation to issue a “Material Request” and “Stock Transfer to Manufacture” for raw material required against a “Job Card”.

Job Card completion will change the production status in Work Order, we can track the completion of production progress for each of the Operations defined in the Work Order.

![Work Order](/files/manufacturing-flow-jc.png)

To access the Job Card list, go to:

> Home > Manufacturing > Production > Job Card

## 1. Prerequisites

Before creating and using a Job Card, it is advised that you create the following first:

- [Bill Of Materials](/erpnext/bill-of-materials)
- [Operation](/erpnext/operation)
- [Workstation](/erpnext/workstation)
- [Work Order](/erpnext/work-order)

## 2. How to Create a Job Card

Job Card for Operations is automatically created when a Work Order is submitted.

This is what a Job Card looks like:

![Job Card](/files/job-card.png)

To use a Job Card follow these steps:

1. Click on the Start Job button, then on Complete Job when you're done.
2. Alternatively, you can also fill the From Time and To Time in the Time Logs table.
3. Select the Employee to whom the Job Card was assigned.
4. Enter the Completed Quantity. This is the number of Items on which the Operation was performed for the selected time interval.
5. Add more rows in the Time Logs table and record time using the Start/Completed buttons.
6. Click on Submit.

In a Work Order, the Operations and Workstations are fetched from the BOM of an Item. For ease of use, you should ensure that the [Routing](/erpnext/routing) is configured in the BOM.

Each Job Card created will have Workstation & Operations assigned. The raw material required from each Source Warehouse will be calculated based on quantity required for production.

On submitting a Work Order, Job Cards will be auto-created based on the values in the Operations table.

![Create Shareholder](/files/work-order-job-card-creation.gif)

### 2.1 Select Work Order with Item to Manufacture

You can select 'Transfer Material Against' as 'Job Card' on the Bill of Materials to transfer raw materials for Production against Job Cards.

In the Work Order, you can select the option:

![Create Shareholder](/files/work-order-transfer-against-job-card.png)

### 2.3 Using a Job Card

Employee assignment and timing detail will also be defined in Job Card. The time taken to do a job can be recorded. If multiple employees are working on the same Operation, add new job cards by clicking on the 'Create Job' Card button.

![Create Shareholder](/files/job-card-form.png)

### 2.4 Material Request against Job Card

A Material Request will be raised from the Job Card as a basis/order to prepare raw material required for the manufacturing process. The Material Request raised will have its reference to the original Job Card number.

![Create Shareholder](/files/material-request-against-job-card.png)

Track the Manufacturing Progress in The Work Order by The Completion of Each Operations defined in Work Order.

Job Card completion allows you to track the manufacturing progress inside the Work Order by looking at the completion of each Operation related to the Work Order.

![Work Order Job Card Completion](/files/work-order-job-card-completion.png)

### 2.5 Scrap Items

While completing the operations, there might be chances that some scrap materials will be produced. This scrap materials are required to be added in the inventory. For that user needs to put the details of the scrap items in the job card. User can also set the defective materials / broken materials in the scrap items table.

![Work Order Job Card Completion](/files/job_card_scrap_item.png)

## 3. Features

### 3.1 Tracking Quality Inspection

> Introduced in Version 13

For production orders, the quality of in-process (semi-finished) goods also needs to be tracked. It is defined by the process (operation) performed on it which is in turn defined in the Job Card. In-process tests are different than incoming and outgoing material tests. Monitoring quality during manufacturing helps to make sure that the finished product produced is of the desired quality. You can create a Quality Inspection for the Production Item against the Job Card.

![Quality Inspection Against Job Card](/files/qi-against-job-card.png)

![Quality Inspection link in Job Card](/files/qi-link-in-job-card.png)

## **Pending Qty in Job Card**

A new **Pending Qty** field has been introduced in the **Job Card (in Version 16)** to handle partial production and prevent incorrect Process Loss calculation.



#### Problem

Previously, while completing a Job Card, the system automatically considered the **remaining quantity** as **Process Loss Qty**. This caused issues in cases where the operation was only partially completed, preventing users from submitting the Job Card.

#### Solution

To support partial completion, a **Pending Qty** field has been added to the Job Card.

- Users can now specify the quantity that is still pending for the operation. 
- The system will **not treat the remaining quantity as Process Loss** if a **Pending Qty** is specified. 
- **Process Loss Qty** will be calculated **only when the Pending Qty is zero**, indicating that the operation is fully completed.



#### Example

- Qty to Manufacture: **10** 
- Completed Qty: **6** 
- Pending Qty: **4**





In this case, the system will **not calculate Process Loss Qty**, as the remaining quantity is marked as pending.



If:

- Qty to Manufacture: **10** 
- Completed Qty: **6** 
- Pending Qty: **0**



Then the remaining quantity (**4**) will be treated as **Process Loss Qty**.



This enhancement allows users to perform **partial production tracking** without affecting Job Card submission.



![](/files/Screen Recording 2026-05-20 at 2.07.12 PM.mov)







For more details, refer the [Quality Inspection](/erpnext/quality-inspection) page.

<!-- page: erpnext/erpnext__journal-entry-template.md -->
---
title: "Journal Entry Template | ERPNext Documentation"
description: "Learn how to create and use Journal Entry Templates in ERPNext to preload recurring accounts, dimensions, entry settings, and other accounting details."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/journal-entry-template"
updated: "2026-08-03"
---

A Journal Entry Template stores the structure of a recurring [Journal Entry](https://docs.frappe.io/erpnext/journal-entry). It can prefill the company, entry type, naming series, opening-entry setting, multi-currency setting, and account rows. Use a template when the same accounts and dimensions recur, but the amount, date, reference, or remark changes each time.



For example, Nova Electronics Trading pays office maintenance from its operating bank account every month. A template can preload **Office Maintenance Expenses** and **Nova Operating Bank**, while the accountant enters the actual amount and reference for that month.

Templates reduce repetitive selection and help users choose the intended accounts consistently. They do not post to the [General Ledger](https://docs.frappe.io/erpnext/general-ledger) by themselves. The resulting Journal Entry must still be reviewed, balanced, saved, and submitted.

## Before you begin

Confirm that:

1. The accounts exist in the company’s [Chart of Accounts](https://docs.frappe.io/erpnext/chart-of-accounts).
2. Each account is a ledger account, not a group account.
3. You know which account should be debited and which should be credited for the recurring transaction.
4. Any required [Cost Center](https://docs.frappe.io/erpnext/cost-center), [Project](https://docs.frappe.io/erpnext/project), or other [Accounting Dimension](https://docs.frappe.io/erpnext/accounting-dimensions) is available.
5. If the template uses accounts in different currencies, [multi-currency accounting](https://docs.frappe.io/erpnext/multi-currency-accounting) is configured.

## Create a Journal Entry Template

To open the list, search for **Journal Entry Template** from the Awesome Bar. Select **Add Journal Entry Template** or open an existing template.



![A Journal Entry Template list showing Monthly Office Maintenance highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-journal-entry-template-journal-entry-template-list.png)

Enter a clear **Template Title** that identifies the recurring purpose, such as `Monthly Office Maintenance`.

Select the **Journal Entry Type**, **Series**, and **Company**. Set **Is Opening** to **Yes** only when the resulting Journal Entry records an opening balance. Enable **Multi Currency** when the template uses an account whose currency differs from the company currency.



![Journal Entry Template fields for entry type, company, and naming series](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-journal-entry-template-journal-entry-template-details.png)

In **Accounting Entries**, add the accounts that should be copied to each Journal Entry. Do not enter transaction amounts in the template. Amounts belong to the actual Journal Entry because they can change for every occurrence.

Select the pencil icon to edit a row and add its Party, Cost Center, Project, or other dimensions when required.



![Accounting Entries with the row edit pencil highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-journal-entry-template-journal-entry-template-account-rows.png)



![A Journal Entry Template account row editor with the Account field highlighted](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-journal-entry-template-journal-entry-template-row-editor.png)

Save the template.

## Important fields and what they mean


| Field                | What it controls                                                                   | Guidance                                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Template Title       | The name users select from a Journal Entry                                         | Use a purpose-based name, not a month or voucher number.                                                                |
| Journal Entry Type   | The intended kind of Journal Entry                                                 | Choose the type that matches the transaction. It can also influence defaults such as bank or cash behavior.             |
| Series               | The naming series copied to the new Journal Entry                                  | Use the company’s approved Journal Entry series.                                                                        |
| Company              | The company copied to the new Journal Entry                                        | Accounts in the template must belong to this company.                                                                   |
| Is Opening           | Marks the resulting entry as an opening entry                                      | Use this only for migration or opening balances. See [Opening Balance](https://docs.frappe.io/erpnext/opening-balance). |
| Multi Currency       | Allows accounts in currencies other than the company currency                      | Review exchange rates and account currencies in the resulting entry.                                                    |
| Account              | A ledger account copied into the Journal Entry                                     | Add at least two accounts so the resulting entry can be balanced.                                                       |
| Party Type and Party | Associates the row with a Customer, Supplier, Employee, or another supported party | Set these only when the selected account requires party-wise accounting.                                                |
| Cost Center          | Tracks income or expense by business unit                                          | Set a default here only if it applies to every entry created from the template.                                         |
| Project              | Tracks the row against a project                                                   | Leave it blank when the project changes each time.                                                                      |


## Choose the right entry type

The template supports the Journal Entry types available in the current ERPNext version, including Journal Entry, Inter Company Journal Entry, Bank Entry, Cash Entry, Credit Card Entry, Debit Note, Credit Note, Contra Entry, Write Off Entry, Opening Entry, Depreciation Entry, and Exchange Rate Revaluation.

The most commonly used choices are:


| Entry type                  | When it is useful                                                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Journal Entry               | General adjustments and recurring accruals where a more specific transaction is not available.                                                        |
| Bank Entry                  | A journal-based bank transaction. For routine customer and supplier payments, prefer a [Payment Entry](https://docs.frappe.io/erpnext/payment-entry). |
| Cash Entry                  | A journal-based cash transaction.                                                                                                                     |
| Opening Entry               | Opening balances during setup or migration. ERPNext marks **Is Opening** accordingly.                                                                 |
| Inter Company Journal Entry | Adjustments between companies. See [Inter Company Journal Entry](https://docs.frappe.io/erpnext/inter-company-journal-entry).                         |
| Exchange Rate Revaluation   | Adjustments arising from currency revaluation.                                                                                                        |


Selecting Bank Entry or Cash Entry on a normal Journal Entry can load the company’s default bank or cash account when the account table is still empty. A template can also store the intended account rows directly. Opening Entry identifies the voucher as an opening transaction, but it does not automatically add the entire Chart of Accounts. Add only the accounts needed for the opening entry.

## Create a Journal Entry from the template

1. Create a new Journal Entry.
2. Open the **More Info** tab.
3. Expand **Additional Info**.
4. Select the template in **From Template**.

![The From Template field highlighted in a new Journal Entry](https://novacompanies.m.frappe.cloud/files/docs-gl-correction-20260803-journal-entry-template-journal-entry-from-template.png)



![Monthly Office Maintenance entered in the From Template field](https://novacompanies.m.frappe.cloud/files/journal-entry-template-20260802-journal-entry-select-template.png)

ERPNext copies the template’s company, entry type, naming series, opening setting, multi-currency setting, and account rows into the new Journal Entry.



![A new Journal Entry with the template fields and account rows loaded](https://novacompanies.m.frappe.cloud/files/journal-entry-template-20260802-journal-entry-template-loaded.png)

Enter the debit and credit amounts, posting date, reference details, and remarks. Add or remove account rows if this occurrence needs them. Confirm that total debit equals total credit, then save and submit the Journal Entry.

## Important warning when selecting a template

Selecting **From Template** clears the existing **Accounting Entries** rows before loading the template’s rows. Choose the template before entering account rows, or copy any work you need to retain.

The template is a starting structure, not a lock. After it loads, you can add more accounts or change copied values before saving. Review every resulting Journal Entry because the template does not validate whether the accounts and dimensions remain appropriate for that month’s transaction.

## Maintain templates safely

Update a template when the recurring accounting treatment changes for future entries. Previously submitted Journal Entries are not changed when a template is edited.

Avoid creating several templates with nearly identical names. Use titles that describe the business event, such as `Monthly Office Maintenance`, `Payroll Accrual`, or `Bank Charges`. Keep one approved template for each recurring pattern and review it when the Chart of Accounts or dimension structure changes.

## Troubleshooting

### The From Template field is not visible

In a new Journal Entry, open **More Info** and expand **Additional Info**. The top-right **Templates** button is the general Frappe form-template feature. It is different from the ERPNext **Journal Entry Template** selected in the **From Template** field.

### The template does not appear in search

Confirm that the Journal Entry Template is saved and that you have permission to read it. Also confirm that the template’s company and accounts are available to your user.

### Existing account rows disappeared

This is expected when **From Template** is selected. ERPNext clears the current Accounting Entries before copying the template’s rows. Select the template first, then add occurrence-specific rows.

### An account cannot be selected

Confirm that it is a non-group ledger account belonging to the template’s company. Also check account currency restrictions when **Multi Currency** is not enabled.

### The Journal Entry is not balanced

The template copies account structure, not debit and credit amounts. Enter the amount on each row and ensure total debit equals total credit before saving.

## FAQs

### Does a Journal Entry Template create or submit entries automatically?

No, It only prefills a new Journal Entry. A user must add the current amounts and references, review the entry, and submit it.

### Can I change the accounts after loading a template?

Yes, You can edit, add, or remove rows before saving the Journal Entry. Treat the template as a reusable starting point.

### Can one template be used for several companies?

No, A template stores one company, and its accounts belong to that company. Create a separate template for each company when the same accounting pattern is needed.

### Should I store amounts in the template?

No, Journal Entry Template account rows define accounts, parties, and dimensions. Enter debit and credit amounts in each actual Journal Entry.

### Can a template include Cost Center or Project?

Yes, Add the dimension on the account row when it should apply every time. Leave it blank when the dimension changes for each transaction.

### Does editing a template update past Journal Entries?

No, Changes affect only entries created from the template after the change. Existing drafts and submitted entries retain their own values.

## Related topics

- [Finance Book](https://docs.frappe.io/erpnext/finance-book)
- [Immutable Ledger](https://docs.frappe.io/erpnext/immutable-ledger-in-erpnext)
- [Repost Accounting Ledger](https://docs.frappe.io/erpnext/repost-accounting-ledger)

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
![Journal Entry list showing the submitted office-maintenance example](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-list.png)
2. Select the **Company**, **Entry Type**, and **Posting Date**. For a general adjustment, keep **Entry Type** as **Journal Entry**.  
![Company and Entry Type selected on a new Journal Entry](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-company-type.png)
3. In **Accounting Entries**, add the account to debit and enter the debit amount. Add the offsetting account and enter the credit amount. Total Debit and Total Credit must be equal before submission.

  The grid shows the main columns. Select the highlighted pencil icon to open the complete row editor when you need Party, reference, currency, Cost Center, Project, or other row-level fields.
  ![Balanced Accounting Entries with the first row pencil icon highlighted](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-accounting-rows.png)
4. In the row editor, confirm the **Account** and enter either a debit or a credit, never both on the same row. In the example, Office Maintenance Expenses is debited by $845.  
![Account and debit fields in the Journal Entry row editor](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-row-editor.png)
5. Add a clear **User Remark** and, when applicable, a Reference Number, Reference Date, Bill Number, Bill Date, and Due Date. These supporting fields do not replace a formal link to an ERPNext document.
6. Save, review the accounts and dimensions, then submit. Submission posts the debit and credit to the General Ledger.  
![Submitted Journal Entry with balanced account rows](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-submitted.png)

## Create a Journal Entry with Quick Entry

Use **Quick Entry** for a straightforward two-account posting. Enter the amount, debit account, credit account, date, and remark. ERPNext fills the Accounting Entries table and saves the draft. Open the full form before submission when you need a Party, document reference, multiple rows, dimensions, or multiple currencies.



![Quick Journal Entry dialog with amount, debit account, and credit account highlighted](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-quick-entry.png)

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



![Ledger action highlighted in the View menu of a submitted Journal Entry](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-view-ledger-menu.png)

The report should show the same total debit and credit under the Journal Entry voucher. In this example, Office Maintenance Expenses is debited by $845 and Nova Operating Bank is credited by $845.



![General Ledger filtered to the submitted Journal Entry](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-general-ledger.png)

For very large entries with more than 100 account rows, current ERPNext can queue submission or cancellation in the background. Wait for processing to finish before relying on the ledger or financial reports.

## Correct or reverse a Journal Entry

Do not edit a submitted posting. If the original should be cancelled and corrected, follow the permitted cancellation and amendment process, subject to linked documents, frozen periods, and [Immutable Ledger](/erpnext/immutable-ledger-in-erpnext) rules.

Use **Actions &gt; Reverse Journal Entry** when the accounting correction should be recorded as a new posting with the debit and credit sides exchanged. Review the generated draft and its Posting Date before submission. On current develop versions, reversal entries are linked to their originals and protected from casual field changes.



![Reverse Journal Entry action highlighted on a submitted entry](https://novacompanies.m.frappe.cloud/files/journal-entry-20260802-journal-entry-reverse-action.png)

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
![](/files/z3sBK9F.png)  
 If this field is unchecked, the Purchase Invoices will not be fetched in the Landed Cost Voucher  
While creating against **Purchase Receipt**: The Item selected should have **Maintain Stock** checked.  
![](/files/vEwpm61.png)  
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

![Lead](/files/lead.png)

You can also record the details of the conversation in the NOTES section.

Further details like Lead Type, Market Segment, Industry can be added in the 'MORE INFORMATION' section.

If you have a healthy number of leads, all this information will help you prioritize the leads you can pursue.

You can assign the Lead to a user by clicking on 'Assign' button on left bar. You can also attach files/images by clicking on 'Attach File' button.

- Features

### Reminders to Follow Up on the Leads

It is important to reach out to leads from time to time and build the relationship. You can create a calendar event from the **Activities** tab for the user and a notification will be shown on that date.

### Adding Multiple Contacts and Addresses

In Busines-to-business(B2B) scenario, in order to close a sales deal, you will have to contact multiple people working in the prospective company. You can add the details of all such people in the same lead. Once you save a Lead, you will get the option to add [Contact](/erpnext/contact) details by clicking on 'New Contact' button. Similarly, you can add the [Address](/erpnext/address) details by clicking on 'New Address'.

![Multiple Contacts and Addresses in Lead](/files/multiple-addresses-and-contacts-in-lead.png)

### 3 Recording Comments, Emails and Events

- **Comments**: You can write your comment in 'Add a comment' box and select 'Comment'.
- **Emails**: You can send an email to the lead by clicking on the 'New Email' button and when the lead responds to your email, it will be appended to your email creating an email thread.
- **Events**: You can also records the Meetings, Calls etc you have had with the Lead by clicking on 'New Event'

### Creating Opportunity, Customer and Quotation

You can create an Opportunity, Customer or a Quotation from the Make dropdown. Relevant field values will be copied over.

### Auto-assigning the Leads to Sales Executives

> Introduced in Version 12

You can define [Assignment Rules](/erpnext/assignment-rule) to automatically assign the leads to sales executives.

![Lead Assignment Rule](/files/lead-assignment-rule.png)

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

![Screenshot 2023-12-28 at 10.30.48 AM](/files/Screenshot 2023-12-28 at 10.30.48 AM.png)

The system will allow you to maintain a list of various lead sources leveraged by you.

![Screenshot 2023-12-28 at 10.35.00 AM](/files/Screenshot 2023-12-28 at 10.35.00 AM.png)

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

![Use legacy controller for Period Closing Voucher in Accounts Settings](https://novacompanies.m.frappe.cloud/files/final-accounting-20260814-legacy-pcv-setting.png)



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

![Letter Head](/files/using-print-format.png)

In a Company master, if no Letter Head is set as default, then in the reports, Letter Head having Default field checked will be fetched.

![Letter Head](/files/using-print-format-1.png)

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

 ![Print Heading](/files/letter-head.png)

 > If you want to make this the default Letter Head, click on "Default Letter Head".

1. After entering values in the Header and Footer section, save the Letter Head.

You can set the Letter Head based on HTML to make changes to it:

![Letter Head based on](/files/letter-head-based-on.gif)

This is how the Letter Head looks in a document's print.

![Print Heading](/files/letter-head-1.png)

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
3. Marketing Developer Platform ![LinkedIn Developer App Product](/files/linkedin-dev-products.png)

### Configure Redirect URLs:

1. Goto your LinkedIn Developers App then **Auth** tab.
2. In **OAuth 2.0 settings** section add **Redirect URLs**: `https://{yoursite}/api/method/erpnext.crm.doctype.linkedin_settings.linkedin_settings.callback`
3. Click **Update** to make changes. ![LinkedIn Redirect URL](/files/linkedin-redirect-urls.png)
4. How to set up LinkedIn Settings

---

To access LinkedIn Settings, go to:

> Home > CRM > Settings > LinkedIn Settings

Current availability

This integration is deprecated. Confirm support in your ERPNext version and the current LinkedIn API requirements before configuring new credentials.



### Company ID

You get the Company ID from your LinkedIn Company URL. 

![LinkedIn Company ID](/files/linkedin-company-id.png)



### Consumer Key and Consumer Secret

You get **Consumer Key** and **Consumer Secret** from your LinkedIn Developer account go to:

> `https://www.linkedin.com/developers/` > My Apps > `{Your App}` > Auth

![LinkedIn Client](/files/linkedin-client.png)



Once you save the doc by filling **Company ID**, **Consumer Key**, and **Consumer Secret** it will redirect to LinkedIn's sign-in page by providing valid LinkedIn credentials and clicking Allow, the member approves your application's request to access their member data and interact with LinkedIn on their behalf. 

![Authorize LinkedIn](/files/authorize-linkedin.jpg)

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

![Add Customer/Supplier in Contact](/files/contact-link.png)
2. Now when an Email is sent to or received from the Contact associated with Customer or Supplier, that email is linked to the Customer or Supplier mentioned in the Links section of the Contact.

![With Filters](/files/email_aggregation.gif)

2. Automatic Email Linking to a Document
----------------------------------------

Automatic Email Linking links an Email to the Document specified in the unique Email Address generated by the system for a document. If an Email is sent or received using the unique Email Address, the system will link that Email to the Document.

1. Enable Automatic Email Linking in Email Account. This feature can be used only with one Email Account at a time.

![Add Customer/Supplier in Contact](/files/enable_email_link.png)
2. Once this feature has been enabled, you will see a unique Email ID generated using the Email ID mentioned in the Email Account.
3. Now you can copy the Email ID by clicking on it and you can send or receive Emails using the unique Email ID. If an Email contains this unique Email ID either in the Recipients or Cc section, the system will link that Email to the specified Document.

![Add Customer/Supplier in Contact](/files/email_link.gif)


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

 ![Lower Deduction Certificate](/files/lower-deduction-certificate.png)

## 3. Using Lower Deduction Certificate

### 3.1 Use in Purchase Invoice

In the following example, we have selected TDS category as 'TDS - 194D - Individual' which has a rate of 5%.

 ![Tax Withholding Category](/files/tax-withholding-category.png)

1. Set the Tax Withholding Category for the Supplier in the supplier master. Then upon selecting that Supplier, a checkbox will become visible in the Purchase Invoice to select whether to apply tax or not and the TDS category will be auto-fetched.

 ![Supplier With Tax Withholding Category](/files/supplier-with-tax-withholding-category.png)

1. Let's create an invoice for 20,000. Saving the invoice automatically calculates tax and appends it in the Purchase Taxes and Charges table. Although the tax category assigned to the supplier has a tax rate of 5%, the prevailing tax rate is 1% which is mentioned in the Lower Deduction Certificate.

 ![Lower TDS in Purchase Invoice](/files/lower-tax-withholding-in-purchase-invoice.png)

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

![](/files/GPSIGPX.png)* Once the loyalty program is set, you can create a Customer and link the Loyalty program to it.

![](/files/9Wphzgr.png)Once this Customer is linked to the Loyalty program, you can now setup your POS profile if it is not set yet:  
![](/files/Lw5UhFp.png)  
Now, you can go to POS transaction:* Select Customer
* Add items
* Pay
* Check the field --> **Redeem Loyalty Points**

![](/files/s2Jps8N.png)

<!-- page: erpnext/erpnext__loyalty-program.md -->
---
title: "Configure Customer Loyalty Programs | ERPNext Documentation"
description: "Set up ERPNext Loyalty Program tiers, earning and redemption factors, customer enrollment, point expiry, and Sales Invoice redemption."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/loyalty-program"
updated: "2026-07-25"
---

A Loyalty Program awards points from submitted sales and lets eligible Customers redeem those points on later [Sales Invoices](/erpnext/sales-invoice). Programs can use one tier or several tiers based on a Customer's cumulative eligible spend.

## Before you begin

Confirm:

- Eligible [Customers](/erpnext/customer), Customer Groups, and Territories.
- The Company currency and loyalty expense account.
- A Cost Center for redemption when required.
- A policy for earning, redemption value, expiry, returns, and tier upgrades.

Test point creation and accounting on the demo Company before enrolling Customers.

## Create a Loyalty Program

1. Open the Loyalty Program list and select **Add Loyalty Program**.
2. Enter the Program Name.
3. Select **Single Tier** or **Multiple Tier**.
4. Set From Date and To Date.
5. Restrict the Customer Group and Territory when required.
6. Enable **Auto Opt In** only when all eligible Customers should join automatically.
7. Add the tier rows.
8. Configure redemption and expiry.
9. Save.

![An ERPNext Loyalty Program with dates, eligibility, and enrollment settings.](https://novacompanies.m.frappe.cloud/files/loyalty-program-form.png)

## Configure tiers

![The Loyalty Program tier table with collection factors and thresholds.](https://novacompanies.m.frappe.cloud/files/loyalty-program-tiers.png)


| Field             | What it means                                           |
| ----------------- | ------------------------------------------------------- |
| Tier Name         | Label assigned when the Customer reaches the threshold  |
| Collection Factor | Eligible amount required to earn one point              |
| Minimum Amount    | Cumulative spend required for the tier                  |
| Auto Opt In       | Enrolls all Customers that match the program conditions |


Example: with a Collection Factor of $100, an eligible $1,000 invoice earns 10 points.

Minimum Amount is evaluated from cumulative eligible sales for the Customer, not only the current invoice.

## Configure redemption

Set:

- **Conversion Factor** for the monetary value of one point.
- **Expense Account** used for the loyalty benefit.
- **Cost Center** where required.
- **Expiry Duration** in days.

Keep earning and redemption factors distinct. A Customer might spend $100 to earn one point while each redeemed point is worth $1.

## Enroll a Customer

If Auto Opt In is disabled:

1. Open the Customer.
2. Select the Loyalty Program.
3. Save.

![A Customer assigned to the Nova Rewards Loyalty Program.](https://novacompanies.m.frappe.cloud/files/loyalty-program-customer.png)

## Earn points

Create and submit an eligible Sales Invoice. ERPNext creates a Loyalty Point Entry linked to the Customer and invoice.

Open **Loyalty Point Entry** to audit earned and redeemed points. Returns and cancellations can affect the available balance, so use the ledger rather than a manually maintained total.

## Redeem points

1. Create a Sales Invoice for the enrolled Customer.
2. Add the Items.
3. Open the Loyalty Points section.
4. Enable **Redeem Loyalty Points**.
5. Enter the number of points.
6. Confirm the Redemption Account and Cost Center.
7. Review the invoice total and submit.

The dot before an Item Code shows stock availability at a glance: green means in stock and red means out of stock.

## Troubleshooting


| Problem                              | What to check                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------------- |
| No points are earned                 | Confirm enrollment, program dates, eligibility, submitted invoice, and tier factor |
| Redeem Loyalty Points is unavailable | Confirm that the Customer has a program and available points                       |
| The tier is unexpected               | Review cumulative eligible spend and minimum thresholds                            |
| Points expired earlier than expected | Check Expiry Duration and the Loyalty Point Entry dates                            |
| Redemption accounting is incorrect   | Review the program's Expense Account and Cost Center                               |


## Frequently asked questions

### Can a program have several tiers?

Yes. Use Multiple Tier and add each threshold in ascending order.

### Are points awarded on draft invoices?

No. The earning workflow depends on submitted eligible invoices.

### Can every Customer be enrolled automatically?

Yes. Enable Auto Opt In and define the eligible Customer Group and Territory.

### Where can I audit a Customer's points?

Use Loyalty Point Entry and the Customer's linked records.

## Related topics

- [Customer](/erpnext/customer)
- [Sales Invoice](/erpnext/sales-invoice)
- [Sales Return](/erpnext/sales-return)
- [Applying a Discount](/erpnext/applying-discount)
- [Point of Sale](/erpnext/point-of-sale)

<!-- page: erpnext/erpnext__maintain-stock-field-frozen-in-item-master.md -->
---
title: "Maintain Stock field Frozen in the Item master\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintain-stock-field-frozen-in-item-master"
updated: "2026-02-26"
---


In the item master, you might witness values in the following fields to be frozen.

1. Maintain Stock
1. Has Batch No.
1. Has Serial No.

![Item Field Frozen](/files/maintain-stock-1.png)

For an item, once stock ledger entry is created, values in these fields will be frozen. This is to prevent user from changing the value which can lead to mis-match of actual stock, and stock level in the system of an item.

For the serialized item, since its stock level is calculated based on the count of available Serial Nos., setting Item as non-serialized mid-way will break the sync, and item's stock level shown in the report will not be accurate, hence Has Serial No. field is frozen.

To make these fields editable once again, you should delete all the stock transactions made for this item. For the Serialized and Batch Item, you should also delete Serial No. and Batch No. record for this item.

<!-- page: erpnext/erpnext__maintaining-suppliers-part-no-in-item.md -->
---
title: "Maintaining Supplier's Item Code In the Item master\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintaining-suppliers-part-no-in-item"
updated: "2026-03-02"
---


For each item, code assigned might differ from the code your supplier has given to that same item. ERPNext allows you to track Supplier's Item Code in the item master. Also you can fetch Supplier's Item Code in your purchase transactions, so that they can easily recognize item referring to their Item Code.

#### 1. Updating Supplier Item Code In Item

In the Item master, under Supplier Details section, enter Item Code as given by the Supplier to this item.

![Supplier Item Code](/files/supplier-item-code.png)

#### 2. Supplier's Item Code In Transactions

Each purchase transaction has field in the Item table where Supplier's Item Code is fetched. This field is hidden in form as well as in the Standard print format. You can make it visible by changing property for this field from [Customize Form.](/erpnext/customize-form.html)

Go to print view, click on Menu > customize, enter a new print format name, look for the Items table, click on the **Select columns** button in it. You'll see the following screen. Now select the "Supplier Part Number" checkbox.

![Supplier item part print format](/files/supplier-item-code-print-format.png)

Supplier Item Code will only be fetched in the purchase transaction, if both Supplier and Item Code selected in purchase transaction is mapped with value mentioned in the Item master.

![Supplier Item Code in transaction](/files/supplier-item-code-in-purchase-order.png)

<!-- page: erpnext/erpnext__maintenance-sales-orders.md -->
---
title: "Maintenance Sales Orders | ERPNext Documentation"
description: "Learn how to create Maintenance Sales Orders in ERPNext for service visits, maintenance schedules, recurring support, and follow-up activities."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintenance-sales-orders"
updated: "2026-07-23"
---

# Maintenance Sales Orders

A Maintenance Sales Order records an agreed maintenance service for a Customer. It uses the Sales Order workflow while enabling maintenance-related actions and allowing service invoicing without a stock delivery.

## Before you begin

Create the [Customer](/erpnext/customer), service [Item](/erpnext/item), and required serial-number or installation details. Confirm access to the maintenance documents used by your process.

## Create a Maintenance Sales Order

1. Open **Sales Order** and select **Add Sales Order**.
2. Select the Company and Customer.
3. Set **Order Type** to **Maintenance**.
4. Add the maintenance Item, quantity, rate, and service date.
5. Enable **Skip Delivery Note** when no stock delivery is needed.
6. Review taxes, payment terms, addresses, and terms.
7. Save and submit the order.

![A full-screen Maintenance Sales Order showing the Skip Delivery Note checkbox beside Order Type.](/files/sales-order-skip-delivery-note-full.webp)

Leave **Skip Delivery Note** disabled when the order includes goods that must be delivered through a [Delivery Note](/erpnext/delivery-note).

## Create maintenance documents

After submission, use the available **Create** actions. Depending on installed features and document state, these can include:

- a **Maintenance Schedule** to plan recurring service;
- a **Maintenance Visit** to record work performed;
- a **Sales Invoice** to bill the Customer.

Review generated documents and confirm the Customer, Items, dates, assigned personnel, serial numbers, and service details.

## Troubleshooting

### Skip Delivery Note is not visible

Confirm that **Order Type** is **Maintenance**. The checkbox is conditional.

### Maintenance actions are missing

Confirm that the order is submitted, required features are configured, and your role can create the target document.

## Frequently asked questions

### Can a Maintenance Sales Order include parts?

Yes, but use the delivery workflow for stock Items that physically leave your Warehouse.

### Is a Maintenance Schedule mandatory?

No. Use it when service must occur on planned dates. A one-time service may use only the documents required by your process.

## Related topics

- [Sales Order](/erpnext/sales-order)
- [Maintenance Schedule](/erpnext/maintenance-schedule)
- [Maintenance Visit](/erpnext/maintenance-visit)

<!-- page: erpnext/erpnext__maintenance-schedule.md -->
---
title: "Maintenance Schedule\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintenance-schedule"
updated: "2026-02-28"
---


**The Maintenance Schedule shows all upcoming Maintenance Visits.**

All machines require regular maintenance, especially those that contain a lot
of moving parts, so if you are in the business of maintaining those or have
some of them in your own premises, this is a useful tool to plan a calendar of
activities for its maintenance.

To create a new Maintenance Schedule go to:

> Home > Support > Maintenance > Maintenance Schedule

A Maintenance Schedule is usually created from a Sales Order of type 'Maintenance'.

![SO Maintenance Schedule](/files/so-maintenance-schedule.png)

## 1. Prerequisites
* [Customer](/erpnext/customer)
* [Item](/erpnext/item)

## 2. How to Create a Maintenance Schedule
1. Go to the Maintenance Schedule, click on New.
1. Select the Customer and the Items for which maintenance needs to be done.
1. Set the start and end dates.
1. Select a Periodicity to set how frequently the visits will happen. The options are "Weekly", "Monthly", "Quarterly", "Half Yearly", "Yearly" and "Random". Maintenance Schedule will get generated based on selected Periodicity. Selecting Random will generate random dates
1. The Number of Visits will be set as per the Periodicity selected. Eg: If you selected Weekly and set the whole month between the start and dates, 4 visits are ideal.
1. Select the Sales Person performing the visits.
1. Save.
1. After saving, click on the **Generate Schedule** button to generate a Maintenance Schedule.
1. Submit.

 ![Maintenance Schedule](/files/maintenance-schedule-1.png)

The **Generate Schedule** button will generate a separate row for each maintenance activity. Each Item in a Maintenance Schedule is allocated to a Sales Person.

When the document is Submitted Calendar events are created for the Sales Person User for each maintenance.

## 3. Related Topics
1. [Serial Number](/erpnext/serial-no)
1. [Warranty Claim](/erpnext/warranty-claim)
1. [Maintenance Visit](/erpnext/maintenance-visit)
1. [Sales Order](/erpnext/sales-order)

<!-- page: erpnext/erpnext__maintenance-visit.md -->
---
title: "Maintenance Visit"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintenance-visit"
updated: "2026-03-02"
---

**A Maintenance Visit is a visit made by an engineer to a Customer’s premise for maintenance work of an Item.**

To access the Maintenance Visit list, go to:


> Home > Support > Maintenance > Maintenance Visit
> 
> 

A Maintenance Visit is usually created from a Sales Order of type 'Maintenance'. ![SO Maintenance Visit](/files/so-maintenance-visit.png)  


1. Prerequisites
----------------

* [Customer](/erpnext/customer)
* [Item](/erpnext/item)

2. How to create a Maintenance Visit
------------------------------------

1. Go to the Maintenance Visit list, click on New.
2. The current date and time will be recorded, this can be edited.
3. Select the Customer.
4. Select the Maintenance Type whether Scheduled, Unscheduled, or Breakdown.
5. Set the completion status whether 'Partially Completed' or 'Fully Completed'.
6. Select the Item Code and Serial Number.
7. Enter a Description of the maintenance, select the Sales Person performing the maintenance, and enter the work done.
8. Save.

![Maintenance Visit](/files/maintenance-visit.png)

### 2.1 Additional Options when Creating Maintenance Visit

* **Customer Feedback**: You can record any feedback given by the Customer regarding this Maintenance Visit.
* The following fields will be fetched from the [Customer](/erpnext/customer) form:


	+ Customer Address
	+ Contact Person
	+ Territory
	+ Customer Group

3. Related Topics
-----------------

1. [Warranty Claim](/erpnext/warranty-claim)
2. [Maintenance Schedule](/erpnext/maintenance-schedule)
3. [Sales Order](/erpnext/sales-order)

<!-- page: erpnext/erpnext__maintenance.md -->
---
title: "Maintenance"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/maintenance"
updated: "2026-02-27"
---

The maintenance schedule and maintenance visits are vital parts of the ERPNext support module, ensuring that the ERP system remains operational, secure, and aligned with business needs over time. Efficient management of these aspects contributes to a reliable and optimized ERP environment for users.

* [Maintenance Schedule](/erpnext/user/manual/en/maintenance-schedule)
* [Maintenance Visits](/erpnext/user/manual/en/maintenance-visit)

<!-- page: erpnext/erpnext__make-a-colorful-gantt-chart.md -->
---
title: "Make A Colorful Gantt Chart\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/make-a-colorful-gantt-chart"
updated: "2026-03-02"
---


ERPNext allows users to add colours to certain documents for better visual cues and representation. A good example of this would be the [Event Calendar](/erpnext/how-to-sync-doc-types-with-calendar), where, for each event you can add a colour.

We will be doing so by customizing [Tasks](/erpnext/tasks) under Projects module.

## Steps To Add Colours To The Gantt Chart

1. Go to [Customize Form](/erpnext/customize-form) in the system and select *Task* in _Enter Form Type_ option. Alternatively, you can reach this screen by going to **Menu > Customize** from the Task list or form.

 ![customize-form](/files/project-gantt-customize-form-1.gif)

1. Add a new field in the doctype of fieldtype color.
1. Check *In List View* option.

 ![customize-form](/files/project-gantt-in-list.png)

1. Save the form, go back to the Task list, and reload.
1. When opening an existing or new Task, you should see a color field. Pick a color for the Task.

 ![customize-form](/files/project-gantt-pick-color.png)

1. Go back to the Task list and switch to Gantt view.

 ![customize-form](/files/project-gantt-colors.png)

<!-- page: erpnext/erpnext__making-custom-reports.md -->
---
title: "Making Custom Reports\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/making-custom-reports"
updated: "2026-03-06"
---


There are three kind of reports in ERPNext.

### 1. Report Builder

Report Builder is an in-built report customization tool in ERPNext. This allows you to define specific fields of the form which shall be added in the report. Also you can set required filters, sorting and give preferred name to report.


&lt;iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/TxJGUNarcQs?rel=0"&gt;
&lt;/iframe&gt;



### 2. Query Report

Query Report is written in SQL which pulls values from account's database and displays the same in the report. Though SQL queries can be written from front end, like HTML, it has been restricted for ERPNext cloud users. This is because it allows users with no access to specific report to fetch data directly from the database.

Check Purchase Order Item to be Received report in Stock module for example of a Query report. [Click here](https://frappeframework.com/docs/user/en/desk/reports/query-report) to learn how to create Query Report.

### 3. Script Report

Script Reports are written in Python and stored on server side. These are complex reports which involves logic and calculation. Since these reports are written on server side, customizing it from hosted account is not possible.

Check Financial Analytics report in Accounts module for an example of Script Report. [Click here](https://frappeframework.com/docs/user/en/desk/reports/script-report) to learn how to create Script Report.

&gt; Note: **Dynamic Filter** is available in Script Reports and Query Reports; however, not in the Report Builder.

<!-- page: erpnext/erpnext__making-fields-visible-in-print-format.md -->
---
title: "Customizing Field Visibility in Print Format\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/making-fields-visible-in-print-format"
updated: "2026-03-02"
---


Each transaction has a Standard Print Format. In the Standard format, only certain fields are displayed by default. If a user wants to display a particular field in the Standard format, it can be customized by using Customize Form tool.

Let's assume in the Sales order, we need to make Shipping Address field visible in the standard print format.

#### Step 1: Go to Customize Form

> Home > Customization > Form Customization > Customize Form

#### Step 2: Document Type

As per our scenario, Sales Order will be selected as Document Type.

![Document Type](/files/customize-make-fields-visible.png)

#### Step 3: Disable Print Hide

Click to open field to be made visible in the Standard Print Format. Disable **Print Hide** field.

![Uncheck Print Hide ](/files/customize-visible in print.gif)

#### Step 4: Update

Update Customize Form to save changed. Reload your ERPNext account, and then check Print Format for confirmation.

<!-- page: erpnext/erpnext__manage-foreign-exchange-difference.md -->
---
title: "Manage Foreign Exchange Difference | ERPNext Documentation"
description: "Record realized foreign-exchange gains or losses in ERPNext when an invoice and its payment use different rates."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manage-foreign-exchange-difference"
updated: "2026-08-14"
---

Because Nova Industries often receives international payments after invoicing, exchange rates can change before settlement.



Nova invoices a customer for EUR 1,200 when `1 EUR = 1.10 USD`, so the receivable is worth USD 1,320. When the customer pays, the rate is 1.15 and the bank receives USD 1,380. The USD 60 difference must be recorded instead of being hidden by changing the payment amount.



The [Payment Entry](/erpnext/payment-entry) settles this realized difference through the configured Exchange Gain/Loss account. This differs from [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation), which measures an unrealized change while a balance remains open. Use this page to record the settlement correctly and keep exchange movement separate from bank fees or write-offs.

## Example

Nova Electronics Distribution issues a EUR 1,200 [Sales Invoice](/erpnext/sales-invoice) when `1 EUR = 1.10 USD`.


| Event                  | EUR   | Rate | USD value |
| ---------------------- | -----: | ----: | ---------: |
| Invoice                | 1,200 | 1.10 | 1,320     |
| Receipt                | 1,200 | 1.15 | 1,380     |
| Realized exchange gain |       |      | 60        |


The Customer has paid the full EUR amount, so its EUR receivable becomes zero. The USD bank receives USD 1,380, while the original receivable carried USD 1,320. The USD 60 difference is a gain.

For a Supplier payment, the debit and credit direction changes. Whether the result is a gain or loss depends on the invoice and payment rates and whether the Company is receiving or paying the foreign currency.

## Before you begin

Complete [Multi Currency Setup](/erpnext/multi-currency-setup). The foreign Customer or [Supplier](/erpnext/supplier) should use a matching receivable or payable account, and the bank or cash account should have its actual currency.

In the [Company](/erpnext/company-setup), configure **Exchange Gain / Loss Account**. Review **Posting Date inheritance for exchange gain / loss** in [Accounts Settings](/erpnext/accounts-settings), which can use the Invoice, Payment, or Reconciliation Date according to current develop options.



![Posting-date setting for exchange gain or loss](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-accounts-settings-exchange-gain-loss-date.png)

Confirm the transaction date and approved rate in [Currency Exchange](/erpnext/currency-exchange), or verify the [provider settings](/erpnext/currency-exchange-settings).

## Create the Payment Entry

The safest route is to create the Payment Entry from the submitted invoice so the reference and outstanding amount are carried forward.

1. Open the submitted Sales Invoice or [Purchase Invoice](/erpnext/purchase-invoice).
2. Select Create &gt; Payment.
3. Confirm Payment Type, Company, Party Type, and Party.
4. Confirm the paid-from and paid-to accounts.
5. Enter the actual amount in each account currency.
6. Enter or verify the payment-date exchange rate.
7. Confirm the invoice in Payment References and its allocated amount.

The currencies are not independent choices on Payment Entry. They come from the selected accounts.



![EUR receivable and USD bank account currencies](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-payment-entry-two-account-currencies.png)



![EUR paid amount, USD received amount, and source rate](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-payment-entry-exchange-rates-and-amounts.png)

## Calculate the exchange difference

When the Payment Entry has a non-zero Difference Amount caused by the rate change, select **Set Exchange Gain/Loss**. ERPNext adds an adjustment row in Payment Deductions or Loss using the configured account. Review the row instead of assuming the label guarantees correct accounting.

The exact sign depends on the workflow. Validate it with the resulting debit and credit rather than forcing a positive or negative amount from memory.

Do not confuse these amounts:


| Difference                                             | Where it belongs                                 |
| ------------------------------------------------------ | ------------------------------------------------ |
| Exchange movement between invoice and payment          | Exchange Gain/Loss account                       |
| Bank fee charged by the bank                           | Bank Charges or another approved expense account |
| Intentional short payment not expected to be collected | Write Off account, subject to policy             |
| Withholding deducted by the Customer                   | Tax withholding workflow and account             |
| Rounding caused by precision                           | Round Off or approved difference handling        |


Several can occur in one payment, but each needs its own row and account. The Payment Entry should end with Difference Amount equal to zero before submission.

Save the Draft and review its preview before submission so finance can verify both account-currency amounts and the balancing Company-currency entry.

## Submit and verify

Submit the Payment Entry, then verify all of the following:

- the invoice outstanding amount is reduced or becomes zero;
- the foreign receivable or payable is cleared by the allocated foreign amount;
- the bank or cash account reflects the actual statement amount;
- the Exchange Gain/Loss account contains only the rate difference;
- the [General Ledger](/erpnext/general-ledger) debit and credit totals balance in Company currency;
- the [Accounts Receivable and Payable](/erpnext/accounts-receivable-and-payable) report agrees with the party statement.

If the payment was entered independently, use [Payment Reconciliation](/erpnext/payment-reconciliation) to allocate it to the invoice. Reconciliation can also generate an exchange difference depending on the account currencies, rates, and posting-date setting.

## Partial and multiple payments

Each payment can use its actual rate. A EUR 1,200 invoice may be settled by EUR 500 at one rate and EUR 700 at another. Each Payment Entry allocates only its portion and realizes the difference for that settlement. Do not change the original invoice rate to match the final bank statement.

When one payment settles multiple invoices, inspect each reference's allocated amount and exchange-rate treatment. Use Payment Entry or the appropriate bulk payment process, then verify that every invoice outstanding balance is correct.

## Advance payments

An advance can be recorded before an invoice exists. Its rate establishes the Company-currency value of the advance. When the advance is later allocated to an invoice, any difference may be recognized according to the reconciliation and posting-date settings. Keep the advance in the correct party account currency and avoid silently changing its historical rate.

## Troubleshooting

### The invoice still has a small outstanding amount after full foreign payment

Check the allocated amount, party account currency, payment rate, and whether the exchange difference was placed in Payment Deductions or Loss. Do not enter exchange differences in Advance Taxes and Charges.

### The bank amount is wrong after adding an adjustment

Separate bank fees, withholding, write-off, and exchange difference. Recalculate the paid and received amounts from the actual bank statement, then use distinct adjustment rows.

### Set Exchange Gain/Loss does not appear

Confirm there is a real currency difference, the Company account is configured, the document is Draft, and the selected accounts and references are correct. Field availability can depend on the Payment Entry state.

### The rate field is read-only

Review [Freeze Exchange Rate](/erpnext/exchange-rate-field-frozen), stale-rate settings, permissions, and the document status. A submitted transaction cannot be casually repriced.

## FAQs

### Should I edit the invoice rate when the bank pays at another rate?

No, keep the invoice rate that represented the invoice date. Use the payment rate and recognize the settlement difference.

### Is an exchange loss always an expense?

It is normally reported through the configured gain or loss account, but presentation depends on your chart and accounting policy. Use accounts approved by finance.

### Can a bank fee be combined with exchange loss?

No, record the bank fee separately so reporting and reconciliation remain clear.

### What if the payment is not linked to the invoice?

Reconcile the unallocated Payment Entry later. The party must match, and the outstanding and unallocated amounts determine what can be allocated.

### Is revaluation required after every payment?

No, a payment realizes its own difference. Revaluation is for eligible balances still open at a reporting date.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Multi Currency Accounting](/erpnext/multi-currency-accounting)
- [Currency Exchange](/erpnext/currency-exchange)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)

<!-- page: erpnext/erpnext__managing-batch-wise-inventory.md -->
---
title: "Managing Batch wise Inventory\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-batch-wise-inventory"
updated: "2026-02-27"
---


Set of items which has same properties and attributes can be group in a single Batch. For example, pharmaceuticals items are batch, so that it's manufacturing and expiry date can be tracked together.

To maintain batches against an Item you need to mention 'Has Batch No' as yes in the Item Master.

![Batch Item](/files/batchwise-stock-1.png)

You can create a new Batch from:

`Stock > Documents > Batch > New`

Read [Stock batch](/erpnext/batch.html) to learn more.

For the Batch item, updating Batch No. in the stock transactions (Purchase Receipt &amp; Delivery Note) is mandatory.

#### Purchase Receipt

When creating Purchase Receipt, you should create new Batch, or select one of the existing Batch master. One Batch can be associated with one Batch Item.

![Batch in Purchase Receipt](/files/batchwise-stock-2.png)

#### Delivery Note

Define Batch in Delivery Note Item table. If Batch item is added under Product Bundle, you can update it's Batch No. in the Packing List table as well.

![Batch in Delivery Note](/files/batchwise-stock-3.png)

#### Batch-wise Stock Balance Report

To check batch-wise stock balance report, go to:

Stock > Standard Reports > Batch-wise Balance History

![Batchwise Stock Balance](/files/batchwise-stock-4.png)

<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/J0QKl7ABPKM?rel=0">
</iframe>

<!-- page: erpnext/erpnext__managing-fractions-in-uom.md -->
---
title: "Managing Fractions in UOM\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-fractions-in-uom"
updated: "2026-02-26"
---

UoM stands for Unit of Measurement. Few examples of UoM are Numbers (Nos), Kgs, Litre, Meter, Box, Carton etc.

There are few UOMs which cannot have value in decimal places. For example, if we have television for an item, with Nos as its UoM, we cannot have 1.5 Nos. of television, or 3.7 Nos. of computer sets. The value of quantity for these items must be whole number.

You can configure if particular UoM can have value in decimal place or no. By default, value in decimal places will be allowed for all the UOMs. To restrict decimal places or value in fraction for any UoM, you should follow these steps.



### UOM List

For UOM list, go to:

`Stock > Setup > UoM`

From the list of UOM, select UOM for which value in decimal place is to be restricted. Let's assume that UoM is Nos.



### Configure

In the UoOM master, you will find a field called "Must be whole number". Check this field to restrict user from enter value in decimal places in quantity field, for item having this UOM.

![UoM Must be Whole No](/files/uom-fraction-1.png)

### Validation

While creating transaction, if you enter value in fraction for item whose UOM has "Must be whole number" checked, you will get error message stating:

`Quantity cannot be a fraction at row #`

![UoM Validation Message](/files/uom-fraction-2.png)

<!-- page: erpnext/erpnext__managing-invoice-discount-in-the-payment-entry.md -->
---
title: "Invoice Discount in Payment Entry | ERPNext Documentation"
description: "Record a settlement discount while clearing an ERPNext invoice."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-invoice-discount-in-the-payment-entry"
updated: "2026-08-01"
---

When a Customer pays less because an approved settlement discount applies, allocate the amount received and record the discount in the Deductions or Loss table. This clears the invoice without hiding the difference.

## Before you begin

Confirm the correct Company, currency, receivable or payable account, and bank or cash ledger. Use submitted source documents and keep the bank reference or remittance advice available.

## Use Invoice Discount in Payment Entry

1. Create a Receive Payment Entry and fetch the invoice.
2. Enter the amount received in the bank.
3. Allocate the full amount being settled against the invoice.
4. Add the discount difference with the approved discount account and Cost Center.
5. Confirm that the Difference Amount is zero, then submit.

![Invoice Discount in Payment Entry in ERPNext](https://novacompanies.m.frappe.cloud/files/payments-05-payment-entry-references.png)

## Important fields and what they mean


| Field              | What it controls                              |
| ------------------ | --------------------------------------------- |
| Allocated Amount   | Invoice amount cleared by the payment.        |
| Paid Amount        | Cash actually received.                       |
| Deductions or Loss | Accounting rows explaining the shortfall.     |
| Account            | Approved discount allowed account.            |
| Cost Center        | Business unit receiving the discount expense. |


## What happens after you submit or process

ERPNext updates the relevant accounting records and, where applicable, the outstanding or unallocated amounts. Review the General Ledger, party ledger, and source document status before treating the workflow as complete. A saved draft does not affect the ledger.

## Troubleshooting

### The invoice remains outstanding after recording a discount

The cash received plus the approved discount must equal the amount being settled. Allocate the full settlement and post the discount to the configured discount allowed or received account.

### Difference Amount increases when the discount is entered

Check whether the discount should be added or deducted for the Payment Type. Verify the paid amount, received amount, and allocated amount before changing the sign.

### The discount posts to the wrong profit and loss account

Select the correct account for discount allowed or discount received and include the required Cost Center. Do not use a generic write-off account when separate reporting is required.

## Frequently asked questions

### Is a settlement discount the same as changing the invoice price?

It is not the same. The original invoice remains the commercial and tax document; the settlement difference is recorded when payment is received or made.

### Should tax be recalculated when a payment discount is granted?

Tax treatment varies by jurisdiction and discount type. Use the appropriate credit note or regional process when tax must change instead of relying only on a Payment Entry deduction.

### Can only part of an invoice receive a discount?

A partial settlement can include a supported discount, but the remaining invoice balance must be intentional and explainable. Verify the outstanding amount after submission.

### Can discounts allowed and received use different accounts?

Separate accounts are recommended when financial reporting distinguishes customer discounts from supplier discounts.

## Related topics

- [Payment Entry](/erpnext/payment-entry)
- [Payment Reconciliation](/erpnext/payment-reconciliation)
- [Bank Reconciliation](/erpnext/bank-reconciliation)
- [Bank Transaction](/erpnext/bank-transaction)
- [Journal Entry](/erpnext/journal-entry)

<!-- page: erpnext/erpnext__managing-multi-level-bom.md -->
---
title: "Managing Multi-level BOM"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-multi-level-bom"
updated: "2026-02-26"
---


Consider a scenario where your manufacturing process involves producing sub-assembly items before the final product. In this case, how should you manage the BOM?

First of all, you need to have BOMs for the sub-assemblies, then these BOMs should be linked to the BOM of the final finished product. In the following screenshot, you can see that the BOM for Brush Bristles (subassembly) is linked to the BOM of the Shaving Brush (final product). This is seen in the Materials table in the Bill of Materials master.

![Multi-level BOM](/files/multi-bom.png)

The 'Materials' table will only show the sub-assemblies while the 'Materials Required (Exploded)' table will show all the raw materials required to manufacture the final product.

BOM materials table where sub-assembly is shown:
![Multi-level BOM](/files/bom-materials.png)

In the exploded view only the raw materials are shown:
![Multi-level BOM](/files/bom-materials-exploded.png)


To use multi-level BOM in a Work Order, enable the 'Use Multi-Level BOM' checkbox. This is enabled by default. If you want to plan materials for sub-assemblies of the Item you're manufacturing leave this enabled. If you plan and manufacture the sub-assemblies separately disable this checkbox.

Let's consider another example to understand this better where a computer is being assembled. The hard disk and DVD drive are also being manufactured and are the sub-assemblies. The multi-level or nested BOM will look like this:

- Personal Computer (FG Item)
 - Mother Board
 - SMTP
 - Accessories and wires
 - Hard Disk (sub-assembly)
 - Item A
 - Item B
 - Item C
 - DVD Drive (sub-assembly)
 - Item X
 - Item Y
 - Item Z


## Caution

Exercise caution when updating the BOM of a sub-assembly. The part which includes the sub assembly with an updated BOM will need to be updated to reference the updated BOM for that part. The practical outcome of this is that changing a screw on a low level assembly will lead to a ripple of updated Bills of Material up through the BOM structure.

Using the example of the personal computer above.
Personal Computer (PC-001 with BOM-PC-001) uses Hard Disk (HDD-001 with BOM-HDD-001).
BOM-HDD-001 includes the three items shown (Item A, B and C).

If we need to exchange Item C for a new item (Item D) then we must update create BOM-HDD-002 (with Items A, B and D). The Hard Disk (HDD-001) is then updated to reference the new BOM-HDD-002. But, BOM-PC-001 is still referencing HDD-001 with BOM-HDD-001. The change from Item C to Item D will not be updated in the Exploded BOM for PC-001.

BOM-PC-002 must be created referencing HDD-001 with BOM-HDD-002 to make this update.

<!-- page: erpnext/erpnext__managing-transactions-in-multiple-currencies.md -->
---
title: "Managing Transactions in Multiple Currencies | ERPNext Documentation"
description: "Create, review, print, pay, and verify foreign-currency sales and purchase transactions in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-transactions-in-multiple-currencies"
updated: "2026-08-14"
---

Nova Industries distributes electronics internationally while keeping its Company accounts in USD.



EuroTech Retail wants to receive and pay a EUR invoice, while Nova must keep its books in USD. Users need to enter, print, collect, and reconcile the sale in EUR without losing the USD value required for accounting.



This guide follows a EUR 1,200 Sales Invoice at `1 EUR = 1.15 USD`. The customer sees EUR 1,200 while ERPNext records USD 1,380 in Company currency. You will see where the currencies and rates come from, how payment is converted, and how to verify the result. The same controls apply to purchases through the corresponding Supplier and payable fields.

## Before you begin

Complete [Multi Currency Setup](/erpnext/multi-currency-setup):

- EUR is enabled in [Currency](/erpnext/currency).
- EuroTech Retail has Billing Currency EUR.
- Euro Receivables is a EUR Receivable [Account](/erpnext/chart-of-accounts) linked to the Customer.
- Nova Europe EUR is an enabled selling [Price List](/erpnext/price-lists).
- A dated EUR to USD rate exists in [Currency Exchange](/erpnext/currency-exchange), or the configured provider covers it.
- The Company has an Exchange Gain/Loss account.

Test the full invoice and payment cycle in Draft before using imported or live data.

## Create a foreign-currency Sales Invoice

1. Open Accounting &gt; Sales and Receivables &gt; Sales Invoice.
2. Select **Add Sales Invoice**.
3. Choose Nova Electronics Distribution and EuroTech Retail.
4. Confirm the Posting Date, Payment Due Date, and EUR Currency.
5. Review the Exchange Rate field. Its label states the direction.
6. Select Nova Europe EUR and confirm Price List Currency EUR.
7. Add the item, quantity, and rate.
8. Review taxes, payment terms, and totals.

![EUR transaction and price-list rates](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-sales-invoice-eur-currency-rate.png)

The screenshot shows two rates:


| Field                    | Purpose in this example                                                             |
| ------------------------ | ----------------------------------------------------------------------------------- |
| Exchange Rate            | Converts the EUR transaction total to the USD Company value. `1 EUR = 1.15 USD`.    |
| Price List Exchange Rate | Converts Price List currency to transaction currency. It is 1 because both are EUR. |


An Actual tax or charge entered directly on the transaction is entered in the transaction currency. Review calculated taxes and Company-currency equivalents according to the tax template and charge type.

## Confirm the receivable account

Open the Accounting section and check **Debit To**. It should be Euro Receivables for this Customer and Company.



![EUR receivable selected on the Sales Invoice](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-sales-invoice-eur-receivable-account.png)

If the selected account is in a foreign currency, the invoice currency must normally match it. Do not switch only the Currency field and ignore Debit To.

## Compare transaction and Company totals

Before submission, compare the party-facing total and the Company-currency total.



![EUR and USD Sales Invoice totals](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-sales-invoice-eur-totals.png)

For EUR 1,200 at 1.15:


| View                        | Amount    |
| --------------------------- | ---------: |
| Customer invoice total      | EUR 1,200 |
| Company-currency total      | USD 1,380 |
| Receivable account currency | EUR       |


Submit only after the rate, account, prices, taxes, and terms are correct. The submitted [Sales Invoice](/erpnext/sales-invoice) retains these values even if a later Currency Exchange record changes.

## Print and send the invoice

Open Print or Preview and confirm that rates, amounts, totals, and amount in words use the expected party-facing currency. The print format should show EUR for the invoice values. Company-currency fields are accounting fields and do not normally replace the agreed invoice currency in the customer-facing document.

If the symbol or number separators are wrong, correct the Currency master or site number format rather than hard-coding symbols into every print format.

## Create the Payment Entry

Create the Payment Entry from the submitted invoice when possible:

1. Open the invoice and select Create &gt; Payment.
2. Confirm Payment Type **Receive** and the Customer.
3. Confirm **Paid From** is the EUR receivable account.
4. Select the actual bank account under **Paid To**.
5. Enter the amount received in the bank account currency.
6. Review Source Exchange Rate and the Company-currency amount.
7. Confirm the invoice reference and allocated amount.

![Account currencies in Payment Entry](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-payment-entry-two-account-currencies.png)



![Paid and received amounts with the source rate](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-payment-entry-exchange-rates-and-amounts.png)

The paid-from and paid-to account currencies control the amount fields. In the example, EUR 1,200 is cleared from the receivable and USD 1,380 is received into the operating bank.

If the payment-date rate differs from the invoice rate, use [Manage Foreign Exchange Difference](/erpnext/manage-foreign-exchange-difference). Keep bank charges, withholding, write-offs, and exchange difference in their appropriate accounts.

## Enter a foreign-currency purchase

On a [Purchase Invoice](/erpnext/purchase-invoice), select the Supplier, EUR, the buying Price List, and the EUR payable account. Review the Exchange Rate and Price List Exchange Rate exactly as on the sales side.



![EUR Purchase Invoice conversion fields](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-purchase-invoice-eur-currency-rate.png)

On submission, the payable outstanding is maintained according to the party account currency. Create a Pay-type Payment Entry and verify the amount removed from the bank and the EUR amount cleared from the payable.

## Transactions in several currencies for one party

Accounts Settings includes **Allow multi-currency invoices against single party account**.



![Allow invoices in multiple currencies against one party account](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-accounts-settings-multi-currency-invoices.png)

This can support a party invoiced in multiple currencies while using a Company-currency party account. It does not make a bank account multi-currency, and it can make outstanding and payment interpretation harder. Use dedicated currency accounts for currencies that the business regularly holds or reconciles. Test [Payment Reconciliation](/erpnext/payment-reconciliation), ageing, credit notes, advances, and returns before enabling the option broadly.

## Verify reports

Use the [General Ledger](/erpnext/general-ledger) filtered by the foreign account. It shows debit, credit, and balance in account currency when appropriate.



![EUR bank balance in the General Ledger](https://novacompanies.m.frappe.cloud/files/docs-multi-currency-2026-foreign-currency-general-ledger.png)

Review [Accounts Receivable and Payable](/erpnext/accounts-receivable-and-payable) in the party or account currency. Financial statements use Company currency. At period end, run [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation) for eligible open foreign balances.

## Troubleshooting

### Currency changes but item rates look wrong

Check Price List, Price List Currency, and Price List Exchange Rate. The transaction Exchange Rate does not necessarily convert the source Item Price.

### The invoice cannot be saved because account currency differs

Use the matching receivable or payable account, or correct the party's per-Company default. Do not change an account currency after postings exist.

### Payment Entry receives the wrong USD amount

Check the paid-to bank currency, source or target rate, paid amount, received amount, and invoice allocation. Use the actual bank amount and account for legitimate differences separately.

### The printed currency differs from the agreement

Verify the submitted transaction Currency and Price List. Then inspect the print format for hard-coded symbols or base-currency fields.

## FAQs

### Can I omit the invoice exchange rate and convert only at payment?

No, ERPNext needs a Company-currency value when the invoice posts. A later payment can use a different rate and recognize the difference.

### Can the invoice and Price List use different currencies?

Yes, Price List Exchange Rate converts item prices, while Exchange Rate converts the transaction to Company currency.

### Why does Payment Entry not have a free Currency selector?

Its currencies come from the paid-from and paid-to accounts. Select accounts that represent the actual balances.

### Can I show Company currency on the print format too?

Yes, with an appropriate print design, but keep the agreed transaction-currency amount clear and verify custom fields and labels.

### What happens when a foreign invoice remains unpaid at month end?

Its foreign amount remains outstanding. Revalue the eligible account to update its Company-currency carrying value according to your closing policy.

## Related topics

- [Multi Currency Accounting](/erpnext/multi-currency-accounting)
- [Sales Invoice](/erpnext/sales-invoice)
- [Purchase Invoice](/erpnext/purchase-invoice)
- [Payment Entry](/erpnext/payment-entry)
- [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)

<!-- page: erpnext/erpnext__managing-tree-structure-masters.md -->
---
title: "Manage Tree Structure Masters"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/managing-tree-structure-masters"
updated: "2026-03-04"
---


Some of the masters in ERPNext are maintained in tree structure. Tree structured masters allow you to set Parent master, and Child masters under those Parents. Setting up this structure allows you creating intelligent report, and track growth at each level in the hierarchy.

Following is the partial list of masters which are maintained in the tree structure.

* Chart of Accounts

* Chart of Cost Centers

* Customer Group

* Territory

* Sales Person

* Item Group

Following are the steps to manage and create record in the tree structured master. Let's consider Territory master to understand managing tree masters.

####Step 1 : Go to Master

`Selling > Setup > Territory`

####Step 2 : Parent Territory

![Default Territories](/files/territory-2.png)

When click on Parent territory, you will see option to add child territory under it. All default Territory groups will be listed under Parent group called "All Territories". You can add further Parent or child Territory Groups under it.

####Step 3: Add new Territory

When click on Add Child, a dialog box will provide two fields.

**Territory Group Name**

Territory will be saved with Territory Name provided here.

**Group Node**

If Group Node selected as Yes, then this Territory will be created as Parent, which means you can further create sub-territories under it. If select No, then it will become child Territory which you will be able to select in another masters.

Only child Territory Groups are selectable in another masters and transactions.
![Default Territories](/files/territory-1.gif)

Following is how Child Territories will be listed under a Parent Territory.

![Adding new Territories](/files/territory-3.png)

Following this steps, you can manage other tree masters as well in ERPNext.

<!-- page: erpnext/erpnext__manufacturer.md -->
---
title: "Manufacturer\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/manufacturer"
updated: "2026-03-06"
---

**A manufacturer created or produces an Item.**

A Manufacturer may not be the same person/company that sells the Item under a specific [Brand](/erpnext/brand). For example, Unico Plastics can be the Manufacturer of plastic brushes but it may be sold under a Brand, say, Super Brushes.

In ERPNext, a Manufacturer can be used to identify Items using a specific part number.

To access the Manufacturer list, go to:

> Home > Stock > Manufacturer

## 1. How to Create a Manufacturer

1. Go to the Manufacturer list and click on New.
2. Enter a Manufacturer name and enter a description if needed.
3. Save.
  [Manufacturer](/files/manufacturer.png)

After creating a Manufacturer, you can create an **Item Manufacturer** record with a Manufacturer Part Number for identification.

![](/files/item_manufacturer.png)

### 1.1 Additional details

The following details can be set for a Manufacturer:

- Website
- Country
- Logo

## 2. Features

### 2.1 Address and Contacts

An [Address](/erpnext/address) and [Contact](/erpnext/contact) can be set for this Manufacturer.

## 3. Related Topics

1. [Item](/erpnext/item)
2. [Supplier](/erpnext/supplier)
3. [Brand](/erpnext/brand)
