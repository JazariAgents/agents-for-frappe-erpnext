<!-- Frappe documentation: erpnext, part 32 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__item-codification.md -->
---
title: "Item Codification\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/item-codification"
updated: "2026-03-02"
---


If you already have a full-fledged business with a number of physical items,
you would have probably coded your items. If you have not, you have a choice.
We recommend that you should codify if you have lot of products with long or
complicated names. In case you have few products with short names, it is
preferable to keep the Item Code same as Item Name.

Item codification has been a sensitive topic and wars have been fought on this
(not joking). In our experience, when you have items that cross a certain
size, life without codification is a nightmare.

### 1. Benefits

 * Standard way of naming things.
 * Less likely to have duplicates.
 * Explicit definition.
 * Helps to quickly find if a similar item exists.
 * Item names get longer and longer as more types get introduced. Codes are shorter.

### 2. Challenges

 * You have to remember the codes!
 * Harder for new team members to pick up.
 * You have to create new codes all the time.

### 3. Example

You should have a simple manual / cheat-sheet to codify your Items instead of
just numbering them sequentially. Each letter should mean something. Here is
an example:

If your business involves wooden furniture, then you may codify as follows:

Item Codification Summary Sheet (SAMPLE)



 First letter: "Material" Third letter: "Size"

 - W - Wood - 0 - less than 1mm
 - H - Hardware - 1 - 1mm - 5mm
 - G - Glass - 2 - 5mm - 10mm
 - U - Upholstery - 3 - 10mm - 10cm
 - P - Plastic

 Second Letter: "Type"

 For Wood: For Hardware:

 - S - Sheet - S - Screw
 - B - Bar - N - Nut
 - L - L-section - W - Washer
 - M - Molded - B - Bracket
 - R - Round


The last few letters could be sequential. So by looking at code **WM304** \-
you know its a wooden molding less than 10cm in size

### 4. Standardization

If you have more than one person naming items, the style of naming items will
change for everyone. Sometimes, even for one person, he or she may forget how
they had named the item and may create a duplicate name _"Wooden Sheet 3mm" or
"3mm Sheet of Wood"?_

### 5. Rationalizing

It is a good practice to have minimum varieties of items so that you keep
minimum stock, housekeeping is simpler etc. When you are planning a new
product and you want to know if you are already purchasing a part in some
other product, the item codes will help you quickly determine if you are using
a similar raw material in another product.

We believe if you do this small investment, it will help you rationalize
things as your business grows, though its okay not to codify if you have less
items.

#### 6. Related Topics
1. [Item Group](/erpnext/item-group)
1. [Item Attribute](/erpnext/item-attribute)
1. [Item Price](/erpnext/item-price)
1. [Item Variants](/erpnext/item-variants)

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

[Screenshot on the live page]  

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

[Screenshot on the live page]

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

[Screenshot on the live page]

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

[Screenshot on the live page]

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



[Screenshot on the live page: Automatically add Taxes and Charges from Item Tax Template]

Decide whether the item is reduced-rated, zero-rated, exempt, or not applicable under your local rules. These classifications can have different reporting consequences, so confirm the intended treatment with your tax adviser.

## Create an Item Tax Template

Go to **Accounting &gt; Taxes &gt; Item Tax Template** and select **Add Item Tax Template**.

1. Enter a descriptive **Title**, such as `Nova Reduced Item Tax 4%`.
2. Select the **Company**.
3. In **Tax Rates**, add a row.
4. Select the tax account and enter the overriding rate.
5. Save the template.

Use the pencil icon to open the child-table row and review all its fields.



[Screenshot on the live page: Open an Item Tax Template rate row]



[Screenshot on the live page: Tax account and rate in the Item Tax Template row]

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



[Screenshot on the live page: Open the Item Tax assignment row]

Set the Item Tax Template and, when relevant, its Tax Category and validity conditions.



[Screenshot on the live page: Item Tax Template assignment, Tax Category, and Valid From]


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



[Screenshot on the live page: Mixed-rate items on one Sales Invoice]



[Screenshot on the live page: Item Tax Template selected on a transaction row]

ERPNext calculates $55.92 on the $699 phone, $5.96 on the $149 service, and $0 on the $99 warranty. Total tax is therefore $61.88 and the Grand Total is $1,008.88.



[Screenshot on the live page: Mixed-rate tax and Grand Total result]

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

[Screenshot on the live page: Download Backup]

You can also set Valuation Method in the item master, especially when a valuation method for an item is different from the default Method as seen in the following screenshot.

[Screenshot on the live page: Download Backup]

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
  Has Variants (picture on the live page)
4. On selecting 'Has Variants' a table will appear. Specify the variant attributes for the Item in the table. In case the attribute has Numeric Values, you can specify the range and create intervals based on the increment values.
  Valid Attributes (picture on the live page)

&gt; Note: You cannot make Transactions against a 'Template'.

### 1.2 Creating the Item Variants Based on Item Attributes

To create 'Item Variants' against a 'Template' click on 'Create'. From there, choose whether to create a single variant or multiple. Single is simple where you create just one or more attributes and one Item will be created. When choosing multiple variants, tick the attributes and multiple items will be created. For example, if you choose Color: Red, Green and Size: Small, Medium, Large, 6 variants will be created.

Creating multiple variants in ERPNext:

[Screenshot on the live page]

To learn more about setting attributes, check out [Item Attributes](/erpnext/item-attribute)

### 1.3 Item Variants Based on Manufacturers

To set up variants based on Manufacturers, in your Item template, set "Variants Based On" as "Manufacturers"  
In this case, to create variants, click on Create &gt; Make Variant. The system will prompt you to select a Manufacturer. You can also optionally put in a Manufacturer Part Number.

[Screenshot on the live page]

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
