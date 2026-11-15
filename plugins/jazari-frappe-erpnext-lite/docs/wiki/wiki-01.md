<!-- Frappe documentation: wiki, part 1 of 1. Index: docs/INDEX.md -->

<!-- page: wiki/wiki-v2__approving-changes.md -->
---
title: "Approving Changes"
space: "Wiki"
url: "https://docs.frappe.io/wiki-v2/approving-changes"
updated: "2026-01-13"
---

Users that do not have System Manager roles need approval to merge their patches.

A Patch can be approved from the desk.

[Screenshot on the live page]  


  

<!-- page: wiki/wiki-v2__check-page-revisions.md -->
---
title: "Check Page Revisions"
space: "Wiki"
url: "https://docs.frappe.io/wiki-v2/check-page-revisions"
updated: "2026-01-13"
---

You can check revisions by clicking on the Kebab (3-dot) menu button and select Revisions.

[Screenshot on the live page].gif)  


  

<!-- page: wiki/wiki-v2__how-to-contribute.md -->
---
title: "How to contribute"
space: "Wiki"
url: "https://docs.frappe.io/wiki-v2/how-to-contribute"
updated: "2026-01-19"
---

## Documentation

Wiki Docs is made using wiki itself so you can contribute by editing the pages directly. A Wiki Approver will review the changes soon.

## Code

Code for this project is hosted on GitHub, [frappe/wiki](https://github.com/frappe/wiki).

Please follow the [contribution guidelines](https://github.com/frappe/erpnext/wiki/Contribution-Guidelines)

<!-- page: wiki/wiki-v2__install-locally.md -->
---
title: "Install locally"
space: "Wiki"
url: "https://docs.frappe.io/wiki-v2/install-locally"
updated: "2026-01-13"
---

Wiki is a Frappe App so deployment tools need no tweaking. If you want to manually install on bench use the following commands


```
# get-app

$ bench get-app https://github.com/frappe/wiki

# install on site

$ bench --site sitename install-app wiki
```
  

<!-- page: wiki/wiki-v2__introduction.md -->
---
title: "Introduction"
space: "Wiki"
url: "https://docs.frappe.io/wiki-v2/introduction"
updated: "2026-01-13"
---

## What is Wiki?

Wiki is an open-source wiki management application built on the Frappe Framework. It's designed to handle dynamic, text-heavy content like documentation and knowledge bases. Think of it as a flexible content management system that allows for quick publishing of small changes and new pages without requiring deployments


[Screenshot on the live page]

## Why Wiki?

Because managing knowledge shouldn't be complicated. Your wiki should be easy to use, flexible, and powerful.

With Wiki, you get:

1. An open-source solution that you can customize to your needs
2. Built on the robust Frappe Framework, ensuring scalability and reliability
3. No vendor lock-in - you own your data and have freedom to modify

## Key Features

Wiki will help you to:

1. Create and manage wiki pages
2. Organize content with wiki spaces
3. Set up controlled wiki updates with approval mechanisms
4. Add attachments to pages
5. Generate automatic table of contents
6. Maintain version history of documents
7. Use markdown format for content authoring
8. Caching for fast load times
9. Support custom scripts via wiki settings
10. Edit dynamic sidebar through drag-and-drop

## Under the Hood

[**Frappe Framework**](https://github.com/frappe/frappe): A full-stack web application framework written in Python and JavaScript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.

## Installation

To install/setup the app, follow the guidelines [here](https://github.com/frappe/wiki?tab=readme-ov-file#local).

## Learning and community

1. [GitHub](https://github.com/frappe/wiki) - Contribute to Wiki and explore its open-source code, issues, and discussions
2. [Telegram Group](https://t.me/frappewiki) - Get instant help from huge community of users
3. [Discussion Forum](https://discuss.frappe.io/c/wiki/72) - Engage with community of Wiki users.

<!-- page: wiki/wiki-v2__new-wiki-group.md -->
---
title: "New Wiki Group"
space: "Wiki"
url: "https://docs.frappe.io/wiki-v2/new-wiki-group"
updated: "2026-01-13"
---

Wiki Groups can be added simply by clicking on the the Edit Sidebar button on the left sidebar and then clicking on the Add Group button followed by adding the Title of the sidebar. You will need to add or move a page to persist the page after save.


> Groups will be saved after an interval post changes
> 
> 

[Screenshot on the live page]  


  

<!-- page: wiki/wiki-v2__new-wiki-page.md -->
---
title: "New Wiki Page"
space: "Wiki"
url: "https://docs.frappe.io/wiki-v2/new-wiki-page"
updated: "2026-01-13"
---

A new Wiki Page can be created simply by clicking the Edit Sidebar button on the left sidebar and then clicking on the + icon near the desired Wiki Group we want the Wiki Page to be in.

Once an empty editor is opened you can add the title and content.
[Screenshot on the live page]

<!-- page: wiki/wiki-v2__use-on-frappe-cloud.md -->
---
title: "Use on Frappe Cloud"
space: "Wiki"
url: "https://docs.frappe.io/wiki-v2/use-on-frappe-cloud"
updated: "2026-01-13"
---

Wiki is available on Frappe Cloud via the [Marketplace](https://frappecloud.com/marketplace/apps/wiki)

Follow the steps below to get a running wiki instance quickly.

1. Visit [frappecloud.com/marketplace/apps/wiki](https://frappecloud.com/marketplace/apps/wiki).
2. Click on the "Install Now" Button.
3. Select a region.
4. Choose a subdomain.
5. A new site with Wiki installed will be created.

<!-- page: wiki/wiki-v2__wiki-migration-guide.md -->
---
title: "Wiki Migration Guide"
space: "Wiki"
url: "https://docs.frappe.io/wiki-v2/wiki-migration-guide"
updated: "2026-01-13"
---

Sidebar Migration
-----------------

Wiki v2 uses a simpler sidebar structure with a parent (Wiki Group) and child (Wiki Page) structure, unlike the earlier version which allows unlimited nesting. Every Wiki Group (nested or not) will be un-nested after migration. Due to the changes in the data structure we need to ensure some things for smooth migration.

1. Make sure there are no Wiki Sidebars with duplicate names (or every item will be under those Wiki Groups will be grouped under a single Wiki Group)
2. Make sure that title fields of `Wiki Sidebar` are not empty

  

<!-- page: wiki/wiki-v2__wiki-settings.md -->
---
title: "Wiki Settings"
space: "Wiki"
url: "https://docs.frappe.io/wiki-v2/wiki-settings"
updated: "2026-01-13"
---

Wiki Settings allow you to change generic configurations of the wiki app.

General
-------

[Screenshot on the live page]


1. **Light Mode Logo**: The default logo that is visible on the top left of each wiki page
2. **Add Dark Mode:** Add dark mode theming to Wiki
3. **Dark Mode Logo:** The logo that is displayed on dark mode instead of the default logo
4. **Default Wiki Space:** The default Wiki Space you will be redirected
5. **Enable Table of Content:** Show or hide the Table of Content displayed on right side
6. **Disable guest access:** Make your wiki only accessible by logged in/authenticated users


Navbar
------

[Screenshot on the live page]


1. **Navbar Items**: Add Navbar Items similar to how it is in Website module
2. **App switcher list:** Add items in top left dropdown menu list
3. **Add Search Bar**: Add a Redisearch powered search bar to the navbar
4. **Use Redisearch for Search:** Use Redis Search for searching wiki pages


Feedback
--------

[Screenshot on the live page]

1. **Enable Feedback:** Allow users to submit feedback
2. **JavaScript**: Allows you to add Custom JS that would be run on each Wiki Page

<!-- page: wiki/wiki-v2__wiki-space.md -->
---
title: "Wiki Space"
space: "Wiki"
url: "https://docs.frappe.io/wiki-v2/wiki-space"
updated: "2026-01-13"
---

Wiki v2 introduced a concept called Wiki Space, which are basically isolated instances of Wiki.

Creating Wiki Space
-------------------

To create a new Wiki Space

1. In desk click on Add Wiki Space
2. Type in the Wiki Space route
3. Optionally add Wiki Pages (that aren't associated with other Wiki Spaces)

[Screenshot on the live page]  


  
