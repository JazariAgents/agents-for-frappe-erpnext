<!-- Frappe documentation: erpnext, part 68 of 69. Index: docs/INDEX.md -->

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

[Screenshot on the live page: New Web Page] *New Web Page*

View your Web Page by clicking on **See on Website** in the side bar.

[Screenshot on the live page: Web Page] *Web Page*

### 1.1 Tips on making a good Web Page

#### Title

The first thing to set is the title of your page. The title has the maximum weight for search engines so choose a title that reflects the keywords that you are targeting for your audience. The route (URL) will be auto-generated from the title but you can change it.

#### Content

You can write your content in Rich Text, Markdown or HTML. If you want to make simple content pages, Rich Text and Markdown are great options.

> Learn markdown in a few minutes at [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).

#### Images

For Rich Text Content, you can directly embed images using the editor. For Markdown and HTML, you must attach the images to the document first. Now get the URL of your image by right-clicking on your attachment and copying the address.

[Screenshot on the live page: Image Link]  


Now, add them to your Markdown or HTML using the appropriate syntax.


```
<!-- markdown -->
[Screenshot on the live page: Alt Text]

<!-- html -->
[Screenshot on the live page]
  

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

[Screenshot on the live page: Web Page Sidebar] *Web Page Sidebar*

Add links and their route in the Sidebar Items table. [Screenshot on the live page: Website Sidebar] *Website Sidebar*

[Screenshot on the live page: Web Page with Sidebar] *Web Page with Sidebar*

### 2.5 Comments

You can enable comments on your Web Page where people can leave a comment with their Name and Email. Enable comments from the **Sidebar and Comments** section.

[Screenshot on the live page: Web Page Comments] *Web Page Comments*

### 2.6 Header

You can add a custom HTML for the header section of the page. This will override the title of the Web Page.

[Screenshot on the live page: Web Page Header] *Web Page Header*

[Screenshot on the live page: Web Page with Custom Header] *Web Page with Custom Header*

### 2.7 Breadcrumbs

You can add a list of breadcrumbs on your Web Page. These will be shown on top before the header.

[Screenshot on the live page: Web Page Breadcrumbs] *Web Page Breadcrumbs*

[Screenshot on the live page: Web Page with Breadcrumbs] *Web Page with Breadcrumbs*

### 2.8 Meta Tags

You can also add Meta Tags to your Web Page. You must add the property key and its value in the Meta Tag Table and it will auto-generate HTML `meta` tags on your Web Page.

[Screenshot on the live page: Web Page Meta Tags] *Web Page Meta Tags*

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

[Screenshot on the live page: Website Banner image]

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

[Screenshot on the live page: Website Setting Home]

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

[Screenshot on the live page: New Website Route Meta]
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

[Screenshot on the live page: Website Settings - Landing Page]
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

[Screenshot on the live page: Website Settings - Banner Image]
*Website Settings - Banner Image*

### 3.2 Favicon

You can also set the favicon of your website in this section. It appears on the
left side of the browser tab.

[Screenshot on the live page: Website Settings - Favicon]
*Website Settings - Favicon*

View your website by clicking on **View Website** in the action bar on top right.

[Screenshot on the live page: Website with Brand and Favicon]
*Website with Brand and Favicon*

## 4. Top Bar

You can customize the menu items in the navbar of your website from the **Top Bar**
section.

[Screenshot on the live page: Website Setting - Top Bar]
*Website Setting - Top Bar*

[Screenshot on the live page: Website Navbar Items]
*Website Navbar Items*

## 5. Banner

You can add a persistent banner to your website which will be shown above the
navbar on all web pages. You can write any valid Bootstrap 4 markup here.

[Screenshot on the live page: Website Settings - Banner]
*Website Settings - Banner*

[Screenshot on the live page: Website Banner]
*Website Banner*

## 6. Footer

You can add address information and categorized links to your footer in the
**Footer** section.

[Screenshot on the live page: Website Settings - Footer Address]
*Website Settings - Footer Address*

[Screenshot on the live page: Website Settings - Footer Links]
*Website Settings - Footer Links*

[Screenshot on the live page: Website Footer]
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

[Screenshot on the live page: Google Integrations]
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

[Screenshot on the live page: Website Settings - Header]
*Website Settings - Header*

## 9. Robots

You can define `robots.txt` rules in this section. This information is used by
web crawlers to decide which pages to index and which to skip.

[Screenshot on the live page: Website Settings - Robots]
*Website Settings - Robots*

> Learn more about `robots.txt` at [Moz - Robots.txt](https://moz.com/learn/seo/robotstxt)

## 10. Redirects

You can define a mapping of route redirects here. The mappings in the following
screenshot makes sure that if a user visits `https://apple.erpnext.com/iphone`,
they will be redirected to `https://apple.erpnext.com/products/iphone`.

ERPNext will raise a `301 Permanent Redirect` response for these routes.

[Screenshot on the live page: Website Settings - Routes Redirects]
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

[Screenshot on the live page: Select Website Theme in Website Settings]

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

[Screenshot on the live page: Included Theme Files]

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

[Screenshot on the live page: Publish Item]  


If you visit `your-site-name/all-products` , you will see the newly created Website Item listed here.

> To view the Website Item page on the website click on the **See on Website** link on the top left just above the item image in the Website Item document.

### Updating the Website Item

[Screenshot on the live page: Website Item Page] *Website Item Page*

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

[Screenshot on the live page: Website Item Product Details]  


#### Recommended Items

You can show **Recommended Items** against Website Items to knudge users to pay attention to a closely related item. This can be enabled by going to **E Commerce Settings** > **Add-ons** > **Enable Recommendations**.

You can then add Recommended Items against a Website Item in the **Recommended Items** section, and add the items to recommend. These will show up in the Website Item Page.

[Screenshot on the live page: Recommended Items]  


#### Offers

Coupon Codes can be added at checkout , but customers must know about these codes. For this, **Offers** can be added to the Website Item for display.

* Go to the **Offers** section in the Website Item.
* Add a short offer title that is one/two words, in the **Offer Title**.
* Add a slightly longer subtitle, a sentence in the **Offer Subtitle**.
* Add lengthy details about the offer in the **Offer Description**. **Save**.

[Screenshot on the live page: Website Item Offers]  


#### Search and SEO

1. **Ranking**: Assign a rank to the Website Item to have control over it's position in the Product Listing. Website Items with higher ranking will be shown higher.
2. **Set Meta Tags**: Meta tags help with SEO. See [Web Page](/erpnext/web-page) to know how to add them.
3. **Website Item Groups**: In this table you can select existing or create new [Item Groups](/erpnext/item-group) to classify items on your website. The Website Item will be visible under Item Group Pages of the Item Groups mentioned in this table.

#### Advanced Display Content

You can add an additional styled section using Bootstrap 4 markup for the Website Item page. [Screenshot on the live page: Website Item Advacned Display]  


### Adding Price Details

Prices can be added against Website Items via **Item Price**. Before adding an Item Price, go to **E Commerce Settings** and make sure **Company, Price List , Default Customer Group** are set.

Now you can go ahead and create an **Item Price** for the Website Item, and select the **Price List** as the one in the **E Commerce Settings**.

You can also add a **Pricing Rule** with a **Discount Percentage** or **Discount Amount** on the existing item price, to show **striked prices**. [Screenshot on the live page: Website Item Page Striked Price]  

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

  


[Screenshot on the live page]

  


[Screenshot on the live page]

  


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
[Screenshot on the live page: Wishlist from Card]

#### The Website Item Page
[Screenshot on the live page: Wishlist from Website Item Page]

The link to the Wishlist page is available on the navbar as seen above. Users can remove items from the Wishlist or move the items to Cart.

[Screenshot on the live page: Wishlist Page]
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

[Screenshot on the live page: Nova Electronics Trading Chart of Accounts used to locate an equity withdrawal account]

## Record the withdrawal

1. Open [Journal Entry](/erpnext/journal-entry) and create a new record.
2. Select Nova Electronics Trading and enter the posting date.
3. Debit **Dividends Paid - NET** by $1,000.
4. Credit **Nova Operating Bank - NET** by $1,000.
5. Add a clear remark identifying the transaction as an owner withdrawal, then save and submit.

[Screenshot on the live page: Submitted owner withdrawal Journal Entry debiting Dividends Paid and crediting Nova Operating Bank]

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
