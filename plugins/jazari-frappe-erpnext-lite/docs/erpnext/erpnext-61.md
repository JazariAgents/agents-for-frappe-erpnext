<!-- Frappe documentation: erpnext, part 61 of 69. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__stripe-integration.md -->
---
title: "Setting up Stripe"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/stripe-integration"
updated: "2026-02-26"
---


To setup Stripe,
`Explore > Integrations > Stripe Settings`

#### Setup Stripe

To enable Stripe payment service, you need to configure parameters like Publishable Key, Secret Key
![Razorpay Settings](/files/stripe_setting.png)

On enabling service, the system will create Payment Gateway record and Account head in chart of account with account type as Bank.

![Stripe COA](/files/stripe_coa.png)

Also it will create Payment Gateway Account entry. Payment Gateway Account is configuration hub from this you can set account head from existing COA, default Payment Request email body template.

![Payment Gateway Account](/files/payment_gateway_account_stripe.png)

After configuring Payment Gateway Account your system is able to accept online payments.

### Setup subscriptions plans

If you need to bill a recurring amount instead of a one-time charge, you can use Stripe's subscription system.

Once you have created your billing plans in Stripe, add one or several new "Payment Plan" in Frappe.

![Payment Plan](/files/payment_plan.png)


Afterwards, when you create your payment request, click the check field "Is a subscription" and add the system will fetch the corresponding susbscription plans from within the corresponding subscription.

![Payment Request](/files/subscription_payment_request.png)

ERPNext will automatically create a new subscription for this customer in Stripe.


####Supporting transaction currencies
```
 "AED",
 "ALL",
 "ANG",
 "ARS",
 "AUD",
 "AWG",
 "BBD",
 "BDT",
 "BIF",
 "BMD",
 "BND",
 "BOB",
 "BRL",
 "BSD",
 "BWP",
 "BZD",
 "CAD",
 "CHF",
 "CLP",
 "CNY",
 "COP",
 "CRC",
 "CVE",
 "CZK",
 "DJF",
 "DKK",
 "DOP",
 "DZD",
 "EGP",
 "ETB",
 "EUR",
 "FJD",
 "FKP",
 "GBP",
 "GIP",
 "GMD",
 "GNF",
 "GTQ",
 "GYD",
 "HKD",
 "HNL",
 "HRK",
 "HTG",
 "HUF",
 "IDR",
 "ILS",
 "INR",
 "ISK",
 "JMD",
 "JPY",
 "KES",
 "KHR",
 "KMF",
 "KRW",
 "KYD",
 "KZT",
 "LAK",
 "LBP",
 "LKR",
 "LRD",
 "MAD",
 "MDL",
 "MNT",
 "MOP",
 "MRO",
 "MUR",
 "MVR",
 "MWK",
 "MXN",
 "MYR",
 "NAD",
 "NGN",
 "NIO",
 "NOK",
 "NPR",
 "NZD",
 "PAB",
 "PEN",
 "PGK",
 "PHP",
 "PKR",
 "PLN",
 "PYG",
 "QAR",
 "RUB",
 "SAR",
 "SBD",
 "SCR",
 "SEK",
 "SGD",
 "SHP",
 "SLL",
 "SOS",
 "STD",
 "SVC",
 "SZL",
 "THB",
 "TOP",
 "TTD",
 "TWD",
 "TZS",
 "UAH",
 "UGX",
 "USD",
 "UYU",
 "UZS",
 "VND",
 "VUV",
 "WST",
 "XAF",
 "XOF",
 "XPF",
 "YER",
 "ZAR"
```

<!-- page: erpnext/erpnext__subcontracting-in-erpnext.md -->
---
title: "Introduction"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/subcontracting-in-erpnext"
updated: "2026-02-26"
---

## Subcontracting 

Subcontracting is a type of job contract that seeks to **outsource** certain types of work to other companies. It allows work on more than one phase of the project to be done at once, often leading to quicker completion. It is practiced by various industries.

For example, manufacturers who make a number of products from complex components subcontract certain components and package them at their facilities.



![](/files/Uqloysk.png)



If your business involves outsourcing certain processes to a third party Supplier where you supply the raw materials and the third party does the labor/production, you can track this by using the [subcontracting feature](https://docs.frappe.io/erpnext/user/manual/en/subcontracting) of ERPNext. 

## Subcontracting Inward

ERPNext also supports **[Subcontracting Inward](https://docs.frappe.io/erpnext/user/manual/en/subcontracting-inward)**, where your company acts as the subcontractor. In this case, a customer provides materials to you for processing or manufacturing. ERPNext enables you to track customer-supplied materials, manage production activities, and bill for the services performed.

<!-- page: erpnext/erpnext__subcontracting-inward.md -->
---
title: "Subcontracting Inward"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/subcontracting-inward"
updated: "2026-07-22"
---

**In Subcontracting Inward, a customer employs you to carry out tasks for their organization, especially manufacturing.**

Not to be confused with the [standard Subcontracting module in ERPNext](https://docs.frappe.io/erpnext/user/manual/en/subcontracting). This is an extension of that module, which allows you to do the exact inverse of it, that is, instead of you outsourcing your manufacturing process to a third party (Supplier), a third party (Customer) outsources their manufacturing process to you.

While this was already possible in ERPNext even before v16, this heavily streamlines the entire process, thereby making it very easy to use.

## Features

1. Receive Raw Materials from Customer without impacting your books
2. Track Raw Materials that you have received from the customer
3. Use extra Raw Materials given by the customer on a per transaction basis if needed
4. Use Raw Materials sourced by you along side the Raw Materials given by the customer and bill them to the customer
5. Reserve the Raw Materials received by the customer to prevent accidental use of the stock committed against another order
6. Create additional Work Orders incase of process loss during manufacturing
7. Optionally, deliver overproduced quantity incase of overproduction
8. Return Raw Materials to customer if required (for ex. QC failure, sent by mistake etc.)
9. Optionally, deliver secondary items produced during manufacturing to the customer
10. Incase of serial or batch Finished Good item, deliver items with the same serial and/or batches that were produced against the order
11. Receive the Finished Goods from the Customer if required (ex. QC fail)

## Prerequisites

1. Every Customer needs to have their own warehouse (dummy) in the masters. This is done by creating a new Warehouse and setting the newly added Customer Link field.
  ![](/files/image311f04.png)
2. While optional, we strongly recommend you to create a group warehouse which will hold all the customer warehouses in it as it will make data analysis much easier. Note that a Group Warehouse does not need the `Customer` Link field set however if your Customer has multiple warehouses, we recommend you to structure the warehouses accordingly.
  ![](/files/image5313b0.png)
3. The Raw Materials provided by the Customer in the Item master. Each Customer Provided Item needs to have the field set in the master. Conversely, Customer Provided Items cannot be purchased so the `Allow Purchase` field has to be unchecked (checked by default in ERPNext).

![](/files/image68b05b.png)

4. The non-stock/service item that will be sold or billed to the Customer. The `Maintain Stock`  field has to be unchecked (checked by default in ERPNext) for this.
  ![](/files/image608243.png)
5. The Finished Good to be produced needs to be marked as a Subcontracted Item

![](/files/image7b1ac7.png)

6. A standard ERPNext [Bill of Materials or ‘BOM’](https://docs.frappe.io/erpnext/user/manual/en/bill-of-materials) for the finished good to be produced.
7. A Subcontracting BOM which specifies the relationship between the non-stock/service item and the Finished Good to be produced. Note that it is also possible to create a Subcontracted Sales Order even without a Subcontracting BOM provided that the Finished Good to be produced has a default BOM set in it’s master.

![](/files/imageecae7c.png)

## How to use

1. Start by creating a Sales Order and check the “Is Subcontracted” checkbox. The Sales Order will now be subcontracted and the schema/form of the child table will change. Proceed by setting the service item in the `Item Code` field. If you have a Subcontracting BOM for this service item, the Finished Good field will be set automatically. Upon changing the quantity of the Service Item, the quantity of the Finished Good will also change based on the conversion factor in the Subcontracting BOM. If you have multiple Subcontracting BOMs for the same service/non-stock item, a dialog box will popup asking you to select the Finished Good from the Subcontracting BOMs present against that service/non-stock item. Save and submit once done.
  ![](/files/image002276.png)

![](/files/image5cd122.png)

2. From the Sales Order, click on `Create > Subcontracting Inward Order`. This DocType holds the list of Finished Goods, Raw Materials required, Service Items and secondary items (if produced). Start by selecting the Customer warehouse you created at the start of the process. If only a single Customer warehouse exists against the Customer, the field will be pre-filled with it. Then select a Delivery Warehouse for each of the Finished Goods to be produced. This will be where the Finished Goods produced by you will be delivered. If all the Finished Goods are to be delivered to the same warehouse, use the `Set Delivery Warehouse` field to set the delivery warehouse for all the Finished Goods in one go.

![](/files/image24b2d8.png)

3. If you need to “explode” the BOM, click on the Finished Good (pencil icon towards the right of the row) and check the `Include Exploded Items` field and click on save. You will see that the Raw Materials in the “Required Items” table will be updated with the exploded items. You may also additionally alter the quantity of the Finished Goods. This will allow you to create another Subcontracting Inward Order against the same Subcontracted Sales Order until the item is fully subcontracted should you need that.

![](/files/image85b6ee.png)

4. Save and submit the Subcontracting Inward Order. You can now receive Raw Materials from the Customer which will be used for the manufacturing process by clicking on Receive -> Raw Material from Customer. This will create a Stock Entry and the Raw Materials will be filled automatically upon creation. You may also additionally add extra Customer Provided Items here should you need it. The extra items, if added, will also be visible in the Required Items table of the Subcontracting Inward Order upon submission of the Stock Entry. Note that for additional Customer Provided Items, you will mandatorily need to specify the Finished Good against which you will be using the Raw Material using the `Against Finished Good` field in the child table.
  ![](/files/image9daef2.png)
5. In this Stock Entry, you may enter the basic rate for each item. Note that this is done purely for taxation purposes and will have no accounting impact on the valuation of your stock. You may verify this by clicking on `View> Accounting Ledger` after submission of the Stock Entry. You will see that everything will be 0.
  ![](/files/image710092.png)
6. It is also possible to create more Stock Entries to receive additional Customer Provided Items at any time, even after receiving the required quantity of the Raw Materials as per the Finished Good’s BOM.
7. Go back to the Subcontracting Inward Order and reload the page. You will now see two new buttons at the top right, “Return” and “Create”. By clicking on `Return > Raw Materials` to Customer, you can return the Raw Material to the customer if needed. By clicking on `Create > Work Order`, a standard Work Order will be created for each of the Finished Good(s) based on the quantity of Raw Materials available for production. Use this Work Order to produce the Finished Good(s) then go back to the Subcontracting Inward Order and reload the page.
  ![](/files/image33a853.png)

:::note
Additional Raw Materials used in the Manufacturing Stock Entry against Work Orders will also be added to the Required Items table in the Subcontracting Inward Order.
:::



8. You will now see the option for “Subcontracting Delivery” under the “Create” button. A new Stock Entry will be created upon clicking it which you can use to deliver the Finished Good(s) to the Customer.

Notes

1. By default, ERPNext will not add the generated secondary Item(s) to this Stock Entry. If you need to deliver the secondary Item(s) generated as well, enable the `Deliver secondary items` in the `Selling Settings` Single DocType.
2. ERPNext by default will only you to deliver the agreed upon quantity if Finished Good(s) as specified in the Subcontracted Sales Order. If you have produced more than the required quantity and want to deliver the overproduced quantity as well, enable the `Allow Delivery of Overproduced Qty` in the `Selling Settings` Single DocType.

![](/files/imagef78089.png)

9. Go back to the Subcontracting Inward Order and reload the page. You will now see the option “Subcontracting Return” under the “Return” button. On clicking it, a new Stock Entry will be created which will allow you to receive the Finished Good(s) that you have produced and delivered to the Customer should you need it.
10. Since the Finished Goods have been produced and delivered, it is time to bill the Customer. Go to the Sales Order created in the first step, from here you can deliver the service/non-stock item by creating a Delivery Note and bill it as well as all the Raw Materials you have used in the process. The Raw Materials procured by you (not provided by the Customer) will already be present in the child table when you create the Sales Invoice against the Subcontracted Sales Order.

Note You can deliver and bill the service/non-stock items even without creating a single Subcontracting Inward Order.

![](/files/imageec69eb.png)

## Important Notes

1. [Stock Reservation](https://docs.frappe.io/erpnext/user/manual/en/stock-reservation) Entries will be created and used extensively by default in this process even if its disabled in `Stock Settings`.
2. If the Raw Material received from the Customer goes unused, it cannot be directly used in another Subcontracting Inward Order. We recommend you to return the unused Raw Material to the Customer and receive it again using another Subcontracting Inward Order where it is to be reused. You do not need to move the Raw Material physically for this and it will be a pure dummy transaction.
3. For any Subcontracting Inward transaction where multiple batches are involved for an item, the Serial and Batch Bundle feature is to be used. Duplicating of child tables is not recommended or even permitted in various transaction types throughout.
4. It is mandatory for the Finished Good BOM to have atleast 1 Customer Provided Item.
5. Do not cancel any Stock Reservation Entries related to the Subcontracting Inward process, doing so will most definitely cause unintended consequences.
6. Using [Alternative Items](https://docs.frappe.io/erpnext/user/manual/en/item-alternative) in Work Orders created against Subcontracting Inward Orders is currently not supported and the checkbox is hidden for the same.
7. While you *can* use [Inventory Dimension](https://docs.frappe.io/erpnext/user/manual/en/inventory_dimension) in this process, it is not officially supported as of yet.
8. [Continuous Raw Material Consumption](https://docs.frappe.io/erpnext/user/manual/en/manufacturing-settings#1-allow-continuous-material-consumption) and [Disassembly Order](https://docs.frappe.io/erpnext/user/manual/en/disassembly-order) are also not supported as of yet.
9. To accurately reflect the value of the finished goods, a *batched item* is recommended. For example: if you have purchased stock of the finished good in the past and its sitting in the same warehouse as your manufactured batch, FIFO will consider the value of the purchased good in the `Deliver to Customer` Stock Entry instead of the batch you manufactured against the Subcontracting Inward Order. A batched item with `Batch-wise Valuation` enabled will ensure that this does not happen.

<!-- page: erpnext/erpnext__subcontracting.md -->
---
title: "Subcontracting"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/subcontracting"
updated: "2026-02-27"
---

**In subcontracting, you employ an external party to carry out tasks for your organization, especially manufacturing.**

Subcontracting is a type of job contract that seeks to outsource certain kinds of work to other companies. It allows work on more than one phase of the project to be done at once, often leading to quicker completion.

Subcontracting is practised by various industries. For example, manufacturers who make several products from complex components subcontract certain components and package them at their facilities.

If your business involves outsourcing certain processes to a third-party Supplier where you supply the raw materials and the third party does the labour/production, you can track this by using the subcontracting feature of ERPNext.

## How to Set up Subcontracting

---

1. Create a Service Item (Non-stock Item). It represents the service cost of the subcontracted operation.
  ![](/files/image0cf7e0.png)
2. Create separate Items for the unprocessed and the processed product. For example, if you supply unpainted X to your Supplier and the Supplier returns you X, you can create two Items: “X-unpainted” and “X”.
3. Create a Warehouse for your Supplier so that you can keep track of Items supplied. (You may supply a month's worth of Items in one go).
4. For the processed Item, in the Item master, enable “Supply Raw Materials for Purchase”.
  ![](/files/imageb3b64c.png)

### Creating a BOM

Make a [Bill Of Materials](/erpnext/bill-of-materials) for the processed Item, with the unprocessed Items as sub-items. Let's consider a simple example, where you manufacture a pen. The processed pen will be named under the Bill of Materials(BOM), whereas the nib, plastic, ink, etc. ,will be categorized as sub-items.

This BOM will be without Operations if all of the production work is done by a third party. Let's see with a simple example of a CPU Assembly:

![](/files/imagefbe036.png)

### Creating a Subcontracting BOM

While optional, creating a Subcontracting BOM allows you to predefine a relationship between your Service Item and Finished Good Item.

When you create a Subcontracted Purchase Order, if you have created a Subcontracting BOM for your Service Item or Finished Good Item, selecting either one will automatically fill out the other details of the Purchase Order line item. If you create a lot of Subcontracted Purchase Orders for the same Service Item and Finished Good Item combination, you can save some time and effort by creating a Subcontracting BOM for that combination in advance.

Using a Subcontracting BOM, you can:

1. Select a default BOM for your Finished Good Item.
2. Select a default UOM for your Service Item.
3. Specify the conversion factor between your Service Item and Finished Good Item.

![](/files/imaged3e66b.png)

In the above image, we have specified that 1 unit of "Painting" will produce 2 units of "Tiles" after the subcontracting process is complete. Upon saving this document, you will see that the conversion factor for this relationship is calculated automatically (0.5 in this case).

Note:

1. There can only be 1 Subcontracting BOM for any Finished Good Item.
2. If there are multiple Subcontracting BOMs for a single Service Item, upon making a Subcontracted Purchase Order and selecting that Service Item, a dialog box will appear which will ask you to select the Finished Good Item for that specific Service Item. The list of those Finished Good Items will be fetched from the list of Subcontracting BOMs, where the Service Item is the one you have entered.

### Creating a Purchase Order

Make a Subcontract Purchase Order for the Service Item and select the Finished Good Item, the one for which you've created a BOM.

1. Enable the "Is Subcontracted" since this Purchase Order is for Subcontracting.
  ![](/files/po - subc.png)
2. Here the Rate field value of the Items table in the Purchase Order will be the service cost you have agreed with the third party or the Supplier.
3. After filling in the details, Save and Submit the [Purchase Order](/erpnext/purchase-order#35-raw-materials-supplied).

### Creating a Subcontracting Order

Make a Subcontracting Order for the Purchase Order by clicking on Create > Subcontracting Order. When you “Save”, in the “Raw Materials Supplied”, all your un-processed Items will be updated based on your Bill of Materials. You can also select the Warehouse in which the raw materials would be reserved for subcontracting under Reserve Warehouse.



![](/files/Screen Recording 2026-02-17 at 11.43.42 AM.mov)











1. The costs involved with the subcontracting process should be recorded in the Rate field of the Items table in the Subcontracting Order shown as follows:
  ![](/files/image0c3d0a.png)
2. In the previous image, we are providing the subcontractor with the following items:
  ```
  8 Motherboards
  8 Processors
  16 RAMs
  8 Hard Disks
  8 Cabinets
  The cost for one CPU including Raw Materials and Service Costs is 1,02,994 and the total cost for all CPUs is 8,23,952
  ```
  ![sco items row qty rate](/files/sco-items-row-qty-rate.png)
3. From a Subcontracting Order, select the raw materials to transfer to the subcontractor:
  ![](/files/subcontracting order.mp4)


4. Once the Subcontracting Order is submitted, you can also view the item's reserved quantity on the item dashboard.

![](/files/imageff75a7.png)

### Creating Stock Entry to Transfer Raw Materials

Now that the raw materials are reserved, make a Stock Entry and deliver the raw material Items to your Supplier.

In the Subcontracting Order, click on Transfer > Material to Supplier. Set the Source and Target Warehouses. The Stock Entry will be of type 'Send to Subcontractor' where you transfer from one Warehouse to another. Tick 'From BOM', select the BOM, enter the quantity, and click the Get Items button.

![](/files/image4e5ebf.png)

### Creating a Subcontracting Receipt to receive the Finished and Scrap items

Receive the Items from your Supplier using a Subcontracting Receipt. You need to enter the Supplier Warehouse from where the raw materials will be taken and finished goods will be received in the Accepted Warehouse. Consider this like a backflush for subcontracting.

Click on Create > Subcontracting Receipt from the Subcontracting Order. Set the Accepted and Supplier Warehouses. Make sure to check the “Consumed Quantity” in the “Raw Materials” table so that the correct stock is maintained at the Supplier’s end. You need to select the Supplier's Warehouse where you'll receive the finished goods.

Scrap items are fetched from the chosen Bill of Materials (BOM) for Finished Goods within the Items table. The Qty is computed using the Qty of the Finished Good Item, while the Rate is determined by either the Valuation Rate or the Scrap Rate specified in the BOM.



![](/files/Screen Recording 2026-02-19 at 10.51.47 AM.mov)





#### Service Expense Account in Subcontracting Receipt

User can set the expense account for the service item in the subcontracting receipt.

![](/files/image564411.png)

If the user sets the expense account in the service item, the same account will be auto-filled in the Service Expense Account field. The user can also manually set the service expense account in the subcontracting receipt. If no service expense account is set, the system will use the Finished Item’s expense account to book the service cost. Once the subcontracting receipt is submitted, the system books the service cost against the service expense account.

![](/files/imagea0223e.png)

### Backflush of Raw Material

![](/files/image4ba089.png)

- **BOM**
  - If you set backflush based on BOM, system will consume raw materials even though you have not transferred materials against the Subcontracting Order and have enough stock at supplier's warehouse.
- **Material Transferred for Subcontract** 
  - If you set backflush based on "Material Transferred for Subcontract" system will consume raw materials based on the materials transferred against the Subcontracting Order. If no stock transferred then no materials will be consume at the time of Subcontracting Receipt.

### Creating a Purchase Receipt

Back to Purchase Order, click on `Create > Purchase Receipt.` There will be no effect on the Stock Ledger and Accounting Ledger since both the Stock and Accounting Ledger are updated when you Submit the Subcontracting Receipt. In case you have "Purchase Taxes and Charges" the Accounting Ledger will update accordingly.

### Supplier Sourced Raw Material

While creating a BOM for subcontracting, there might be a few raw materials like nuts and bolts that the Suppliers will have to procure themselves.

While creating a Stock Entry for "Transfer" from a Subcontracting Order, these items can be excluded one by one, but it is impossible to do so if you have more than 100 items.

If some raw material is sourced by the Supplier directly, then such raw materials have to be included in the BOM.

- It will have zero value in BOM
- In the Subcontracting Order, this raw material will not appear in Supplied Items since it is not supplied
- Also, while creating a "Transfer", such items will be excluded from the Stock Entry

![](/files/imaged2428f.png)

However, the Supplier may choose to include the supplier-provided items in their Sales Order sent to you.

## Notes

---

- Make sure that the “Rate” of the processed Item is the processing/service cost (excluding the raw material cost).
- ERPNext will automatically add the raw material rate for your valuation purpose when you receive the finished item in your stock.
- ERPNext will automatically default the 'Reserve Warehouse' in the Subcontracting Order from the BOM. If not found in the BOM, it would default it from the default Warehouse set in the Item. You can set the default Reserve Warehouse for all the Items in the Subcontracting Order from the 'Reserve Warehouse' field in the Raw Materials Supplied section.

:::note
New in V16
:::



## Features

### Creating multiple Subcontracting Orders from a single Subcontracted Purchase Order

ERPNext now allows users to create multiple Subcontracting Orders from a single Purchase Order.

How to use:

1. When you click on Create Subcontracting Order from your Purchase Order, by default ERPNext will fill the Finished Good Items and Service Items table based on the Purchase Order.
2. The user is now allowed to edit the quantity of each Finished Good Item as per their needs.
3. If you create a partial Subcontracting Order and then try to create a new one against the same PO, ERPNext will automatically calculate the remaining quantity left to subcontract and fill out the new document accordingly.

Note:

1. Once the PO is fully subcontracted ie. no items in the PO are left to be subcontracted, user will not be allowed to create new Subcontracting Orders from the PO.
2. The quantity entered by the user cannot exceed the available quantity to subcontract (fetched from the PO).

In both the above cases, an error will be thrown accordingly.

### Stock Reservation

In ERPNext v16, you can now reserve the Raw Materials to be sent to the Supplier.

Just above the Raw Materials table, you will now see the checkbox `Reserve Stock`. If you check this option and submit the Subcontracting Order, the stock will be reserved against the Subcontracting Order which will essentially make sure that the committed stock is not used anywhere else by mistake. The reserved stock will be automatically utilised if and when Raw Material is sent to the Supplier by using the `Send to Subcontractor` Stock Entry made against the Subcontracting Order.

![](/files/image3fc0a5.png)

Note that if the `Auto Reserve Stock` option is enabled in `Stock Settings`, this option will be checked by default.



## Related Topics

---

1. [Purchase Order](/erpnext/purchase-order)
2. [Purchase Receipt](/erpnext/purchase-receipt)
3. [Quality Inspection](https://docs.erpnext.com/docs/user/manual/en/quality-inspection)

<!-- page: erpnext/erpnext__subcontracting__reports.md -->
---
title: "Reports"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/subcontracting/reports"
updated: "2026-02-19"
---

# Subcontracting Reports in ERPNext

ERPNext provides dedicated reports to help monitor materials sent to subcontractors, track pending receipts, and review the overall status of subcontracting orders. These reports improve visibility, prevent material loss, and ensure accurate production and costing control.

## Subcontracted Raw Materials to be Transferred

This report shows the raw materials that need to be sent to subcontractors against open subcontracting Purchase Orders. It helps identify pending material transfers so that suppliers receive the required inputs on time and production is not delayed.

![](/files/telegram-cloud-photo-size-5-6104774370766032817-y.jpg)
*Subcontracted raw materials to be transferred report*

## Subcontracted Item to be Received

This report lists subcontracted finished goods that are yet to be received from suppliers. It provides visibility into pending receipts and helps teams follow up on delayed deliveries and plan inventory accordingly.

![](/files/telegram-cloud-photo-size-5-6104774370766032818-y.jpg)
*Subcontracted Item to be received*

## Subcontract Order Summary

This report provides an overall view of subcontracting Purchase Orders, including material transfer status and receipt progress. It is useful for monitoring order completion and tracking the end-to-end subcontracting cycle.

![](/files/image28ddad.png)

<!-- page: erpnext/erpnext__subscription-plan.md -->
---
title: "Subscription Plan | ERPNext Documentation"
description: "Create an ERPNext Subscription Plan to define the item, price, billing interval, payment gateway, and accounting dimensions used for recurring invoices."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/subscription-plan"
updated: "2026-08-14"
---

A Subscription Plan defines what ERPNext bills on a recurring basis, how much it charges, and how often it charges it. You add one or more plans to a [Subscription](/erpnext/subscription), and ERPNext uses them when it creates recurring Sales Invoices or Purchase Invoices.



Use a separate plan for each distinct combination of item, price, currency, and billing frequency. For example, Nova Industries can use **Nova Device Care Monthly** for a USD 199 monthly warranty service and a separate yearly plan for customers who pay in advance.

![Subscription Plan for a monthly warranty service](https://novacompanies.m.frappe.cloud/files/sales-receivables-subscription-plan-subscription-plan-overview.png)

## Before you begin

Create the following records first:

- An [Item](/erpnext/item) for the product or service being billed. Use a non-stock service Item when no stock delivery is involved.
- An [Item Price](/erpnext/item-price) and [Price List](/erpnext/price-lists) if the plan will obtain its rate from a Price List.
- A [Payment Gateway Account](/erpnext/payment-gateway) if an external payment integration will collect the recurring charge.
- A [Cost Center](/erpnext/cost-center) or other accounting dimensions if subscription income or expense must be reported separately.

Accounts Users, Accounts Managers, and System Managers can create Subscription Plans when their role permissions have not been customized.

## Create a Subscription Plan

1. Go to **Accounting &gt; Subscriptions &gt; Subscription Plan**.
2. Select **Add Subscription Plan**.
3. Enter a unique **Plan Name**. Use a name that communicates the service and interval, such as `Nova Device Care Monthly`.
4. Select the **Currency** and the **Item** being billed.
5. Choose how ERPNext determines the subscription price and enter the corresponding rate or Price List.
6. Set the **Billing Interval** and **Billing Interval Count**.
7. Add payment and accounting details when required.
8. Save the plan.

Saving a plan does not create an invoice. Add the saved plan to a Subscription to begin the recurring billing workflow.

## Choose how the price is determined

The highlighted fields control the rate ERPNext uses when it generates an invoice from the Subscription.

![Subscription pricing method and cost fields](https://novacompanies.m.frappe.cloud/files/sales-receivables-subscription-plan-subscription-plan-pricing.png)


| Subscription Price Based On | How ERPNext calculates the rate                                                                                                                                                              | Use it when                                                                                                 |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Fixed Rate**              | Uses the value entered in **Cost**.                                                                                                                                                          | The charge remains the same for every billing cycle.                                                        |
| **Based On Price List**     | Reads the Item rate from the selected Price List. The applicable customer or supplier context can affect the returned Item Price.                                                            | You maintain recurring rates through standard Item Prices.                                                  |
| **Monthly Rate**            | Treats **Cost** as the monthly rate and calculates the charge for the covered number of months. Proration can apply when enabled in [Subscription Settings](/erpnext/subscription-settings). | The billing period may span one or more months and you want the amount calculated from a monthly base rate. |


Changing a plan does not rewrite invoices that have already been generated. Review the next invoice after changing a rate, Price List, or billing interval.

## Set the billing frequency

The **Billing Interval** supplies the unit: Day, Week, Month, or Year. The **Billing Interval Count** tells ERPNext how many of those units make one billing cycle.

![Billing Interval and Billing Interval Count](https://novacompanies.m.frappe.cloud/files/sales-receivables-subscription-plan-subscription-plan-billing-interval.png)

Examples:


| Billing Interval | Count | Result                   |
| ---------------- | -----: | ------------------------ |
| Month            | 1     | Bills every month        |
| Month            | 3     | Bills every three months |
| Week             | 2     | Bills every two weeks    |
| Year             | 1     | Bills every year         |


The count must be at least 1. The Subscription's start date and invoice-generation settings determine the actual billing dates. Calendar-month alignment, invoice timing, trial periods, and renewal behavior belong on the Subscription rather than the plan.

## Important fields and what they mean


| Field                           | What it controls                                                                                                                                  |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Plan Name**                   | The unique name shown when you add the plan to a Subscription.                                                                                    |
| **Currency**                    | The currency used for the plan's rate and generated invoice line. Keep it consistent with the party and transaction currency.                     |
| **Item**                        | The product or service added to the generated invoice. ERPNext uses the Item's accounting defaults when it builds the invoice line.               |
| **Subscription Price Based On** | Selects the fixed-rate, Price List, or monthly-rate calculation.                                                                                  |
| **Cost**                        | Stores the fixed or monthly base rate. It appears only when the selected pricing method requires it.                                              |
| **Price List**                  | Supplies the Item Price when pricing is based on a Price List.                                                                                    |
| **Billing Interval**            | Defines whether the cycle is measured in days, weeks, months, or years.                                                                           |
| **Billing Interval Count**      | Defines how many intervals make one billing cycle.                                                                                                |
| **Product Price ID**            | Stores an external payment provider's price identifier when an integration requires it. Leave it blank for ordinary ERPNext invoicing.            |
| **Payment Gateway**             | Links the plan to a configured Payment Gateway Account for integrated collection workflows.                                                       |
| **Cost Center**                 | Assigns the generated invoice line to the selected Cost Center when the integration and Subscription flow carry the accounting dimension forward. |


## Use the plan in a Subscription

Open a new Subscription, select the Customer or Supplier, set the service dates, and add the plan in the **Subscription Plans** table. A customer Subscription generates [Sales Invoices](/erpnext/sales-invoice), while a supplier Subscription generates [Purchase Invoices](/erpnext/purchase-invoice).

One Subscription can contain multiple plans. This is useful when the same Customer receives a base service plus separately priced support, storage, or add-ons. Keep each charge as its own plan so rates and intervals remain understandable.

## Troubleshooting

### The generated invoice rate is zero

For **Based On Price List**, confirm that the selected Price List contains an active Item Price for the plan's Item, currency, quantity, party context, and invoice date. If no applicable price is found, ERPNext can return a zero plan rate.

### The plan bills at the wrong frequency

Check both **Billing Interval** and **Billing Interval Count**. A Month interval with a count of 3 means one invoice every three months, not three invoices each month. Then verify the Subscription's start date and invoice-generation settings.

### The plan cannot be saved

Confirm that the Plan Name is unique, all required fields are present, and Billing Interval Count is 1 or higher.

### The payment gateway does not collect payment

Linking a gateway on the plan does not complete the integration by itself. Verify the Payment Gateway Account, provider credentials, Product Price ID when required, and the Subscription payment workflow.

## Frequently asked questions

### Can I use one plan for several customers?

You can reuse a Subscription Plan. Add the same plan to multiple customer Subscriptions when the item, currency, pricing method, and billing interval are identical.

### Can one Subscription contain several plans?

You can add several plans. Each plan becomes a separate recurring invoice line. Use this for a base service with optional add-ons.

### Should I create separate monthly and yearly plans?

Usually, yes. Separate plans make the price and billing commitment explicit and reduce the chance of selecting the wrong interval.

### Does saving a plan create an invoice?

Saving the plan does not create an invoice. The plan is a reusable billing definition, and invoice generation begins only after it is added to an active Subscription.

## Related topics

- [Subscription](/erpnext/subscription)
- [Subscription Settings](/erpnext/subscription-settings)
- [Item](/erpnext/item)
- [Price Lists](/erpnext/price-lists)
- [Sales Invoice](/erpnext/sales-invoice)
- [Purchase Invoice](/erpnext/purchase-invoice)

<!-- page: erpnext/erpnext__subscription-settings.md -->
---
title: "Subscription Settings | ERPNext Documentation"
description: "Configure grace periods and automatic cancellation for unpaid recurring invoices generated by ERPNext subscriptions."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/subscription-settings"
updated: "2026-07-31"
---

**Subscription Settings** controls how ERPNext handles unpaid subscription invoices across the site. Configure it before relying on automatic recurring billing.

## Configure unpaid-invoice handling

Search for **Subscription Settings** and review:


| Setting                                | What it controls                                                                                 |
| -------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Grace Period                           | Time allowed after an invoice becomes overdue before the subscription is treated as unpaid       |
| Cancel Subscription After Grace Period | Automatically cancels a subscription when the unpaid condition continues beyond the grace period |


![Subscription Settings with grace-period, cancellation, and prorating controls](https://novacompanies.m.frappe.cloud/files/sales-receivables-subscription-settings-subscription-settings.png)

Use a grace period that matches your collection process. A short period stops service quickly but may cancel customers after a temporary payment delay. A longer period is more forgiving but allows unpaid exposure to grow.

## Recommended rollout

1. Create a test Subscription with a short billing period.
2. Generate an invoice and confirm its due date.
3. Test both paid and unpaid outcomes.
4. Confirm the Subscription moves through the expected Active, Grace Period, Unpaid, and Cancelled states.
5. Only then enable automatic cancellation for production subscriptions.

These settings affect future subscription processing. They do not cancel or reverse Sales Invoices that have already been generated.

## Related topics

- [Subscription](/erpnext/subscription)
- [Sales Invoice](/erpnext/sales-invoice)
- [Payment Entry](/erpnext/payment-entry)
- [Accounts Receivables](/erpnext/accounts-receivables)

<!-- page: erpnext/erpnext__subscription.md -->
---
title: "Subscription | ERPNext Documentation"
description: "Configure recurring customer or supplier billing with plans, invoice timing, taxes, discounts, and billing history in ERPNext."
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/subscription"
updated: "2026-08-14"
---

Northstar Retail, a customer of Nova Industries, buys a monthly device-care plan for the phones it resells. Creating each Sales Invoice by hand would be repetitive and makes it easy to miss a billing date.



A Subscription turns that continuing customer relationship into scheduled billing. ERPNext uses the selected Subscription Plan to create recurring Sales Invoices for Northstar Retail, while a supplier subscription would instead create recurring Purchase Invoices for services Nova Industries buys.



Use a Subscription when the same product or service is billed on a regular schedule, such as maintenance, software access, rentals, retainers, or support plans.



## Before you begin

Create an Item for the recurring charge, then create a **Subscription Plan** that defines its price and billing interval. Confirm the Company's income, receivable, tax, and Cost Center defaults before generating invoices.

## Create a Subscription Plan

In the Subscription Plan, select the Item and currency, then choose how ERPNext determines the price:


| Price basis         | Use it when                                       |
| ------------------- | ------------------------------------------------- |
| Fixed Rate          | Every subscriber pays the same rate               |
| Based On Price List | The rate should come from an Item Price           |
| Monthly Rate        | The charge should be prorated from a monthly rate |


Set the billing interval and interval count. For example, **Month** with a count of **1** bills monthly, while a count of **3** bills every three months.



![Monthly subscription plan for a service item](https://novacompanies.m.frappe.cloud/files/subscription-plan-subscription-plan.png)

## Create a Subscription

1. Search for **Subscription** and select **Add Subscription**.
2. Select **Customer** or **Supplier**, then choose the Party and Company.
3. Enter the subscription start date and, if applicable, the end date.
4. Configure when invoices should be generated.
5. Add one or more Subscription Plans.
6. Add taxes, a Cost Center, or an additional discount when needed.
7. Save.

![Subscription with customer, term, billing history, and invoice timing](https://novacompanies.m.frappe.cloud/files/subscription-subscription-overview.png)

## Choose when invoices are generated


| Generate Invoice At             | Result                                                            |
| ------------------------------- | ----------------------------------------------------------------- |
| Postpaid (bill at period end)   | Invoice is created after the service period                       |
| Prepaid (bill at period start)  | Invoice is created at the beginning of the period                 |
| Bill N days before period start | Invoice is created the specified number of days before the period |


**Days Until Due** controls the invoice due date. **Submit Generated Invoices** submits generated invoices automatically; leave it off if someone should review each invoice first. **Bill Even If Previous Invoice Unpaid** keeps generating invoices even when an earlier invoice is unpaid. Use that option deliberately because it can increase the customer's outstanding balance.

Enable **Follow Calendar Months** when billing should align to calendar boundaries rather than the original start date. Enable **Cancel When Period Ends** when the subscription must stop at the end of its current billing period.

## Plans, taxes, and discounts

Add every recurring component as a row in **Plans**. You can combine a base plan and add-ons in one subscription. The generated invoice uses the plan quantity, tax template, and any additional discount saved on the Subscription.



![Subscription plans, billing controls, and taxes](https://novacompanies.m.frappe.cloud/files/subscription-subscription-plans-taxes.png)

## Billing history and status

The billing history shows planned and generated periods. Subscription status moves through states such as Trialing, Active, Grace Period, Unpaid, Completed, Cancelled, and Refunded based on dates and payment conditions.

Review generated Sales Invoices from the Subscription dashboard. Cancelling a Subscription stops future billing but does not cancel invoices that already exist.

## Troubleshooting

**No invoice is generated**

Check the start date, next billing period, invoice timing, scheduler, and whether an earlier invoice is unpaid. Also confirm that the plan Item and Company accounting defaults are valid.

**The invoice amount is unexpected**

Open the linked Subscription Plan and confirm its price basis, rate, interval, quantity, taxes, and discount.

**A subscription should stop after the current term**

Enable **Cancel When Period Ends** instead of cancelling immediately.

## Related topics

- [Subscription Settings](/erpnext/subscription-settings)
- [Sales Invoice](/erpnext/sales-invoice)
- [Item Price](/erpnext/item-price)
- [Payment Request](/erpnext/payment-request)
- [Auto Repeat Recurring Orders and Invoices](/erpnext/auto-repeat-recurring-orders-and-invoices)
