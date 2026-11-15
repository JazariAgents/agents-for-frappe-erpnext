<!-- Frappe documentation: erpnext, part 18 of 18. Index: docs/INDEX.md -->

<!-- page: erpnext/erpnext__warehouse-ledger-link.md -->
---
title: "Linking stock warehouse and accounts"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/warehouse-ledger-link"
updated: "2026-03-02"
---


The value of stock stored in the warehouses needs to be tracked.

Each warehouse is linked to a ledger in chart of accounts through the 'Account' field in the warehouse.

![Stock Asset Ledger in Warehouse](/files/stock-asset-ledger-in-warehouse.png)

If the Account field is empty in a warehouse, then the Account mentioned in the parent of that warehouse is considered. If an Account could not be determined by tracing the hierarchy, then the Default Inventory Account mentioned in the Company record is considered.

![Default Inventory Account in Company](/files/default-inventory-account-in-company.png)

When a company is created, a ledger named 'Stock In Hand' is created by default in Chart of Accounts.

**Chart of Accounts > Assets > Current Assets > Stock Assets > Stock In Hand.**

If required, you can create additional ledgers under 'Stock Assets' group.

![Stock Asset Ledger in Chart of Accounts](/files/stock-asset-ledger-in-coa.png)

<!-- page: erpnext/erpnext__warehouse.md -->
---
title: "Warehouse\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/warehouse"
updated: "2026-04-27"
---

**A warehouse is a commercial building for storage of goods. Warehouses are used
by manufacturers, importers, exporters, wholesalers, transport businesses,
customs, etc.**

They are usually large plain buildings in industrial areas of
cities, towns, and villages. They mostly have loading docks to load and unload
goods from trucks.

The terminology of 'Warehouse' in ERPNext is a bit broader though and maybe can be regarded as "storage locations". You can create a sub-Warehouse which could be a shelf inside your actual location.

This can become quite a detailed Tree like the following:

*Warehouse > Room > Row > Shelf > Bin*

To access the Warehouse list, go to:

> Home > Stock > Settings > Warehouse

## 1. How to create a Warehouse

1. Go to the Warehouse list, click on New.
2. Enter a name for the Warehouse.
3. Set/check the Parent Warehouse. If you tick on 'Is Group', you can create sub-Warehouses under this group Warehouse.
4. Save.

Warehouses are saved with their respective Company’s abbreviations. This facilitates
identifying which Warehouse belongs to which company at a glance.

### 1.1 Additional options when creating a Warehouse

**Account**: Set a default account here for all transactions with this Warehouse. Setting this account will show transactions from this Warehouse in the Accounting Ledger.
**Warehouse Type**: You can create a Warehouse Type to classify Warehouses. For example, Supplier Warehouses, Stock Warehouses, WIP Warehouses, Rooms, etc. can be tagged. This classification is useful when generating reports or in certain stock transactions.

#### Address and contact

You can add Billing, Shipping, and other types of addresses for the Warehouse. You can also add a contact, this could be the Warehouse Manager for example.

![Warehouse](/files/warehouse.png)

### 1.2 After Saving

After saving a Warehouse, you'll see the following options:

- **Stock Balance**: This will open the Stock Balance report to display the quantity, valuation, balance, etc.
- **General Ledger**: This will open the General Ledger to display the accounting transactions.
- **Non-Group to Group**: If the Warehouse is a Non-Group Warehouse, i.e. cannot contain other Warehouses under it, this button will make this a Group Warehouse.

## 2. Features

### 2.1 Tree View

You can also switch to 'Tree' View which will show all the group and child Warehouses.

![Warehouse](/files/warehouse-tree.png)

### 2.2 Warehouse Account

In ERPNext, if you enable [Perpetual Inventory](/erpnext/v13/user/manual/en/stock/perpetual-inventory), every Warehouse must belong to a specific company to maintain
company-wise stock balance. To do so, each Warehouse should be linked with an
Account in the Chart of Accounts (the same name as the Warehouse itself). This account captures the monetary equivalent of the goods or materials stored in that specific warehouse.

If you have a more detailed Warehouse Tree, most likely it's a good idea to link the sub-locations (room, row, shelf, etc.) to the account of the actual Warehouse (the root Warehouse of that Tree) as most
scenarios do not require to account for value of stock items per Shelf or Bin. For example, if you have Warehouse A, and the room, rows are B, C, etc., then link B and C to the account of A.

> Tip: ERPNext maintains stock balance for every distinct combination
> of Item and Warehouse. Thus you can get the stock balance for any specific Item in a particular Warehouse on any particular date.

### 3. Related Topics

1. [Stock Entry Purpose](/erpnext/v13/user/manual/en/stock/articles/stock-entry-purpose)
2. [Stock Level Report](/erpnext/v13/user/manual/en/stock/stock-level-report)

<!-- page: erpnext/erpnext__warranty-claim.md -->
---
title: "Warranty Claim"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/warranty-claim"
updated: "2026-02-28"
---

**A Warranty Claim is when a Customer claims free repairs within the Warranty Period of the item/service you're providing.**

If you are selling Items under warranty or if you have sold and extended service contract like the Annual Maintenance Contract (AMC), your Customer may contact you about an issue or a break-down of the product and provide you the Serial No of this Item.

To access the Warranty Claim list, go to:


> Home > Support > Warranty > Warranty Claim
> 
> 

1. Prerequisites
----------------

Before creating and using Warranty Claim, it is advised that you create the following first:

* [Customer](/erpnext/customer)
* [Serial Number](/erpnext/serial-no)
* [Item](/erpnext/item)

2. How to Create Warranty Claim
-------------------------------

1. Go to the Warranty Claim list, click on New.
2. Select a Customer.
3. Select the Serial Number of the Item on which Warranty Claim is to be recorded. The system will then automatically fetch the Serial No’s details and indicate whether this is under warranty or AMC.
4. Enter a description of the Issue. User can upload and image and create a table.
5. Save. ![Warranty Claim](/files/warranty-claim.png)

### 2.1 Additional Options when Creating a Warranty Claim

* **Status**: While creating a Warranty Claim, the status will be set as "Open". User can change the status to:


	+ Work In Progress: Fix/repairs are being done on the Item.
	+ Closed: The repairs have been done and the Warranty Claim is now closed.
	+ Cancelled: The Warranty Claim was invalid, and the claim was closed.
* **Issue Date**: While creating the Warranty Claim, the current date will be captured. This field is editable.

3 Features
----------

### 3.1 Item and Warranty Details:

Once a Serial Number is selected, the following details about the Item will be fetched:

* Item Code
* Item Name
* Item Description

The details about Warranty/AMC will be fetched according to the Serial Number.

* **Warranty / AMC Status:** The possible options are "Under Warranty", "Out of Warranty", "Under AMC", or "Out of AMC". The status can be changed to Out of Warranty/AMC if the Item has been tampered with or Warranty is void depending on your terms of service.
* Warranty Expiry Date
* AMC Expiry date

![Warranty Serial](/files/warranty-serial.png)

### 3.2 Resolution

* **Resolution Date:** When the warranty or AMC is Closed, current date and time will be fetched in resolution Date field automatically. This field is also editable.
* **Resolved By:** Set the Email ID of the User who has resolved the Warranty Claim. The email ID is linked with [User](/erpnext/adding-users) created in the system.
* **Resolved Details:** This is a text field. User can enter details about the Warranty or AMC claim. A User can also upload the image, enter or create a table.

![Warranty Resolution](/files/warranty-resolution.png)

### 3.3 Customer Details

The following details of the [Customer](/erpnext/customer) will be fetched:

* Customer Name
* Contact Person
* Territory
* Customer Group
* Customer Address

**Service Address:** User can enter the Service Address if it is different from Customer Address.

![Warranty Customer](/files/warranty-customer.png)  


### 3.4 More Information

* **Company:** The Warranty or AMC is created from the company will be selected automatically.
* **Raised By:** User can enter the Name of the person who has raised the Warranty or AMC in case the Customer is an organization.
* **From Company:** User can enter the name of the company from which the warranty or AMC has been created.

If a Customer visit is required to address the issue, you can create a new Maintenance Visit record from this.

4. Related Topics
-----------------

1. [Issue](/erpnext/issue)
2. [Maintenance Visit](/erpnext/maintenance-visit)

<!-- page: erpnext/erpnext__warranty.md -->
---
title: "Warranty"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/warranty"
updated: "2026-02-27"
---

By effectively managing warranty claims and serial numbers within ERPNext's Support module, users can streamline customer support processes, ensure accurate tracking of warranty-related information, and enhance overall customer satisfaction by providing timely and effective resolutions to warranty claims.

* [Warranty Claim](/erpnext/user/manual/en/warranty-claim)
* [Serial Number](/erpnext/user/manual/en/serial-no)

  

<!-- page: erpnext/erpnext__web-form.md -->
---
title: "Web Forms"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/web-form"
updated: "2026-02-28"
---

Stakeholders who are not part of your organization may need to interact with your ERPNext instance. You can authorize customers, suppliers, job applicants, students, and guardians to access certain information or even create certain transactions. For example, you can let anyone create an account on your website (created with ERPNext) and apply for a job. You can let your customers see the details of the complaints they have registered. These can be done using Web Forms.

> There are two types of in-built interfaces available in ERPNext. The > *Desk View* and the *Web View*. Desk is for users who regularly interact > with ERPNext instance, like employees of your organization.

> Web View is for users who need to interact with an ERPNext instance occasionally. > Web forms are similar to the forms you generally fill in various websites on the > internet. Webforms are part of the *Web View* interface in ERPNext.

To create a new **Web Form** go to:


> Home > Website > Web Site > Web Form
> 
> 

![New Web Form](/files/new-web-form-1.png) *New Web Form*

Select the **DocType** based on which you want to build your Web Form. The **Route** will be set based on the **Title** of your Web Form. You can also add an Introduction text to show a friendly message above your form.

Add fields to your Web Form. These are the fields from the DocType you have selected. You can change the Label for these fields. Try to keep number of fields to be minimum as long forms are cumbersome to fill.

![Web Form Fields](/files/new-web-form-2.png) *Web Form Fields*

Click on **See on Website** in the sidebar to view your Web form. ![Web Form](/files/web-form.png) *Web Form*

Here is an explanation of each of the checkboxes on the right.

1. **Published**: Web Form will be accessible only if this is enabled.
2. **Login Required**: User can fill the Web Form only if they are logged in. When Login Required is checked,
3. **Route to Success Link**: Go to Success Link after the form is submitted.
4. **Allow Edit**: If this is unchecked the form becomes read-only once it is saved.
5. **Allow Multiple**: Allow user to create more than one record.
6. **Show as Grid**: Show records in a table format.
7. **Allow Delete**: Allow user to delete the records that he/she has created.
8. **Allow Comments**: Allow user to add comments on the created form.
9. **Allow Print**: Allow user to print the document in the selected Print Format.
10. **Allow Incomplete Forms**: Allow user to submit form with partial data.

2. Features
-----------

### 2.1 Sidebar

You can also show contextual links in a sidebar on your Web Form. Set it up in **Sidebar Settings**.

![Web Form Sidebar](/files/web-form-sidebar.png) *Web Form Sidebar*

![Web Form with Sidebar](/files/web-form-with-sidebar.png) *Web Form with Sidebar*

### 2.2 Creating Web Forms with Child Table

You can add child tables to your web forms, just like regular forms.

![Web form Grid](/files/grid-in-webform.png)  


### 2.3 Payment Gateway Integration

You can now add a Payment Gateway to the web form, so that you can ask users to pay against a web form. A good example for this is a conference ticket.

![Web form payment](/files/payment-in-webform.png)  


### 2.4 Portal User

We have also introduced roles for Website users. Before version 11, if you assigned any 'Role' to a user he would get access to 'Desk View'. From version 11 you can assign a 'Role' but still disallow access to 'Desk View' by unchecking 'Desk Access' in Role.

![Disallow Desk Access](/files/disallow_desk_access.png)  


In Portal Settings, you can set a role against each menu item so that only users with that role will be allowed to see that item.

![portal settings](/files/portal-settings.png)  


### 2.5 Custom Script

You can write custom scripts for your Web Form for things like validating your inputs, auto-filling values, showing a success message, or any arbitrary action.

To learn how to write custom scripts for your Web Forms, read [Custom Scripts documentation](https://frappeframework.com/docs/user/en/desk/scripting/client-script).

### 2.6 Custom CSS

You can customize the look and feel of your Web Form by writing your own Custom CSS. Inspect the elements on the page to see what classes are available for styling. Learn more about CSS [here](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics).

### 2.7 Actions

You can add the text in 'Success Message' field and this text will be shown to user once he successfully submits the web form . And the user is redirected to the URL given at 'Success URL' when clicked on 'Continue' button. This is only applicable to webforms accessible without the user login(webforms with 'Login Required' checkbox unchecked).

![Success Message](/files/success_message.png)  


### 2.8 Result

When a website user submits the form, the data will be stored in the document/doctype for which web form is created.

### 2.9 Customizing

For customizing web forms, see the [Frappe Web Forms Documentation](https://frappeframework.com/docs/user/en/web-form)

<!-- page: erpnext/erpnext__web-page-builder.md -->
---
title: "Web Page Builder\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/web-page-builder"
updated: "2026-02-28"
---


> Introduced in Version 13

**Page Builder lets you quickly create web pages from pre-configured web templates.**

## 1. How to create a page using Page Builder

1. Follow the steps to [create a Web Page](/erpnext/web-page).
1. Enable full width by ticking the "Full Width" checkbox.
1. Select Content Type as **Page Builder**.
1. Click on Add Row in the Page Building Blocks Table.
1. Select a Web Template.
1. Click on the **Edit Values** button.
1. Enter values in the dialog and click on Submit.
1. Click on Save.
1. The web page will be published only when **Published** is ticked.

![New Web Page with Page Builder](/files/new-web-page-with-page-builder.png)
_New Web Page with Page Builder_

![Page Builder Edit Values Dialog](/files/page-builder-edit-values-dialog.png)
_Page Builder Edit Values Dialog_

View your Web Page by clicking on **See on Website** in the sidebar.

![Web Page](/files/web-page-with-page-builder-preview.png)
_Web Page with Page Builder_

### 1.1 Add Sections

You can add more sections to your page by adding more rows in the Page Building Blocks
table. The framework comes with a great set of Web Templates for you to create
all sorts of pages.

![More Sections](/files/web-page-with-more-sections.png)
_Web Page with another section_

![More Sections - Preview](/files/web-page-with-more-sections-preview.png)
_Web Page with another section - Preview_

### 1.2 Section Options

If you click to expand a row in the Page Building Blocks table, you have the
following additional options:

- **Add Container**: If checked, the web template will be rendered in a centered constrained box.
- **Add Space on Top**: If checked, it will add a decent amount of space above the section.
- **Add Space on Bottom**: If checked, it will add a decent amount of space below the section.
- **Add Gray Background**: If checked, it will add a gray background to the section.
- **Hide Block**: If checked, it will hide the section block.
- **CSS Class**: Add any CSS class and style it in the CSS field in the Style section.

![Section Options](/files/page-builder-section-options.png)
_Section Options_

<!-- page: erpnext/erpnext__web-page.md -->
---
title: "Web Page"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/web-page"
updated: "2026-02-28"
---

**Static Content like your Home Page, About Us, Contact Us, Terms pages can be created using the Web Page.**

To access Web Page go to:


> Home > Website > Web Site > Web Page
> 
> 

1. How to create a Web Page
---------------------------

1. Go to the Web Page list and click on New.
2. Enter a Title and add content in Main Section. The route will auto generated but you can change it.
3. Click on Save.
4. The web page will be published only when **Published** is ticked.

![New Web Page](/files/new-web-page.png) *New Web Page*

View your Web Page by clicking on **See on Website** in the side bar.

![Web Page](/files/web-page.png) *Web Page*

### 1.1 Tips on making a good Web Page

#### Title

The first thing to set is the title of your page. The title has the maximum weight for search engines so choose a title that reflects the keywords that you are targeting for your audience. The route (URL) will be auto-generated from the title but you can change it.

#### Content

You can write your content in Rich Text, Markdown or HTML. If you want to make simple content pages, Rich Text and Markdown are great options.

> Learn markdown in a few minutes at [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).

#### Images

For Rich Text Content, you can directly embed images using the editor. For Markdown and HTML, you must attach the images to the document first. Now get the URL of your image by right-clicking on your attachment and copying the address.

![Image Link](/files/get-image-link.png)  


Now, add them to your Markdown or HTML using the appropriate syntax.


```
<!-- markdown -->
![Alt Text](/path/to/image-url.png)

<!-- html -->
<img alt="Alt Text" src="/path/to/image-url.png">
  

```
2. Features
-----------

### 2.1 Slideshow

You can also add a Slideshow to your Web Page. Refer how to create a Slideshow at [Homepage Slideshow](/erpnext/homepage#22-homepage-slideshow)

### 2.2 Scheduled Publishing

You can schedule your Web Pages for publishing if you set Start Date and End Date for your Web Page. They will be set as published within the date ranges and will be unpublished outside the range automatically.

Unpublished pages will throw an `Error 404` when they are visited.

### 2.3 Javascript and CSS

You can add a JS script to your Web Page in the **Script** section. Make sure to write your script inside the `frappe.ready` callback.


```
frappe.ready(() => {
    // your script here
});
  

```
You can add CSS styling to your Web Page in the **Style** section. Inspect the elements to see what classes are available for styling. If you are using HTML Content, you can use your own classes and style them here.

### 2.4 Sidebar

You can add a Website Sidebar with custom links on your Web Page. In the **Sidebar and Comments** section enable **Show Sidebar**. Select an existing Website Sidebar or create a new one.

![Web Page Sidebar](/files/web-page-sidebar.png) *Web Page Sidebar*

Add links and their route in the Sidebar Items table. ![Website Sidebar](/files/new-website-sidebar.png) *Website Sidebar*

![Web Page with Sidebar](/files/web-page-with-sidebar.png) *Web Page with Sidebar*

### 2.5 Comments

You can enable comments on your Web Page where people can leave a comment with their Name and Email. Enable comments from the **Sidebar and Comments** section.

![Web Page Comments](/files/web-page-comments.gif) *Web Page Comments*

### 2.6 Header

You can add a custom HTML for the header section of the page. This will override the title of the Web Page.

![Web Page Header](/files/web-page-header.png) *Web Page Header*

![Web Page with Custom Header](/files/web-page-with-custom-header.png) *Web Page with Custom Header*

### 2.7 Breadcrumbs

You can add a list of breadcrumbs on your Web Page. These will be shown on top before the header.

![Web Page Breadcrumbs](/files/web-page-breadcrumbs.png) *Web Page Breadcrumbs*

![Web Page with Breadcrumbs](/files/web-page-with-breadcrumbs.png) *Web Page with Breadcrumbs*

### 2.8 Meta Tags

You can also add Meta Tags to your Web Page. You must add the property key and its value in the Meta Tag Table and it will auto-generate HTML `meta` tags on your Web Page.

![Web Page Meta Tags](/files/web-page-meta-tags.gif) *Web Page Meta Tags*

<!-- page: erpnext/erpnext__website-banner.md -->
---
title: "Website Banner Resizing\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/website-banner"
updated: "2026-03-04"
---


Each ERPNext account website automatically generated from it. On a website, logo is set based on logo image selected in the Setup Wizard. You can change or edit property for your company's logo from the Website Settings.

`Explore > Website > Website Settings`

For the exact steps on how to upload a Website Banner and resize it, please refer to the help given below.

![Website Banner image](/files/brand-logo.gif)

<!-- page: erpnext/erpnext__website-components.md -->
---
title: "Website Components"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/website-components"
updated: "2026-02-28"
---

ERPNext offers a diverse set of website components that cater to various needs, including webpage elements like web forms, sidebars, and slideshows.

Web forms in ERPNext allow businesses to gather customer data efficiently through customisable forms embedded directly on web pages. Sidebars provide a convenient space on web pages to display navigational links, social media feeds, or promotional content, improving user experience and engagement. Slideshows are dynamic components that showcase images or promotions in a visually appealing manner, grabbing visitors' attention and conveying key messages effectively.

By leveraging these website components in ERPNext, businesses can create interactive, user-friendly web experiences that drive engagement and support their digital marketing strategies.

* [Web Page](/erpnext/user/manual/en/web-page)
* [Web Page Builder](/erpnext/user/manual/en/web-page-builder)
* [Web Form](/erpnext/user/manual/en/web-form)
* [Website Route Meta](/erpnext/user/manual/en/website-route-meta)

<!-- page: erpnext/erpnext__website-home-page.md -->
---
title: "Website Home Page"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/website-home-page"
updated: "2026-03-04"
---


It is very much possible in ERPNext to setup certain standard page as default website Home Page. Following are steps to setup default website home page.

#### **Step 1: Create a Web Page**
To create a web page go to: `Website > Web Site > Web Page` and then click on the `New` button in the upper right.

* Fill in the page title
* Give the page a route (keep it lower case)
* Add content to the `Main Content` section. If you want, you can use markdown to create a more complex page.
* Tick (Check) the `Published` check box
* Click the `Save` button.

#### **Step 2: Open Website Settings Page**
To Open website settings page go to: `Website > Setup > Website Settings`

#### **Step 3: Set Home page**

Enter the same value you entered for the `route` field in the previous section to the `Home Page` field. ERPNext will set this route to be the same as /index for your page.

![Website Setting Home](/files/Selection_021.png)

#### **Step 4: Save Website Settings Form.**

After setting up Home Page Press `Save` button from website settings page and refresh the system from Help menu. Like this you can set any standard page as your default website home page. When some one visited to your website, he/she will see home page as default landing page on your website.

<!-- page: erpnext/erpnext__website-route-meta.md -->
---
title: "Website Route Meta\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/website-route-meta"
updated: "2026-02-28"
---


**Arbitrary meta tags can be added in your web pages using Website Route Meta.**

Meta Tags are invisible tags that provide data about your page to search engines
and website visitors. When used correctly, these tags may help boost your SEO
and rankings on popular search engines. These tags will be placed in the
`` section of your page. ERPNext allows you add arbitrary meta tags in
your web pages to improve the SEO of your pages.

To access Website Route Meta go to:

> Home > Website > Web Site > Website Route Meta

## 1. How to add meta tags to a web page

1. Go to the Website Route Meta list and click on New.
1. Enter the route. Make sure the route doesn't start with a slash (`/`). A Web
 Page for this route should exist.
1. Add key value pairs for each meta tag. For e.g., to add keywords to your web
 page, enter "keywords" as the Key and add comma separated keywords in the
 Value column.
1. Click on Save.

![New Website Route Meta](/files/new-website-route-meta.png)
*New Website Route Meta*

Now if you check the page source of your web page, the meta tags will look
something like this:

```html


```

> **Note:** Meta Tags are not only limited to Web Page, but they can be added to
> any route that has a website page in ERPNext.
>
> For e.g., You can add meta tags to your blog posts if you know the route which
> you can get from the Blog Post form.

<!-- page: erpnext/erpnext__website-settings.md -->
---
title: "Website Settings\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/website-settings"
updated: "2026-02-28"
---


Website related settings like landing page and website wide theme can be
configured here.

To access Website Settings, go to:
> Home > Website > Setup > Website Settings

## 1. Landing Page

Configure the default landing page of your website by setting the **Home Page**
field to the route of that page. You can put any route here including standard
routes like `home`, `about`, `contact`, `login`, `all-products`, and `blog`.

You can also set a [Web Page](/erpnext/web-page) as the
landing page.

If you want to use the ERPNext [Homepage](/erpnext/homepage),
you must set it as `home`.

![Website Settings - Landing Page](/files/website-settings-landing-page.png)
*Website Settings - Landing Page*

You can also set the **Title Prefix** here. It will be appended to the browser title
on every page. You can put your company name here.

## 2. Website Theme

Create a personalized theme for your Website and set it here. Learn more about
configuring Website Theme [here](/erpnext/website-theme).

## 3. Brand

### 3.1 Brand Logo

You can set the brand logo for your website in this section. Upload the Brand
Image first and then click on "Set Banner from Image" button. It will generate a
Banner HTML with your uploaded logo.

![Website Settings - Banner Image](/files/website-settings-banner-image.png)
*Website Settings - Banner Image*

### 3.2 Favicon

You can also set the favicon of your website in this section. It appears on the
left side of the browser tab.

![Website Settings - Favicon](/files/website-settings-favicon.png)
*Website Settings - Favicon*

View your website by clicking on **View Website** in the action bar on top right.

![Website with Brand and Favicon](/files/website-brand-and-favicon.png)
*Website with Brand and Favicon*

## 4. Top Bar

You can customize the menu items in the navbar of your website from the **Top Bar**
section.

![Website Setting - Top Bar](/files/website-settings-top-bar.png)
*Website Setting - Top Bar*

![Website Navbar Items](/files/website-navbar-items.png)
*Website Navbar Items*

## 5. Banner

You can add a persistent banner to your website which will be shown above the
navbar on all web pages. You can write any valid Bootstrap 4 markup here.

![Website Settings - Banner](/files/website-settings-banner.png)
*Website Settings - Banner*

![Website Banner](/files/website-banner.png)
*Website Banner*

## 6. Footer

You can add address information and categorized links to your footer in the
**Footer** section.

![Website Settings - Footer Address](/files/website-settings-footer-address.png)
*Website Settings - Footer Address*

![Website Settings - Footer Links](/files/website-settings-footer-links.png)
*Website Settings - Footer Links*

![Website Footer](/files/website-footer.png)
*Website Footer*

#### Configuring "Powered by" Section

You can configure Powered by section by editing "Footer Powered By"

## 7. Google Integrations

### 7.1 Google Indexing

#### How to set up automated Google Indexing

In order to allow ERPNext to request Google crawlers to index a web page, you need to authorize ERPNext to send a request whenever the user requests the data. Google Drive Integration is set up with the following steps:

- Create OAuth 2.0 Credentials via [Google Settings](/erpnext/google_settings)

- Enable indexing in the Website Settings

- Now click on **Authorize API Indexing Access** to authorize ERPNext to send a publish request.

- Once Authorized, an indexing request is automatically sent on creation/update/trash of any new blog post or web pages created via the user.

![Google Integrations](/files/website-settings-integrations.png)
*Google Integrations*

### 7.2 Google Analytics

You can enable Google Analytics on your website. Just get your [Google Analytics
ID](https://support.google.com/analytics/answer/1008080?hl=en) from your Google
Console and set it here.

By default, Google Analytics will collect the full IP address of your website visitors.
By checking "Google Analytics Anonymize IP", ERPNext will instruct Google Analytics to
anonymize the IP address before it is sent to Google servers. You can find out more about
the effect of this setting in [Google's documentation](https://support.google.com/analytics/answer/2763052).

## 8. HTML Header

You can use this section to set meta tags across all of your web pages. A common
use case is to add Google site verification tags.

![Website Settings - Header](/files/website-settings-header.png)
*Website Settings - Header*

## 9. Robots

You can define `robots.txt` rules in this section. This information is used by
web crawlers to decide which pages to index and which to skip.

![Website Settings - Robots](/files/website-settings-robots-txt.png)
*Website Settings - Robots*

> Learn more about `robots.txt` at [Moz - Robots.txt](https://moz.com/learn/seo/robotstxt)

## 10. Redirects

You can define a mapping of route redirects here. The mappings in the following
screenshot makes sure that if a user visits `https://apple.erpnext.com/iphone`,
they will be redirected to `https://apple.erpnext.com/products/iphone`.

ERPNext will raise a `301 Permanent Redirect` response for these routes.

![Website Settings - Routes Redirects](/files/website-settings-route-redirects.png)
*Website Settings - Routes Redirects*

> If you are migrating your existing website to ERPNext based website,
> you can map your old routes to new ones here and these redirects will be
> picked up by Google and will help you maintain your SEO rankings.

## 11. Chat

You can enable website visitor chat on your website in the Chat section. The
chat widget will be shown between **From** time and **To** time. You can also
set **Chat Operators** (Users) who will get notified when a visitor sends a
message.

> Chat is an experimental feature.

<!-- page: erpnext/erpnext__website-theme.md -->
---
title: "Website Theme\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/website-theme"
updated: "2026-02-28"
---


ERPNext provides advanced theming capabilities to customize the look and feel of
your website and make it match your brand.

> Home > Website > Setup > Website Theme

## 1. How to create a Website Theme

1. Go to the Website Theme list and click on New.
1. Enter a Theme Name.
2. Customize your theme.
3. Click on Save.

> **Note:** Make sure you set the Website Theme in Website Settings for the
> theme to be applied.

![Select Website Theme in Website Settings](/files/website-theme.png)

## 2. Features

### 2.1 Theme Configuration

The section "Theme Configuration" is there for bootstrapping a basic theme. Here
you can choose your color scheme, font and button styles.

### 2.2 Stylesheet

If you know [SCSS](https://sass-lang.com/guide) and [Bootstrap 4 theming](https://getbootstrap.com/docs/4.3/getting-started/theming/),
you can manually write custom SCSS.

In the "Custom Overrides" field you can overwrite the variables defined by any
app's theme file. The content of this field will be included *before* importing
any other SCSS. For example, the variable `$spacer` is set to `1rem` by default.
Just redefine it to `$spacer: 2rem;` to make all spaces twice as big.

In the "Custom SCSS" field you can add your own styles. This will be included
*after* importing the app's themes. You can also override any specific style.
For example, if you don't like our buttons, just include the following:

```scss
.btn-primary {
 background-color: $teal;
 color: $orange;
}
```

### 2.3 Included Theme Files

If you take a look at the default theme generated by the configure dialog, it
imports `frappe/public/scss/website` and `erpnext/public/scss/website`. These
are the default theme files for `frappe` and `erpnext` app. If you have any other
apps installed, they might also provide their own `website.scss` file.

The section "Included Theme Files" lists all installed apps. Each app can bring
it's own theme file (`[app]/public/scss/website.scss`). A theme might be complete,
providing styles for the entire website, or just an add-on. For example, it might
style only the elements it introduces. By checking the boxes you can choose which
theme should be included in your website.

![Included Theme Files](/files/website-theme-included-theme-files.gif)

### 2.4 Custom JS

You can also write custom JavaScript that will run when your theme is applied.
Use it add/remove classes from elements, or any script that helps you change how
your elements look.

<!-- page: erpnext/erpnext__website.md -->
---
title: "Website Setup"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/website"
updated: "2026-02-28"
---

Setting up a website in ERPNext involves a seamless process to establish an online presence for your businesses. There is a user-friendly Website module that allows users to create, customize, and manage their websites with ease.

Users can start by selecting a theme from a range of pre-designed templates or create a custom design using ERPNext's built-in tools. The Website module provides intuitive drag-and-drop functionality for adding and arranging elements such as text, images, videos, forms, and interactive components.

* [Website Theme](/erpnext/user/manual/en/website-theme)
* [Home Page](/erpnext/user/manual/en/website-home-page)

<!-- page: erpnext/erpnext__website_item.md -->
---
title: "Website Item"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/website_item"
updated: "2026-03-02"
---

The Website information about an Item has been moved to a new DocType called **Website Item**. Publishing an Item is as simple as a button click. Once an Item has a Website Item created against it, it is successfully published.

The Prerequisites here are [Items](/erpnext/item).

### Publishing an Item

The **Publish in Website** button is visible on every **unpublished** item under **Actions**. This button will create a **Website Item** and thus publish the Item on the website.

![Publish Item](/files/publish-item.gif)  


If you visit `your-site-name/all-products` , you will see the newly created Website Item listed here.

> To view the Website Item page on the website click on the **See on Website** link on the top left just above the item image in the Website Item document.

### Updating the Website Item

![Website Item Page](/files/web-item-page-overview.png) *Website Item Page*

Once a Website Item has been created, you can update information in it that will be displayed on the website. Here are the fields:

#### General

1. **Website Item Name**: The title of the Website Item on the website is picked from this field.
2. **Route**: This is auto-generated and just mentions the route your Item’s full page view will be available at.
3. **Published**: If you want to hide or take down your published Item, you can uncheck this checkbox.

#### Display Images

1. **Website Image**: It is automatically populated with the Image from the Item master. You can change it as well.
2. **Slideshow**: If you add a Slideshow, that will be shown in the Website Item’s page. If a slideshow is absent, it will default to showing the website image (if present).
3. **Image Description**: It is an alternative text in case the image fails to appear.

#### Stock Information

1. **Website Warehouse**: Select the Warehouse that will hold the stock for this Website Item. The Website Item’s availability will be shown depending on the balance stock in this selected Warehouse.
2. **On Backorder**: If enabled then it will be indicated that the Website Item is available on backorder and not usually pre-stocked. **Available on Backorder** will be visible instead of **Out of Stock** or **In Stock**.

> Note: If the Website Warehouse isn't set and 'Maintain Stock' for an Item is ticked, the product page will list the Item as 'Not in Stock'.

#### Display Information

1. **Short Website Description**: This is a text field where you can mention a short summary like description, for the **List View**. You can also add some HTML here that will show up in the List View. e.g `This item is <b>100%</b> pure!`
2. **Website Description**: This is a rich text editor field, where you can format your website item description to make it attractive and informative. The Item Description is used as a fallback if a Website Description is not mentioned.
3. **Website Specifications**: You can mention the Website Item's specifications such as weight, manufacturer, dimensions, material, etc. You can also add common specifications in the Item Group that this Website Item belongs to and copy it here by clicking on **Copy From Item Group**. This information will be visible on the **Product Details** section in the Website Item’s page.

#### Display Additional Information

The **Product Details** section can be viewed in a tabbed section along with other information too. For this:

* In the **Display Additional Information** section, and enable **Add Section with Tabs**.
* You can now add tabs in the **Tabs** table by adding a label and content for it. The content field is an HTML editor where you can add advanced HTML, to beautify your tab, or a simple paragraph.
* This tabbed section will set **Product Details** as the first tab which will contain the **Website Specifications** stated above (if present).
* This will be followed by tabs from the **Tabs** table

![Website Item Product Details](/files/web-item-product-details.png)  


#### Recommended Items

You can show **Recommended Items** against Website Items to knudge users to pay attention to a closely related item. This can be enabled by going to **E Commerce Settings** > **Add-ons** > **Enable Recommendations**.

You can then add Recommended Items against a Website Item in the **Recommended Items** section, and add the items to recommend. These will show up in the Website Item Page.

![Recommended Items](/files/recommended-items.png)  


#### Offers

Coupon Codes can be added at checkout , but customers must know about these codes. For this, **Offers** can be added to the Website Item for display.

* Go to the **Offers** section in the Website Item.
* Add a short offer title that is one/two words, in the **Offer Title**.
* Add a slightly longer subtitle, a sentence in the **Offer Subtitle**.
* Add lengthy details about the offer in the **Offer Description**. **Save**.

![Website Item Offers](/files/web-item-offers.png)  


#### Search and SEO

1. **Ranking**: Assign a rank to the Website Item to have control over it's position in the Product Listing. Website Items with higher ranking will be shown higher.
2. **Set Meta Tags**: Meta tags help with SEO. See [Web Page](/erpnext/web-page) to know how to add them.
3. **Website Item Groups**: In this table you can select existing or create new [Item Groups](/erpnext/item-group) to classify items on your website. The Website Item will be visible under Item Group Pages of the Item Groups mentioned in this table.

#### Advanced Display Content

You can add an additional styled section using Bootstrap 4 markup for the Website Item page. ![Website Item Advacned Display](/files/web-item-advanced-display.png)  


### Adding Price Details

Prices can be added against Website Items via **Item Price**. Before adding an Item Price, go to **E Commerce Settings** and make sure **Company, Price List , Default Customer Group** are set.

Now you can go ahead and create an **Item Price** for the Website Item, and select the **Price List** as the one in the **E Commerce Settings**.

You can also add a **Pricing Rule** with a **Discount Percentage** or **Discount Amount** on the existing item price, to show **striked prices**. ![Website Item Page Striked Price](/files/web-item-striked-price.png)  

<!-- page: erpnext/erpnext__weekly-auto-repost.md -->
---
title: "Weekly Auto Repost"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/weekly-auto-repost"
updated: "2026-07-01"
---

# Auto Repost of Incorrect Stock Valuation in ERPNext

---

## 1. What is this feature?

Sometimes the stock value recorded against an item can become **incorrect**. This usually happens when several stock transactions for the **same item and warehouse** are entered very close together (or backdated), and the system ends up calculating the stock value from the wrong earlier transaction.

When this happens:

- The **stock value** shown in your reports doesn’t match what it should be, **or**
- The **stock value** and the **accounting value** (your inventory ledger in the General Ledger) no longer agree.

Normally, fixing this means a person has to open the relevant reports, spot the wrong entries, and manually trigger a “repost” to recalculate them.

**This feature automates that clean-up.** Once you switch it on, the system **checks your stock every week** and, where it finds incorrect values **in the current financial year**, it **automatically reposts the affected items** to correct them — no manual effort required.

---

## 2. When should you use it?

Turn this on if **any** of the following are true for your business:

- You enter a **high volume** of stock transactions, especially many for the same items and warehouses.
- You frequently make **backdated** or **corrective** stock entries.
- You’ve previously found mismatches in the **Stock Ledger Variance** report or the **Stock and Account Value Comparison** report and had to fix them by hand.
- You want **stock value and accounting value to stay reconciled** without someone checking every week.

When **not** to rely on it:

- If you only have a **small number** of stock transactions and rarely see valuation issues, you may not need it (you can still turn it on for peace of mind — it simply does nothing when there’s nothing to fix).
- It is **not** a replacement for correct setup. If the underlying configuration is wrong (see Section 6), the feature will **tell you** rather than silently repost.

---

## 3. What exactly does it check and fix?

Every week the system looks at two standard reports for **each company**:


| Report                                 | What it catches                                                                                                 |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Stock Ledger Variance**              | Items whose stock quantity/value has become internally inconsistent (the “wrong previous transaction” problem). |
| **Stock and Account Value Comparison** | Vouchers where the **stock value** does not match the **accounting value** posted to the inventory account.     |


For anything it finds **in the current financial year**, it automatically creates a **repost** to recalculate and correct the values.

**Important:** it only acts on the **current financial year**. Older periods are intentionally left untouched (they are usually closed/audited, and reposting them could disturb finalised accounts). If you need to correct a previous year, do that manually and deliberately.

---

## 4. How to turn it on (step by step)

1. In the search bar, go to **Stock Reposting Settings**.
2. Find the section **Auto Reposting of Incorrect Valuation**.
3. Tick the checkbox **“Auto Repost Incorrect Valuation Entries (Weekly)”**.
4. **Save**.

That’s it. The feature is **off by default**, so nothing happens until you tick this box. Once ticked, it runs **automatically once a week** in the background — you don’t need to start it manually.

To turn it off again, simply un-tick the box and Save.

---

## 5. What happens after it runs?

- The system quietly creates **Repost Item Valuation** entries for the items/vouchers that need correcting. These run in the background and update the stock values.
- You can review what was reposted by opening the **Repost Item Valuation** list.
- It is designed to be **safe to run repeatedly**: it will not create duplicate reposts for something that is already being corrected.

You generally don’t need to do anything — corrected values will simply appear once the reposts finish.

---

## 6. The one thing it can’t fix on its own — and how you’ll know

Some mismatches are **not** caused by calculation order, but by a **setup mistake**: a **warehouse is linked to the wrong type of account**.

For inventory accounting to work, a warehouse must be linked to an account whose **Account Type is “Stock”**. If a warehouse points to some other kind of account (for example a normal expense or receivable account), then **no amount of reposting will ever make the values match** — the problem is the configuration, not the calculation.

When the feature detects this situation, it does **not** waste time reposting. Instead it **sends a notification to the System Manager** describing:

- which voucher is affected,
- which warehouse is involved, and
- which account is set incorrectly.

**What to do if you receive this notification:**

1. Open the **Warehouse** mentioned in the message.
2. Check the **Account** linked to it.
3. Make sure that account’s **Account Type is “Stock”** (or link the warehouse to the correct Stock account).
4. Save. The next weekly run (or a manual repost) can then reconcile the values.

---

## 7. Good to know (limitations & tips)

- **Journal Entries are never auto-reposted.** ERPNext does not repost Journal Entries, so any stock/account difference caused by a manual Journal Entry to an inventory account will **not** be touched by this feature. Review and correct those manually.
- **Current financial year only.** Older periods are deliberately skipped.
- **Runs weekly.** It is a scheduled clean-up, not an instant fix. If you need an urgent correction, you can still trigger a repost manually as before.
- **Large companies:** the weekly check examines every item-warehouse, so on very large databases it runs as a background task and may take a while — this is normal and does not slow down day-to-day work.
- **Notifications may repeat:** if a wrongly-configured warehouse account is not fixed, you may receive the same notification on the following week’s run until it is corrected.

---

## 8. Quick FAQ

**Q: Will it change my accounts or stock without telling me?**  
It corrects stock **valuation** by reposting (the standard, supported way ERPNext recalculates stock value). It only acts on genuinely incorrect entries in the current year. For configuration problems it **notifies** rather than changing anything.

**Q: Is it safe to leave on permanently?**  
Yes. When there’s nothing wrong, it simply finds nothing and does nothing.

**Q: Can I see what it did?**  
Yes — check the **Repost Item Valuation** list to see the reposts that were created.

**Q: I turned it on but nothing happened.**  
It runs on a **weekly schedule**, not immediately. Also, if your stock values are already correct, there’s nothing for it to do.

**Q: Who gets the “wrong account” notification?**  
Users with the **System Manager** role.

<!-- page: erpnext/erpnext__what-if-emails-are-not-being-received-by-the-recipients.md -->
---
title: "What if Emails are not being received by the Recipients?"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/what-if-emails-are-not-being-received-by-the-recipients"
updated: "2026-03-04"
---

When an Email is sent, you assume that the Email will be received by the Recipient, but if you receive a feedback that they haven't received the Email, following are the steps to troubleshoot:

  


1) Sending an Email to an Email address that is misspelled or does not exist results in that Email not being delivered. While it seems obvious, it is easily overlooked and happens often.

  


2) The second thing you can do to check is to send an Email to yourself, this can be done via creating a New Communication.

  


*Go to Communication List > Click on New.* 

  


3) If the above method fails, kindly configure your Email Account again.

  


*Go to Email Account > Open the Email to check > if as per you everything is correct, click on Save. It will throw an error if there is any issue with the Configuration and you can rectify it accordingly.*

  


4) Check Email Queues for the unsent messages or errors if any.

  


*If the state is Error(as in the screenshot below), you can find the error cause by opening that email and scroll down to Error field to know the error.* 

  


![](/files/lNVCy3g.png)

  


![](/files/NJJmwTX.png)

  


***﻿NOTE: The error can differ from what can be seen in the above screenshot.***

  

<!-- page: erpnext/erpnext__why-ERP.md -->
---
title: "Why should businesses use an ERP?"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/why-ERP"
updated: "2026-08-14"
---

> If you are already convinced you need an all-in-one enterprise solutions system for your organization, you can skip this page.



Today, small and medium-sized businesses (SMEs) also face some of the problems that large enterprises do. One of them being planning and managing their resources. SMEs face similar complexities but have limited resources to deal with them.

Small businesses (like their bigger counterparts) have to:

1. Do accounts to track their sales/purchases.
2. Do their taxes.
3. Pay their employees.
4. Manage deliveries within promised timelines.
5. Deliver quality goods and services.
6. Communicate with customers, answer their queries.

Large enterprises invest millions of dollars in highly sophisticated systems like SAP. SAP and similar systems are able to handle requirements from these large enterprises to bring their **multi-country**, **multi-company**, **multi-currency**, global businesses into a single platform. This has helped them achieve consolidation of data/records in the fundamental processes such as accounting, taxation, payroll, reporting, and supply chain to name a few.



In contrast to large enterprises, SMEs have been left out of the **1st wave of digital revolution (1995-2015)**. The main reason for being left out is because they don't have the financial resources to **license, hire programmers and customize** such software to match their needs. Systems like SAP have been a **no-go** for most SMEs. Such systems need a **minimum** CAPEX or OPEX layout of **$100k (Yes, One Hundred Thousand Dollars)** and upwards. Even with cloud offerings (Software as a Service, SAAS) from such vendors, there is no easy Do It Yourself (DIY) people can feel confident about.



So even today, small businesses continue to struggle to keep things organized. They often use a mix of applications and tools such as spreadsheets, accounting software, web-based CRMs to manage their day to day record keeping. As a consequence, they have to access different systems to understand customers' master data, sales, cash flows, or profitability. The information exists in different silos. It becomes hard to combine the data in order to get useful insights or alerts. This leads to SMEs being **reactive** instead of being **proactive** in their day to day operations. With such a constrained way of working, there's limited scope for **growth**.



ERPNext addresses some fundamental problems SMEs struggle with when managing their resources:

1. **Affordability**: It is a Free and Open Source Software, freely available to download and install.
2. **Completeness**: All necessary modules are available. [View full list](https://erpnext.com/docs/v13/user/manual/en).
3. **Customization**: It is easy to add fields, or add more features.
4. **Efficiency**: Computing requirements are relatively low (cheaper to host and manage).
5. **Wholesomeness**: A single system and database that allows multiple users to record transactions or extract data simultaneously.

## Is ERPNext only for SMEs?

ERPNext is a powerful and versatile ERP system that is well-suited for SMBs and large enterprises and is equally competitive as any of the market leaders of ERP world. It is highly scalable, flexible, secure, lightening-fast, high-performance, cost-effective, and compliant. It also offers a wide range of features and benefits that can help large enterprises to improve their operations and achieve their goals.

Here are brief highlights on how ERPNext can benefit large enterprises:

- **ERPNext can help large enterprises to improve their financial performance.** ERPNext provides real-time insights into financial data, which can be used to make better decisions about budgeting, forecasting, and investing.
- **ERPNext can help large enterprises to streamline their operations.** ERPNext can automate tasks and processes, which can free up employees to focus on more strategic work.
- **ERPNext can help large enterprises to automate their supply chain.** ERPNext can improve efficiency and reduce costs by automating the flow of information of goods and materials.
- **ERPNext can help large enterprises to make better decisions.** ERPNext provides real-time data and insights, which can be used to identify trends, make predictions, and optimize operations.

If you are a large enterprise looking for an ERP system that can help you to improve your operations and achieve your goals, ERPNext is a good option to consider. Here are some of the strengths of ERPNext that make it a good solution for large enterprises:

- **Scalability:** ERPNext is a cloud-based ERP system, which means that it can scale to meet the needs of even the largest enterprises. It can be easily deployed and managed on a large number of users and devices.
- **Flexibility:** ERPNext is a highly flexible ERP system that can be customized to meet the specific needs of any business. It has a wide range of modules that can be used to manage different aspects of a business, such as accounting, manufacturing, sales, and HR.
- **Security:** ERPNext is a secure ERP system that uses industry-standard security features to protect data. It has a robust authentication system that prevents unauthorized access to data.
- **Performance:** ERPNext is a high-performance ERP system that can handle large volumes of data and transactions. It is designed to be efficient and reliable, even under heavy load.
- **Support:** ERPNext has a strong community of users and developers who provide support. There are also a number of third-party partners who offer professional services for ERPNext.Check out a variety of [User Stories](https://erpnext.com/blog/customer-success-stories) to know more.

<!-- page: erpnext/erpnext__wishlist.md -->
---
title: "Wishlist"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/wishlist"
updated: "2026-03-02"
---

ERPNext gives users the provision to enable the **Wishlist** feature on their web store. To enable this go to:

> E Commerce Settings > Add-ons > Enable Wishlist

Users can add Website Items to their wishlist via the wishlist icons on:
#### The Product Listing
![Wishlist from Card](/files/wishlist-card.png)

#### The Website Item Page
![Wishlist from Website Item Page](/files/wishlist-web-page.png)

The link to the Wishlist page is available on the navbar as seen above. Users can remove items from the Wishlist or move the items to Cart.

![Wishlist Page](/files/wishlist.png)
*Wishlist Page*

> This feature requires users to be logged in. Guest users will be redirected based on the **Guest Display Settings** section in **E Commerce Settings**.

<!-- page: erpnext/erpnext__withdrawing-salary-from-owners-equity-account.md -->
---
title: "Withdrawing Salary from Owner's Equity Account\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/withdrawing-salary-from-owners-equity-account"
updated: "2026-08-14"
---

Jordan Lee owns Nova Electronics Trading and wants to take $1,000 from the business for personal use. This is not payment for work performed by an employee. Recording it as salary expense would reduce Nova's profit and could misstate both management reports and tax records.



When the payment is legally an owner's draw, distribution, or dividend, record it against an Equity account instead of a salary Expense account. Nova uses **Dividends Paid** for this example because it already exists in the child company's approved Chart of Accounts. Ask a qualified accountant which equity account and tax treatment apply to your legal structure and jurisdiction.

## Before you begin

Confirm that the withdrawal is not payroll, reimbursement, a director loan, or repayment of money the owner previously advanced to the company. Those situations require different accounts and may require payroll or tax reporting.

- Identify the bank or cash account from which money will leave.
- Confirm the appropriate non-group Equity account with your accountant.
- Use a posting date in an open [Accounting Period](/erpnext/accounting-period).

## Check the equity account

Open the [Chart of Accounts](/erpnext/chart-of-accounts) for the company. Use an existing approved equity-withdrawal account, or ask an authorised accountant to create one under the Equity root.

![Nova Electronics Trading Chart of Accounts used to locate an equity withdrawal account](https://novacompanies.m.frappe.cloud/files/docs-accounting-reports-20260814-owner-draws-chart-of-accounts.png)

## Record the withdrawal

1. Open [Journal Entry](/erpnext/journal-entry) and create a new record.
2. Select Nova Electronics Trading and enter the posting date.
3. Debit **Dividends Paid - NET** by $1,000.
4. Credit **Nova Operating Bank - NET** by $1,000.
5. Add a clear remark identifying the transaction as an owner withdrawal, then save and submit.

![Submitted owner withdrawal Journal Entry debiting Dividends Paid and crediting Nova Operating Bank](https://novacompanies.m.frappe.cloud/files/docs-accounting-reports-20260814-owner-draw-journal-entry.png)

## Understand the accounting impact


| Account                    | Debit  | Credit | Effect                                                                  |
| -------------------------- | ------ | ------ | ----------------------------------------------------------------------- |
| Dividends Paid, Equity     | $1,000 |        | Reduces the owner's accumulated equity without creating salary expense. |
| Nova Operating Bank, Asset |        | $1,000 | Reduces the company's bank balance.                                     |


The entry does not affect the Profit and Loss Statement because neither row uses an income or expense account. It reduces Cash and Equity on the [Balance Sheet](/erpnext/accounting-reports). Verify the result in the [General Ledger](/erpnext/general-ledger) before relying on financial statements.

## Troubleshooting

### The withdrawal appears as salary expense

The debit row uses an Expense account. Cancel and amend the entry according to your controls, then use the approved Equity account after confirming the treatment with your accountant.

### The entry cannot be submitted

Check that debit and credit totals match, both accounts belong to the selected company, the posting period is open, and the bank account permits posting.

## Frequently asked questions

### Can every business owner use an owner's draw?

The permitted treatment depends on the entity type and local law. Corporations, partnerships, and sole proprietorships may treat payments to owners differently.

### Should I use Payment Entry instead?

A [Payment Entry](/erpnext/payment-entry) is normally used for customer, supplier, employee, or account transfers. A Journal Entry makes the equity debit and bank credit explicit for this accounting adjustment.

### Does this replace payroll?

Payments that are legally salary or wages must continue through the applicable payroll process. An owner withdrawal is not a shortcut around payroll obligations.

## Related topics

- [Journal Entry](/erpnext/journal-entry)
- [Chart of Accounts](/erpnext/chart-of-accounts)
- [General Ledger](/erpnext/general-ledger)
- [Payment Entry for Capital Account](/erpnext/payment-entry-for-capital-account)
- [Accounting Entries](/erpnext/accounting-entries)

<!-- page: erpnext/erpnext__woocommerce_integration.md -->
---
title: "WooCommerce Integration"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/woocommerce_integration"
updated: "2026-02-27"
---


> Deprecated in Version 15
> 
> 

Using WooCommerce Integration, the system creates Sales Orders in ERPNext for the orders created on WooCommerce using the WooCommerce webhook.

While creating a Sales Order from WooCommerce, if the Customer or Item is missing in ERPNext, the system will create new Customer/Item by using the respective details from WooCommerce order data. It also creates Address linked to the Customer using the shipping details from the order data.

1. How to set up WooCommerce?
-----------------------------

### 1.1 Generate API Key and API Secret

1. From your WooCommerce site's sidebar, click on Settings.
2. Click on the "Advanced" tab then click on the REST API link.

![Woocommerce API](/files/wc-add-key.png)
3. Click on "Add key" button. Provide the necessary details and click on "Generate API key" button.

![Woocommerce API Key](/files/wc-generate-keys.png)

### 1.2 Woocommerce Settings

1. On your ERPNext site, go to: **Home > Integrations > Settings > Woocommerce Settings**.
2. Paste the API key and secret generated in the previous step into the "API consumer key" and "API consumer secret" fields.
3. In the "Woocommerce Server URL" paste the url of your WooCommerce site.
4. Make sure "Enable Sync" is checked.
5. Select the "Tax Account" and "Freight and Forwarding Account" in the Account Details Section.
6. Select the "Creation User" in Defaults section. This user will be used to create Customers, Items and Sales Orders. Ensure that the user has the relevant permissions.
7. Select the "Company" that will be used to create the Sales Orders.
8. Click Save.
9. After saving the Woocommerce Settings, "Secret" and "Endpoint" are generated automatically.

![Woocommerce Settings](/files/woocommerce-settings.png)  


### 1.3 Woocommerce Webhook Settings

1. Now from your woocommerce site's sidebar, go to Settings.
2. Click on the "Advanced" tab then click on the Webhooks link and then click on "Add webhook" button.
3. Give the webhook a name of your choice.
4. Click on Status dropdown and select "Active".
5. Select Topic as "Order created".
6. Copy the "Endpoint" from "Woocommerce Settings" doctype in your ERPNext site and paste it in "Delivery URL" field.
7. Copy "Secret" from "Woocommerce Settings" doctype in your ERPNext site and paste it in "Secret" field.
8. Keep API VERSION as it is and click on Save Webhook. Now it is successfully set up.

![Woocommerce Webhook](/files/wc-webhook.png)  


A GIF below to show the entire process:

![Woocommerce Set Up](/files/woocommerce-setup.gif)  



> **Note:** In the above screenshot and GIF, in place of delivery url on woocommerce website, you need to paste the url you will obtain after saving the "Woocommerce Settings" in the "Endpoint" field in your ERPNext instance. Here other URL was pasted as localhost was being used.
> 
> 

### 1.4 Woocommerce order creation and syncing

1. From your Woocommerce website, register yourself as a user on the Account page.
2. Now Click on Addresses option and provide the required details.
3. Click on "Shop" option and now available products can be seen.
4. Add the desired products into the cart and click on **View Cart**.
5. From the cart, once you have added the desired products, you can click on "Proceed to Checkout".
6. All billing details and Order details can be seen now. Once you are ok with it, click on **Place Order** button.
7. "Order Received" message can been seen indicating that the order has been placed successfully.
8. Now on your ERPNext instance, check the following Document Types: Customer, Address, Item, Sales Order. They will be fetched and created from the webhook data.
9. In case the orders are not synced, you can check the error in **Home > Settings > Core > Error Log**.

![Woocommerce Set Up](/files/woocommerce-order.gif)  


2. Features
-----------

### 2.1 Defaults

In the Woocommerce Settings DocType:

* **Warehouse**: This Warehouse will be used to create Sales Orders. The default Warehouse is "Stores".
* **Delivery After (Days)**: This is the default offset (days) for the Delivery Date in Sales Orders. The default offset is 7 days from the order placement date.
* **Sales Order Series**: You can set a separate series for Sales Orders created via woocommerce. The default series is "SO-WOO-".
* **UOM**: This is the default UOM used for Items and Sales Orders. The default UOM is "Nos".

![Woocommerce Defaults](/files/wc-defaults.png)  


3. Related Topics
-----------------

1. [Sales Order](/erpnext/sales-order)
2. [Item](/erpnext/item)
3. [Customer](/erpnext/customer)
4. [Address](/erpnext/address)

<!-- page: erpnext/erpnext__work-order-consumed-materials.md -->
---
title: "Work Order Consumed Materials"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/work-order-consumed-materials"
updated: "2026-03-02"
---


To access the Work Order Consumed Materials, go to:

> Home > Manufacturing > Reports > Work Order Consumed Materials

![Task](/files/work-order-consumed-materialse15a6b.png)

This report shows the information about the raw materials which has been transfer to work in progress warhouse as well consumed in manufacturing process.

<!-- page: erpnext/erpnext__work-order-summary.md -->
---
title: "Work Order Summary\n"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/work-order-summary"
updated: "2026-02-26"
---


To access the Work Order Summary, go to:

> Home > Manufacturing > Reports > Work Order Summary


![Task](/files/work-order-summary.png)

This report will give information about the Work Order. Using this report user will understand the number of produced quantity against each Work Order as well the status of the Work Order.

Using this report user can check the status of the Work Orders which are linked to the Sales Order. Also using this report users can check the Work Orders based on the status like Not Started, In Process, Completed, and Stopped.

<!-- page: erpnext/erpnext__work-order.md -->
---
title: "Work Order"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/work-order"
updated: "2026-02-27"
---

**A Work Order is a document given to the manufacturing shop floor by the Production Planner as a signal to manufacture a certain quantity of a certain Item.**

![Work Order](/files/manufacturing-flow-wo.png)  


The Work Order also helps generate the material requirements (Stock Entry) for the Item to be produced from its **Bill of Materials**.

The **Work Order** can be generated from the [Production Plan](/erpnext/production-plan) based on Sales Orders.

To access the Work Order list, go to:

> Home > Manufacturing > Production > Work Order

1. Prerequisites
----------------

Before creating and using a Work Order, it is advised that you create the following first:

* [Bill Of Materials](/erpnext/bill-of-materials)
* [Operation](/erpnext/operation)
* [Workstation](/erpnext/workstation)

2. How to Create a Work Order
-----------------------------

1. Go to the Work Order list, click on New.
2. Select the Item to be manufactured.
3. The default BOM for that item will be fetched by the system. You can also change the BOM.
4. Enter the quantity to manufacture. Raw material Items will be fetched only when this is set.
5. If the selected BOM has Operations mentioned in it, the system will fetch all Operations from BOM, these values can be changed. Refer [section 3.2](/erpnext/work-order#32-operations-table) to know more.
6. Set the Planned Start Date (an Estimated Date at which you want the Production to begin). ![Work Order](/files/work-order.png)
7. **Use Multi-Level BOM**: This is enabled by default. If you want to plan materials for sub-assemblies of the Item you're manufacturing leave this enabled. If you plan and manufacture the sub-assemblies separately, you can disable this checkbox. To know more, visit [this page](/erpnext/managing-multi-level-bom).
8. Select Warehouses:


	1. **Source Warehouses**: Select this Warehouse in the Item row. The warehouse where you store your raw materials. Each required item can have a separate source warehouse. Group warehouse also can be selected as source warehouse. On submission of the Work Order, the raw materials will be reserved in these warehouses for production usage.
	2. **Work-in-Progress Warehouse**: The warehouse where your Items will be transferred when you begin production. Group Warehouse can also be selected as a Work in Progress warehouse.
	3. **Target Warehouse**: The warehouse where you store finished Items before they are shipped.
	4. **Scrap Warehouse**: If the BOM results in Scrap material, the Scrap Warehouse needs to be selected.
9. **Required Items**: All the required items (raw materials) will be fetched from BOM and populated in this table. Here you can also change the Source Warehouse for any item. And during the production, you can track transferred raw materials from this table.

> Note: You can save a Work Order without selecting the Warehouses, but Warehouses are mandatory for submitting a Work Order.

A Work Order can also be directly created from a [Sales Order](/erpnext/sales-order#214-after-submitting).

### 2.1 Additional Options when Creating a Work Order

* **Sales Order**: If you create a Work Order from a Sales Order, it will be fetched here. You can also link an existing Sales Order which has the Item to be manufactured to this Work Order.
* **Project**: Link the Work Order to a Project to track progress in cases like engineer to order.
* **Allow Alternative Item**: Sometimes when manufacturing a finished good, specific materials may not be available. For example, using plastic beads instead of plastic crystals. The finished good itself could be different. Ticking this checkbox will allow you the select an Alternative Item. To know more, visit [this page](/erpnext/item-alternative).
* **Skip Material Transfer to WIP Warehouse**: Usually, a Stock Entry is created when the raw materials are transferred to a Work In Progress Warehouse. In this case, the raw material is considered to be consumed hence the Stock Entry is skipped. The next option will be shown if you tick this checkbox.
* **Backflush Raw Materials From Work-in-Progress Warehouse**: Ticking this checkbox will automatically create a Stock Entry with the type 'Manufacture'. This means that the raw materials were consumed from the Source Warehouse, used to manufacture finished goods and another Stock Entry was created for your Target Warehouse. ![Options when creating WO](/files/work-order-options.png)

3. Features
-----------

### 3.1 Time

The Planned Start Date and Expected Delivery Date can be set here. The default for Planned Start Date is the current date and time at the time of creating the Work Order.

### 3.2 Required Items table

The Source Warehouse can be changed for the raw material items used here. The default Warehouse can be set at the Item level in the [Item](/erpnext/item#28-item-defaults) master or globally in [Stock Settings](/erpnext/stock-settings#23-default-warehouse).

* **Required Quantity**: This will be calculated automatically based on the [Bill Of Materials](/erpnext/bill-of-materials).
* **Transferred Quantity**: Once the Work Order starts and Job Cards are run, items are transferred from the Source Warehouse to Work In Progress Warehouse. This field shows the quantity in the WIP Warehouse. Note that if you tick on 'Skip Material Transfer to WIP Warehouse', this column will not be updated.
* **Consumed Quantity**: When the Item from the WIP Warehouse is consumed and the finished product is manufactured, this field will be updated.
* **Allow Alternative Item**: If a particular Item (raw material or sub-assembly) is not available, ticking this checkbox will allow you to select an alternative item defined in the Item Alternative list.
* **Skip Material Transfer**: If you don't want to transfer the specific raw material to the work in progress warehouse then you need to enable this checkbox.

Once uncheck this checkbox for an Item, you can still select it in the BOM and Work Order, but no Stock Entries will be created against it.

Once the Work Order is saved the following two fields will also show the availability in the respective Warehouses in the Required Items table:

* Available Qty at Source Warehouse
* Available Qty at WIP Warehouse

![WO material Qty](/files/work-order-material-qty.png)  


### 3.2 Operations table

Materials can be transferred against a Work Order or a Job Card. This is usually fetched from the [Bill Of Materials](/erpnext/bill-of-materials), but you can change it in the Work Order also.

The following will be fetched from the BOM:

* In the Operations table: The Workstations where the Operations will be performed ![PO Opeartions](/files/PO-operations.png)
* In the Items table: The Operations which will be performed on the Items ![PO reassigning Operations](/files/PO-reassigning-operations.png)

These values can also be changed.

Once the Work Order is saved the following fields will be shown:

* **Completed Qty**: The number of Items on which this Operation was performed.
* **Status**: Whether the Operation is Pending, Work In Progress, or Completed. The status here is updated when the Job Cards are updated.
* **Operation Time**: This is fetched from the BOM, but can be changed.
* **Planned Operating Cost**: This is calculated based on the Operating Time, Hourly Rate, Quantity being manufactured, etc.

The Actual Operation Time, Actual Operating Cost, Actual Start Time, and Actual End Time are updated when Job Cards are updated.

### 3.3 Operation Cost

In this section, the following are shown:

* **Planned Operating Cost**: This is fetched as per the BOM and the Operations defined in it.
* **Actual Operating Cost**: This is fetched from the Job Cards based on the Operations run on the Items.
* **Additional Operating Cost**: Any additional expenses you may have incurred when manufacturing the Item can be added here.
* **Total Operating Cost**: This is calculated as Actual Operating Cost + Additional Operating Cost.

These values are calculated as per the Job Cards.

![Work Order Operation Costs](/files/wo-operation-cost.png)  


### 3.4 More Information

Here the Item Description and Stock UOM is shown for the Item being manufactured.

When a Work Order is created from a [Material Request](/erpnext/material-request), it'll be shown here.

### 3.5 Transferring Materials for Manufacturing

* Once you have submitted your Work Order, you need to Transfer the Raw Materials to initiate the Manufacturing Process.
* This will create a Stock Entry with all the Items required to complete this Work Order to be added to the WIP Warehouse. This will add the sub-assembly Items as is or explode them to show the raw materials depending on whether you ticked 'Use Multi-Level BOM' or not.
* Click on 'Start'. Once you click on Start, Job Cards will be created for the [Operations](/erpnext/job-card) involved.

![Transfer Materials](/files/PO-material-transfer.png)
* Mention the quantity of materials to be transferred in this run.

![Material Transfer Qty](/files/PO-material-transfer-qty.png)
* You'll be taken to a Stock Entry for 'Material Transfer for Manufacture'. Submit it.
* Material Transferred for Manufacturing will be updated in the Work Order based on the Stock Entry.

![Stock Entry for PO](/files/PO-material-transfer-updated.png)
* **Note:** User can only transfer items which has "Include Item In Manufacturing" enabled in the item master

### 3.6 Material Transfer through Stock Entry

Use cases for this option are:

* If a material transfer is done in bulk and/or is not required to be tracked against a particular Work Order.
* If the responsibility for Material Transfer and Production Entry lies with two separate Users.

If this is the case, you can tick the 'Skip Material Transfer' checkbox, which will allow you to make the Stock Entry of type 'Manufacture' directly by clicking on the ‘Finish’ button.

### 3.7 Creating Job Cards

* Progress in the Work Order can be tracked using Job Cards
* Drafts of Job Cards are created based on when a Work Order is Submitted.
* To create more Job Cards against a Work Order click on the plus sign next to Job Card on the Work Order dashboard.

To know more about Job Cards, visit [this page](/erpnext/job-card).

### 3.8 Updating Finished Goods

* Once you are done with the Work Order you need to update the Finished Goods.
* This will create a Stock Entry that will deduct all the items and sub-assemblies from the WIP Warehouse and add them to the Finished Goods Warehouse.
* Click on 'Finish'.

![Update Finished Goods](/files/PO-FG-update.png)
* Mention the quantity of materials to be transferred.

> Tip: You can also partially complete a Work Order by updating the Finished Goods stock creating a Stock Entry.

### 3.9 Capacity Planning in Work Order

* When a Work Order is submitted, based on the Planned Start Date and the availability of the Workstations, the system schedules all operations for the Work Order (if Work Order has Operations specified).
* Drafts of Time Logs are also created based on the scheduled operations.

On Submitting the Work Order, the system will reserve a slot for each of the Work Order Operations serially after the planned start date based on the Workstation availability. The Workstation availability depends on the Workstation timings, holiday list, and if some other Work Order Operation is scheduled in that slot.

You can mention the number of days for the system to try scheduling the operations in the Manufacturing Settings. This is set to 30 Days by default. If the operation requires time exceeding the available slot, the system will ask you to break the operations. Once the scheduling is done the system will create Time Logs and save them. You can Modify them and submit them later.

### 4.0 Stopping a Work Order

When you stop a Work Order its status is changed to Stopped indicating that all production process against that Work Order has stopped. But before stopping the work order user has to make sure that the raw materials which were transferred to the Work In Progress warehouse have been returned or not. In case, if the user has tried to stop the work order without returning the raw materials then the system will throw the error and not allow the user to stop the work order.

To stop a Work Order, click on the 'Stop' button.

![PO - stop](/files/PO-stop.png)  


You can also re-open the stopped Work Order.

![Reopen Work Order](/files/reopen-work-order.png)  


### 4.1 Return Non Consumed Materials to the Stores from WIP Warehouse

If you have transferred extra materials to the Work In Progress warehouse and after completion of the work order you want to return it to the Store warehouse. Then you have to goto the Work Order and click on Return Components. After that system creates the return stock entry with type as Material Transfer for Manufacture.

![Return Components](/files/return-components.png)  


You can also checks the returned components against the work order using Work Order Consumed Materials report

![Return Components Qty](/files/work-order-consumed-materials-returned-qty.png)  


### 4.2 Transfer Addtional Materials

The Transfer Materials button is not showing because all required materials have already been transferred from Store to WIP warehouse against the work order, but the user wants to transfer additional materials since some are damaged.


![](/files/no-option-additional-transfer.png)

**Configuration**

To fixed the issue, user has to set the percentage for 'Transfer Extra Raw Materials to WIP (%)' in Manufacturing Settings.


![](/files/configuration-to-define.png)

Once the user sets the 'Transfer Extra Raw Materials to WIP (%)' in Manufacturing Settings, they can transfer additional materials from the store to WIP against the work order.


![](/files/additional-transfer-option-in-wo.png)



5. Related Topics
-----------------

1. [Job Card](/erpnext/job-card)
2. [Pick List](/erpnext/pick-list#22-create-pick-list-from-work-order)

<!-- page: erpnext/erpnext__workflow-actions.md -->
---
title: "Workflow Actions"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workflow-actions"
updated: "2026-03-02"
---


> Introduced in Version 11
> 
> 

**'Workflow Actions' is a single place where you can track and manage all pending actions you have to take on Workflows.**

Workflow Actions will send email notifications only if the 'Send Email Alert' checkbox is ticked in the Workflow that you've created.

To access Workflow Actions, go to:


> Home > Settings > Workflow Actions
> 
> 

If a User is eligible to take action on some workflows, emails will be sent to the user with the relevant document as attachment. From there the user can `Approve` or `Reject` the Workflow.

![Workflow Action Email](/files/workflow-actions-email.png)  


Also the users will see entries in their Workflow Action list:

![Screenshot 2024-06-03 at 10.47.43 AM](/files/Screenshot 2024-06-03 at 10.47.43 AM.png)  


**Note:**

* You can set email template for Workflow Actions on each state. The template might consist of a message for users to proceed with the next Workflow Actions.
* Workflow Actions will not be created for a transition to optional states.

### Related Topics

1. [Workflows](/erpnext/workflows)
2. [Assignment Rule](/erpnext/assignment-rule)

<!-- page: erpnext/erpnext__workflow-state.md -->
---
title: "Workflow State"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workflow-state"
updated: "2026-03-02"
---

**A 'Workflow State' is a specific status that a document (such as a sales order, purchase order, or leave application) can be in during its lifecycle.**

Workflow states are crucial for managing multi stage approval processes, ensuring proper checks and balances, and maintaining the flow of operations.

Different Workflow States may be achieved before or after applying different Workflow Actions on them. If you want to create a Workflow where there are multiple approvals from manager, senior manager, general manager, etc, you can set the states for it from Workflow States.

![Screenshot 2024-05-27 at 10.12.28 AM](/files/Screenshot 2024-05-27 at 10.12.28 AM.png)  


The system represents different states in different colours based on the Style tagged to each stage.

* Success - Green
* Danger - Red
* Inverse - Black
* Primary - Dark Blue
* Info - Light Blue
* Warning - Orange

### Related Topics

1. [Workflows](/erpnext/workflows)
2. [Workflow Actions](/erpnext/workflow-actions)
3. [Assignment Rule](/erpnext/assignment-rule)

<!-- page: erpnext/erpnext__workflow-transition-tasks.md -->
---
title: "Workflow Transition Tasks"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workflow-transition-tasks"
updated: "2026-03-02"
---

> Note: To be added in version 16
>
>

## Introduction
Workflow Transition Tasks are actions that can be run during state transitions in workflows. Each Workflow Transition can link to a set of transition tasks.
![Link to Workflow Transition Tasks](/files/Screenshot 2025-07-20 at 2.06.27 PM.png)

![A Typical set of transition tasks](/files/Screenshot 2025-07-20 at 2.08.23 PM.png)

Each Workflow Transition Task can have tasks of the following types:

1. App-Defined Actions (specified by each Frappe app through hooks.py)
2. [Server Scripts](/framework/user/en/desk/scripting/server-script)
3. [Webhooks](/framework/user/en/guides/integration/webhooks)

![A server script transition task](/files/Screenshot 2025-07-20 at 2.38.43 PM.png)

On top of this, each transition task can be either:

1. **Synchronous**: This is the default mode of transition tasks. All of the transition tasks run one-by-one when the state transition is initiated. Even if one of them fails, the transition is reversed.
2. **Asynchronous**: This mode can be enabled using the 'Asynchronous' checkbox. Each asynchronous transition task runs after the state transition is completed, meaning it has zero influence over state completion, and is run in a separate background job of its own.

### App-Defined Actions
Each Frappe app defines them using the 'workflow_methods' [hook](/framework/user/en/python-api/hooks).

Any dotted path method defined through the workflow_methods hook has to accept `doc: Document` as the parameter, which is the document on which the transition is being applied.

An example of an app-defined task is:

```python 
# hooks.py
workflow_methods = [{"name": "Create a customer", "method":
					 "myapp.shop.doctype.kirana.create_customer"}]

# myapp/shop/doctype/kirana.py
def create_customer(doc):
    customer = frappe.new_doc("Customer")
    customer.customer_name = "Customer " + doc.name
    customer.customer_type = "Individual"

    customer.save()
```

These will be available in the 'Tasks' drop-down if any of the apps has provided them.
![app-defined tasks](/files/Screenshot 2025-07-20 at 2.56.05 PM.png)

If you are an end user, you can not create app-defined actions on your own and will have to use server scripts as mentioned below.



### Server Scripts
These also take the `doc: Document` parameter and can be set using the 'Workflow Task' Script Type.
![server script tasks](/files/Screenshot 2025-07-20 at 3.00.48 PM.png)

And then these have to be linked to in the transition task:
![A server script transition task](/files/Screenshot 2025-07-20 at 2.38.43 PM.png)


### Webhooks
These can be created by setting the 'Doc Event' field of the webhook to 'workflow_transition':
![workflow_transition webhook](/files/Screenshot 2025-07-20 at 3.03.12 PM.png)

And then these have to be linked to in the transition task:
![link to webhook](/files/Screenshot 2025-07-20 at 3.13.25 PM.png)

### Related Topics
* [Workflow State](/erpnext/user/manual/en/workflow-state)
* [Workflow Actions](/erpnext/user/manual/en/workflow-actions)
* [Workflows](/erpnext/user/manual/en/workflows)

<!-- page: erpnext/erpnext__workflow.md -->
---
title: "Workflow"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workflow"
updated: "2026-03-02"
---

A typical 'Workflow' in ERPNext involves various stages to manage different aspects of business operations. It starts with creating a document and taking it through series of steps. Users can track the status of each document and collaborate with team members by assigning tasks and tracking their progress.

ERPNext streamlines processes by automating repetitive tasks that need multi phase attention by different people. ERPNext offers a comprehensive workflow to enhance productivity and efficiency across various departments within an organisation.

* [Workflow State](/erpnext/user/manual/en/workflow-state)
* [Workflow Actions](/erpnext/user/manual/en/workflow-actions)
* [Workflows](/erpnext/user/manual/en/workflows)
* [Workflow Transition Tasks](/erpnext/user/manual/en/workflow-transition-tasks)

<!-- page: erpnext/erpnext__workflows.md -->
---
title: "Workflows"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workflows"
updated: "2026-03-02"
---

**With workflows you can rewrite how a particular process/workflow is approved in ERPNext.**

You can set multiple levels of approval for an ERPNext Workflow. To allow multiple people to submit multiple requests, for approvals by multiple users, ERPNext requires you to fill the Workflow conditions. ERPNext tracks the multiple permissions before submission.

Consider a scenario, where multiple levels of approval are required for a quotation. A sales person (user with 'Sales User' role) will create a quotation. Then it is either approved or rejected by a sales lead (user with 'Sales Manager' role). If approved by sales lead, it is further approved or rejected by regional manager (user with 'Regional Manager' role).

To make a Workflow and transition rules go to:

> Home > Settings > Workflow

Once a Workflow is created, you can take actions on it via [Workflow Actions](/erpnext/workflow-actions).

1. Prerequisites
----------------

Before creating a Workflow, it is advised to create these first:

* [Workflow Actions](/erpnext/workflow-actions)
* Workflow States like Approved, Canceled, etc.

2. How to Create a Workflow
---------------------------

1. Go to the Workflow list, click on New.
2. Enter a name for the **Workflow** and select the DocType on which to be applied.
3. Enter the different states of the Workflow. Enter Doc Status for them, select which field to update from the Update Field column, enter what the value will be updated to under Update Value.

The Workflow States can have different colors according to the state. Eg: Green for success. Document statuses: Saved = 0, Submitted = 1, Cancelled = 2.

![Workflow](/files/workflow.png)
4. Enter the Transition Rules.

![Workflow Transition Rules](/files/workflow-transition-rules.png)

### 2.2 Things to note when creating a Workflow

* Creating a Workflow in ERPNext essentially overrides the regular Save and Submit workflow. Thus the document will function based on your Workflow and not based on the pre-set code workflow. Hence there might be no Submit button/option if you have not specified it in the Workflow you create.

If you don't apply a Workflow to a document, and that document is submittable, then it has the default workflow with states: Draft - Submitted - Cancelled. If you are applying a Workflow to a submittable document, then those default states should be handled by the user.
* A document cannot be canceled unless it is submitted.
* If you wish to give the option to cancel, you will have to write a workflow transition step that says from submitted you can cancel.
* If fields under Update Field column are not updated, a new custom field will be created with the name you set in the 'Workflow State Field' field.

### 2.3 Other options for a Workflow

1. Is Active: On ticking this, all other Workflows for the selected DocType become inactive.
2. Don't Override Status: This Workflow's status will not override the status of the document (Quotation) in the list view.
3. Send Email Alerts: Emails will be sent to the user with next possible workflow actions.

3. Features
-----------

### 3.1 Enable/Disable Optional Workflow State

> Introduced in Version 12

In States, optional Workflow state means that the state may not be a part of final approval.

E.g. states like Canceled or Rejected can be optional. ![Optional State](/files/workflow-optional-state.png)  


**Note:** Workflow Actions are not created for optional states.

### 3.2 Conditions

You can also add a condition for the Transition to be applicable. For example, in this case, if sales executive creates a quotation with grand total of $100,000 or more, a particular role must approve. For this to happen in the particular transition, you can set a property for **Condition**:


```
doc.grand_total <= 100000
  

```
Here, `grand_total` is the field name of the field 'Grand Total' of Quotation. To see the field name of a field go to Menu > Customize.

This can be extended to any property of the document.

> Introduced in Version 13

In Version 13, you can use date/time, session, get*value and get*list functions in your condition expressions.

Allowed functions:

* frappe.db.get_value
* frappe.db.get_list
* frappe.session
* frappe.utils.now_datetime
* frappe.utils.get_datetime
* frappe.utils.add*to*date
* frappe.utils.now

Examples:


```
doc.creation > frappe.utils.add_to_date(frappe.utils.now_datetime(), days=-5, as_string=True, as_datetime=True)
  

```
4. Example of a Quotation Approval Process
------------------------------------------

When a quotation is saved by sales user, the status of the document changes to "Draft" and when clicked on submit the status changes to 'Approval Pending By Sales Manager':

![Workflow State in Transaction](/files/workflow-status-in-transaction.png)  


When the Sales Manager logs in, he can either Approve or Reject. If approved the status of the document changes to "Approval Pending By Regional Manager".

![Workflow Action Options](/files/workflow-action-options.png)  


When the Regional Manager opens the quotation, he can finally "Approve" or "Reject" it.

![Workflow Action Options](/files/workflow-action-options-2.png)  


5. Video
--------

### 6. Related Topics

1. [Workflow Actions](/erpnext/workflow-actions)
2. [Assignment Rule](/erpnext/assignment-rule)

<!-- page: erpnext/erpnext__workspace.md -->
---
title: "Customizing Workspace"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workspace"
updated: "2026-03-04"
---

When you log in, you're presented with the Desk. It features a persistent sidebar sorted into categories. Each sidebar item links to a page called Workspace.

A Workspace represents a module (for example CRM in ERPNext). A Workspace includes the following:

* A dashboard section for that particular module.
* A shortcut section for frequently used masters, transactions or pages.
* A masters section where all the reports and masters are grouped and listed.

Standard Workspace
------------------

Every module in ERPNext has its own Standard Workspace which is generated with appropriate shortcuts and links.

Any customization to be made to the Standard Workspace can be done with Customize Workspace option in the top right corner of the Workspace.


> Note: These customizations will be user-specific and will only be visible to that user.
> 
> 

Custom Workspace
----------------

You can also create your own Workspaces by simply creating a new Workspace document.

1. Go to the Workspace list and click on New.
2. **Name**: The text you enter here will be shown in the sidebar.
3. **Module**: Select the module which the Workspace will represent.
4. ***Is Standard***: If checked, this Workspace will be shown in the sidebar. Otherwise it will be treated as a customized version of a Standard Workspace.
5. ***Extends Another Page***: If checked, this Workspace will be treated as a customized version of another Workspace.
6. ***Is Default***: If checked, this Workspace will be the default Workspace displayed to all users for a particular module.
7. ***Dashboard***: Add a Dashboard to display it on the top of the Workspace.
8. ***Shortcuts***: Add Shortcuts to a specific page, reports or list which will be displayed below the dashboard.
9. ***Link Cards***: You can add cards that will display a list that links to a specific page, report, or list.

<!-- page: erpnext/erpnext__workstation.md -->
---
title: "Workstation"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workstation"
updated: "2026-02-28"
---

**A Workstation stores information regarding the place where the workstation operations are carried out.**

Data regarding the operation cost, rent, electricity can be stored here.

An Operation takes place at a Workstation. The Operation is the work performed and the Workstation is the place/machine where it is performed. For example, melting is an Operation that can be done at 10 different Workstations.

:::note
An Operation can take place at multiple Workstations.
:::























## How to create a Workstation

1. Go to the Workstation list, click on New.
2. Enter a name for the Workstation.
3. Under Operating Costs, enter operating component with the cost:
  1. Electricity
  2. Rent
  3. Consumables
  4. Wages
4. Save.

Optionally, you can enter a description for the Workstation.

---

### Operating Components

Using this table you can divide the different cost components and set it to the Operation.

![](/files/Screenshot%202025-08-19%20at%2012.57.24%20PM.png)

### Workstation Operating Component

User can also define the expense account per component company wise in the Workstation Operating Component.

![](/files/CleanShot 2026-02-19 at 12.20.21@2x.png)

---

A [Holiday List](/hr/holiday-list) can be added to exclude counting these days for the Workstation.















The hours when the Workstation will be Operational can be added. On adding a Holiday list, the days listed as holidays won't be counted as working for the Workstation.

Under Working Hours table, you can add start and end times for a Workstation. For example, a Workstation may be active from 9 am to 1 pm, then 2 pm to 5 pm. You can also specify the working hours based on shifts. While scheduling a [Work Order](/erpnext/work-order), the system will check for the availability of the Workstation based on the working hours specified.

:::note
You can enable overtime for a Workstation in Manufacturing Settings.
:::









![](/files/CleanShot 2026-02-19 at 12.22.41@2x.png)

After saving the Workstation, the following actions can be performed against it:

![](/files/CleanShot 2026-02-19 at 12.23.30@2x.png)

---

## Features

### Production Capacity

Production Capacity is the total number of jobs can be executed at the same time in the respective workstation.

![](/files/CleanShot 2026-02-19 at 12.24.54@2x.png)

---



---

## Related Topics

1. [Bill Of Materials](/erpnext/bill-of-materials)
2. [Operation](/erpnext/operation)
3. [Routing](/erpnext/routing)
4. [Work Order](/erpnext/work-order)
5. [Job Card](/erpnext/job-card)

<!-- page: erpnext/erpnext__workstation_type.md -->
---
title: "Workstation Type"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/workstation_type"
updated: "2026-02-26"
---

If users have the same types of multiple Workstations (Machines) and users want to auto-assign jobs to the available workstation based on workstation type then this feature is the good option for them. A Workstation Type document will allow you to set the same operating cost to multiple operations by just setting the Workstation Type in the Operations table in [BOM](https://docs.frappe.io/erpnext/user/manual/en/bill-of-materials) or [Routing](https://docs.frappe.io/erpnext/user/manual/en/routing).

![](/files/CleanShot 2026-02-19 at 12.10.36@2x.png)

After adding Workstation Type, users has to assign the Workstation Type to the respective Workstation and set the Workstation Type to the respective Operation in the BOM.

![](/files/CleanShot 2026-02-19 at 12.11.38@2x.png)

After setting up Workstation Type when user make the Work Order with Operations system will create Job Cards against the Operation and set the available Workstation based on the Workstation Type set in the BOM.

![](/files/CleanShot 2026-02-19 at 12.13.04@2x.png)

<!-- page: erpnext/erpnext__zenoti_integration.md -->
---
title: "Zenoti Integration"
space: "ERPNext"
url: "https://docs.frappe.io/erpnext/zenoti_integration"
updated: "2026-02-26"
---

>Introduced in version 13.

Zenoti Integration pulls the purchase orders and sales invoices from Zenoti and creates Purchase Order and Sales Invoice against them in ERPNext.

While creating these records if Customer, Supplier or Item is missing in ERPNext the system will create new Customer, Supplier or Item by pulling respective details from Zenoti.

### How to Setup?
Zenoti Integration is available through *Ecommerce Integrations* on [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations).

### App Installation

- If you are hosting your ERPNext site on Frappe Cloud, you can quickly install the app by going to your site Dashboard. The app is available in [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations).
- If your site is hosted by Frappe, please raise a support ticket to get the app installed on your site.
- If you are self hosting ERPNext you can install the app using Frappe bench. Refer [bench documentation](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) for installing Frappe Apps. `bench get-app ecommerce_integrations --branch main`

The repository for app is hosted on GitHub: [http://github.com/frappe/ecommerce_integrations/](http://github.com/frappe/ecommerce_integrations/).

### Prerequisite

1. For each center in Zenoti there should be a cost center and a warehouse created in ERPNext which will be used in Cost Center and Warehouse Mapping table in Zenoti Settings in ERPNext.
2. Items*(alteast those having stock impact)* have to be created. Data import can be used for this.
3. Opening stock entries have to be created using Stock Reconciliation in ERPNext.
4. Item Tax Templates have to be created from Tax Groups in Zenoti with proper accounts and tax rates.
5. Create an account to book liability for the sales of gift or prepaid cards and tips, this is to be set as *Liability Income Account to book Gift & Prepaid cards* in Zenoti Settings.
6. Set appropriate accounts in the mode of payments. Also add "Card", "Custom" and "Points" as Mode of Payment.
7. "Enable Perpetual Inventory" should be unchecked in Company Master.

### Important details for setting up Zenoti on ERPNext

> To access Zenoti Settings, go to: Awesome search bar > Zenoti Settings.

![Zenoti setting page](/files/Zenoti Settings Screen.png)

1. **Last Sync:** Date and time of when the invoices were synced last.
2. **API Key:** API Key from Zenoti. If you do not have an API Key, you can easily generate one by going to Admin > Setup > API section.
3. **Sync Interval:** Duration in hours between each syncing. Following options are avaliable *(1, 3, 6, 12, 24)*
4. **Default Purchase Warehouse:** Warehouse to be set for all the Purchase Orders. Usually this is the main center in Zenoti so put the one you created for main center.
5. **Default Buying Price List:** This is required in ERPNext to maintain price of the Items. You can create a new or or use the existing one *Standard Buying* provided by ERPNext.
6. **Default Selling Price List:** This is required in ERPNext to maintain price of the Items. You can create a new or or use the existing one *Standard Selling* provided by ERPNext.
7. **Liability Income Account to book Tips, Gift & Prepaid cards:** Add here the account you created to book Tips and sales of Gift & Prepaid cards.
8. **Default Customer Group:** If on creation of new customer while syncing sales invoice a specific customer group is to be assigned to them then add that here. If nothing is added then the default *All Customer Group* will be set for those new customer.
9. **Default Supplier Group:** If on creation of new supplier while syncing purchase order a specific supplier group is to be assigned to them then add that here. If nothing is added then the default *All Supplier Group* will be set for those new supplier.
10. **Cost Center and Warehouse Mapping:** In this table map all the Centers of Zenoti to their corresponding Cost Centers and Warehouses in ERPNext.

### What will be synced or will have to be created manually

#### Item
Items will have to be created manually into ERPNext from Zenoti one time at the start. Then it will be created on a demand basis when syncing sales /purchase orders.

#### Item Tax Template
Item Tax Template will be created manually based on Tax Groups on zenoti.

#### Customer
Customer and Customer Group will be created on demand basis while syncing sales invoices. If there are no customer groups in Zenoti, “Default Customer Group” mentioned in Zenoti Settings will be used. If not mentioned in Zenoti Settings “All Customer Groups” will be used.

#### Supplier
Supplier and Supplier Group will be created on demand basis while syncing purchase orders. If there are no supplier groups in Zenoti, “Default Supplier Group” mentioned in Zenoti Settings will be used. If not mentioned in Zenoti Settings “All Supplier Groups” will be used.

#### Warehouse
Warehouses will have to be created in ERPNext manually and mapped with Centres of Zenoti via Cost Center and Warehouse Mapping table in Zenoti Settings.

#### Cost Center
Cost Centers will have to be created in ERPNext manually and mapped with Centres of Zenoti via Cost Center and Warehouse Mapping table in Zenoti Settings.

#### Employees
Employees will have to be created manually into ERPNext from Zenoti one time at the start. Then it can be created on a demand basis when syncing sales/purchase records. For Employees fields "Date of Birth", "Date of Joining" are mandatory. Hence when creating employee from sales/purchase records "Date of Joining" will be set as the day the employee is created and "Date of Birth" as 25 years before "Date of Joining". These can be changed later on.

#### Purchase Order
Purchase Order will be created in Zenoti and sync into the ERPNext at the end of the day.
Supplier and Item will be created on demand basis if new.

> Note: Purchase Invoice from the Purchase Order have to be created manually.

#### Debit Note
Debit Note will be created automatically and remain in Draft mode based for Return Purchase Order in Zenoti.

#### Sales Invoice
Invoice will be created automatically via API on the given interval set in Zenoti Settings.
Customer and Item will be created on demand basis if new.

#### Credit Note
Credit Note will be created automatically based on Return Invoice in Zenoti and will only contain products and not services.

#### Gift/Prepaid Card Sales
Each Gift/Prepaid card will be treated as Items.
Gift/Prepaid Cards will be treated as mode of payment for future invoices where the payment was done using these in Zenoti.

#### Stock Reconciliation
At the end of the day, stock will be synced via Stock Reconciliation.
