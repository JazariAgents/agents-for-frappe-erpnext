<!-- Frappe documentation: framework, part 6 of 6. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__python-api__hooks.md -->
---
title: "Hooks"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/python-api/hooks"
updated: "2026-08-15"
---

Hooks allow you to "hook" into functionality and events of core parts of the Frappe Framework. This page documents all of the hooks provided by the framework.

> Jump to list of all [available hooks](#list-of-available-hooks) in Frappe.

## How does hooks work?

Hooks are places in the core code that allow an app to override the standard implementation or extend it. Hooks are defined in **hooks.py** of your app.

Let's learn by example. Add the following hooks in your app's **hooks.py**.

```
test_string = "value"
test_list = ["value"]
test_dict = {
    "key": "value"
}
  

```

Now, open the python console by running the command `bench --site sitename console` and run the following lines:

```
❯ bench --site sitename console
Apps in this namespace:
frappe, frappe_docs

In [1]: frappe.get_hooks("test_string")
Out[1]: ["value"]

In [2]: frappe.get_hooks("test_dict")
Out[2]: {"key": ["value"]}

In [3]: frappe.get_hooks("test_list")
Out[3]: ["value"]
  

```

When you call `frappe.get_hooks`, it will convert all the values in a list. This means that if the hook is defined in multiple apps, the values will be collected from those apps. This is what enables the cascading nature of hooks.

Now, the hook value can be consumed in different ways. For example, for including JS assets using `app_include_js`, all of the values are included. But for overriding whitelisted method, the last value in the list is used.

So the implementation of the hook is totally dependent on how the author of the feature intended it to be used.

## How are conflicting hooks resolved?

Hooks are resolved using "last writer wins" strategy. Last installed app on site will have highest priority over others.

- When the hook overrides existing behaviour like overriding a class then only overrides from last app will work.
- When the hook extends behaviour then extensions will be applied in order of installation on the site.

> If you need to change this order you can do so by going to "Installed Applications" page and clicking on "Update Hooks Resolution Order"

## App Meta Data

These are automatically generated when you create a new app. Most of the time you don't need to change anything here.

1. `app_name` - slugified name of the app
2. `app_title` - presentable app name
3. `app_publisher`
4. `app_description`
5. `app_version`
6. `app_icon`
7. `app_color`

## Javascript / CSS Assets

The following hooks allow you to inject static JS and CSS assets in various parts of your site.

### Desk

These hooks allow you to inject JS / CSS in `desk.html` which renders the [Desk](/framework/v14/user/en/desk).

```
# injected in desk.html
app_include_js = "assets/js/app.min.js"
app_include_css = "assets/js/app.min.css"

# All of the above support a list of paths too
app_include_js = ["assets/js/app1.min.js", "assets/js/app2.min.js"]
  

```

### Portal

These hooks allow you to inject JS / CSS in `web.html` which renders the [Portal](/framework/v14/user/en/portal-pages).

```
# injected in the web.html
web_include_js = "assets/js/app-web.min.js"
web_include_css = "assets/js/app-web.min.css"
# All of the above support a list of paths too
web_include_js = ["assets/js/web1.min.js", "assets/js/web2.min.js"]
  

```

### Web Form

These hooks allow you to add inject static JS and CSS assets in `web_form.html` which is used to render Web Forms. These will work only for Standard Web Forms.

```
webform_include_js = {"ToDo": "public/js/custom_todo.js"}
webform_include_css = {"ToDo": "public/css/custom_todo.css"}
  

```

> For user created Web Forms, you can directly write the script in the form &gt; itself.

### Page

These hooks allow you to inject JS assets in Standard Desk Pages.

```
page_js = {"page_name" : "public/js/file.js"}
  

```

For e.g., Background Jobs is a standard page that is part of Core module in Frappe Framework. To add custom behaviour in that page you can add a JS file in your custom app `custom_app/public/js/custom_background_jobs.js` and add the following line in your hooks file.

**custom\_app/hooks.py**

```
page_js = {"background_jobs": "public/js/custom_background_jobs.js"}
  

```

## Sounds

Frappe ships with a set of audio notifications for events like a success action, document submission, error, etc. You can add your own sounds using the `sounds` hook.

**app/hooks.py**

```
sounds = [
    {"name": "ping", "src": "/assets/app/sounds/ping.mp3", "volume": 0.2}
]
  

```

You can play your added sound using the client utility method:

```
frappe.utils.play_sound("ping")
  

```

## Install Hooks

These hooks allow you to run code before and after installation of your app. For example, [ERPNext](https://github.com/frappe/erpnext) has these [defined](https://github.com/frappe/erpnext/blob/ecfa6344c02b18455637455742202c7fadf1b35d/erpnext/hooks.py#L42-L43).

```
# python module path
before_install = "app.setup.install.before_install"
after_install = "app.setup.install.after_install"
after_sync = "app.setup.install.after_sync"
  

```

**app/setup/install.py**

```
# will run before app is installed on site
def before_install():
    pass

# will run after app is installed on site
def after_install():
    pass

# will run after app fixtures are synced
def after_sync():
    pass
  

```

## Uninstall Hooks

These hooks allow you to run code before and after uninstallation of your app.

**app/hooks.py**

```
before_uninstall = "app.setup.uninstall.before_uninstall"
after_uninstall = "app.setup.uninstall.after_uninstall"
  

```

**app/setup/uninstall.py**

```
# will run before app is uninstalled from site
def before_uninstall():
    pass

# will run after app is uninstalled from site
def after_uninstall():
    pass
  

```

## Migrate Hooks

These hooks allow you to run code before and after a migration is run on your site via the command `bench --site sitename migrate`.

**app/hooks.py**

```
before_migrate = "app.migrate.before_migrate"
after_migrate = "app.migrate.after_migrate"
  

```

**app/migrate.py**

```
def after_migrate():
    # run code after site migration
    pass
  

```

## Build Hooks

This hook allows you to extend the build system via the `bench build` command. It runs after completing builds for all the apps on the bench. Build hooks let you run code at the end of `bench build`, after assets and translations are compiled.

### after\_build

Runs when your own app is built. Use it to post-process your app's assets



**app/hooks.py**

```
after_build = "app.build.after_build"
```

**app/build.py**

```python
def after_build() -> None:
	pass
```

### after\_app\_build

:::note
Only available in develop branch for now
:::



Runs on every build, whichever apps are being built. Use it when your app produces assets for **other** apps - e.g. Frappe Studio compiling the studio frontends shipped inside other apps.



**app/hooks.py**

```
after_app_build = "papp.build.after_app_build"
```

```markdown
**app/hooks.py**

```py
after_app_build = "app.build.after_app_build"
```

**app/build.py**

```python
def after_app_build(built_apps: list[str]) -> None:
	for app in built_apps:
		pass
```

```

**app/build.py**

```python
def after_app_build(built_apps: list[str]) -> None:
	for app in built_apps:
        pass
# `built_apps` is the value of `--app`/`--apps`, or all apps on the bench when
# `bench build` runs without arguments.
```

## Test Hooks

This hook allows you to run code before tests are run on a site. You can use this hook to add seed data to your database which will be available to your tests.

**app/hooks.py**

```
before_tests = "app.tests.before_tests"
  

```

**app/migrate.py**

```
def before_tests():
    # add seed data to the database
    pass
  

```

## File Hooks

These hooks allows you to change the implementation of handling user uploaded files.

**app/hooks.py**

```
before_write_file = "app.overrides.file.before_write"
write_file = "app.overrides.file.write_file"
delete_file_data_content = "app.overrides.file.delete_file"
  

```

**app/overrides/file.py**

```
# will run before file is written to disk
def before_write():
    pass

# will override the implementation of writing file to disk
# can be used to upload files to a CDN instead of writing
# the file to disk
def write_file():
    pass


# will override the implementation of deleting file from disk
# can be used to delete uploaded files from a CDN instead of
# deleting file from disk
def delete_file():
    pass
  

```

## Email Hooks

These hooks allows you to change the default email module implementation of sending emails and setting default sender address.

**app/hooks.py**

```
override_email_send = "app.overrides.email.send"
get_sender_details = "app.overrides.email.get_sender_details"
  

```

By default frappe uses the currently logged in users name and id as sender details on all emails. This can be overriden with `get_sender_details` hook. And if you want to extend the email modules functionality by using a thirdy party server or app for sending emails then you can use `override_email_send` hook. This hook will send all the email information (sender, recipient, content(mime)) to a function in custom\_app.

**app/overrides/email.py**

```
# will be edited as "John Doe <johndoe@example.com>"
def get_sender_details():
    return "John Doe", "johndoe@example.com"

# self - EmailQueue object refrence for updating status
def send(self, sender, recipient, msg):
    # smtp or http request
    self.update_status("Sending")
  

```

> Note: You'll have to handle the status change of email queue in your custom app depending on the webhook response you get from your mail provider/server

## Extend Bootinfo

After a successful login, the Desk is injected with a dictionary of global values called `bootinfo`. The `bootinfo` is available as a global object in Javascript as `frappe.boot`.

The `bootinfo` dict contains a lot of values including:

- System defaults
- Notification status
- Permissions
- User settings
- Language and timezone info

You can add global values that makes sense for your app via the `extend_bootinfo` hook.

```
# python module path
extend_bootinfo = "app.boot.boot_session"
  

```

The method is called with one argument `bootinfo`, on which you can directly add/update values.

**app/boot.py**

```
def boot_session(bootinfo):
 bootinfo.my_global_key = "my_global_value"
  

```

Now, you can access the value anywhere in your client side code.

```
console.log(frappe.boot.my_global_key)
  

```

## Website Context

When a Portal Page is rendered, a dictionary is built with all of the possible variables that the page might need to render. This dict is also known as `context`. You can use these hooks to add or modify values in this dict.

**app/hooks.py**

```
website_context = {
    "favicon": "/assets/app/image/favicon.png"
}
update_website_context = "app.overrides.website_context"
  

```

The `website_context` hook is a simple dict of key value pairs. Use this hook for simple value overrides.

You can use the `update_website_context` hook for more complex scenarios as it allows you to manipulate the context dict in a python method. The method is called with one argument, which is the `context` dict. You can either modify the context directly by mutating it or return a dict that will be merged with `context`.

**app/overrides.py**

```
def website_context(context):
 context.my_key = "my_value"
  

```

## Website Controller Context

Frappe ships with standard web pages like `/404` and `/about`. If you want to extend the controller context for these pages you can use the `extend_website_page_controller_context` hook.

**app/hooks.py**

```
extend_website_page_controller_context = {
    "frappe.www.404": "app.pages.context_404"
}
  

```

The above hook configuration will allow you to extend the context of the 404 page so that you can add your own keys or modify existing ones.

**app/pages.py**

```
def context_404(context):
    # context of the 404 page
    context.my_key = "my_value"
  

```

## Web pages with dynamic routes

Dynamic routes are the routes with dynamic values in them.

**Example:**

```
/profile/<name>
```

here "name" is the dynamic part but same profile page is rendered. By default, Frappe supports dynamic routes from documents in "Web Page" doctype. To add more dynamic routes, `get_web_pages_with_dynamic_routes` can be used.

**app/[hooks.py](http://hooks.py)**

```
get_web_pages_with_dynamic_routes = "script.get_web_pages_with_dynamic_routes"
  

```

**script.py**

```
def get_web_pages_with_dynamic_routes():
 return [{
       "doctype": "Custom Web Page", // Doctype extended from WebsiteGenerator https://frappeframework.com/docs/user/en/guides/portal-development/generators
       "route": "/profile/<name>",
       "name": "profile-page" // name of the web view document to render
    }, ...]
```

## Website Clear Cache

Frappe Framework caches a lot of static web pages for fast subsequent rendering. If you have created web pages that use cached values, and you want to invalidate the cache, this hook is place to do it.

**app/hooks.py**

```
website_clear_cache = "app.overrides.clear_website_cache"
  

```

The method is called with one argument `path`. `path` is set when cache is being cleared for one route, and is `None` when cache is cleared for all routes. You need to handle this case if your cache is page specific.

**app/overrides.py**

```
def clear_website_cache(path=None):
    if path:
        # clear page related cache
    else:
        # clear all cache
  

```

## Website Redirects

Website Redirects allow you to define redirects from one route to another. Frappe will generate a 304 Redirect response when the source URL is requested and redirect to the target URL. You can redirect plain URLs or you can use regex to match your URLs.

**app/hooks.py**

```
website_redirects = [
    {"source": "/compare", "target": "/comparison"},
    {"source": "/docs(/.*)?", "target": "https://docs.tennismart.com/\1"},
    {"source": r'/items/item\?item_name=(.*)', "target": '/items/\1', match_with_query_string=True},
]
  

```

The above configuration will result in following redirects:

- `/compare` to `/comparison`
- `/docs/getting-started` to `https://docs.tennismart.com/getting-started`
- `/docs/help` to `https://docs.tennismart.com/help`
- `/items/item?item_name=racket` to `https://docs.tennismart.com/items/racket`

## Website Route Rules

Website Route Rules allow you to map URLs to custom controllers. This is commonly used to generate clean URLs for pages.

Let's say you want to have `/projects` route to display list of projects. This can be done by creating a `projects.html` and `projects.py` in `www` folder.

You also want to have `/project/<name>` route to show a project page where name is the dynamic. To do this you can use the `website_route_rules` hook.

**app/hooks.py**

```
website_route_rules = [
    {"from_route": "/projects/<name>", "to_route": "app/projects/project"},
]
  

```

Now, you can create your controller files in `app/projects` folder.

**app/projects/project.py**

```
def get_context(context):
    project_name = frappe.form_dict.name
    project = frappe.get_doc("Project", project_name)
    context.project = project
  

```

**app/projects/project.html**

```
<h1>{{ project.title }}</h1>
<p>{{ project.description }}</p>
  

```

## Website Path Resolver

Frappe does some standard route resolving eg. any request to "/profile" gets internally converted to "/me". `website_path_resolver` can be used to override this behaviour.

**app/[hooks.py](http://hooks.py)**

```
website_path_resolver = "path.to.custom_resolver_method"
```

**Note:** Yourcustom\_resolver\_method will get the requested route, is expected to return a processed route.

## Website 404

Frappe renders a default `/404` route when a page is not found. You can change this using the `website_catch_all` hook.

**app/hooks.py**

```
website_catch_all = "not_found"
  

```

The above configuration will render `/not_found` when a 404 is occurred. It is upto you to implement the template `www/not_found.html` and controller `www/not_found.py`.

## Default Homepage

Homepage is the page which is rendered when you visit the root URL (`/`) of your site. There are multiple ways to configure what page is rendered as the default homepage.

By default, the homepage is `index`. So, frappe will try to render `index.html` from `www` folder. This can be overridden using the `homepage` hook.

**app/hooks.py**

```
homepage = "homepage"
  

```

The above configuration will load the `www/homepage.html` as the default homepage.

You can also have role based homepage by using the `role_home_page` hook.

**app/hooks.py**

```
role_home_page = {
    "Customer": "orders",
    "Supplier": "bills"
}
  

```

The above configuration will make `/orders` the default homepage for users with the **Customer** role and `/bills` for users with the **Supplier** role.

You can have even more control over the logic by using the `get_website_user_home_page` hook.

**app/hooks.py**

```
get_website_user_home_page = "app.website.get_home_page"
  

```

**app/website.py**

```
def get_home_page(user):
    if is_projects_user(user):
        return "projects"
    if is_partner(user):
        return "partner-dashboard"
    return "index"
  

```

> If all of these hooks are defined, the `get_website_user_home_page` will have &gt; higher priority over the others, and `role_home_page` will have higher &gt; priority over `homepage`.

## Portal Sidebar

Some Portal views are shown with a sidebar with links to quickly jump to pages. These sidebar items can be customized via hooks.

**app/hooks.py**

```
portal_menu_items = [
    {"title": "Dashboard", "route": "/dashboard", "role": "Customer"},
    {"title": "Orders", "route": "/orders", "role": "Customer"},
]
  

```

The above configuration will add two sidebar links for users with the role Customer.

![Portal Sidebar](/files/hooks-portal-menu-items.png)



These sidebar items are hardcoded in your app so they are not customizable from Desk. For e.g., if you want to hide a sidebar link temporarily you will have to make changes in your code.

There is another hook called `standard_portal_menu_items` which allows you to do that. The sidebar links set in `standard_portal_menu_items` hook will be synced with the database.

**app/hooks.py**

```
standard_portal_menu_items = [
    {"title": "Dashboard", "route": "/dashboard", "role": "Website Manager"},
    {"title": "Orders", "route": "/orders", "role": "Website Manager"},
]
  

```

The above configuration will sync sidebar items to the Portal Settings which can later be edited by any System User.

![Portal Settings](/files/hooks-standard-portal-menu-items.png)



## Brand HTML

This hook allows you to customize the brand logo in the navbar of your website.

**app/hooks.py**

```
brand_html = '<div><img src="tennismart.png"> TennisMart</div>'
  

```

If the `brand_html` is defined, it will override the default brand html in the navbar. It is not recommended to use hooks to change your brand logo, unless you want to version control it, otherwise you can use Website Settings to change it.

## Base Template

When a web page is rendered, it extends `templates/base.html` by default. You can override the base template by overriding the `base_template` hook.

**app/hooks.py**

```
base_template = "app/templates/my_custom_base.html"
  

```

You can also customize base templates based on routes. For e.g., if you want to use a different base template for all the routes that start with `docs/*` then you can use the `base_template_map` hook. The key must be a regex that matches the route. All other routes will fallback to the default base template.

**app/hooks.py**

```
base_template_map = {
    r"docs.*": "app/templates/doc_template.html"
}
  

```

## Integrations

These hooks allow you to customize behaviour of 3rd-party integrations in Frappe.

### Braintree Success Page

This hook allows you to override the default redirect URL on successful payment of Braintree transaction.

**app/hooks.py**

```
braintree_success_page = "app.integrations.braintree_success_page"
  

```

The method is called with one argument `data` which has the meta data of the payment.

**app/integrations.py**

```
def braintree_success_page(data):
    # data.reference_doctype
    # data.reference_docname
    return "/thank-you"
  

```

## Calendars

The calendar hook is a list of doctype names which are shown as menu items for quick navigation from the Calendar page in Desk.

**app/hooks.py**

```
calendars = ["Appointment"]
  

```

![Event Menu Shortcuts](/files/hooks-event-menu-shortcuts.png)



## Clear Cache

This hook allows you to clear your app specific cache values when the global cache is being cleared by frappe.

**app/hooks.py**

```
clear_cache = "app.cache.clear_cache"
  

```

You can use this hook to clear your app specific cache. The method is called without any arguments.

**app/cache.py**

```
def clear_cache():
    frappe.cache().hdel("app_specific_cache")
  

```

## Default Mail Footer

If you want to set the default footer of all the emails that are sent out by Frappe, you can use the `default_mail_footer` hook.

**app/hooks.py**

```
default_mail_footer = """
 <div>
 Sent via <a href="https://tennismart.com" target="_blank">TennisMart</a>
</div>
"""
  

```

Now, all the emails will have **Sent via TennisMart** in the footer.

## Session Hooks

These hooks are triggered over the login lifecycle of a user. `on_login` is triggered immediately after a successful login, `on_session_creation` is triggered after the session is setup, `on_logout` is triggered after the user logs out.

**app/hooks.py**

```
on_login = "app.overrides.successful_login"
on_session_creation = "app.overrides.allocate_free_credits"
on_logout = "app.overrides.clear_user_cache"
  

```

The method will be called with one argument `login_manager`.

**app/overrides.py**

```
def allocate_free_credits(login_manager):
    # allocate free credits to frappe.session.user
    pass
  

```

## Auth Hooks

These hooks are triggered during request authentication. Custom headers, Authorization headers can be validated here, user is verified and mapped to the request using `frappe.set_user()`. Use `frappe.request` and `frappe.*` to validate request and map user.

**app/hooks.py**

```
auth_hooks = ["app.overrides.validate_custom_jwt"]
  

```

The method will be called during request authentication.

**app/overrides.py**

```
def validate_custom_jwt():
    # validate jwt from header, verify signature, set user from jwt.
    pass
  

```

Use this method to check for incoming request header, verify the header and map the user to the request. If header verification fails DO NOT throw error to continue with other hooks. Unverified request is treated as "Guest" request by default. You may use third party server, shared database or any alternative of choice to verify and map request and user.

## Fixtures

Fixtures are database records that are synced using JSON files when you install and update your site.

Let's say you want to create a set of categories in the database whenever you install your app. To do that, create the set of categories in your local site, and add the doctype name in the `fixtures` hook.

```
fixtures = [
    # export all records from the Category table
    "Category"
]
  

```

Now, run the following command:

```
bench --site sitename export-fixtures
  

```

This command will create a JSON file for each doctype which will contain the data to generate list of records. You can test this by creating a new site and by installing your app on that site.

You can also add conditions for exporting records.

```
fixtures = [
    # export all records from the Category table
    "Category",
    # export only those records that match the filters from the Role table
    {"dt": "Role", "filters": [["role_name", "like", "Admin%"]]},
]
  

```

Some fields are for internal use only. They will be set and kept up-to-date by the system automatically. These will not get exported: `modified_by`, `creation`, `owner`, `idx`, `lft` and `rgt`. For child table records, the following fields will not get exported: `docstatus`, `doctype`, `modified` and `name`.

## Document Hooks

### Modify List Query

You can customize how list of records are queried for a DocType by adding custom match conditions using the `permission_query_conditions` hook. This match condition must be a valid WHERE clause fragment for an SQL query.

**app/hooks.py**

```
permission_query_conditions = {
    "ToDo": "app.permissions.todo_query",
}
  

```

The method is called with a single argument `user` which can be `None`. The method should return a string that is a valid SQL WHERE clause.

**app/permissions.py**

```
def todo_query(user):
    if not user:
        user = frappe.session.user
    # todos that belong to user or assigned by user
    return "(`tabToDo`.owner = {user} or `tabToDo`.assigned_by = {user})".format(user=frappe.db.escape(user))
  

```

Now, if you use the `frappe.db.get_list` method, your WHERE clause will be appended to the query.

```
todos = frappe.db.get_list("ToDo", debug=1)

# output
'''
select `tabToDo`.`name`
from `tabToDo`
where ((`tabToDo`.owner = 'john@doe.com' or `tabToDo`.assigned_by = 'john@doe.com'))
order by `tabToDo`.`modified` DESC
'''
  

```

> This hook will only affect the result of `frappe.db.get_list` method and not &gt; `frappe.db.get_all`.

### Document Permissions

You can modify the behaviour of `doc.has_permission` document method for any DocType and add custom permission checking logic using the `has_permission` hook.

**app/hooks.py**

```
has_permission = {
    "Event": "app.permissions.event_has_permission",
}
  

```

The method will be passed the `doc`, `user` and `permission_type` as arguments. It should return `True` or a `False` value. If `None` is returned, it will fallback to default behaviour.

**app/permissions.py**

```
def event_has_permission(doc, user=None, permission_type=None):
    # when reading a document allow if event is Public
    if permission_type == "read" and doc.event_type == "Public":
        return True

    # when writing a document allow if event owned by user
    if permission_type == "write" and doc.owner == user:
        return True

    return False
  

```

### Extend DocType Class

> Note: this is available in v16+

You can extend the class for standard doctypes by using the `extend_doctype_class` hook. This hook allows you to add properties, methods, and functionality to existing DocType classes without overriding them completely, enabling multiple apps to extend the same DocType class.

**app/hooks.py**

```python
extend_doctype_class = {
    "Address": ["app.extensions.address.AddressMixin"]
}
```

**app/extensions/address.py**

```python
from frappe.model.document import Document

class AddressMixin(Document):
    @property
    def full_address(self):
        return f"{self.address_line1}, {self.city}, {self.country}"
    
    def custom_validation(self):
        # Custom validation logic
        pass

    def validate(self):
        super.validate()
        self.custom_validation()
```

#### Multiple Extensions

You can define multiple extensions for the same DocType. For example, the `ValidationMixin` could be used in **Contact** as well as in **Address**, while the `GeocodingMixin` is used only in **Address**.

**app/hooks.py**

```python
extend_doctype_class = {
    "Address": [
        "app.extensions.address.GeocodingMixin",
        "app.extensions.common.ValidationMixin"
    ],
    "Contact": [
        "app.extensions.common.ValidationMixin"
    ]
}
```

#### Hooks Resolution Order

When multiple apps define extensions for the same DocType, the extensions are applied in the hooks resolution order. If apps are resolved in the order `frappe`, `app1`, `app2`, the final class will be:

```python
class ExtendedAddress(App2Mixin, App1Mixin, Address):
    pass
```

#### Interaction with `override_doctype_class`

The `extend_doctype_class` hook works on top of `[override_doctype_class](#override-doctype-class)`. If both hooks are defined, extensions are applied to the overridden class instead of the base class.

For example, if ERPNext overrides the Address class and custom apps extend it:

```python
# ERPNext overrides Address
override_doctype_class = {
    "Address": "erpnext.setup.doctype.address.address.Address"
}

# Custom apps extend it
extend_doctype_class = {
    "Address": ["app1.extensions.Prop1Mixin", "app2.extensions.Prop2Mixin"]
}

# Final class becomes:
class ExtendedAddress(Prop2Mixin, Prop1Mixin, ERPNextAddress):
    pass
```

This hook is ideal for adding virtual fields, computed properties, and custom methods without disrupting the core functionality. It's recommended to use this hook instead of `[override_doctype_class](#override-doctype-class)` when you only need to add functionality rather than replace it.

### Override DocType Class

You can override/extend the class for standard doctypes by using the `override_doctype_class` hook. Unlike `[extend_doctype_class](#extend-doctype-class)`, this hook completely replaces the original class. This can cause issues when you have multiple apps overriding the same DocType class. In v16+, prefer using `[extend_doctype_class](#extend-doctype-class)` instead.

**app/hooks.py**

```
override_doctype_class = {
    "ToDo": "app.overrides.todo.CustomToDo"
}
  

```

**app/overrides/todo.py**

```
from frappe.desk.doctype.todo.todo import ToDo

class CustomToDo(ToDo):
    def on_update(self):
        self.my_custom_code()
        super().on_update()

    def my_custom_code(self):
        pass
  

```

> It is recommended that you extend the standard class of the doctype, otherwise you will have to implement all of the core functionality.

### Override Form Scripts

You can override/extend [Standard Form Scripts](/framework/v14/user/en/api/form#standard-form-scripts) by using the `doctype_js` hook.

**app/hooks.py**

```
doctype_js = {
    "ToDo": "public/js/todo.js",
}
  

```

**app/public/js/todo.js**

```
frappe.ui.form.on("Todo", {
    refresh: function(frm) {
        frm.trigger("my_custom_code");
    },
    my_custom_code: function(frm){
        console.log(frm.doc.name)
    }
});
  

```

> The events/functions defined in `app/public/todo.js` will extend &gt; those in the standard form script of `ToDo` doctype.

### CRUD Events

You can hook into various CRUD events of any doctype using the `doc_events` hook.

**app/hooks.py**

```
doc_events = {
    "*": {
        # will run after any DocType record is inserted into database
        "after_insert": "app.crud_events.after_insert_all"
    },
    "ToDo": {
        # will run before a ToDo record is inserted into database
        "before_insert": "app.crud_events.before_insert_todo",
    }
}
  

```

The method will be passed the doc and the method name as arguments.

**app/crud\_events.py**

```
def after_insert_all(doc, method=None):
    pass

def before_insert_todo(doc, method=None):
    pass
  

```

> See [Controller Hooks](/framework/v14/user/en/basics/doctypes/controllers#controller-hooks) &gt; for a list of all available hooks.

### Override Whitelisted Methods

Whitelisted Methods are python methods that are accessible on a REST endpoint and consumed by a client. You can override standard whitelisted methods that are part of the core framework using the `override_whitelisted_methods` hook.

**app/hooks.py**

```
override_whitelisted_methods = {
    "frappe.client.get_count": "app.whitelisted.custom_get_count"
}
  

```

The method should have the same signature as the original method.

**app/whitelisted.py**

```
def custom_get_count(doctype, filters=None, debug=False, cache=False):
    # your custom implementation of the standard get_count method provided by frappe
    pass
  

```

### Ignore Links on Delete

To ignore links to specific DocTypes when deleting documents, you can specify them in the `ignore_links_on_delete` hook like so:

**app/hooks.py**

```
ignore_links_on_delete = ["Communication", "ToDo"]
  

```

### Form Timeline

The timeline section of [form view](/framework/v14/user/en/desk#form-view) of a document shows an audit trail of actions performed on that document like views, value changes, comments and related communications, etc.

Apart from these standard actions, there might arise a situation where you need to add your own custom actions. You can do this via `additional_timeline_content` hook.

```
additional_timeline_content: {
    # show in each document's timeline
    "*": ["app.timeline.all_timeline"]
    # only show in ToDo's timeline
    "ToDo": ["app.timeline.todo_timeline"]
}
  

```

The method will be passed the doctype and docname as arguments. You can perform queries and return actions related to that document as a list of dicts as shown in the example. Each dict in the list must have a `creation` value which will be used to sort the item in the timeline.

```
def todo_timeline(doctype, docname):
    # this method should return a list of dicts
    return [
        {
             # this will be used to sort the content in the timeline
            "creation": "22-05-2020 18:00:00",
            # this JS template will be rendered in the timeline
            "template": "custom_timeline_template",
            # this data will be passed to the template.
            "template_data": {"key": "value"},
        },
        ...
    ]
  

```

## Scheduler Events

You can use Scheduler Events for running tasks periodically in the background using the `scheduler_events` hook.

**app/hooks.py**

```
scheduler_events = {
    "hourly": [
        # will run hourly
        "app.scheduled_tasks.update_database_usage"
    ],
}
  

```

**app/scheduled\_tasks.py**

```
def update_database_usage():
    pass
  

```

> After changing any scheduled events in `hooks.py`, you need to run `bench migrate` for changes to take effect.

### Available Events

- `hourly`, `daily`, `weekly`, `monthly`

These events will trigger every hour, day, week and month respectively.

- `hourly_long`, `daily_long`, `weekly_long`, `monthly_long`

Same as above but these jobs are run in the [long worker](/framework/v14/user/en/basics/directory-structure#worker_long) suitable for long running jobs.

- `all`

The `all` event is triggered every 60 seconds. This can be configured via the `scheduler_tick_interval` key in `common_site_config.json`

- `cron`

A valid cron string that can be parsed by [croniter](https://pypi.org/project/croniter/).

Usage Examples:

```
scheduler_events = {
    "daily": [
        "app.scheduled_tasks.manage_recurring_invoices"
    ],
    "daily_long": [
        "app.scheduled_tasks..take_backups_daily"
    ],
    "cron": {
        "15 18 * * *": [
            "app.scheduled_tasks..delete_all_barcodes_for_users"
        ],
        "*/6 * * * *": [
            "app.scheduled_tasks..collect_error_snapshots"
        ],
        "annual": [
            "app.scheduled_tasks.collect_error_snapshots"
        ]
    }
}
  

```

## Jinja Customization

Frappe provides a list of [global utility methods](/framework/v14/user/en/api/jinja) in Jinja templates. To add your own methods and filters you can use the `jinja` hook.

**app/hooks.py**

```
jinja = {
    "methods": [
        "app.jinja.methods",
        "app.utils.get_fullname"
    ],
    "filters": [
        "app.jinja.filters",
        "app.utils.format_currency"
    ]
}
  

```

**app/jinja/methods.py**

```
def sum(a, b):
    return a + b

def multiply(a, b):
    return a * b
  

```

> If the path is a module path, all the methods in that module will be added.

**app/utils.py**

```
def get_fullname(user):
    first_name, last_name = frappe.db.get_value("User", user, ["first_name", "last_name"])
    return first_name + " " + last_name

def format_currency(value, currency):
    return currency + " " + str(value)
  

```

Now, you can use these utilities in your Jinja templates like so:

```
<h1>Hi, {{ get_fullname(frappe.session.user) }}</h1>
<p>Your account balance is {{ account_balance | format_currency("INR") }}</p>
<p>1 + 2 = {{ sum(1, 2) }}</p>
  

```

## Prevent Auto Cancellation of Linked Documents

To prevent documents of a specific DocType from being automatically cancelled on the cancellation of any linked documents you can use the `auto_cancel_exempted_doctypes` hook.

**app/hooks.py**

```
auto_cancel_exempted_doctypes = ["Payment Entry"]
  

```

In the above example, if any document (for e.g Sales Invoice) that is linked with Payment Entry is cancelled, it will skip the auto-cancellation of the linked Payment Entry document.

## Notification configurations

The notification configuration hook is used to customize the items shown in the Notification dropdown in Desk. It can be configured by the `notification_config` hook.

**app/hooks.py**

```
notification_config = "app.notification.get_config"
  

```

The method is called without any arguments.

**app/notification.py**

```
def get_config():
 return {
        "for_doctype": {
            "Issue": {"status":"Open"},
            "Issue": {"status":"Open"},
        },
        "for_module_doctypes": {
            "ToDo": "To Do",
            "Event": "Calendar",
            "Comment": "Messages"
        },
        "for_module": {
            "To Do": "frappe.core.notifications.get_things_todo",
            "Calendar": "frappe.core.notifications.get_todays_events",
            "Messages": "frappe.core.notifications.get_unread_messages"
        }
    }
  

```

The above configuration has three parts:

1. `for_doctype` part of the above configuration marks any "Issue" or "Customer Issue" as unread if its status is Open
2. `for_module_doctypes` maps doctypes to module's unread count.
3. `for_module` maps modules to functions to obtain its unread count. The functions are called without any argument.

## Required Apps

When building apps, you might create apps that build on top of other apps. To make sure dependent apps are installed when someone installs your app, you can use the `required_apps` hook.

**app/hooks.py**

```
required_apps = ["erpnext"]
  

```

The above configuration will make sure `erpnext` is installed when someone installs your app.

## User Data Protection &amp; Privacy

User Data Privacy features like personal data download and personal data deletion come out of the box in Frappe. What constitutes as personal data may be defined by the App publisher in the application's `hooks.py` file as `user_data_fields`.

**app/hooks.py**

```
user_data_fields = [
    {"doctype": "Access Log"},
    {"doctype": "Comment", "strict": True},
    {
        "doctype": "Contact",
        "filter_by": "email_id",
        "rename": True,
    },
    {"doctype": "Contact Email", "filter_by": "email_id"},
    {
        "doctype": "File",
        "filter_by": "attached_to_name",
        "redact_fields": ["file_name", "file_url"],
    },
    {"doctype": "Email Unsubscribe", "filter_by": "email", "partial": True},
]
  

```

DocTypes that have user data should be mapped under this hook using the above format. Upon data deletion or download requests from users, this hook will be utilized to map over the specified DocTypes. The options available to modify documents are:




| Field           | Description                                                                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `doctype`       | DocType that contains user data.                                                                                                                                                               |
| `filter_by`     | Docfield to filter the documents by. If unset, defaults to `owner`.                                                                                                                            |
| `partial`       | If set, all text fields are parsed and user's full name and username references will be redacted.                                                                                              |
| `redact_fields` | Fields that have to be redacted. If unspecified, it considers partial data redaction from all text fields.                                                                                     |
| `rename`        | If document name contains user data, set this field to rename document to anonymize it.                                                                                                        |
| `strict`        | If set to True, any user data will be redacted from all documents of current DocType. If unset, it defaults to False which means it only filters through documents in which user is the owner. |


> Note: Personal Data Download only utilizes the doctype and filter\_by fields defined in `user_data_fields`

Related Topics:

1. [Personal Data Deletion](https://docs.erpnext.com/docs/user/manual/en/setting-up/personal-data-deletion)
2. [Personal Data Download](https://docs.erpnext.com/docs/user/manual/en/setting-up/personal-data-download)

## Signup Form Template

If you want to add additional fields to the signup form you can use this hook. Create a template file which contains the custom signup form. Pass this template to the custom signup hook.

```
signup_form_template = "school/templates/signup-form.html"
  

```

> Note: If you want custom fields in signup form, it will require additional fields in the user doctype. You will have to add these fields using fixtures. Also you will have to write your own submit handler for this signup form and a function on the server side which will signup the user. This way you can also write validations for the custom fields you add.

## SMS Hooks

These hooks allow you to customize the SMS sending functionality in Frappe by integrating with third-party SMS providers or implementing custom SMS logic.

### Send SMS

This hook allows you to override the default SMS sending logic for notifications, bulk SMS, and other general SMS functionality.

**app/hooks.py**

```python
send_sms = "app.overrides.sms.send_sms"
```

The method is called with the SMS details including recipient, message content, and other metadata.

**app/overrides/sms.py**

```python
def send_sms(receiver_list, msg, sender=None, success_msg=True):
    """
    Override default SMS sending logic
    
    Args:
        receiver_list: List of mobile numbers or single mobile number
        msg: SMS message content
        sender: Sender ID (optional)
        success_msg: Whether to show success message (optional)
    """
   
    # Send SMS via custom provider
    response = custom_sms_provider.send_sms(
        to=receiver_list,
        message=msg,
        from_number=sender
    )
    
    if response.status_code == 200:
        frappe.msgprint(_("SMS sent successfully"))
        return True
    else:
        frappe.throw(_("Failed to send SMS"))
        return False
```

### Send Token via SMS

This hook allows you to override SMS OTP sending logic for two-factor authentication and mobile login flows.

**app/hooks.py**

```python
send_token_via_sms = "app.overrides.sms.send_token_via_sms"
```

The method is called with OTP details for authentication purposes.

**app/overrides/sms.py**

```python
def send_token_via_sms(otpsecret, token=None, phone_no=None):
   """
    Generate OTP and send using local send_otp function.
    :param otpsecret: OTP secret for generating HOTP
    :param token: Token to use for HOTP generation
    :param phone_no: Phone number to send OTP to
    """
    if not phone_no:
        return False
    try:
        hotp = pyotp.HOTP(otpsecret)
        otp_code = hotp.at(token_int)
        result = send_otp(
            number=phone_no,
            otp_length=len(otp_code),
            otp_expiry=5,  # 5 minutes expiry
            otp=otp_code
        )
        return result.get("success", False)
    except Exception as e:
        frappe.log_error(
            message=f"Failed to send OTP: {str(e)}",
            title="OTP Error"
        )
        return False 
```

## List of available hooks


| Hook Name                                | Explanation                                                                                                               |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `additional_timeline_content`            | [Form Timeline](#form-timeline)                                                                                           |
| `after_install`                          | [Install Hooks](#install-hooks)                                                                                           |
| `after_migrate`                          | [Migrate Hooks](#migrate-hooks)                                                                                           |
| `after_sync`                             | [Install Hooks](#install-hooks)                                                                                           |
| `app_include_css`                        | [Desk Assets](#desk)                                                                                                      |
| `app_include_js`                         | [Desk Assets](#desk)                                                                                                      |
| `app_logo_url`                           | [App Meta Data](#app-meta-data)                                                                                           |
| `app_title`                              | [App Meta Data](#app-meta-data)                                                                                           |
| `auto_cancel_exempted_doctypes`          | [Prevent Auto Cancellation](#prevent-auto-cancellation-of-linked-documents)                                               |
| `base_template_map`                      | [Base Template](#base-template)                                                                                           |
| `base_template`                          | [Base Template](#base-template)                                                                                           |
| `before_install`                         | [Install Hooks](#install-hooks)                                                                                           |
| `before_migrate`                         | [Migrate Hooks](#migrate-hooks)                                                                                           |
| `before_tests`                           | [Test Hooks](#test-hooks)                                                                                                 |
| `before_write_file`                      | [File Hooks](#file-hooks)                                                                                                 |
| `bot_parsers`                            | *Deprecated*                                                                                                              |
| `braintree_success_page`                 | [Braintree Success Page](#braintree-success-page)                                                                         |
| `brand_html`                             | [Brand HTML](#brand-html)                                                                                                 |
| `calendars`                              | [Calendars](#calendars)                                                                                                   |
| `clear_cache`                            | [Clear Cache](#clear-cache)                                                                                               |
| `communication_doctypes`                 |                                                                                                                           |
| `default_mail_footer`                    | [Default Mail Footer](#default-mail-footer)                                                                               |
| `delete_file_data_content`               | [File Hooks](#file-hooks)                                                                                                 |
| `doc_events`                             | [Document CRUD Events](#crud-events)                                                                                      |
| `doctype_js`                             | [Override Form Scripts](#override-form-scripts)                                                                           |
| `domains`                                |                                                                                                                           |
| `dump_report_map`                        | *Deprecated*                                                                                                              |
| `extend_bootinfo`                        | [Extend Bootinfo](#extend-bootinfo)                                                                                       |
| `extend_website_page_controller_context` | [Website Controller Context](#website-controller-context)                                                                 |
| `filters_config`                         |                                                                                                                           |
| `fixtures`                               | [Fixtures](#fixtures)                                                                                                     |
| `get_site_info`                          |                                                                                                                           |
| `get_translated_dict`                    |                                                                                                                           |
| `get_website_user_home_page`             | [Default Homepage](#default-homepage)                                                                                     |
| `get_web_pages_with_dynamic_routes`      | [Web pages with dynamic routes](#web-pages-with-dynamic-routes)                                                           |
| `has_permission`                         | [Document Permissions](#document-permissions)                                                                             |
| `has_website_permission`                 |                                                                                                                           |
| `home_page`                              | [Default Homepage](#default-homepage)                                                                                     |
| `jenv`                                   | [Jinja Customization](#jinja-customization)                                                                               |
| `leaderboards`                           |                                                                                                                           |
| `look_for_sidebar_json`                  |                                                                                                                           |
| `make_email_body_message`                |                                                                                                                           |
| `notification_config`                    | [Notification configuration](#notification-configurations)                                                                |
| `on_login`                               | [Session Hooks](#session-hooks)                                                                                           |
| `on_logout`                              | [Session Hooks](#session-hooks)                                                                                           |
| `on_print_pdf`                           | On printing                                                                                                               |
| `on_session_creation`                    | [Session Hooks](#session-hooks)                                                                                           |
| `extend_doctype_class`                   | [Extend DocType Class](#extend-doctype-class)                                                                             |
| `override_doctype_class`                 | [Override DocType Class](#override-doctype-class)                                                                         |
| `override_doctype_dashboards`            |                                                                                                                           |
| `override_whitelisted_methods`           | [Override Whitelisted Methods](#override-whitelisted-methods)                                                             |
| `ignore_links_on_delete`                 | [Ignore Links on Delete](#ignore-links-on-delete)                                                                         |
| `permission_query_conditions`            | [Modify List Query](#modify-list-query)                                                                                   |
| `portal_menu_items`                      | [Portal Sidebar](#portal-sidebar)                                                                                         |
| `required_apps`                          | [Required Apps](#required-apps)                                                                                           |
| `role_home_page`                         | [Default Homepage](#default-homepage)                                                                                     |
| `scheduler_events`                       | [Scheduler Events](#scheduler-events)                                                                                     |
| `setup_wizard_complete`                  |                                                                                                                           |
| `setup_wizard_exception`                 |                                                                                                                           |
| `setup_wizard_requires`                  |                                                                                                                           |
| `setup_wizard_stages`                    |                                                                                                                           |
| `setup_wizard_success`                   |                                                                                                                           |
| `signup_form_template`                   | [Signup Form Template](#signup-form-template)                                                                             |
| `sounds`                                 | [Sounds](#sounds)                                                                                                         |
| `standard_portal_menu_items`             | [Portal Sidebar](#portal-sidebar)                                                                                         |
| `standard_queries`                       | [Standard Queries](https://www.linkedin.com/pulse/understanding-standardqueries-hook-frappe-framework-el-shafeai--m4ozf/) |
| `send_sms`                               | [SMS Hooks](#send-sms)                                                                                                    |
| `send_token_via_sms`                     | [SMS Hooks](#send-token-via-sms)                                                                                          |
| `template_apps`                          |                                                                                                                           |
| `translated_languages_for_website`       |                                                                                                                           |
| `translator_url`                         |                                                                                                                           |
| `treeviews`                              | DocTypes that use TreeView as the default view (instead of ListView)                                                      |
| `update_website_context`                 | [Website Context](#website-context)                                                                                       |
| `user_privacy_documents`                 | *Deprecated* (Use `user_data_fields` hook)                                                                                |
| `user_data_fields`                       | [User Data Protection &amp; Privacy](#user-data-protection-&amp;-privacy)                                                 |
| `web_include_css`                        | [Portal Assets](#portal)                                                                                                  |
| `web_include_js`                         | [Portal Assets](#portal)                                                                                                  |
| `website_catch_all`                      | [Website 404](#website-404)                                                                                               |
| `website_clear_cache`                    | [Website Clear Cache](#website-clear-cache)                                                                               |
| `website_context`                        | [Website Context](#website-context)                                                                                       |
| `website_generators`                     | *Deprecated* (Use Has Web View in DocType instead)                                                                        |
| `website_redirects`                      | [Website Redirects](#website-redirects)                                                                                   |
| `website_route_rules`                    | [Website Route Rules](#website-route-rules)                                                                               |
| `website_user_home_page`                 | *Deprecated* (Use `homepage` hook)                                                                                        |
| `welcome_email`                          |                                                                                                                           |
| `write_file_keys`                        | *Deprecated*                                                                                                              |
| `write_file`                             | [File Hooks](#file-hooks)                                                                                                 |

<!-- page: framework/framework__user__en__python-api__language.md -->
---
title: "Language Resolution\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/python-api/language"
updated: "2026-02-17"
---


Here, let's take a look into how language in Frappe is resolved, and how you may
be able to use them in your Frappe apps or scripts.

The language for your session depends on the value of `frappe.lang`. This is
resolved in the following order:

1. Form Dict > _lang
1. Cookie > preferred_language _[Guest User only]_
1. Request Header > Accept-Language _[Guest User only]_
1. User document > language
1. System Settings > language

## Form Dict: _lang

The Form Dict's `_lang` parameter has the highest priority. Setting this will
update all translatable components in given request. Frappe uses this mechanism
in certain places to handle Email Templates and Print views.

## Cookie: preferred_language

Although, it may not be practical to pass a `?_lang=ru` in every request. If you
want persistent yet temporary language setting, you can set the
`preferred_language` key in cookies. Frappe utilizes this for the website
language switcher. This method may be used to persist language
based on the client.

> Only considered for Guest Users. Ignored for logged in users.

## Request Header: Accept-Language

Another relatively cleaner, and standard way to manage languages is using the
`Accept-Language` header. If the previous two methods aren't set, Frappe starts
resolving this header's values, which have an ordered set of a range of
acceptable languages by the client. You can check out [the Mozilla
Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language)
on this topic for more clarity perhaps.

> Only considered for Guest Users. Ignored for logged in users.

## User & System Settings

The User document has a `language` field that sets the session language for said
user. This setting persists across devices, clients. This allows a particular
user to view the website, and Desk in a language of their choice. Say for
instance, a user sets their language as "Russian" on a "French" site, when they
login, the site would be translated to Russian automatically.

The `language` field in the System Settings sets the language for the entire
site. It has the lowest priority and is the fallback language for all sessions.

<!-- page: framework/framework__user__en__python-api__response.md -->
---
title: "Responses\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/python-api/response"
updated: "2026-02-17"
---


Here, let's take a look into how responses are built in Frappe, and how you may
be able to use them in your Frappe apps or scripts.

If you have already gone through the [Router
Documentation](/framework/v14/user/en/python-api/routing-and-rendering), you might've noticed the
`build_response` function that Frappe internally utilizes to build responses
depending on the type of the content. The logic that defines this behaviour is a
part of the module
[frappe.utils.response](https://github.com/frappe/frappe/blob/develop/frappe/utils/response.py),
of which `build_response` is the meat and potatoes.

```python
def build_response(response_type=None):
 if "docs" in frappe.local.response and not frappe.local.response.docs:
 del frappe.local.response["docs"]

 response_type_map = {
 "csv": as_csv,
 "txt": as_txt,
 "download": as_raw,
 "json": as_json,
 "pdf": as_pdf,
 "page": as_page,
 "redirect": redirect,
 "binary": as_binary,
 }

 return response_type_map[frappe.response.get("type") or response_type]()
```

The above snippet represents the current implementation of `build_response`
which maps different functions that act as handlers for different content types.
Let's take a deeper look into the response handler for the **"download"**
`response_type` in Frappe v13.

```python
def as_raw():
 response = Response()
 response.mimetype = (
 frappe.response.get("content_type")
 or mimetypes.guess_type(frappe.response["filename"])[0]
 or "application/unknown"
 )
 response.headers["Content-Disposition"] = (
 f'{frappe.response.get("display_content_as", "attachment")};'
 f' filename="{frappe.response["filename"].replace(" ", "_")}"'
 ).encode("utf-8")
 response.data = frappe.response["filecontent"]
 return response
```

Depending on the value of the `Content-Disposition` header, the browser
receiving the response may behave differently. If unset, the value defaults to
**"attachment"**.

If `frappe.response.display_content_as` is set to **"inline"**, it indicates
that the content is expected to be displayed inline in the browser, that is, as
a Web page or as part of a Web page, while **"attachment"** means the contents
are to be downloaded and saved locally.

To create an API endpoint that would directly download the file you require, you
could craft something like the following to download the file directly.

```python
@frappe.whitelist()
def download(name):
 file = frappe.get_doc("File", name)
 frappe.response.filename = file.file_name
 frappe.response.filecontent = file.get_content()
 frappe.response.type = "download"
 frappe.response.display_content_as = "attachment"
```

<!-- page: framework/framework__user__en__python-api__routing-and-rendering.md -->
---
title: "Request Lifecycle\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/python-api/routing-and-rendering"
updated: "2026-02-17"
---


The user of a web application can visit different URLs like `/about`, `/posts` or `/api/resources`. Each request is handled based on the following request types.

1. API requests that start with `/api` are handled by [rest API handler](https://github.com/frappe/frappe/blob/develop/frappe/api.py#L16).
1. File downloads like backups (`/backups`), public files (`/files`), and private files (`/private/files`) are handled separately to respond with a downloadable file.
1. Web page requests like `/about`, `/posts` are handled by the website router. This is explained further on this page.

Learn more about [API requests](/framework/v14/user/en/api/rest) and [Static Files](/framework/v14/user/en/basics/static-assets) in detail.

## Request pre-processing

A few things happen before the routing rules are triggered. These include preprocessing the request initializing the recorder and the rate limiter.

## Path Resolver

Once the request reaches to website router from `app.py` it is passed through the path resolver.

Path resolver does the following operations:

### Redirect Resolution

Path resolver tries to resolve any possible redirect for an incoming request path. Path resolver gets redirect rules for [`website_redirects` hook](/framework/v14/user/en/python-api/hooks#website-redirects) and route redirects from website settings.

### Route Resolution

If there are no redirects for incoming requests path resolver tries to resolve the route to get the final endpoint based on rules from [website_routing_rules hook](https://frappeframework.com/docs/v14/user/en/python-api/hooks#website-route-rules) and dynamic route set in documents of DocType with `has_web_view` enabled.

### Renderer Selection

Once the final endpoint is obtained it is passed through all available [Page Renderers](#page-renderer) to check which page renderer can render the given path. A first page renderer to return `True` for `can_render` request will be used to render the path.

## Page Renderer

A page renderer takes care of rendering or responding with a page for a given endpoint. A page renderer is implemented using a python class. A page renderer class needs to have two methods i.e., `can_render` and `render`.

Path resolver calls `can_render` to check if a renderer instance can render a particular path.
Once a renderer returns `True` from `can_render`, it will be that renderer class's responsibility to render the path.

### Example page renderer class

```py
from frappe.website.page_renderers.base_renderer import BaseRenderer

class PageRenderer(BaseRenderer):
 def can_render(self):
 return True

 def render(self):
 response_html = "Response"
 return self.build_response(response_html)

```

Following are the standard page renderers which handle all the generic types of web pages.

### StaticPage

Using StaticPage you can serve PDFs, images, etc., from the `www` folder of any app installed on the site. Any file that is **not** one of the following types `html`, `md`, `js`, `xml`, `css`, `txt` or `py` is considered to be a static file.
The preferred way of serving static files would be to add them to the `public` folder of your frappe app. That way it will be served by NGINX directly leveraging compression and caching while also reducing latency.

### TemplatePage

The TemplatePage looks up the `www` folder in all apps, if it is an HTML or markdown file, it is returned, in case it is a folder, the `index.html` or `index.md` file in the folder is returned.

### WebformPage

The WebformPage tries to render web form in the Web Form list if the request path matches with any of the available Web Form's routes.

### DocumentPage

The DocumentPage tries to render a document template if it is available in `/templates` folder of the DocType. The template file name should be the same as the DocType name. Example: If you want to add a document template for User doctype, the `templates` folder of User DocType should have `user.html`. The folder structure will look like `doctype/user/templates/user.html`

### ListPage

If a DocType has a list template in `/templates` folder of the DocType, the ListPage will render it. Please check [Blog Post templates folder](https://github.com/frappe/frappe/tree/develop/frappe/website/doctype/blog_post/templates) for implementation reference.

### PrintPage

The PrintPage renders a print view for a document. It uses [standard print format](https://github.com/frappe/frappe/blob/develop/frappe/templates/print_formats/standard.html) unless a different print format is set for a DocType via `default_print_format`.

### NotFoundPage

The NotFoundPage renders a standard not found page and responds with `404` status code.

### NotPermittedPage

The NotPermittedPage renders standard permission denied page with `403` status code.

## Adding a custom page renderer

If you have any other requirements which are not handled by Standard Page renderers a custom page renderer can be added via `page_renderer` [hook]

```py
# in hooks.py of your custom app

page_renderer = "path.to.your.custom_page_renderer.CustomPage"

```

A Page renderer class needs to have two methods i.e., `can_render` and `render`

Path resolver calls `can_render` to check if a renderer instance can render a particular path.
Once a renderer returns `True` from can_render, it will be that renderer class's responsibility to render the path.

**Note:** Custom page renderers get priority and it's `can_render` method will be called before [Standard Page Renderers](#page-renderer).

**Example:**
```py

from frappe.website.utils import build_response
from frappe.website.page_renderers.base_renderer import BaseRenderer

class CustomPage(BaseRenderer):
 def can_render(self):
 return True

 def render(self):
 response_html = "Custom Response"
 return self.build_response(response_html)

```
**Note:** You can also extend Standard Page Renderers to override or to use some standard functionalities.

<!-- page: framework/framework__user__en__python-api__search.md -->
---
title: "Search\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/python-api/search"
updated: "2026-02-17"
---


Searching in Frappe is managed by the [Search](https://github.com/frappe/frappe/blob/develop/frappe/search) module. It is a wrapper for [Whoosh](https://pypi.org/project/Whoosh/) a full text search library written in Python.

You can extend the `FullTextSearch` class to create a search class for a specific requirement. For example the [`WebsiteSearch`](https://github.com/frappe/frappe/blob/develop/frappe/search/website_search.py) is a wrapper for indexing public facing web pages and exposing a search.

## The `FullTextSearch` class

Each FullTextSearch (FTS) instance holds a Schema defined by the class itself. That means, a specific FTS implementation will have it's specific schema. You can create a new implementation if you wish to index with a different schema. Along with this the `FTS` class has other controllers to facilitate creating, updating and querying the index.

### Extending the FTS class

When initializing a FTS based class, you need to provide an index name. On instantiation, the following params are initialized
- `index_name`: name of the index provided.
- `index_path`: path of the index in the sites folder
- `schema`: return by the `get_schema` function
- `id`: id used to recognize the document in the index

Once instantiated you can run the `build` function. It gets all the documents from `get_items_to_index`, the documents are a list of `frappe._dict` (frappe dicts) conforming to the defined schema. These documents are then added to the index and written to the file.

You can search the index using the `search` method of the FTS class. These functions are documented in the API reference [here](/framework/v14/user/en/api/full-text-search).

An example implementation for blog will look like the following:

```python
class BlogWrapper(FullTextSearch):
 # Default Schema
 # def get_schema(self):
 # return Schema(name=ID(stored=True), content=TEXT(stored=True))

 # def get_id(self):
 # return "name"

 def get_items_to_index(self):
 docs = []
 for blog_name in get_all_blogs():
 docs.append(get_document_to_index(blog_name))
 return docs

 def get_document_to_index(self, name):
 blog = frappe.get_doc("Blog Post", name)
 return frappe._dict(name=name, content=blog.content)

 def parse_result(self, result):
 return result["name"]
```

- `get_items_to_index`: Get all routes to be indexed, this includes the static pages in www/ and routes from published documents
- `get_document_to_index`: Render a page and parse it using BeautifulSoup
- `parse_result`: all the search results are parsed using this function

<!-- page: framework/framework__user__en__rate-limiting.md -->
---
title: "Rate Limiting\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/rate-limiting"
updated: "2026-02-17"
---


Frappe framework has out of the box support for rate-limiting HTTP requests.

Frappe framework implements fixed window rate-limiting based on time consumed by requests. The limit is enforced on the sum of time taken by all HTTP requests made in the configured window. The cycle resets after every `window` seconds, for instance, setting `window` to 3600 seconds will reset the usage counter to 0 at the beginning of every hour based on site's timezone.

**Note:** Requests over limit are not processed and are sent HTTP `429` (Too Many Requests) response.

You can enable rate limiting on your site by adding configuration similar to the following in `site_config.json`:

```json
{
 "rate_limit": {
 "limit": 600,
 "window": 3600
 }
}
```

Key | Description
------- | -----------
`limit` | Maximum amount of time permitted to use in the rate limit window (in seconds).
`window` | Size of the rate limit window (in seconds).


The returned HTTP headers of every HTTP request show the current rate limit status, e.g.

```
curl -i https://frappe.io/docs
HTTP/1.1 200 OK
X-RateLimit-Limit: 600000000
X-RateLimit-Remaining: 518060453
X-RateLimit-Reset: 3513
X-RateLimit-Used: 100560
```

In case of requests made after configured limits are exhausted, HTTP `429` response is returned along with the rate limit status:

```
curl -i https://frappe.io/docs
HTTP/1.1 429 TOO MANY REQUESTS
X-RateLimit-Limit: 600000000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1242
Retry-After: 1242
```

Header | Description
--------------------- | -----------
Retry-After | Time remaining till the current rate limit window resets (in seconds).
X-RateLimit-Limit | Time permitted to use in a rate limit window (in microseconds).
X-RateLimit-Remaining | Time remaining (to be used) in the current rate limit window (in microseconds).
X-RateLimit-Reset | Time remaining till the current rate limit window resets (in seconds).
X-RateLimit-Used | Time used for processing the current request (in microseconds).

<!-- page: framework/framework__user__en__security-faqs.md -->
---
title: "Security FAQs"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/security-faqs"
updated: "2026-04-23"
---

This page contains some frequently asked questions related to security. Please review this before raising security issue with Frappe team.





### Frappe allows uploading malicious files like .EXE

Frappe is not an anti-virus, so it doesn't scan any kind of files that get uploaded. Frappe has inbuilt validation to block certain extensions and you can tweak this from "System Setting" > Files > Allowed File Extensions.

### Frappe shows complete traceback of error

Error traces help developers debug issues faster. In vast majority of the cases they do not reveal anything that isn't already available in our source code which is open source. If you still wish to disable tracebacks then go to "System Settings" and uncheck "Show Full Error and Allow Reporting of Issues to the Developer"

### Frappe doesn't encrypt the password when sending a request

Frappe recommends proper HTTPS (TLS) setup in production, if that is setup properly every request is encrypted at transport layer, so there is little security benefit from encrypted request content manually again on top of it.

If you're using a tool like Burp Suite to intercept an encrypted request by setting up a proxy/certificate that allows you to see unencrypted traffic then you're not really operating in real threat model. In real world, if TLS is compromised, you have much bigger problems.

In addition to this Frappe stores login password with PBKDF2 + SHA256 hash. Once stored, it's not possible to retrieve the passwords. Password fields that need value to be retrievable (e.g. API secrets) are stored with symmetric encryption using Fernet.

### Frappe enables "autocomplete" on password fields

Autocomplete + password managers are widely considered as better option for security and UX. Disabling autocomplete is outdated practice and major browsers don't even respect it if you disable it. Refer: <[https://developer.mozilla.org/en-US/docs/Web/Security/Securing_your_site/Turning_off_form_autocompletion#the_autocomplete_attribute_and_login_fields](https://developer.mozilla.org/en-US/docs/Web/Security/Securing_your_site/Turning_off_form_autocompletion#the_autocomplete_attribute_and_login_fields)>

### Frappe doesn't expire passwords every 30/90 days

Password rotation isn't necessarily secure and can even cause harmful side effects: <[https://www.sans.org/blog/time-for-password-expiration-to-die/](https://www.sans.org/blog/time-for-password-expiration-to-die/)>

If you still want this behaviour you can enable it from "System Settings" > "Force User to Reset Password"

### Frappe doesn't allow configuring password requirements to include upper, lowercase and special characters

Hard-coded requirements for passwords are generally bad UX. Password strength is largely based on entropy, see this comic for a good illustration of this: <[https://xkcd.com/936/](https://xkcd.com/936/)>

Frappe instead runs heuristics to compute password strength. By default we require a reasonably strong password, but if you want to increase this strength then you can configure it in "System Settings" > "Password" > " Minimum Password Score"

### Frappe sets cookie path to `/` which can allow other applications on same origin to use the cookie

Frappe doesn't allow configuring different applications on different paths. So this can't happen. By default, all pages on your configured domain/subdomain are served by Frappe.

### Frappe doesn't add "Secure" flag to cookies

Frappe adds a "Secure" flag to cookies only when it's accessed from the HTTPS scheme.

We recommend enabling HSTS on your domain so unencrypted traffic is blocked. <[https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)>

We allow non-HTTPS connections to support deployments in internal networks where users might not want to setup TLS.

### The site reveals that it's running on Frappe

It is trivial to figure out which application a site is running if you know application characteristics. E.g. preload headers, asset file names, and API paths. It's impossible to mask all of this information.

Even if we hide branding from UI, it won't take much time to figure out that a particular site is running on Frappe.

### Frappe allows adding links to external websites in comments

In a collaborative environment like Frappe, linking to external tools and resources is often a necessary part of the workflow, so disabling them completely isn't practical. To address the potential phishing risks, it is possible to display a warning modal before a user leaves the Desk. This feature can be enabled from "System Settings" > "Show External Link Warning".



### XSS in Print Formats or Developer Fields

Fields such as Print Formats, Custom Scripts, and other developer-focused HTML fields are intentionally designed to allow raw HTML/JavaScript for customization. These are only accessible to trusted users (e.g. System Managers/Developers), so rendering scripts in these contexts is expected behavior and not considered an XSS vulnerability. Reports of script execution in such fields are therefore invalid unless untrusted or low-privilege users can exploit them.

<!-- page: framework/framework__user__en__testing.md -->
---
title: "Testing"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/testing"
updated: "2026-05-10"
---


Frappe provides some basic tooling to write automated tests. There are some
basic rules:

1. Test can be anywhere in your repository but must begin with `test_` and
 should be a `.py` file.
1. The test runner will automatically build test records for dependent DocTypes
 identified by the `Link` type field (Foreign Key).
1. For non-DocType tests, you can write simple unit tests and prefix your file
 names with `test_`.


## Writing Tests

When you create a new DocType (in developer mode), the boilerplate files also
contain the `test_{doctype}.py` file. The test file should handle creating
dependencies and cleaning them up.

Here is a sample test file referred from `test_event.py`.

```py
import frappe
import unittest

def create_events():
 if frappe.flags.test_events_created:
 return

 frappe.set_user("Administrator")
 doc = frappe.get_doc({
 "doctype": "Event",
 "subject":"_Test Event 1",
 "starts_on": "2014-01-01",
 "event_type": "Public"
 }).insert()

 doc = frappe.get_doc({
 "doctype": "Event",
 "subject":"_Test Event 3",
 "starts_on": "2014-01-01",
 "event_type": "Public"
 "event_individuals": [{
 "person": "test1@example.com"
 }]
 }).insert()

 frappe.flags.test_events_created = True


class TestEvent(unittest.TestCase):
 def setUp(self):
 create_events()

 def tearDown(self):
 frappe.set_user("Administrator")

 def test_allowed_public(self):
 frappe.set_user("test1@example.com")
 doc = frappe.get_doc("Event", frappe.db.get_value("Event",
 {"subject":"_Test Event 1"}))
 self.assertTrue(frappe.has_permission("Event", doc=doc))

 def test_not_allowed_private(self):
 frappe.set_user("test1@example.com")
 doc = frappe.get_doc("Event", frappe.db.get_value("Event",
 {"subject":"_Test Event 2"}))
 self.assertFalse(frappe.has_permission("Event", doc=doc))
```


## Writing Tests for Commands

To write tests for your Bench commands, you can group your tests under a
Class that extends `BaseTestCommands` from `frappe.tests.test_commands` and
`unittest.TestCase` so that it runs during the `bench run-tests` command.

For reference, here is are some tests written for the `bench execute` command.

```py
class TestCommands(BaseTestCommands, unittest.TestCase):
 def test_execute(self):
 # test 1: execute a command expecting a numeric output
 self.execute("bench --site {site} execute frappe.db.get_database_size")
 self.assertEqual(self.returncode, 0)
 self.assertIsInstance(float(self.stdout), float)

 # test 2: execute a command expecting an errored output as local won't exist
 self.execute("bench --site {site} execute frappe.local.site")
 self.assertEqual(self.returncode, 1)
 self.assertIsNotNone(self.stderr)

 # test 3: execute a command with kwargs
 # Note:
 # terminal command has been escaped to avoid .format string replacement
 # The returned value has quotes which have been trimmed for the test
 self.execute("""bench --site {site} execute frappe.bold --kwargs '{{"text": "DocType"}}'""")
 self.assertEqual(self.returncode, 0)
 self.assertEqual(self.stdout[1:-1], frappe.bold(text='DocType'))
```

## Running Tests

Running tests could require additional dependencies specified by apps in their `dev-requirements.txt` file. Before running tests, make sure all apps have development dependencies installed using `bench setup requirements --dev`.

Run the following command to run all your tests. It will build all
the test dependencies once and run your tests. You should run tests from
`frappe_bench` folder.

```bash
# run all tests
bench --site [sitename] run-tests

# run tests for only frappe app
bench --site [sitename] run-tests --app frappe

# run tests for the Task doctype
bench --site [sitename] run-tests --doctype "Task"

# run tests for All doctypes in specified Module Def
bench --site [sitename] run-tests --module-def "Contacts"

# run a test using module path
bench --site [sitename] run-tests --module frappe.tests.test_api

# run a specific test from a test file
bench --site [sitename] run-tests --module frappe.tests.test_api --test test_insert_many

# run tests without creating test records
bench --site [sitename] run-tests --skip-test-records --doctype "Task"

# profile tests and show a report after tests execute
bench --site [sitename] run-tests --profile --doctype "Task"
.
----------------------------------------------------------------------
Ran 1 test in 0.010s

OK

9133 function calls (8912 primitive calls) in 0.011 seconds

Ordered by: cumulative time

ncalls tottime percall cumtime percall filename:lineno(function)
 2 0.000 0.000 0.008 0.004 /home/frappe/frappe-bench/apps/frappe/frappe/model/document.py:187(insert)
 1 0.000 0.000 0.003 0.003 /home/frappe/frappe-bench/apps/frappe/frappe/model/document.py:386(_validate)
 13 0.000 0.000 0.002 0.000 /home/frappe/frappe-bench/apps/frappe/frappe/database.py:77(sql)
 255 0.000 0.000 0.002 0.000 /home/frappe/frappe-bench/apps/frappe/frappe/model/base_document.py:91(get)
 12 0.000 0.000 0.002 0.000


# verbose log level for tests
bench --site [sitename] --verbose run-tests
```

## Checking if Tests are Running

You can check if your code is being executed as part of a test by evaluating the `frappe.in_test` global. On older framework versions, you can evaluate `frappe.flags.in_test` instead (this will be deprecated in an upcoming version).

You can use the global to add branching in your code based on whether tests are running or not. Example:

```py
if not frappe.in_test:
    notify_error_to_user()
```

## Running Tests Parallelly

As the number of tests grows in the project, it takes a long time for tests to complete if it runs serially on one machine.
Running tests in parallel across many test machines can save time in Continuous Integration (CI).

### Parallel Tests

**Command:**

```bash
bench --site [sitename] --app [app-name] run-parallel-tests --build-id &lt;build-number&gt; --total-build &lt;total-number-of-builds&gt;
```

**Usage:**

If you want to run tests across 2 CI instances your command will be as follows:

```bash
# in first CI instance
bench --site [sitename] run-parallel-tests --build-id 1 --total-builds 2

# in second CI instance
bench --site [sitename] run-parallel-tests --build-id 2 --total-builds 2
```

**Note:** The command will split all test files into 2 parts and execute them in those CI instances.
The first half of the test list will be executed in the first instance and the second half of the test list will be executed in the second instance.

### Parallel tests with orchestrator

It may happen that each test takes a different amount of time for completion which may result in imbalanced time across CI builds. To mitigate this you can use [test orchestrator](https://github.com/frappe/test-orchestrator) which runs the next test based on the availability of CI instance. The command to use the test orchestrator for the parallel test is as follows.

**Command:**

```bash
bench --site [sitename] --app [app-name] run-parallel-tests --use-orchestrator
```

**Usage:**

If you want to run tests across 2 CI instances your command will be as follows

```bash
# in first CI instance
bench --site [sitename] run-parallel-tests --use-orchestrator

# in second CI instance
bench --site [sitename] run-parallel-tests --use-orchestrator
```

**Note:** Environment variables `CI_BUILD_ID` and `ORCHESTRATOR_URL` are required for this command. `CI_BUILD_ID` is the unique ID that you get for each build run of CI.
`ORCHESTRATOR_URL` is the publicly accessible URL that you get after hosting the [orchestrator](https://github.com/frappe/test-orchestrator).

### Comparison

For clarity on how the above variants of parallel test commands may work check the following example.

Suppose there are 4 test files as follows

```sh
test_module_one.py 4 mins (execution time)
test_module_two.py 2 mins
test_module_three.py 1 min
test_module_four.py 1 min
```

Time required without parallel test command.

```sh
test_module_one.py 4 mins
test_module_two.py 2 mins
test_module_three.py 1 min
test_module_four.py 1 min
==============================
Total Wait Time 8 mins
```

Time required with the first command that auto splits test files across 2 test instances.

```sh
# First instance # Second instance
test_module_one.py 4 mins test_module_three.py 1 min
test_module_two.py 2 mins test_module_four.py 1 min
---------------------------- ----------------------------
 6 mins 2 mins

==============================
Total Wait Time 6 mins
```

It may happen that the time required with the second command that uses orchestrator which runs tests based on availability across 2 test instances.

```sh
# First instance # Second instance
test_module_one.py 4 mins test_module_two.py 2 mins
---------------------------- test_module_three.py 1 mins
 4 mins test_module_four.py 1 min
 ----------------------------
 4 mins
==============================
Total Wait Time 4 mins
```

**Note:** Only one test file is executed on the first instance because it is busy for 4 mins. By that time, the 2nd instance is able to execute other test files which help in balancing time across builds.
&lt;/total-number-of-builds&gt;&lt;/build-number&gt;

<!-- page: framework/framework__user__en__translations.md -->
---
title: "Translations\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/translations"
updated: "2026-02-17"
---


Frappe comes with a built-in translation system for capturing translatable strings
from code and extracting them into CSV files for different languages.

## How it works

Translations happen in three steps.

### 1. Extracting translatable strings

Many strings like field `label` and `description` that are easily parseable from
JSON files of DocTypes are automatically marked as translatable without any
explicit hint.

Other strings are extracted from source code files such as `.json`, `.js`,
`.py`. These are extracted only if they are marked explicitly by the author in
`_()` or `__()` methods.

For example:

```py
message = _("You don't have permissions to access this file")
```

### 2. Translating the extracted strings

Once we have a list of strings that we want to translate, they are put into CSV
files based on the language. Translations are primarily contributed by various
users of Frappe and ERPNext on the [translator portal](https://translate.erpnext.com).

The submitted translations are verified and then converted into a [Pull Request](https://github.com/frappe/frappe/pull/7805/files)
by a bot every week and merged into the core.

### 3. Translating strings in app

Translations are nothing but a key-value pair made of original string and it's
translation in a language. It might look like this:

```js
{
 "1 hour ago": "एक घंटे पहले",
 "1 minute ago": "1 मिनट पहले",
 "1 month": "1 महीना",
 "1 week": "1 सप्ताह",
 "1 year": "1 साल",
 "3 months": "3 महीने",
 "6 months": "6 महीने",
 "About": "के बारे में",
 "About Us Settings": "हमारे बारे में सेटिंग्स",
 "About Us Team Member": "हमारे बारे में टीम के सदस्य",
 "Academic Term": "शैक्षणिक शब्द",
 "Academic Year": "शैक्षणिक वर्ष",
 "Academics User": "अकादमिक उपयोगकर्ता",
 ...
}
```

When the string is written as `__('1 hour ago')` in the code, the `__` method
looks up the dictionary to find whether a translation exists for that string. If
yes, the translated string would be returned and it would show up.

This was an example of how translations work in JavaScript files, but the same
works in Python too.

## Tips on writing a valid translatable string

There are a few rules that need to be followed for the translation parser to
pick up the strings properly from code.

### 1. Literal strings

The string to be translated must always be a literal string, not a variable or
expression.

Example in Python

```py
# This will work
message = _('Document submitted successfully')
frappe.msgprint(message)

# This will also work
frappe.msgprint(_('Document submitted successfully'))

# This won't work
message = 'Document submitted successfully'
frappe.msgprint(_(message))
```

Example in JavaScript

```js
// This will work
message = __('Document submitted successfully')
frappe.msgprint(message)

// This won't work
message = 'Document submitted successfully'
frappe.msgprint(__(message))
```

### 2. Variables

If you have variables in your string, you must use the positional formatter
`{0}`, any other type of formatter won't work.

Example in Python

```py
# This is fine
_('Welcome {0}, get started with ERPNext in just a few clicks.').format(full_name)

# These are not
_('Welcome %s, get started with ERPNext in just a few clicks.' % full_name)

_('Welcome %(name)s, get started with ERPNext in just a few clicks.' % {'name': full_name})

# This one uses the positional formatter,
# but won't work because the string is formatted before it is passed to _()
_('Welcome {0}, get started with ERPNext in just a few clicks.'.format(full_name))
```

Example in JavaScript

```js
// This is fine
__('Welcome {0}, get started with ERPNext in just a few clicks.', [full_name])

// This is not
__(`Welcome ${full_name}, get started with ERPNext in just a few clicks.`)
```

### 3. Blocks

Don't split your string into separate blocks of strings and then concatenate
them. Don't write multiline strings. Always write your string in a single even
if the string is very large.

Example in Python

```py
# This is fine
_('You have {0} subscribers in your mailing list.').format(len(subscribers))

# Don't split strings
_('You have ') + len(subscribers) + _(' subscribers in your mailing list.')

# Don't write multiline strings
_('You have {0} subscribers \
 in your mailing list').format(len(subscribers))
```

Example in JavaScript

```js
// This is fine
__('You have {0} subscribers in your mailing list.', [subscribers.length])

// Don't split strings
__('You have ') + subscribers.length + __(' subscribers in your mailing list.')

// Don't write multiline strings
__('You have {0} subscribers' +
 'in your mailing list', [subscribers.length])
```

### 4. Plural

Don't try to pluralize words using logic. Every language has different plural
forms.

```py
# Don't do this
msg = _("You have {0} pending invoice").format(invoice_count)
if invoice_count > 1:
 msg += _("s")

# Write separate strings
# Every language has different plural forms
if invoice_count > 1:
 msg = _("You have {0} pending invoices").format(invoice_count)
else:
 msg = _("You have {0} pending invoice").format(invoice_count)
```

### 5. No Trailing Spaces

Don't start or end the sentence with spaces. Trailing spaces gets trimmed for other languages when passed through translation engine.

If you have to add space around your text, you can do it outside the translation syntax.

```py
# Don't do this
msg = _(" You have {0} pending invoice ")

# Do this
msg = ' ' + _("You have {0} pending invoices") + ' '
```

### 6. Adding context for a string

A translatable string can have different meaning in different context.
For example, string "Change" can mean "to make or become different" or "Coins".
So to tackle this issue `context` variable can be used to set the context for
a string so that it can be translated differently in different
language using [Translation Tool](https://docs.erpnext.com/docs/user/manual/en/translations).

In JavaScript

```js

__("Change", null, "Coins")

// Here "Coins" is the context for text "Change"
```

In Python

```py

_("Change", context="Switch")

# Here "Switch" is the context for text "Change"
```

## Adding a New Language

To add a new language, follow these steps:

#### Step 1: Export to a file

```sh
$ bench --site sitename get-untranslated [lang] [path-to-file]
```

#### Step 2: Translate

Create another file with updated translations (in the same order as the source
file). For this you can use the [Google Translator](https://translate.google.com/) or
[Bing Translator](http://www.bing.com/translator/).

#### Step 3: Import your translations

```sh
$ bench update-translations [lang] [source-path] [translated-path]
```

A new file will be created with the name `[lang].csv` in the `translations`
folder in each app.

#### Step 4: Update `languages.json`

Add your language in `frappe/geo/languages.json`

#### Step 5: Commit each app and push

Commit your changes with the `.csv` files in each app and push them to their
repositories.

<!-- page: framework/framework__user__en__tutorial__controller-methods.md -->
---
title: "Controller Methods"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/tutorial/controller-methods"
updated: "2026-02-17"
---

Controller methods allow you to write business logic during the lifecycle of a document.

Let's create our second doctype: **Library Member**. It will have the following fields:

1. First Name (Data, Mandatory)
2. Last Name (Data)
3. Full Name (Data, Read Only)
4. Email Address (Data)
5. Phone (Data)

![](/files/TqEJOjO.gif)

After you have created the doctype, go to Library Member list, clear the cache from **Settings > Reload** and create a new Library Member.

If you notice, the Full Name field is not shown in the form. This is because we set it as Read Only. It will be shown only when it has some value.

Let's write code in our python controller class such that Full Name is computed automatically from First Name and Last Name.

Open your code editor and open the file `library_member.py` and make the following changes:

**librarymember.py**

```
class LibraryMember(Document):
    #this method will run every time a document is saved
    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'
```

---

**NOTE**

If the above snippet doesn't work for you , make sure server side scripts are enabled, and then restart bench

```
bench set-config -g server_script_enabled true
```

---

We wrote the logic in the `before_save` method which runs every time a document is saved. This is one of the many hooks provided by the `Document` class. You can learn more about all the available hooks at [Controller](https://docs.frappe.io/framework/user/en/basics/doctypes/controllers) docs.

Now, go back and create another Library Member and see the Full Name show up after save.

Next: [Types of DocType](/framework/v14/user/en/tutorial/types-of-doctype)

<!-- page: framework/framework__user__en__tutorial__create-a-doctype.md -->
---
title: "Create a DocType"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/tutorial/create-a-doctype"
updated: "2026-04-14"
---

DocType is analogous to a Model in other frameworks. Apart from defining properties, it also defines the behavior of the Model.

## Enable Developer Mode

Before we can create DocTypes, we need to enable developer mode on our bench. This will enable boilerplate creation when we create doctypes and we can track them into version control with our app.

Go to your terminal and quit the bench server if it's already running then from the `frappe-bench` directory, run the following command:

```
bench set-config -g developer_mode true
bench start
```

## Creating a DocType

While in Desk, navigate to the **DocType List** using the [Awesomebar](/framework/user/en/desk#awesomebar). This list will include DocTypes bundled with the framework, those that are a part of the installed Frappe apps and custom ones, which you can create specific to each site.

The first doctype we will create is **Article**. To create it, click on New.

1. Enter Name as Article
2. Select Library Management in Module
3. Add the following fields in the Fields table:
  1. Article Name (Data, Mandatory)
  2. Image (Attach Image)
  3. Author (Data)
  4. Description (Text Editor)
  5. ISBN (Data)
  6. Status (Select) - Enter two options: Issued and Available (Type Issued, hit enter, then type Available)
  7. Publisher (Data)

Refer the following GIF to check how it should be done:

![Article DocType](/files/article-doctype.gif)



After adding the fields, click on Save.

You will see a **Go to Article List** button at the top right of the form. Click on it to go to the Article List. Here you will see a blank list with no records because the table has no records.

Let's create some records. But before that, we need to clear the Desk cache. Click on the **Settings** dropdown on the right side of the navbar and click on **Reload**.

Now, you should see the **New** button. Click on it and you will see the Form view of the Article doctype. Fill in the form and click on Save. You have created your first Article document. Go back to the list view and you should see one record.

![Article New Form](/files/article-new-form.gif)



### What happened when you created the Article DocType?

**1. Database Table**

A database table with the name `tabArticle` was created with the fields we specified in the fields table. You can confirm this by checking it from the MariaDB console

```
bench --site library.localhost mariadb
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 2445938
Server version: 10.4.13-MariaDB Homebrew

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [_ad03fa1a016ca1c4]> desc tabArticle;
+--------------+--------------+------+-----+-----------+-------+
| Field        | Type         | Null | Key | Default   | Extra |
+--------------+--------------+------+-----+-----------+-------+
| name         | varchar(140) | NO   | PRI | NULL      |       |
| creation     | datetime(6)  | YES  |     | NULL      |       |
| modified     | datetime(6)  | YES  | MUL | NULL      |       |
| modified_by  | varchar(140) | YES  |     | NULL      |       |
| owner        | varchar(140) | YES  |     | NULL      |       |
| docstatus    | int(1)       | NO   |     | 0         |       |
| parent       | varchar(140) | YES  | MUL | NULL      |       |
| parentfield  | varchar(140) | YES  |     | NULL      |       |
| parenttype   | varchar(140) | YES  |     | NULL      |       |
| idx          | int(8)       | NO   |     | 0         |       |
| article_name | varchar(140) | YES  |     | NULL      |       |
| image        | text         | YES  |     | NULL      |       |
| author       | varchar(140) | YES  |     | NULL      |       |
| description  | longtext     | YES  |     | NULL      |       |
| isbn         | varchar(140) | YES  |     | NULL      |       |
| status       | varchar(140) | YES  |     | Available |       |
| publisher    | varchar(140) | YES  |     | NULL      |       |
| _user_tags   | text         | YES  |     | NULL      |       |
| _comments    | text         | YES  |     | NULL      |       |
| _assign      | text         | YES  |     | NULL      |       |
| _liked_by    | text         | YES  |     | NULL      |       |
+--------------+--------------+------+-----+-----------+-------+
21 rows in set (0.002 sec)

MariaDB [_ad03fa1a016ca1c4]>
```

The fields we specified in Title Case were converted to snake case automatically, and are used as the column names in the table. For e.g., `article_name`, `image`, `author` , and `description`.

However, many other fields were created like `name`, `creation`, `modified`, `modified_by` . These are standard fields created for all doctypes. `name` is the primary key column.

If you created a record with the Form, you can also run a standard select query to get the rows.

```
MariaDB [_ad03fa1a016ca1c4]> select * from tabArticle;
+------------+----------------------------+----------------------------+---------------+---------------+-----------+--------+-------------+------------+-----+-----------------------------+--
| name       | creation                   | modified                   | modified_by   | owner         | docstatus | parent | parentfield | parenttype | idx | article_name                | i
+------------+----------------------------+----------------------------+---------------+---------------+-----------+--------+-------------+------------+-----+-----------------------------+--
| bd514646b9 | 2020-10-10 16:24:43.033457 | 2020-10-10 16:24:43.033457 | Administrator | Administrator |         0 | NULL   | NULL        | NULL       |   0 | The Girl with all the Gifts | N
+------------+----------------------------+----------------------------+---------------+---------------+-----------+--------+-------------+------------+-----+-----------------------------+--

MariaDB [_ad03fa1a016ca1c4]>
```

**2. Desk Views**

There are a number of views that were also created for our DocType. The Article List is the list view that shows the records from the database table. The Form view is the view that is shown when you want to create a new document or view an existing one.

**3. Form Layout**

If you notice, the layout of fields in the form is according to how you ordered them in the Fields table. For e.g., Article Name is the first field followed by Image which is followed by Author. In later parts of the tutorial we will learn how to customize this further.

**4. Boilerplate code**



---

**NOTE**

Make sure you uncheck the 'Custom?' checkbox in the doctype configuration. Otherwise the files discussed below won't be generated. An explaination for this is given [here](https://discuss.erpnext.com/t/whats-the-difference-between-customize-form-vs-custom-doctype/42676/2)



---

If you look at the changes in your app, you should find a number of files that were created. Go to your terminal and from the `frappe-bench` directory run the following commands.

```
$ cd apps/library_management
$ git status -u
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
    library_management/library_management/doctype/__init__.py
    library_management/library_management/doctype/article/__init__.py
    library_management/library_management/doctype/article/article.js
    library_management/library_management/doctype/article/article.json
    library_management/library_management/doctype/article/article.py
    library_management/library_management/doctype/article/test_article.py

nothing added to commit but untracked files present (use "git add" to track)
  

```

**article.json** - JSON file that defines the doctype attributes

**article.js** - Client-side controller for the Form view

**article.py** - Python controller for Article

**test_article.py** - Python Unit Test boilerplate for writing tests

As you can see, a DocType describes a lot of things about the model. Not only does it define the table and column names but also how it will be rendered in various views in the Desk.

Good job following the tutorial so far. Let's keep going!

Next: [DocType Features](/framework/user/en/tutorial/doctype-features) 

<!-- page: framework/framework__user__en__tutorial__create-a-site.md -->
---
title: "Create a Site"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/tutorial/create-a-site"
updated: "2026-05-06"
---

Each site comes with a database. They may be customized through site specific scripting or Apps may be installed on them.

## Create a new site

To create a new site, run the following command from the `frappe-bench` directory:

```
$ bench new-site library.localhost
MySQL root password:

Installing frappe...
Updating DocTypes for frappe        : [========================================] 100%
Set Administrator password:
*** Scheduler is disabled ***
Current Site set to library.localhost
```

This command will create a new database, so you need to enter your MariaDB root password. It will also ask to set the password for the Administrator user, just set a password that you won't forget. This will be useful later.

Now, you will have a new folder named `library.localhost` in the `sites` directory.

If site creation fails for any reason, you'll be prompted to roll back the changes. This will delete the `library.localhost` or equivalent in your sites directory, and delete the database/user that was created. This will allow you to easily retry without having to manually cleanup the unusable site.

## Site Directory Structure

The site directory structure will look something like this:

```
sites/library.localhost
├── indexes
│   └── web_routes
├── locks
├── logs
├── private
│   ├── backups
│   └── files
├── public
│   └── files
└── site_config.json
```

The `indexes` folder has indexes generated via Website Search.

The `locks` folder maintains file based locks over in-site documents as well as indicators of the state of the site itself.

As you can see, the `private` folder will contain any database backups and private files. Private files are user uploaded files that need authentication to be accessible.

The `public` folder will contain files that are accessible without authentication. This can contain website images that should be accessible without login.

The `site_config.json` file contains configuration that is specific to this site which should not be version controlled. This is similar to an environment variables file. If you look at the contents of the file, it contains the database configuration values for this site.

```
{
 "db_name": "_ad03fa1a016ca1c4",
 "db_password": "pz1d2gN5y35ydRO5",
 "db_type": "mariadb"
}
```

## Access site in your browser

`bench` allows you to create multiple sites and access them separately in the browser on the same port. This is what we call multi-tenancy support in bench.

Frappe will identify which site to serve by matching the hostname of the request with the site name, so you should be able to access your site on [http://library.localhost:8000](http://library.localhost:8000)

If your site name doesn't end with `.localhost`, this will not work directly for you, because you have to tell your operating system that site_name should point to localhost. To do that, you can add the following entry to your `/etc/hosts` file.

```
127.0.0.1 site_name
```

This will map `library.localhost` to `localhost`. Bench has a convenient command to do just that.

```
$ bench --site site_name add-to-hosts
```

This will ask for your root password and will add an entry to your `/etc/hosts` file.

![Site Login Page](/files/site-login-page.png)

Great, now you can access your site at `http://library.localhost:8000`. Congratulations for making it this far.

## Install app on site

To install our Library Management app on our site, run the following command:

```
$ bench --site library.localhost install-app library_management

Installing library_management...
```

To confirm if the app was installed, run the following command:

```
$ bench --site library.localhost list-apps
frappe
library_management
```

You should see `frappe` and `library_management` as installed apps on your site.

> When you create a new site, the `frappe` app is installed by default.

## Login to Desk

> Before proceeding with below make sure that the site is in developer mode. To ensure that run below command in your site 
>
> ```
> bench set-config -g developer_mode 1
> ```
>
> Then restart the bench using `bench start` command

  
To create DocTypes in our app, we must log in to Desk. Go to [http://library.localhost:8000](http://library.localhost:8000) and it should show you a login page.

Enter Administrator as the user and password that you set while creating the site.

![Setup Wizard](/files/setup-wizard.png)

After successful login, you will see the setup wizard. This is a one-time setup wizard used to set up localization details for your site. Go ahead, select your language, and complete the wizard.

Good job making it this far!

You should see the Desk that looks something like this:

![Desk](/files/desk.png)

## Site commands

We ran a couple of bench commands with the `--site` option. These commands are called site commands.

Here are some of the useful site commands.

**Python Console**

```
# access the python console
$ bench --site library.localhost console
Apps in this namespace:
frappe, library_management

In [1]:  

```

**MariaDB Console**

```
# access the mariadb console
$ bench --site library.localhost mariadb
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 2333498
Server version: 10.4.13-MariaDB Homebrew

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [_ad03fa1a016ca1c4]>  

```

**Database Backup**

```
$ bench --site library.localhost backup
Backup Summary for library.localhost at 2020-10-06 23:21:17.277960
Config  : ./library.localhost/private/backups/20201006_232116-library_test-site_config_backup.json   94.0B
Database: ./library.localhost/private/backups/20201006_232116-library_test-database.sql.gz           217.4KiB
Backup for Site library.localhost has been successfully completed
  
```

You can see a list of all site commands by running the following command:

```
$ bench --help
Usage: bench frappe [OPTIONS] COMMAND [ARGS]...

Options:
  --site TEXT
  --profile Profile
  --verbose Verbose
  --force Force
  --help Show this message and exit.

Commands:
  add-system-manager          Add a new system manager to a site
  add-to-email-queue          Add an email to the Email Queue
  add-to-hosts                Add site to hosts
  backup                      Backup
  browse                      Opens the site on web browser
  build                       Minify + concatenate JS and CSS files, build...
  build-message-files         Build message files for translation
  build-search-index
  bulk-rename                 Rename multiple records via CSV file
  clear-cache                 Clear cache, doctype cache and defaults
  clear-website-cache         Clear website cache
  console                     Start ipython console for a site
  data-import                 Import documents in bulk from CSV or XLSX...
  destroy-all-sessions        Clear sessions of all users (logs them out) 

```

Next: Create a DocType

<!-- page: framework/framework__user__en__tutorial__create-an-app.md -->
---
title: "Create an App"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/tutorial/create-an-app"
updated: "2026-02-17"
---

Create a Frappe app scaffold using the bench CLI.

Create app
----------

Before we start, make sure you're in a bench directory. To confirm, run `bench find .`:


```
$ bench find .
/home/frappe/frappe-bench is a bench directory!
  

```
To create our Library Management app, run the `new-app` command:


```
bench new-app library_management
```

You should get some prompts, and output like the following. You can enter information manually, or press enter to select the defaults

```
App Title (default: Library Management):
App Description: Library Management System
App Publisher: Faris Ansari
App Email: faris@example.com
App Icon (default 'octicon octicon-file-directory'):
App Color (default 'grey'):
App License (default 'MIT'):
'library_management' created at /home/frappe/frappe-bench/apps/library_management

Installing library_management
$ ./env/bin/pip install -q -U -e ./apps/library_management
$ bench build --app library_management
yarn run v1.22.4
$ FRAPPE_ENV=production node rollup/build.js --app library_management
Production mode
✔ Built js/moment-bundle.min.js
✔ Built js/libs.min.js
✨  Done in 1.95s.
```

You will be prompted with details of your app, fill them up and an app named `library_management` will be created in the `apps` folder.

To see a complete list of all icons supported in the octicons library, check out <https://primer.style/octicons/>

App directory structure
-----------------------

Your app directory structure should look something like this:


```
apps/library_management
├── README.md
├── library_management
│   ├── hooks.py
│   ├── library_management
│ │ └── __init__.py
│ ├── modules.txt
│ ├── patches.txt
│ ├── public
│ │ ├── css
│ │ └── js
│ ├── templates
│ │ ├── __init__.py
│ │ ├── includes
│ │ └── pages
│ │ └── __init__.py
│ └── www
└── pyproject.toml
  

```
* **library_management:** This directory will contain all the source code for your app


	+ **public**: Store static files that will be served from Nginx in production
	+ **templates**: Jinja templates used to render web views
	+ **www**: Web pages that are served based on their directory path
	+ **library_management:** Default Module bootstrapped with app
	+ **modules.txt:** List of modules defined in the app
	+ **patches.txt**: Patch entries for database migrations
	+ **hooks.py**: Hooks used to extend or intercept standard functionality provided by the framework
	+ **pyproject.toml:** Specifies how your app is built, you can optionally add 3rd party Python dependencies here which will get installed when your app is installed.

Next: [Create a Site](/framework/user/en/tutorial/create-a-site)

<!-- page: framework/framework__user__en__tutorial__doctype-features.md -->
---
title: "DocType Features\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/tutorial/doctype-features"
updated: "2026-02-17"
---

In the previous chapter, we created the Article doctype. Let's see what other features we can customize.

Naming
------

If you created a document with the Form, you might have noticed that the `name` value of the document was a randomly generated hash. Let's make a change so that the Article Name we provide becomes the `name` of the document.

To do that, open the doctype list from the search bar and click on Article. Now, scroll down to the Naming section and in the Auto Name field enter **field:article_name**. Click on Save.

Now, go back to the Article List and create a new article again.

![](/files/nTqBymM.gif)

 

Now, the **name** of the document will be the Article Name and it must be unique across Articles. So you cannot create another article with the same name.

You can also check the database records by running a select query in the mariadb console.

```
MariaDB [_ad03fa1a016ca1c4]> select * from tabArticle;

| ------------ | ---------------------------- | ---------------------------- | --------------- | --------------- | ----------- | -------- | ------- |
| name | creation | modified | modified_by | owner | docstatus | parent | parent
| ------------ | ---------------------------- | ---------------------------- | --------------- | --------------- | ----------- | -------- | ------- |
| bd514646b9 | 2020-10-10 16:24:43.033457 | 2020-10-10 16:24:43.033457 | Administrator | Administrator | 0 | NULL | NULL
| Catch 22 | 2020-10-10 16:41:49.734499 | 2020-10-10 16:41:49.734499 | Administrator | Administrator | 0 | NULL | NULL
| ------------ | ---------------------------- | ---------------------------- | --------------- | --------------- | ----------- | -------- | ------- |

```

> Learn more about various types of [DocType Naming](/framework/v14/user/en/basics/doctypes/naming).

Form Layout
-----------

Let's customize the layout of how the fields are laid out in the form while making good use of the available space. Go to the Article doctype, scroll to the Fields section, and add two new fields of type **Column Break** and **Section Break**. We will also hide the Image field as it is not needed to be shown in the form. Check out the GIF to see it in action.

![](/files/XqlAtTg.gif)

Form Settings

Go to the Article doctype and scroll down to the **Form Settings** section. Enter **image** in the Image Field. This will show the image at the left top of the form. You can also enable **Allow Rename** to allow renaming of documents.

 

![](/files/QRZDdTG.gif)

Permissions
-----------

You can also configure what roles you want to allow and which actions you want to restrict for a DocType. Go to the Article doctype, scroll down to the **Permission Rules** section, and add the roles.

You can also configure the type of action that is allowed for a particular role. Let's add a **Librarian** role that has permission for all actions and a **Library Member** role that has permission for **Read** action.

![](/files/UOan9ER.gif)

You can test this by creating a new User that has the **Librarian** role, and another User that has the **Library Member** role. Login with each user, and see what actions are allowed.

Next: [Controller Methods](/framework/v14/user/en/tutorial/controller-methods)

<!-- page: framework/framework__user__en__tutorial__form-scripts.md -->
---
title: "Form Scripts"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/tutorial/form-scripts"
updated: "2026-02-17"
---

Form Scripts are client-side javascript code that enhances the UX of your Forms.


Let's say you want to create a membership for a member. To do this, you have to
go to the Library Membership list, create a new form, select the member and
other fields and then save.

Similarly, when you want to create a transaction against a member, you have to
make a new Library Transaction form.

We can make this process easier. Write the following code in **library_member.js**

```js
frappe.ui.form.on('Library Member', {
 refresh: function(frm) {
 frm.add_custom_button('Create Membership', () => {
 frappe.new_doc('Library Membership', {
 library_member: frm.doc.name
 })
 })
 frm.add_custom_button('Create Transaction', () => {
 frappe.new_doc('Library Transaction', {
 library_member: frm.doc.name
 })
 })
 }
});
```

Now, refresh your page and go to the Library Member form. You should see two buttons
on the top right. Click on them to try them out. They will automatically set the
Library Member in each of those documents making the process easier.

![Library Member Form Actions](/files/library-member-form-actions.png)

We have only scratched the surface here. You can do a lot more with Form
Scripts. Learn more about the API at [Form Scripts
API](/framework/v14/user/en/api/form).

Next: [Portal Pages](/framework/v14/user/en/tutorial/portal-pages)

<!-- page: framework/framework__user__en__tutorial__install-and-setup-bench.md -->
---
title: "Install and Setup Bench"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/tutorial/install-and-setup-bench"
updated: "2026-02-17"
---

Bench is the command line tool to manage Frappe apps and sites.

Installation
------------

If you haven't installed Bench, follow the [Installation](/framework/user/en/installation) guide. After installation, you should be able to run commands that start with `bench`.

Run the following command to test your installation:


```
$ bench --version
5.1.0
```
Create the frappe-bench directory
---------------------------------

Let's create our project folder which will contain our apps and sites. Run the following command:


```
$ bench init frappe-bench
```
This will create a directory named `frappe-bench` in your current working directory. It will do the following:

1. Create a python virtual environment under `env` directory.
2. Fetch and install the `frappe` app as a python package.
3. Install node modules of `frappe`.
4. Build static assets.

Directory Structure
-------------------


```
.
├── Procfile
├── apps
│   └── frappe
├── config
│   ├── pids
│   ├── redis_cache.conf
│   ├── redis_queue.conf
│   └── redis_socketio.conf
├── env
│   ├── bin
│   ├── include
│   ├── lib
│   └── share
├── logs
│   ├── backup.log
│   └── bench.log
└── sites
    ├── apps.txt
    ├── assets
    └── common_site_config.json
```
* **env**: Python virtual environment
* **config**: Config files for Redis and Nginx
* **logs**: Log files for every process (web, worker)
* **sites:** Sites directory


	+ **assets:** Static assets that served via Nginx in production
	+ **apps.txt:** List of installed frappe apps
	+ **common_site_config.json:** Site config that is available in all sites
* **apps:** Apps directory


	+ **frappe:** The Frappe app directory
* **Procfile:** List of processes that run in development

Start the Bench Server
----------------------

Now that we have created our `frappe-bench` directory, we can start the Frappe web server by running the following command:


```
$ cd frappe-bench
$ bench start
18:16:36 system | redis_cache.1 started (pid=11231)
18:16:36 system | redis_socketio.1 started (pid=11233)
18:16:36 system | redis_queue.1 started (pid=11234)
18:16:36 system | socketio.1 started (pid=11236)
18:16:36 system | web.1 started (pid=11237)
18:16:36 system | watch.1 started (pid=11240)
18:16:36 system | schedule.1 started (pid=11241)
18:16:36 system | worker_short.1 started (pid=11242)
18:16:36 redis_queue.1 | 11234:C 10 Jul 2020 18:16:36.320 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
18:16:36 redis_queue.1 | 11234:C 10 Jul 2020 18:16:36.320 # Redis version=6.0.5, bits=64, commit=00000000, modified=0, pid=11234, just started
18:16:36 redis_queue.1 | 11234:C 10 Jul 2020 18:16:36.320 # Configuration loaded
18:16:36 system | worker_long.1 started (pid=11244)
18:16:36 redis_cache.1 | 11231:C 10 Jul 2020 18:16:36.318 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
18:16:36 redis_cache.1 | 11231:C 10 Jul 2020 18:16:36.318 # Redis version=6.0.5, bits=64, commit=00000000, modified=0, pid=11231, just started
18:16:36 redis_cache.1 | 11231:C 10 Jul 2020 18:16:36.318 # Configuration loaded
18:16:36 redis_cache.1 | 11231:M 10 Jul 2020 18:16:36.320 * Increased maximum number of open files to 10032 (it was originally set to 256).
18:16:36 redis_queue.1 | 11234:M 10 Jul 2020 18:16:36.325 * Increased maximum number of open files to 10032 (it was originally set to 256).
18:16:36 system | worker_default.1 started (pid=11245)
18:16:36 redis_cache.1 | 11231:M 10 Jul 2020 18:16:36.337 * Running mode=standalone, port=13000.
18:16:36 redis_cache.1 | 11231:M 10 Jul 2020 18:16:36.337 # Server initialized
18:16:36 redis_cache.1 | 11231:M 10 Jul 2020 18:16:36.337 * Ready to accept connections
18:16:36 redis_queue.1 | 11234:M 10 Jul 2020 18:16:36.367 * Running mode=standalone, port=11000.
18:16:36 redis_queue.1 | 11234:M 10 Jul 2020 18:16:36.367 # Server initialized
18:16:36 redis_queue.1 | 11234:M 10 Jul 2020 18:16:36.367 * Ready to accept connections
18:16:36 redis_socketio.1 | 11233:C 10 Jul 2020 18:16:36.359 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
18:16:36 redis_socketio.1 | 11233:C 10 Jul 2020 18:16:36.359 # Redis version=6.0.5, bits=64, commit=00000000, modified=0, pid=11233, just started
18:16:36 redis_socketio.1 | 11233:C 10 Jul 2020 18:16:36.359 # Configuration loaded
18:16:36 redis_socketio.1 | 11233:M 10 Jul 2020 18:16:36.374 * Increased maximum number of open files to 10032 (it was originally set to 256).
18:16:36 redis_socketio.1 | 11233:M 10 Jul 2020 18:16:36.417 * Running mode=standalone, port=12000.
18:16:36 redis_socketio.1 | 11233:M 10 Jul 2020 18:16:36.418 # Server initialized
18:16:36 redis_socketio.1 | 11233:M 10 Jul 2020 18:16:36.418 * Ready to accept connections
18:16:37 socketio.1 | listening on *: 9000
18:16:41 web.1 | * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
18:16:41 web.1 | * Restarting with fsevents reloader
18:16:41 watch.1 | yarn run v1.22.4
18:16:41 watch.1 | $ node rollup/watch.js
18:16:42 watch.1 |
18:16:42 watch.1 | Rollup Watcher Started
18:16:42 watch.1 |
18:16:42 watch.1 | Watching...
18:16:42 web.1 | * Debugger is active!
18:16:42 web.1 | * Debugger PIN: 100-672-925
18:16:43 watch.1 | Rebuilding frappe-web-b4.css
18:16:44 watch.1 | Rebuilding frappe-chat-web.css
18:16:44 watch.1 | Rebuilding chat.js
18:16:45 watch.1 | Rebuilding frappe-recorder.min.js
18:16:48 watch.1 | Rebuilding checkout.min.js
18:16:48 watch.1 | Rebuilding frappe-web.min.js
18:16:51 watch.1 | Rebuilding bootstrap-4-web.min.js
18:16:52 watch.1 | Rebuilding control.min.js
18:16:54 watch.1 | Rebuilding dialog.min.js
18:16:57 watch.1 | Rebuilding desk.min.css
18:16:57 watch.1 | Rebuilding frappe-rtl.css
18:16:58 watch.1 | Rebuilding printview.css
18:16:58 watch.1 | Rebuilding desk.min.js
18:17:04 watch.1 | Rebuilding form.min.css
18:17:04 watch.1 | Rebuilding form.min.js
18:17:07 watch.1 | Rebuilding list.min.css
18:17:07 watch.1 | Rebuilding list.min.js
18:17:09 watch.1 | Rebuilding report.min.css
18:17:09 watch.1 | Rebuilding report.min.js
18:17:12 watch.1 | Rebuilding web_form.min.js
18:17:12 watch.1 | Rebuilding web_form.css
18:17:13 watch.1 | Rebuilding email.css
18:17:13 watch.1 | Rebuilding social.min.js
18:17:13 watch.1 | Rebuilding barcode_scanner.min.js
18:17:15 watch.1 | Rebuilding data_import_tools.min.js
  

```
This will start several processes including a Python web server based on Gunicorn, redis servers for caching, job queuing and socketio pub-sub, background workers, node server for socketio and a node server for compiling JS/CSS files.

The web server will start listening on the port `8000` but we don't have any sites yet to serve. Our next step is to create our app and create a site that will have this app installed.

Make sure not to close the terminal where `bench start` is running. To run bench commands, create another terminal and cd into the `frappe-bench` directory.

Good job on following the tutorial so far!

Next: [Create an App](/framework/user/en/tutorial/create-an-app)

<!-- page: framework/framework__user__en__tutorial__types-of-doctype.md -->
---
title: "Types of DocType\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/tutorial/types-of-doctype"
updated: "2026-02-17"
---


Let's learn about the different types of doctype in the framework by creating
more doctypes.

## Library Membership

Let's create another doctype: **Library Membership**. It will have the following
fields:

1. Library Member (Link, Mandatory)
2. Full Name (Data, Read Only)
3. From Date (Date)
4. To Date (Date)
5. Paid (Check)

It will have **Is Submittable** enabled. It will have Naming set as
**LMS.#####** and restricted to **Librarian** role. Also, the Title Field should
be set to `full_name` in the View Settings section.

![Library Membership DocType](/files/library-membership-doctype.gif)

The Link field **Library Member** is similar to a Foreign Key column in other
frameworks. It will let you link the value to a record in another DocType. In
this case, it links to a record of Library Member DocType.

The Full Name field is a Read Only field that will be automatically **fetched
from** from the `full_name` field in the linked record **Library Member**.

Now, go to the Library Membership list and create a new document. You will see
that the Library Member field is a dropdown with existing records shown as
options. Select a Library Member and the Full Name will be fetched
automatically. Pretty cool, right?

### Linked DocTypes

Linked DocTypes are DocTypes that are linked in other doctypes as Link fields.
All doctypes are linkable. We can classify doctypes broadly into Master and
Transactional based on the type of data they store. Article, Library Member are
examples of Master data because they represent an entity (physical or virtual).
Library Membership is an example of doctype which stores transactional data.

### Submittable DocTypes

When you enable **Is Submittable** in a DocType is becomes a Submittable
DocType. A Submittable doctype can have 3 states: **Draft**, **Submitted** and
**Cancelled**. A document in the **Draft** state can be changed like any
document, however once it is in **Submitted** state, the value of any field in
the document cannot be changed. A Submitted document can be **Cancelled**, which
makes the document invalid. If you notice, an extra field was added in our
Library Membership doctype called **Amended From**. This field is used to keep
track of amendments in documents. Once a document is Cancelled, it can only be
amended, which means it can be duplicated and the cancelled document will be
linked to the new amended document via the **Amended From** field.

### Controller Validation for Membership

Now, let's write code that will make sure whenever a Library Membership is
created, there is no active membership for the Member.

**library_membership.py**

```py
import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryMembership(Document):
    # check before submitting this document
    def before_submit(self):
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                # check if the membership's end date is later than this membership's start date
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active membership for this member")
```

We wrote our logic in the `before_submit` method which will run before we submit
the document. We used the `frappe.db.exists` method to check if a Library
Membership record exists with our provided filters. If it exists, we used
`frappe.throw` to stop the execution of program with a message that will show up
letting the user know the reason.

Now, try creating a Library Membership with an overlapping period and you should
see an error when you submit the document.

![Library Membership Validation](/files/library-membership-validation.png)

## Library Transaction

Let's create a DocType to record an Issue or Return of an Article by a Library
Member who has an active membership.

This doctype will be called **Library Transaction** and will have the following
fields:

1. Article - Link to Article
2. Library Member - Link to Library Member
3. Type - Select with 2 options: Issue and Return
4. Date - Date of Transaction

This doctype will also be a Submittable doctype.

![Library Transaction Doctype](/files/library-transaction-doctype.gif)

### Validation for Transaction

When an Article is issued, we should verify whether the Library Member has an
active membership. We should also check whether the Article is available for
Issue. Let's write the code for these validations.

**library_transaction.py**

```py
import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryTransaction(Document):
    def before_submit(self):
        if self.type == "Issue":
            self.validate_issue()
            # set the article status to be Issued
            article = frappe.get_doc("Article", self.article)
            article.status = "Issued"
            article.save()

        elif self.type == "Return":
            self.validate_return()
            # set the article status to be Available
            article = frappe.get_doc("Article", self.article)
            article.status = "Available"
            article.save()

    def validate_issue(self):
        self.validate_membership()
        article = frappe.get_doc("Article", self.article)
        # article cannot be issued if it is already issued
        if article.status == "Issued":
            frappe.throw("Article is already issued by another member")

    def validate_return(self):
        article = frappe.get_doc("Article", self.article)
        # article cannot be returned if it is not issued first
        if article.status == "Available":
            frappe.throw("Article cannot be returned without being issued first")

    def validate_membership(self):
        # check if a valid membership exist for this library member
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                "from_date": ("<", self.date),
                "to_date": (">", self.date),
            },
        )
        if not valid_membership:
            frappe.throw("The member does not have a valid membership")

```

There is a lot of code here but it should be self explanatory. There are inline
code comments for more explanation.

## Library Settings

Let's create the last doctype for our app: **Library Settings**. It will have
the following fields:

1. Loan Period - Will define the loan period in number of days
2. Maximum Number of Issued Articles - Restrict the maximum number of articles that can be issued by a single member

Since we don't need to have multiple records for these settings, we will enable
**Is Single** for this doctype.

![Library Settings Doctype](/files/library-settings-doctype.gif)

After creating the doctype, click on **Go to Library Settings**, to go to the
form and set the values for **Loan Period** and **Maximum Number of Issued
Articles**.

### Single DocTypes

When a DocType has **Is Single** enabled, it will become a Single DocType. A
single doctype is similar to singleton records in other frameworks. It does not
create a new database table. Instead all single values are stored in a single
table called `tabSingles`. It is used usually for storing global settings.

### Validation for Library Settings

Let's make the change in Library Membership such that, the To Date automatically
computed based on the Loan Period and the From Date.

**library_membership.py**

```py
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

import frappe


class LibraryMembership(Document):
    # check before submitting this document
    def before_submit(self):
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                # check if the membership's end date is later than this membership's start date
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active membership for this member")

        # get loan period and compute to_date by adding loan_period to from_date
        loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
        self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)
```

We have used `frappe.db.get_single_value` method to get the value of
`loan_period` from the Library Settings doctype.

Now, let's make the change in Library Transaction such that when an Article is
Issued, it checks whether the maximum limit is reached.

**library_transaction.py**

```py
import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryTransaction(Document):
    def before_submit(self):
        if self.type == "Issue":
            self.validate_issue()
            self.validate_maximum_limit()
            # set the article status to be Issued
            article = frappe.get_doc("Article", self.article)
            article.status = "Issued"
            article.save()

        elif self.type == "Return":
            self.validate_return()
            # set the article status to be Available
            article = frappe.get_doc("Article", self.article)
            article.status = "Available"
            article.save()

    def validate_issue(self):
        self.validate_membership()
        article = frappe.get_doc("Article", self.article)
        # article cannot be issued if it is already issued
        if article.status == "Issued":
            frappe.throw("Article is already issued by another member")

    def validate_return(self):
        article = frappe.get_doc("Article", self.article)
        # article cannot be returned if it is not issued first
        if article.status == "Available":
            frappe.throw("Article cannot be returned without being issued first")

    def validate_maximum_limit(self):
        max_articles = frappe.db.get_single_value("Library Settings", "max_articles")
        count = frappe.db.count(
            "Library Transaction",
            {
                "library_member": self.library_member,
                "type": "Issue",
                "docstatus": DocStatus.submitted(),
            },
        )
        if count >= max_articles:
            frappe.throw("Maximum limit reached for issuing articles")

    def validate_membership(self):
        # check if a valid membership exist for this library member
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                "from_date": ("<", self.date),
                "to_date": (">", self.date),
            },
        )
        if not valid_membership:
            frappe.throw("The member does not have a valid membership")

```

We added a `validate_maximum_limit` method and used `frappe.db.count` to count
the number of transactions made by the member.

With that, we have covered the basics of doctype creation and types of doctype.
We also wrote business logic for various doctypes.

Good job making it this far. Let's keep going.

Next: [Form Scripts](/framework/v14/user/en/tutorial/form-scripts)

<!-- page: framework/framework__user__en__tutorial__whats-next.md -->
---
title: "What's Next?"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/tutorial/whats-next"
updated: "2026-02-17"
---


The goal of this tutorial was to give an introduction to the various parts of
the framework. We have only scratched the surface here. Frappe Framework has a
lot more features that have enabled us to build complex software such as
ERPNext.

You can deep dive into topics by going through the rest of the documentation.
Here are some topics to get you started:

1. [Architecture](/framework/user/en/basics/architecture)
2. [DocType](/framework/user/en/basics/doctypes)
3. [Document API](/framework/user/en/api/document)
4. [Form API](/framework/user/en/api/form)
5. [Bench CLI](/framework/user/en/bench)

## Need Help?

You can ask for help on our public forum: [discuss.frappe.io](https://discuss.frappe.io)

<!-- page: framework/framework__user__en__ui-testing.md -->
---
title: "UI Testing\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/ui-testing"
updated: "2026-02-17"
---


You can write UI tests using [Cypress](https://cypress.io). It is a NodeJS based
full-stack testing framework which doesn't rely on Selenium.

To write integration tests, create a `.js` file in the `cypress/integration`
directory.

### Example

Here is an example of an integration test to check insertion of a ToDo

```js
context('ToDo', () => {
 before(() => {
 cy.login('Administrator', 'admin');
 cy.visit('/desk');
 });

 it('creates a new todo', () => {
 cy.visit('/app/todo/new-todo-1');
 cy.fill_field('description', 'this is a test todo', 'Text Editor').blur();
 cy.get('.page-title').should('contain', 'Not Saved');
 cy.get('.primary-action').click();
 cy.visit('/desk#List/ToDo');
 cy.location('hash').should('eq', '/app/todo');
 cy.get('.list-row').should('contain', 'this is a test todo');
 });
});
```

### Running Cypress Locally

Cypress uses any chromium based browser installed on your system to run tests.
Every app has it's own cypress test suite. To run test for an app, run the
following command from the `frappe-bench` directory.

```sh
bench --site [sitename] run-ui-tests [app]
```

This will open the Cypress Electron shell where you can run any test manually or
run all of the tests.

You can also run tests in headless mode.

```sh
# run in headless mode
bench --site [sitename] run-ui-tests [app] --headless
```

To enable cypress parallel testing you can pass `--parallel` flag.
More information on how cypress parallel tests work can be found [here](https://docs.cypress.io/guides/guides/parallelization).

```sh
# run tests parallelly
bench --site [sitename] run-ui-tests [app] --parallel
```

### Code Coverage
Code coverage helps to identify which lines of the source code were executed during the tests. In order to measure code coverage, the source code needs to be instrumented and this instrumented source code needs to be integrated with our test runner to collect the coverage and generate a report.

For Cypress tests in Frappe, the `.js` files are instrumented using [Istanbul](https://istanbul.js.org/) and the [Cypress code-coverage plugin](https://github.com/cypress-io/code-coverage) is used to merge coverage from each test and save the combined result.

**Code Instrumentation:**

In order to compute which lines of the source code were executed, additional counters are inserted into the code through **_instrumentation_**. For example:

Before instrumentation:

```bash
function foo(a, b) {
 if (a < b)
 return b - a;
 else
 return a - b;
}
```

After instrumentation:

```bash
cov_1m1jljnmzu();

function foo(a, b) {
 cov_1m1jljnmzu().f[0]++;
 cov_1m1jljnmzu().s[0]++;

 if (a < b) {
 cov_1m1jljnmzu().b[0][0]++;
 cov_1m1jljnmzu().s[1]++;
 return b - a;
 } else {
 cov_1m1jljnmzu().b[0][1]++;
 cov_1m1jljnmzu().s[2]++;
 return a - b;
 }
}
```

When using this modified (instrumented) source code for testing, these counters get incremented as the code is executed, and a coverage object is generated. The Cypress code-coverage plugin then handles the collected coverage and generates coverage reports.

**Generating Code Coverage Report Locally:**

1. Instrument source code using [istanbul/nyc](https://github.com/istanbuljs/nyc) :

 ```bash
 npx nyc instrument -x 'frappe/public/dist/**' -x 'frappe/public/js/lib/**' -x '**/*.bundle.js' --compact=false --in-place frappe
 ```
 This replaces the existing source code in the frappe folder with the instrumented source code. The `-x` flag is used to exclude specified paths. You can also use the `-n` flag to specify paths to be included. See [here](https://github.com/istanbuljs/nyc/blob/master/docs/instrument.md) for more details about the `nyc instrument` command

2. Run Cypress tests:

 ```bash
 bench --site test_site run-ui-tests frappe --with-coverage
 ```

3. Generate report:

 ```bash
 npx nyc report --reporter=text
 ```
 See [here](https://istanbul.js.org/docs/advanced/alternative-reporters/) for alternate report formats

### Testing-Library Queries
You can also use [Testing Library](https://testing-library.com/) queries within your Cypress tests. Testing Library provides testing utilities that:

- Make it easier to write UI tests that resemble the way users interact with the app
- Make it easier to find elements in the DOM without knowing all the implementation details
- Help keep the tests maintainable (so minor refactors don't break tests)

> See [Testing Library Docs](https://testing-library.com/docs/queries/about) for more details about usage

Testing Library provides several queries to find elements on a page. Here are some examples:

- [ByRole](https://testing-library.com/docs/queries/byrole)

 Look [here](https://www.w3.org/TR/html-aria/#docconformance) for table of HTML elements and their default roles

 | Query | Element |
 | -------------------------------------- | --------------------------------------------------------------------------------------------- |
 | `findByRole('button', {name: 'Save'})` | `` with [accessible name](https://www.tpgi.com/what-is-an-accessible-name/) = 'Save' |
 | `findByRole('checkbox')` | `` |
 | `findByRole('textbox')` | ``, `` _(Also matches other elements with default role='textbox')_ |
 | `findByRole('searchbox')` | `<input type="search">` |
 | `findByRole('listbox')` | `<select>`, `` |

- [ByLabelText](https://testing-library.com/docs/queries/bylabeltext)

 | Query | Element |
 | ----------------------------- | -------------------------------------------- |
 | `findByLabelText('Optimize')` | element associated with the label 'Optimize' |

- [ByPlaceholderText](https://testing-library.com/docs/queries/byplaceholdertext)

 | Query | Element |
 | ------------------------------- | ------------------------------- |
 | `findByPlaceholderText('Name')` | element with placeholder='Name' |

- [ByText](https://testing-library.com/docs/queries/bytext)

 | Query | Element |
 | ---------------------------- | --------------------------------------- |
 | `findByText('example.json')` | element with textContent='example.json' |

- [ByDisplayValue](https://testing-library.com/docs/queries/bydisplayvalue)

 | Query | Element |
 | -------------------------------- | ---------------------------------------------------------------------------------------------------------- |
 | `findByDisplayValue('Option 1')` | `</select>` with selected `<option>` 'Option 1' _(Also matches `<input>` or `<textarea>` with matching value attribute)_ |

- [ByTitle](https://testing-library.com/docs/queries/bytitle)

 | Query | Element |
 | -------------------------- | ------------------------------ |
 | `findByTitle('Open Link')` | element with title='Open Link' |

- [ByAltText](https://testing-library.com/docs/queries/byalttext/)
- [ByTestId](https://testing-library.com/docs/queries/bytestid/)
</textarea></option>

<!-- page: framework/framework__user__en__using_frappe_as_oauth_service.md -->
---
title: "Using Frappe as OAuth Service"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/using_frappe_as_oauth_service"
updated: "2026-02-17"
---

In this guide we will learn how to use Frappe Framework for authenticating 3rd party apps with OAuth. We will learn how to set up Grafana server and how to connect to the Frappe Framework for authenticating Grafana.

We hope this guide will be useful for beginners and we won’t be writing any code other than some configuration files.

Prerequisites
-------------

* A server running a debian based system(Debian, Ubuntu, Pop OS etc..)
* A Frappe Cloud account. You can sign up for Frappe Cloud [here](https://frappecloud.com/)

OR
* A Frappe Framework site(easier if it’s on the same server)
* Basic text editing knowledge

Frappe Framework
----------------

Frappe Framework is a low-code, Python, and JavaScript web framework that is used to build delightful web applications. Frappe framework was initially developed for building enterprise-level applications, but it has evolved to be a framework for building general-purpose applications without much fuss. It’s open source and MIT licensed.

The interesting thing about Frappe Framework is that you don’t have to write code to make everything work. It was built to be as useful for anyone without prior programming knowledge. You can generate DB schemas, REST APIs, Webhooks, Reports and much more without writing a single line of code. You can check all the feature [here](https://frappeframework.com)

Grafana
-------

Grafana is an awesome metrics visualization platform built by Grafana Labs. Grafana generates interactive graphs from data and can be used for alerting. Grafana has dashboards, which can pull data from the data source and generate graphs that make the most sense out of the data. Grafana is used internally at Frappe for visualizing server statistics for multiple clients and gives a lot of insights to the servers.

### Installing Frappe Framework

Installing the Frappe Framework is an art in itself. It requires many moving parts for optimal functioning. Don't let this make you afraid; we have an elaborate guide on how to install and setup Frappe Framework in the [Framework documentation](https://frappeframework.com/docs/v14/user/en/installation#debian-ubuntu).

If you want the easy way, you can install and setup Frappe Framework with Docker. You can read more about it [here](https://github.com/frappe/frappe_docker).

The easiest way is to use [Frappe Cloud](https://frappecloud.com) to spin up a new site with Frappe Framework installed.

### Installing Grafana

For installing Grafana, you can refer to the [Official Grafana Installation Guide](https://grafana.com/docs/grafana/v9.0/setup-grafana/installation/). We are assuming you're installing Grafana on a Debian-based system.

Once installed, you have to add grafana to systemd. You can do that by


```
# add to systemd to start on bootup
systemctl enable grafana-server.service
# start the service
systemctl start grafana-server
# check status
systemctl status grafana-server
  

```
Configuring Frappe for OAuth
----------------------------

Once you have logged into your site and completed the getting started process for the site, we will create a new entry in the `OAuth Client` doctype.

For accessing the `OAuth Client` doctype, you can use the awesomebar or press Ctrl + G to invoke the awesomebar and type in "OAuth Client", the autocomplete will show you the list of options.

![Dropdown for OAuth Client](/files/g-2.png)  


Select "New OAuth Client" from the dropdown, and you'll be taken to a page for adding the OAuth scopes and settings for the application you want to add OAuth for.

![New OAuth Client](/files/g-3.png)  


Here, you have to configure the:

* App Name (Grafana here)
* Open ID scopes
* Redirect URIs

The redirect URI for Grafana from their docs is `<grafana-url>/login/generic_oauth`. > If you’re on a server without a URL, you can provide the IP address of the server for the `<grafana-url>` part.

Once you have added the details in the respective fields, you will receive an `App Client ID` and `App Client Secret`. These will be used in the Grafana configuration for the OAuth setup.

![OAuth Client details added](/files/g-5.png)  


### Configuring Grafana for OAuth

As we have our Client ID and Client Secret from our Frappe framework site, it's time to connect to our Grafana server for the authentication.

The Grafana configuration files are in the `/etc/grafana` folder on an Ubuntu/Debian system. We will be editing the `grafana.ini` file.


```
$ sudo vim grafana.ini
  

```
Inside the configuration file, for setting up OAuth, you need to edit the `[oauth.generic_oauth]` section. Here you have to uncomment the lines and add the required data.


```
[auth.generic_oauth]
enabled = True
name = Frappe
client_id = ""
client_secret = ""
scopes = openid all
auth_url = <frappe_site_url>/api/method/frappe.integrations.oauth2.authorize
token_url = <frappe_site_url>/api/method/frappe.integrations.oauth2.get_token
api_url = <frappe_site_url>/api/method/frappe.integrations.oauth2.openid_profile
  

```
Also, you will have to add the domain name of the Grafana server to the config if you're using a reverse proxy. You can define the domain and root_url in the `server` section of the `grafana.ini` file.

Once you have done this and saved the file, you have to restart Grafana to make it work. You can use


```
$ sudo systemctl restart grafana-server.service
  

```
to restart Grafana on an Ubuntu/Debian system.

That is mostly it. Now reload your Grafana site, and you'll be able to see a "Sign in with Frappe" button on the login page.

![Signin with Frappe Grafana](/files/g-6.png)  


If you have done everything correctly, you'll be logged into Grafana with the credentials from your Frappe site.

![Logging in with Frappe GIF](/files/grafana-oauthlogin.gif)  

<!-- page: framework/framework__user__en__videos.md -->
---
title: "Video Tutorials for Frappe Framework\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/videos"
updated: "2026-05-10"
---


This 10-part video tutorial will teach you how to build complex apps in Frappe

Pre-requisites: [You must have some understanding of Python, Javascript and MySQL before you start this tutorial.](/framework/v14/user/en/prerequisites)

---

&lt;iframe allowfullscreen="" frameborder="0" height="376" src="https://www.youtube.com/embed/videoseries?list=PL3lFfCEoMxvzHtsZHFJ4T3n5yMM3nGJ1W" width="670"&gt;&lt;/iframe&gt;

<!-- page: framework/framework__user__en__web-form.md -->
---
title: "Web Form"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/web-form"
updated: "2026-06-26"
---

Frappe provides an easy way to generate forms for your website with very little configuration. These forms may be public (anyone can fill them up), can be configured to require login, or can be made available through private request links.

![Web Form](/files/v-14-webform-conference-register.png)

## Creating a Web Form

To create a Web Form, type "new web form" in awesomebar and hit enter.

1. Enter Title
2. Select DocType for which the record should be created.
3. Add some introduction (Optional).
4. Click on "Get Fields" button to get all fields from selected doctype OR select fields for your web form.
5. Publish it and you are good to go.

![Create Web Form](/files/v-14-webform.png)

![Web Form Fields](/files/v-14-webform-fields.png)

[Customize Web Form →](/framework/v14/user/en/web-form/customization)

[Private Web Form Requests →](/framework/user/en/web-form/web-form-request)

## Standard Web Forms

If you check the "Is Standard" checkbox, a new folder will be created in the  
`module` of the Web Form. In this folder, you will see a `.py` and `.js` file  
that you can use to configure the web form. These files need to be checked into  
version control with your custom app. You can install this app on any site and  
it will have this web form installed.

> `Is Standard` field will only be visible when you are in developer mode.

<!-- page: framework/framework__user__en__web-form__customization.md -->
---
title: "Customization"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/web-form/customization"
updated: "2026-06-26"
---

You can customize your webform to make it more unique and enable functionalities to meet your usecase.

## Fields Layout

You can add `Column Breaks` & `Section Breaks` in webform fields table to change the layout of the form fields.

![Web Form Field Layout](/files/v-14-webform-field-layout.png)

![Web Form Layout](/files/v-14-webform-layout.png)

## Multi Step Webform

Updating the layout makes webform look better but still if webform has many fields it becomes lengthy.  
We can add `Page Breaks` to segregate the sections in different pages (called as Multi Step Webform).

> You can add maximum 9 Page Breaks which will only allow 10 Pages.

![Web Form Page Break](/files/v-14-webform-page-break.png)

![Step Web Form Page 1](/files/v-14-step-webform-page1.png)

![Step Web Form Page 2](/files/v-14-step-webform-page2.png)

> All the customization options mentioned below can be done from the Customization Tab of webform document.

## Submit Button Label

You can change the label of submit button on the webform.

![Web Form Submit Label](/files/v-14-webform-submit-label.png)

## Banner Image

You can now add banner image on webform.

![Banner Image](/files/v-14-webform-banner-image.png)

## Breadcrumbs

You can customize the breadcrumbs in a Web Form by adding JSON object.

> Breadcrumbs are only visible if the webform `[list view](/framework/v14/user/en/web-form/settings#list-settings)` is enabled.

Example:

![Custom Breadcrumbs](/files/v-14-webform-custom-breadcrumbs.png)

![Webform Breadcrumbs](/files/v-14-webform-breadcrumbs.png)

## After Submit Page

You can give custom success title and message which will appear after user has submitted the webform.

![Webform Success Title & Message](/files/v-14-success-title-message.png)

![Webform Success Page](/files/v-14-success-page.png)

Based on the access extra buttons will be visible on the submit page like 

 See previous responses

 Edit your response

 View your response  
 & 

 Submit another response

![Webform Success Page](/files/v-14-success-actions.png)

If the Web Form is opened through a [Web Form Request](vscode-file://vscode-app/framework/user/en/web-form/web-form-request), these action links preserve the request key where needed.

Configure your webform to redirect to a specific URL after 5 seconds after it has been submitted by setting `success_url` field.

![Webform Breadcrumbs](/files/SuccessURLGif.gif)



## Custom CSS

You can add custom css to change the look of the webform

Example:

```css
.web-form-header {
 margin-bottom: 2rem;
 border: 1px solid var(--blue-200) !important;
 border-radius: var(--border-radius);
 background-color: var(--blue-50) !important;
}

.web-form-head {
 border: none !important;
 padding-bottom: 2rem !important;
}

.web-form {
 border: 1px solid var(--dark-border-color) !important;
 border-radius: var(--border-radius);
 padding-top: 2rem !important;
}
```

![Web Form Custom CSS](/files/v-14-webform-custom-css.png)

## Client Script

You can also add a custom client script to the web form

##### Event Handler

Write an event handler to do actions when a field is changed.

```js
frappe.web_form.on([fieldname], [handler]);
```

##### Get Value

Get value of a particular field

```js
value = frappe.web_form.get_value([fieldname]);
```

##### Set Value

Set value of a particular field

```js
frappe.web_form.set_value([fieldname], [value])
```

##### Validate

`frappe.web_form.validate` is called before the web_form is saved. Add custom  
validation by overriding the `validate` method. To stop the user from saving,  
return `false`;

```js
frappe.web_form.validate = () => {
 // return false if not valid
}
```

##### Set Field Property

```js
frappe.web_form.set_df_property([fieldname], [property], [value]);
```

##### Trigger script when form is loaded

Initialize form with customisation after it is loaded

```js
frappe.web_form.after_load = () => {
 // init script here
}
```

#### Examples

##### Reset value if invalid

```js
frappe.web_form.on('amount', (field, value) => {
 if (value < 1000) {
 frappe.msgprint('Value must be more than 1000');
 field.set_value(0);
 }
});
```

##### Custom Validation

```js
frappe.web_form.validate = () => {
 let data = frappe.web_form.get_values();
 if (data.amount < 1000) {
 frappe.msgprint('Value must be more than 1000');
 return false;
 }
});
```

##### Hide a field based on value

```js
frappe.web_form.on('amount', (field, value) => {
 if (value < 1000) {
 frappe.web_form.set_df_property('rate', 'hidden', 1);
 }
});
```

##### Show a message on startup

```js
frappe.web_form.after_load = () => {
 frappe.msgprint('Please fill all values carefully');
}
```

<!-- page: framework/framework__user__en__web-form__settings.md -->
---
title: "Settings"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/web-form/settings"
updated: "2026-06-26"
---

## Webform Settings

There are multiple checkboxs in the `Settings` tab that can be used to enable and disable different functionalities.

### Login Required

If you want responses from guest user, just disable the `login_required` checkbox. Logged In users can also use it. It is disabled by default.

If you only want responses from logged in user just enable the `login_required` checkbox.

> Enabling it will make **Allow Multiple Responses, Allow Editing After Submit, Allow Delete, Allow Comments, Show Attachments** and **Show List** checkboxes visible.

### Key Required

Enable *Key required* when the Web Form should only be opened with a private key from a [Web Form Request](/framework/user/en/web-form/web-form-request).

This is useful for surveys or invitation flows where the respondent does not have a user account, but the form should not be public. The request key can carry visible pre-filled form values and hidden document values.

If *Login required* is also enabled, the user must be logged in and must have a valid request key.

### Allow Multiple Responses

It is used to enable users to give multiple responses which they can see in Webform List View.

> Enabling it will also enable [show_list](/framework/user/en/web-form/settings#show-list) checkbox in List Setting section

### Allow Editing After Submit

It will allow user to edit there submitted responses.

### Allow Delete

It will allow user to delete there submitted responses from Webform List View.

### Anonymous

By setting this the response received will be anonymous.

### Apply Document Permission

By default if user has read access to the documents submitted by different users it will be visible in the Webform List View. But he/she can only open the record from list view if **Apply Document Permission** checkbox is checked.

### Allow Print

It will add a print button to print the document. It will only be visible on View Mode.

### Allow Comments

It will add comment section below the webform where users can communicate. All the comments will be linked to the document.

### Show Attachments

It will show all the attachments attached in the document in Attachment Section.

### Max Attachment Size (in MB)

It will restrict users to attach large files.

### Allow Incomplete Forms

It will allow submission of forms even if mandatory fields are not populated.

## List Settings

![Web Form](/files/v-14-web-form-list-settings.png)



### Show List

It will enable `List View` where you can see all the submitted forms. You can only open the form that you own. 

![Web Form](/files/v-14-web-form-list-view.png)





> If `apply_document_permissions` is enabled you can open other forms.

### Title & List Columns

You can change the title of the list and also can add/remove/arrange list view columns 

![Web Form](/files/v-14-web-form-update-title-list-columns.png)



![Web Form](/files/v-14-web-form-updated-list-view.png)



## Sidebar Settings

![Web Form](/files/v-14-web-form-show-sidebar.png)



### Show Sidebar

Show webform with sidebar. Select or create a website sidebar where you can add link to current webform and other related webforms or webpages. 

![Web Form](/files/v-14-web-form-with-sidebar.png)

<!-- page: framework/framework__user__en__zero-_downtime_migrations.md -->
---
title: "Zero* downtime migrations"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/zero*_downtime_migrations"
updated: "2026-02-17"
---

Zero* downtime migrations let the site run in read only mode during site upgrade process. This means your static site, dynamic pages which only need to read data can continue to work without any noticable difference. Any actions that requires writing to database will be disabled and only resume when upgrade is finished.

### How does this work

Zero downtime migration utilizes one of following two means to enable read-only mode:

1. Using read-replicas.
2. Using "read only transactions" which are provided by databases.

In either case writes on your database are disabled until maintenance mode is lifted.

Both web pages and Desk will show persisten read only warnings during updates. All forms are also made read only so you can not modify any data.

![zero downtime migration](/files/zero-downtime-migration.png)

### Caveats to keep in mind

* Not all apps automatically support this feature. They might behave erratically if they are not designed to work in read only mode.
* During update database schema changes, client side app is updated so you'll ocassionally face some glitches. These can not be fully avoided, the intent behind this feature is only to reduce the impact of downtime.

### Enabling Read Only Mode during upgrades

1. [Optional/Recommended] - Setup a read replica by following the [replication guide](https://frappeframework.com/docs/v14/user/en/guides/database-settings/setup-read-from-secondary-db)
2. Edit your site config to enable this feature. `bench --site develop set-config allow_reads_during_maintenance 1`

### Supporting read only mode in your app

If you are an app developer and want to add support for this feature in your app then you need to modify your app

#### Server side changes

You can use `frappe.flags.read_only` to disable or modify behaviour in read only mode.

Example: Logging page visits


```
@frappe.whitelist()
def log_visit():
    if frappe.flags.read_only:
        return

    doc = frappe.new_doc("Doc Visit")
    doc.insert()

```
#### Jinja / Client side page changes

You should ideally update the UI to indicate that your app is in read only mode and write-actions can not be performed right now.

Website context includes `read_only_mode` key in context by default, you can use this to add warning or toggle features on your pages conditionally. Example:


```
<!-- some html page -->
{% if read_only_mode %}
    <div class="alert">Site is running in read only mode. Full functionality will be restored soon.</div>
{% endif %}
<!-- other content -->

```

<!-- page: framework/framework__using-vue-inside-a-desk-page.md -->
---
title: "Using Vue in a Desk Page"
space: "Framework"
url: "https://docs.frappe.io/framework/using-vue-inside-a-desk-page"
updated: "2026-05-10"
---

Using Vue to add pages to your Desk based app gives you a best-of-both-worlds type of convenience:

1. You get to use Vue with its reactivity and composability
2. You get to use [Frappe JS APIs](/framework/user/en/api/server-calls)

This is possible without having to manually configure a Vue app. You can follow
the steps below to set it up.

### Create a Page

Navigate to the Page DocType (at `/app/page`) and create a new Page entry.
New files will be created for your page in the module you select.

![Page DocType!](/files/page.png)

### Check created files

Under the module folder in your app's directory, you'll find a new folder with three
files in it:

```
└── app
    └── app
        └── module
            └── page
                └── test_vue
                    ├── __init__.py
                    ├── test_vue.json
                    └── test_vue.js
```

Among these, in the newly created JavaScript file you'll see `make_app_page` being called:

```javascript
frappe.pages['test-vue'].on_page_load = function (wrapper) {
  var page = frappe.ui.make_app_page({
    parent: wrapper,
    title: 'None',
    single_column: true,
  });
};
```

This is used to create a new page. See the [Page API](/framework/user/en/api/page) for more info.

This file will be loaded when you visit to `/app/test-vue`, you can visit the
path and an empty page with the title "None" will be shown.


### Creating Vue files

To use Vue, your `.vue` source files need to be transpiled and bundled. Frappe
Framework does this out of the box.

We'll now create two files, a `.vue` file, and a `.js` file that loads your Vue
code. You can add these files under your app's `public/js` folder:

```
└── app
    └── app
        └── public
            └── test_vue
                ├── TestVue.vue
                └── test_vue.bundle.js
```

First, we'll create the `.vue` file `TestVue.vue`. Some simple Vue code to test the setup:

```vue
&lt;script setup&gt;
import { ref } from 'vue';

const message = ref('Hello, World');
&lt;/script&gt;
&lt;template&gt;
  <h1>{{ message }}</h1>
&lt;/template&gt;
```

Second, the `.js` file that loads the Vue code:

```javascript
import { createApp } from 'vue';
import TestVue from './TestVue.vue';

// A simple function to mount your Vue app
function setup_vue(wrapper) {
  const app = createApp(TestVue);
  app.mount(wrapper.get(0));
  return app;
}

// We'll call this function from the generated test_vue.js file
frappe.ui.setup_vue = setup_vue;
export default setup_vue;
```

### Require the bundle

In the generated `test_vue.js` file, add the following code to load the Vue app:

```javascript
frappe.pages['test-vue'].on_page_load = function (wrapper) {
  const page = frappe.ui.make_app_page({
    parent: wrapper,
    title: 'Test Vue',
    single_column: true,
  });

  // hot reload when in developer mode
  if (frappe.boot.developer_mode) {
    frappe.hot_update ??= frappe.hot_update;
    frappe.hot_update.push(() =&gt; load_vue(wrapper));
  }
};
frappe.pages['test-vue'].on_page_show = (wrapper) =&gt; load_vue(wrapper);

// Simple callback function to load Vue in the page
async function load_vue(wrapper) {
  const $parent = $(wrapper).find('.layout-main-section');
  $parent.empty();

  // Require the bundle and mount the Vue app
  await frappe.require('test_vue.bundle.js');
  frappe.test_vue_app = frappe.ui.setup_vue($parent);
}
```

This will call the `load_vue` function that `requires` the bundle and mounts the
Vue app when the page is loaded or shown.


### Build or run the dev server

To build your code you can call:

```bash
bench build
```

Note: this will build the frontend code for all the apps on your bench.

To run the dev server you can navigate the frappe app's (i.e `bench/apps/frappe`) folder and run:

```bash
npm run build -- --apps app --watch
```

This will watch for any changes in your app and rebuild the code, which should
trigger a hot reload in your browser.

If you've done everything right you should see your page show the Vue app's message:

![Vue Works](/files/It-works.png)
