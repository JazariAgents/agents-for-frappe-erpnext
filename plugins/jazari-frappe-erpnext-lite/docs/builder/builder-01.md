<!-- Frappe documentation: builder, part 1 of 1. Index: docs/INDEX.md -->

<!-- page: builder/builder__data-script.md -->
---
title: "Data Script"
space: "Builder"
url: "https://docs.frappe.io/builder/data-script"
updated: "2026-06-03"
---

The Data Script feature is essential for retrieving, processing, and delivering dynamic data to your web pages from various sources. This guide will help you effectively utilize Data Script to ensure your content is always current and relevant.

## Key Concepts

### Data Binding

To display data on your page, assign it to the `data` variable. This variable is used to pass data to the web page.

```python
data.events = ...  # Example of assigning data to the 'events' variable
data.user_list = ...  # Example of assigning data to the 'user_list' variable
```

**Note:**

- Data scripts must be written in Python and are executed server-side.
- They run in a restricted Python environment and can only access whitelisted modules. Find the list of whitelisted methods [here](https://frappeframework.com/docs/user/en/desk/scripting/script-api).

### **Redirecting Visitors**

You can redirect a page visitor to any URL from within a Data Script using the `redirect()` helper. This is useful for enforcing authentication, routing users based on roles, or sending visitors to external resources.

#### **Basic Usage**

```
redirect("/login")           # 302 redirect (default)
redirect("/login", 301)      # custom HTTP status code
```

The `redirect()` function sends an HTTP redirect response to the client. It accepts two arguments:


| **Argument**       | **Required** | **Default** | **Description**                                                       |
| ------------------ | ------------ | ----------- | --------------------------------------------------------------------- |
| `location`         | Yes          | —           | The URL to redirect to (relative or absolute)                         |
| `http_status_code` | No           | `302`       | The HTTP status code (e.g., `301` for permanent, `302` for temporary) |


## Retrieving Data

### From Frappe DocType

#### Fetching a Document List

To retrieve all records of a specific DocType:

```python
data.users = frappe.db.get_all("User")
```

To retrieve a filtered subset of documents (e.g., active users):

```python
data.active_users = frappe.db.get_all("User", filters={"enabled": 1})
```

#### Fetching a Single Document

To retrieve a single document by its name or another identifier:

```python
data.user = frappe.get_doc("User", "&lt;user-email&gt;")
```

### From Dynamic Route

To retrieve data based on dynamic route parameters:

```python
# Example route: /blog/:blog_slug
blog_slug = frappe.form_dict.blog_slug
data.blog_post = frappe.get_doc("Blog Post", {"slug": blog_slug})
```

**Usage:**

1. Set up a dynamic route in your web page settings (e.g., `/blog/:blog_slug`).
2. In your data script, access the route parameter using `frappe.form_dict.&lt;parameter_name&gt;`.
3. Use this parameter to fetch the relevant data.

### From Different Frappe Sites

Use FrappeClient to fetch data from external Frappe sites:

```python
client = FrappeClient(
    'https://&lt;frappe-site-url&gt;',
    api_key='xxxxxxxxxx',
    api_secret='xxxxxxxxxx'
)

users = client.get_list('User', fields=['name', 'first_name', 'last_name'], filters={'user_type':'System User'})
```

[Refer to this link](https://github.com/frappe/frappe-client#api) for all supported APIs of `FrappeClient`.

To get `api_key` and `api_secret`:

1. Go to User list and open a user.
2. Click on the "Settings" tab.
3. Expand the API Access section and click on Generate Keys.
4. Copy the API Secret from the popup and keep it safe.
5. Note the "API Key" field in this section.

### From External Resources

Fetch data from external APIs or resources:

```python
data.posts = frappe.make_get_request("https://jsonplaceholder.typicode.com/posts")
```

## Processing Data

Process retrieved data using Python code:

```python
data.users = frappe.db.get_all("User", fields=["name", "first_name", "last_name"])

# Processing data
for user in data.users:
    user.full_name = user.first_name + " " + user.last_name

# Adding routes to each user
for user in data.users:
    user.route = "/user/" + user.name
```

## Passing Data to Client-Side

To pass data to the client-side, set the `data.page_data` variable:

```python
data.page_data = {
    "enabled_languages": ["English", "Spanish", "French"]
    # ...
}
```

This data will be available on the client-side as `window.page_data`.

<!-- page: builder/builder__external-editor.md -->
---
title: "External Editor"
space: "Builder"
url: "https://docs.frappe.io/builder/external-editor"
updated: "2026-05-13"
---

You can edit builder scripts in VS Code or in any of its forks. This guide will help you configure and help resolve common issues that you might face with external editor integration.

## Setup 

1. Install VS Code extension from the marketplace by searching for "Frappe Script Editor" in VS Code or your preferred fork
2. Complete extension setup, here is the [guide](https://github.com/frappe/frappe-script-editor#setup)
3. Open builder settings > Developer Settings

[Screenshot on the live page]

4. Click on **Request Access** button and click **Allow** in the popup

[Screenshot on the live page]

5. Open scripts in an external editor by right-clicking the block and selecting "Open Client Script in Windsurf", the editor's name will change in the option based on which one you are using.

[Screenshot on the live page]

## Common issues

### Request access button not visible

1. Click on settings icon next to site url in the address bar 
2. Enable **Apps on device** option, doing this will grant builder permission to open external editor directly, no need to click **Request access** button again
3. Click on **Reset Permission** button, reload the site and then the button will be visible

[Screenshot on the live page]

<!-- page: builder/builder__introduction.md -->
---
title: "Introduction"
space: "Builder"
url: "https://docs.frappe.io/builder/introduction"
updated: "2026-01-06"
---

## Frappe Builder

Frappe Builder is a low-code website builder designed for simplicity, speed, and flexibility. Craft beautiful websites effortlessly with an intuitive visual builder. Whether you're a designer looking for ease or a developer seeking customization, Frappe Builder empowers you. It also features a click-to-publish option that gives you the complete end-to-end website creation experience.

[Video on the live page]

### Motivation

Most existing solutions were either too complex, too restrictive, or difficult to integrate with the Frappe ecosystem. Additionally, pages built with these tools were often bloated with unnecessary scripts and styles. I wanted to take a stab at solving this problem while prioritising performance from day one. I aimed to address two major issues with this project: providing an intuitive way to design a web page and enabling one-click publishing. As a web developer, it helps me scratch my own itch, and I hope it helps others too.

### Key Features

- **Intuitive Visual Builder:** Simplify your workflow with a Figma-like editor.
- **Responsive Views:** Ensure your sites look great on any device without the fuss.
- **Frappe CMS Integration:** Easily fetch data from your database and create dynamic pages.
- **Scripting Capabilities:** Customize with client scripts, global scripts, and styles.
- **One-Click Publishing:** Instantly share your creation with the world in a single click.
- **Performance Excellence:** Frappe Builder does not bloat web pages with unnecessary scripts hence pages are highly performant, consistently scoring high on Google Lighthouse tests.
- **Production Ready**: [Frappe.io](https://frappe.io) built on Frappe Builder, stands as a testament to its reliability in delivering production-ready solutions.

### Under the Hood

- [Frappe Framework](https://github.com/frappe/frappe): A full-stack web application framework.
- [Frappe UI](https://github.com/frappe/frappe-ui): A Vue-based UI library, to provide a modern user interface.


### Installation

To install/setup the app, follow the [guidelines here](https://github.com/frappe/builder#getting-started-production).


### Links

- [Telegram Public Group](https://t.me/frappebuilder)
- [Discuss Forum](https://discuss.frappe.io/c/frappe-builder/83)
- [Documentation](https://docs.frappe.io/builder)
- [Figma Plugin (Beta)](https://www.figma.com/community/plugin/1417835732014419099/figma-to-frappe-builder)

<!-- page: builder/builder__setting-up.md -->
---
title: "Learning Resources"
space: "Builder"
url: "https://docs.frappe.io/builder/setting-up"
updated: "2026-06-10"
---

### Streams

<iframe src="https://www.youtube-nocookie.com/embed/NzRh-aGzlsQ?si=Ps1TeYfL6K7ATIE6" width="560" height="315" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0" allowfullscreen></iframe>



**Crash Course | Part 1**  

<iframe src="https://www.youtube-nocookie.com/embed/x2FKlAf3XRk?si=W3cwn68JgeA0MjT5" width="560" height="315" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0" allowfullscreen></iframe>



**Crash Course | Part 2**



### Talks

**Demo of Figma-To-Builder plugin**  

<iframe src="https://www.youtube-nocookie.com/embed/rO6p2-N99bc?si=bVyrj7orcGm8DViQ" width="560" height="315" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" frameborder="0" allowfullscreen></iframe>
