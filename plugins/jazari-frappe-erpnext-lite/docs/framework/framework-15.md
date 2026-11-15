<!-- Frappe documentation: framework, part 15 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__guides__app-development__adding-social-login-provider.md -->
---
title: "Adding Social Login Provider\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/adding-social-login-provider"
updated: "2026-02-17"
---


This guide discusses how to add a social login provider to frappe via pull request.

### Add your provider in `SocialLoginKey.get_social_login_provider`

```
providers["Frappe"] = {
 "provider_name": "Frappe",
 "enable_social_login": 1,
 "custom_base_url": 1,
 "icon":"/assets/frappe/images/favicon.png",
 "redirect_url": "/api/method/frappe.www.login.login_via_frappe",
 "api_endpoint": "/api/method/frappe.integrations.oauth2.openid_profile",
 "api_endpoint_args":None,
 "authorize_url": "/api/method/frappe.integrations.oauth2.authorize",
 "access_token_url": "/api/method/frappe.integrations.oauth2.get_token",
 "auth_url_data": json.dumps({
 "response_type": "code",
 "scope": "openid"
 })
}
```

### Add provider key in exact same type case in options of `social_login_provider` select field on `Social Login Key` DocType. e.g. `Frappe`

Once the user adds a social login provider and enables it the `Authorization Code` is sent back by the provider api server on to the redirect_url mentioned on the same server. You will have to add a whitelisted method allowing guest access in `frappe.integrations.oauth2_logins`. e.g. `login_via_office365`

There many implementations of OAuth 2.0 + OpenID Connect. Here we'll discuss two ways of accessing openid information.

#### User Creation via OpenID Profile Endpoint

example:

```
@frappe.whitelist(allow_guest=True)
def login_via_frappe(code, state):
 login_via_oauth2("frappe", code, state, decoder=json.loads)
```

#### User Creation via id_token

example:

```
@frappe.whitelist(allow_guest=True)
def login_via_office365(code, state):
 login_via_oauth2_id_token("office_365", code, state, decoder=json.loads)
```

<!-- page: framework/framework__user__en__guides__app-development__connected-app.md -->
---
title: "Set up a new Connected App"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/connected-app"
updated: "2026-02-17"
---

You can use **Connected App** to allow your frappe instance to access other web services on your behalf.


> This example shows how to connect to Google Mail, but you can use any service supporting OAuth 2.0.
> 
> 

First, create a new **Connected App** and give it a name. Most providers offer an URL like `/.well-known/openid-configuration` where they publish all OAuth endpoints. Enter this URL and click on "Get OpenID Configuration".

If you don't know this URL, please go to the "Endpoints" section and manually enter the *Authorization URI* and *Token URI*. The Authorization URI is where you will be redirected to give your consent. The Token URI is the endpoint where the system can exchange an authorization code for an access or refresh token. Please check the documentation of the specific integration or third party service to get the right values.

[Screenshot on the live page: new_connected_app]  


Now the configuration should look like this:

[Screenshot on the live page: fetched_openid_config]  


Click on "Save". Now you should see a new read-only field called *Redirect URI*. Note that the last part of it is specific to your **Connected App**. You'll need to register the Redirect URI with your provider (Google, in this case).

Copy the Redirect URI, head to the third party service and create new OAuth 2.0 client credentials. You will need to specify the authorized JavaScript origins and the Redirect URI you just copied. Enter the domain name of your frappe instance as authorized JavaScript origin. On a production server this might be `https://erp.mycompany.com`. For local development you can use something like `http://localhost:8000`.


> It is crucial that the authorized JavaScript origins and the authorized redirect URIs are correct. Otherwise you will not be able to connect.
> 
> 

[Screenshot on the live page: Create OAuth 2.0 client credentials]  


Copy the client ID and secret from the third party service to your **Connected App** and save.

[Screenshot on the live page: client_credentials]  


Next, you'll need to define what scopes your system needs to access. In this example, we want to connect to an email inbox, so we need the scope `https://mail.google.com/`. For other use cases, please check the available scopes at your providers' documentation.

[Screenshot on the live page: scope]  


Lastly, we can define extra parameters. The Google documentation states that we'll need the parameter `access_type=offline`, so that for our server can access the email inbox in the background and keep refreshing the access token without user intervention. If we don't pass this parameter, the temporary access will quickly expire and we'll need to log in again and again.

[Screenshot on the live page: extra_parameters]  


Now you and your users can click on "Connect to ..." on the top right. This will open a new browser tab that shows the third party service's consent screen. After this, you will be redirected to your frappe instance.

[Screenshot on the live page: connect]  


In the backend, your server will exchange a code that it obtained during the redirect for a temporary access token and, optionally, a refresh token. These can then be used to access the third party service on your behalf.

<!-- page: framework/framework__user__en__guides__app-development__custom-module-icon.md -->
---
title: "Custom Module Icon"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/custom-module-icon"
updated: "2026-02-17"
---


If you want to create a custom icon for your module, you will have to create an SVG file for your module and set the path to this file in the `desktop/config.py` of your app.  


This icon is loaded via AJAX first time, then it will be rendered.

Example:

```py
from frappe import _

 def get_data():
    return {
     "Frappe Apps": {
     "color": "orange",
     "icon": "assets/frappe/images/frappe.svg",
     "label": _("Frappe.io Portal"),
     "type": "module"
    }
  }
 ```

> PS: A great place to buy SVG icons for a low cost is the awesome [Noun Project](http://thenounproject.com/)

<!-- page: framework/framework__user__en__guides__app-development__custom_action_link_field.md -->
---
title: "Custom Action in Link Field"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/custom_action_link_field"
updated: "2026-02-17"
---


You can add a new custom link option to the standard link field by defining the function in the namespace `frappe.ui.form.ControlLink.link_options`.

In the `frappe.ui.form.ControlLink.link_options`, you have access to the link field object.

### 1. Adding Custom Option

```js
frappe.ui.form.ControlLink.link_options = function(link) {
 return [
 {
 html: ""
 + " "
 + __("Custom Link Option")
 + "",
 label: __("Custom Link Option"),
 value: "custom__link_option",
 action: () => {}
 }
 ];
}
 
```

Once a function is assigned to `frappe.ui.form.ControlLink.link_options`, the link field will have a new link option:

[Screenshot on the live page: 182354398 c1fc9f55 4464 4683 bb74 982ec2546f71]

<!-- page: framework/framework__user__en__guides__app-development__dialogs-types.md -->
---
title: "Dialogs Types\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/dialogs-types"
updated: "2026-02-17"
---


Frappe provides a group of standard dialogs that are very useful while coding.

## Alert Dialog

[Screenshot on the live page]

Alert Dialog is used for showing non-obstructive messages.

It has 2 parameters:

- **txt:** The message to be shown in the `Alert Dialog`
- **seconds:** The duration that the message will be displayed. The default is `3 seconds`.

### Example

 show_alert('Hi, do you have a new message', 5);

---

## Prompt Dialog

[Screenshot on the live page]

Prompt Dialog is used for collecting data from users.

It has 4 parameters:

- **fields:** a list with the fields objects
- **callback:** a function to process the data in the dialog
- **title:** the title of the dialog
- **primary_label:** the label of the primary button

### Example

 frappe.prompt([
 {'fieldname': 'birth', 'fieldtype': 'Date', 'label': 'Birth Date', 'reqd': 1}
 ],
 function(values){
 show_alert(values, 5);
 },
 'Age verification',
 'Subscribe me'
 )

---
## Confirm Dialog

[Screenshot on the live page]

Confirm Dialog is used to get a confirmation from the user before executing an action.

It has 3 arguments:

- **mesage:** The message to display in the dialog
- **onyes:** The callback on positive confirmation
- **oncancel:** The callback on negative confirmation

### Example

 frappe.confirm(
 'Are you sure to leave this page?',
 function(){
 window.close();
 },
 function(){
 show_alert('Thanks for continue here!')
 }
 )

---

## Message Print

[Screenshot on the live page]

Message Print is used for showing information to users.

It has 2 arguments:

- **message:** The message to display. It can be a HTML string
- **title:** The title of the dialog

### Example

 msgprint("**Server Status**"
 + "

---

"
 + ""
 + "* **28%** Memory
"
 + "* **12%** Processor
"
 + "* **0.3%** Disk
"
 + "
", 'Server Info')

---

### Custom Dialog

[Screenshot on the live page]

You can extend and build your own custom dialogs using `frappe.ui.Dialog`

### Example

 var d = new frappe.ui.Dialog({
 'fields': [
 {'fieldname': 'ht', 'fieldtype': 'HTML'},
 {'fieldname': 'today', 'fieldtype': 'Date', 'default': frappe.datetime.nowdate()}
 ],
 primary_action: function(){
 d.hide();
 show_alert(d.get_values());
 }
 });
 d.fields_dict.ht.$wrapper.html('Hello World');
 d.show();

<!-- page: framework/framework__user__en__guides__app-development__executing-code-on-doctype-events.md -->
---
title: "Executing Code On Doctype Events\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/executing-code-on-doctype-events"
updated: "2026-02-17"
---


To execute code when a DocType is inserted, validated (before saving), updated, submitted, cancelled, deleted, you must write in the DocType's controller module.

#### 1. Controller Module

The controller module exists in the `doctype` folder in the Module of the `DocType`. For example, the controller for **ToDo** exists in `frappe/desk/doctype/todo/todo.py` (version 5). A controller template is created when the DocType is created. which looks like

 from __future__ import unicode_literals

 import frappe
 from frappe.model.document import Document

 class CustomType(Document):
 pass

#### 2. Document Properties

All the fields and child tables are available to the class as attributes. For example the **name** property is `self.name`

#### 3. Adding Methods

In this module, you can add standard methods to the class that are called when a document of that type is created. Standard Handlers are:

1. `autoname`: Called while naming. You can set the `self.name` property in the method.
1. `before_insert`: Called before a document is inserted.
1. `validate`: Called before document is saved. You can throw an exception if you don't want the document to be saved
1. `on_update`: Called after the document is inserted or updated in the database.
1. `on_submit`: Called after submission.
1. `on_cancel`: Called after cancellation.
1. `on_trash`: Called after document is deleted.

<!-- page: framework/framework__user__en__guides__app-development__exporting-customizations.md -->
---
title: "Exporting Customizations to your App"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/exporting-customizations"
updated: "2026-02-17"
---

A common use case is to extend a DocType via Custom Fields and Property Setters for a particular app. To save these settings to an app, go to **Customize Form**

You will see a button for **Export Customizations**

[Screenshot on the live page]  


Here you can select the module and whether you want these particular customizations to be synced after every update.

The customizations will be exported to a new folder `custom` in the module folder of your app. The customizations will be saved by the name of the DocType

[Screenshot on the live page]  


When you do `bench update` or `bench migrate` these customizations will be synced to the app.


> Warning: Using this feature whenever a customization are synced all property setters and custom permissions are replaced on site with what's specified in the code. If this behaviour is not desired then you should not use this feature. 
> 
> 

<!-- page: framework/framework__user__en__guides__app-development__fetch-custom-field-value-from-master-to-all-related-transactions.md -->
---
title: "Fetch a Field Value from a Document into a Transaction\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/fetch-custom-field-value-from-master-to-all-related-transactions"
updated: "2026-02-17"
---


Let's say, there is a custom field "GSTIN" in Supplier, which should be fetched in Purchase Order.


### Scenario I: You want to keep this field updated

In this scenario, the custom field will be updated automatically based on the value in Supplier when you save the Purchase Order and will be re-updated everytime you save the Purchase Order. Since this field needs to be updated automatically, it overwrites user input. If you want to allow user input, refer to Scenario II.

#### Steps:

1. Create a Custom Field **GSTIN** for *Supplier* document with *Field Type* as **Data**.
 [Screenshot on the live page]

1. Create another Custom Field **GSTIN** for *Purchase Order* document, but in this case with *Field Type* as **Read Only** or check **Read Only** checkbox. Set **Fetch From** as `supplier.gstin`.
 
[Screenshot on the live page]

1. Go to the user menu and click "Reload".

1. Now, on selection of Supplier in a new Purchase Order, **GSTIN** will be fetched automatically from the selected Supplier.
 
[Screenshot on the live page]

### Scenario II: You want to allow user input if value not found

In this scenario, the value is fetched from the Supplier the first time the Purchase Order is created. If the value is not found in Supplier, you can enter it manually. The value will only be fetched on saving Purchase Order if the field is empty.

#### Steps:

1. Create a Custom Field **GSTIN** for *Supplier* document with *Field Type* as **Data**.
 
[Screenshot on the live page]

1. Create another Custom Field **GSTIN** for *Purchase Order* document with *Field Type* as **Data**. Set **Fetch From** as `supplier.vat_number` and tick the checkbox titled **Fetch If Empty**.
 
[Screenshot on the live page]

1. Go to the user menu and click "Reload".

1. Now, on selection of Supplier in a new Purchase Order, **GSTIN** will be fetched automatically from the selected Supplier. If GSTIN is not found in supplier, you can enter it manually.
 
[Screenshot on the live page]

<!-- page: framework/framework__user__en__guides__app-development__generic-oauth-client.md -->
---
title: "Prerequisites\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/generic-oauth-client"
updated: "2026-02-17"
---


- [Connected App](/framework/v14/user/en/guides/app-development/connected-app)

 **Connected App** stores the client ID and secret, scopes and endpoints of the platform you're integrating with.

## Getting started

> This example uses Google, but you can use any service supporting OAuth 2.0.

Your integration will most probably need a settings doctype (for example, "Google Settings"). Here you create a link field to **Connected App**. A System Manager can later create a **Connected App**, enter the client credentials and link it to your integration. You will know which **Connected App** belongs to your integration via your settings DocType.

```py
google_settings = frappe.get_single('Google Settings')
connected_app_name = google_settings.get('connected_app')

connected_app = frappe.get_doc('Connected App', connected_app_name)
```

Now you have an instance of your **Connected App**, containing the credentials and endpoint URIs. If a user didn't connect yet, they can open the **Connected App** and click the "Connect to ..." button on the top right. Alternatively, you can get the authorization URI and use it for your own custom button or redirect:

```py
authorization_uri = connected_app.initiate_web_application_flow() # optional
```

Once the user is authorized, you can get an authenticated session like this:

```py
session = connected_app.get_oauth2_session()
```

> If the user is not authenticated at this time, they will be redirected to the authentication page.

Now you can retrieve any allowed resource from the target platform:

```py
session.get('https://www.googleapis.com/oauth2/v2/userinfo')
```

If the access token is expired, the session will automatically try to refresh it.

<!-- page: framework/framework__user__en__guides__app-development__how-enable-developer-mode-in-frappe.md -->
---
title: "How to Enable Developer Mode in Frappe"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/how-enable-developer-mode-in-frappe"
updated: "2026-02-17"
---

When you are in application design mode and you want the changes in your DocTypes, Reports etc to affect the app repository, you must be in **Developer Mode**.

To enable developer mode, update the `site_config.json` file of your site in the sites folder:


```
frappe-bench/sites/{your site}/site_config.json
```
Inside the `frappe-bench` folder, run


```
bench set-config -g developer_mode 1
```
OR, manually, write `"developer_mode": 1` inside the `{ .. }` of `site_config.json`


```
{
  "developer_mode": 1,
  ...
}
```
After setting developer mode, clear the cache:


```
bench --site {your site} clear-cache
```
Some apps might require additional dependencies to build and test in development mode. Install them using bench:


```
bench setup requirements --dev
```

<!-- page: framework/framework__user__en__guides__app-development__how-to-create-custom-fields-during-app-installation.md -->
---
title: "How To Create Custom Fields During App Installation\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/how-to-create-custom-fields-during-app-installation"
updated: "2026-02-17"
---


Your custom app can automatically add **Custom Fields** to DocTypes outside of your app when it is installed to a new site.

To do this, add the new custom fields that your app requires, using the Frappe web application.

In your `hooks.py` file, add `"Custom Fields"`

 fixtures = ["Custom Field"]

Export fixtures before you commit your app with:

 $ bench --site mysite export-fixtures

This will create a new folder called `fixtures` in your app folder and a `.csv` or `.json` file will be created with the definition of the custom fields you added.

This file will be automatically imported when the app is installed in a new site or updated via `bench update`.

Note: You can also add single DocTypes like "Website Settings" as fixtures

<!-- page: framework/framework__user__en__guides__app-development__how-to-improve-a-standard-control.md -->
---
title: "How To Improve A Standard Control\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/how-to-improve-a-standard-control"
updated: "2026-02-17"
---


Frappe has a couple of elegant and useful widgets, but some times we need to edit them to add small improvements. This small article will describe how to add new resources to the standard widgets.

Let me explain first our goal:

> Add `many` alternative translations in `numerous records` and in a `lot of doctypes`

Look the highlighted sections in the __goal__, we have _many translations_ to add in _many records_ and in _many doctypes_, so, we heave a **many of work**, so we have a lot to do right?

The answer for this question is: _-Of course not! Because we know that if one element exists in many records and in many doctypes, this element is the `Control` or `Widget`_

So, what we need do, is improve your goal based on the `Control`, to reduce our quantity of work.

But, where will we find this magic element, the control? _-For now, we can look it in the JavaScript sources - let's look now at [Github](https://github.com/frappe/frappe/blob/develop/frappe/public/js/frappe/form/controls/control.js)_

> Don't worry if you don't understand the code for now, our goal there is simplify our work.

Let's go ahead with the thought!

We know where we need to make the changes, but how will we dismember which are the controls that are affected by our feature and which aren't ?

We need to keep in mind, that `Control` are instance of `DocFields` and the `DocFields` have a field that is very important for us in this case, the field that will help us to dismember which are affected by our feature and which aren't is the field `options` in the `DocField`.

_-Wait!, we understood that the field `options` can help us, but, how will it help us?_

Good question, we will define a word to put in the `options` of the `DocFields` that we need to include the feature, this world will be **`Translatable`.**

> If you forget how to customize the options of a field look [this article](https://kb.erpnext.com/kb/customize/creating-custom-link-field), it can refresh your knowledge.

Well, with the defined word in `options` of our selected `DocFields`, now is time to code:

_-At last, we think we would never stop talking!_

```js
 frappe.ui.form.ControlData = frappe.ui.form.ControlData.$extend({
 make_input: function(){
 var options = this.df.options;
 if (!options || options!=="Translatable"){
 this._super();
 return;
 }
 var me = this;
 $('\
 \
 \
 \\
 \
 ').prependTo(this.input_area);
 this.$input_area = $(this.input_area);
 this.$input = this.$input_area.find('input');
 this.$btn = this.$input_area.find('.dialog-btn');
 this.set_input_attributes();
 this.$input.on("focus", function(){
 me.$btn.toggle(true);
 });
 this.$input.on("blur", function(){
 setTimeout(function(){ me.$btn.toggle(false) }, 500);
 });
 this.input = $this.input.get(0);
 this.has_input = true;
 var me = this;
 this.setup_button();
 },
 setup_button: function(){
 var me = this;
 if (this.only_input){
 this.$btn.remove();
 return;
 }
 this.$btn.on("click", function(){
 var value = me.get_value();
 var options = me.df.options;
 if (value && options && options==="Translatable"){
 this.open_dialog();
 }
 });
 },
 open_dialog: function(){
 if (this.frm && !this.frm.is_dirty()) {
 new frappe.ui.form.TranslationSelector({
 doc: doc,
 df: this.doc,
 text: this.value
 });
 }
 }
 });
```

_-Other letter soup, for my gosh!_

In fact, it IS a soup of letters, for a newbie, but we are not a beginner.

Let me explain what this code does;

 - At line 1 the code overrides the `ControlData` by one extended `Class` of itself.
 - The method `make_input` checks if the docfield is **`Translatable`** to make the new `Control` if not, it calls the *original* `make_input` using `_super()`
 - The method `setup_button` checks if the docfield is **`Translatable`** to enable it show a `dialog`
 - The method `open_dialog` invokes a new instance of the `TranslationSelector` that we will create in the code below.

<!-- page: framework/framework__user__en__guides__app-development__insert-a-document-via-api.md -->
---
title: "Insert A Document Via Api\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/insert-a-document-via-api"
updated: "2026-02-17"
---


You can insert documents via a script using the `frappe.get_doc` method

### Examples:

#### 1. Insert a ToDo

 todo = frappe.get_doc({"doctype":"ToDo", "description": "test"})
 todo.insert()

---

#### 2. Insert without the user's permissions being checked:

 todo = frappe.get_doc({"doctype":"ToDo", "description": "test"})
 todo.insert(ignore_permissions = True)


---

#### 3. Submit after inserting

 todo = frappe.get_doc({"doctype":"ToDo", "description": "test"})
 todo.insert(ignore_permissions=True)
 todo.submit()

---

#### 4. Insert a document on saving of another document

 class MyType(Document):
 def on_update(self):
 todo = frappe.get_doc({"doctype":"ToDo", "description": "test"})
 todo.insert()

----

#### 5. Insert a document with child tables:

 sales_order = frappe.get_doc({
 "doctype": "Sales Order",
 "company": "_Test Company",
 "customer": "_Test Customer",
 "delivery_date": "2013-02-23",
 "sales_order_details": [
 {
 "item_code": "_Test Item Home Desktop 100",
 "qty": 10.0,
 "rate": 100.0,
 "warehouse": "_Test Warehouse - _TC"
 }
 ]
 })
 sales_order.insert()

<!-- page: framework/framework__user__en__guides__app-development__overriding-link-query-by-custom-script.md -->
---
title: "Overriding Link Query By Custom Script\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/overriding-link-query-by-custom-script"
updated: "2026-02-17"
---


You can override the standard link query by using `set_query` via the Client Script DocType from the desk.

The `set_query` method takes one of two formats: `set_query(field_name, options_function())` for regular fields, or `set_query(field_name, child_table_name, options_function())` for fields in child tables.

### 1. Adding Filters

You can add filters to the query:

```js
frappe.ui.form.on("Bank Reconciliation", "onload", function(frm) {
 frm.set_query("bank_account", function() {
 return {
 "filters": {
 "account_type": "Bank",
 "group_or_ledger": "Ledger"
 }
 };
 });
});
```

A more complex query:

```js
frappe.ui.form.on("Bank Reconciliation", "onload", function(frm){
 frm.set_query("bank_account", function(){
 return {
 "filters": [
 ["Bank Account", "account_type", "=", "Bank"],
 ["Bank Account", "group_or_ledger", "!=", "Group"]
 ]
 }
 });
});
```
---

### 2. Calling a Different Method to Generate Results

You can also set a server side method to be called on the query:

```js
frm.set_query("item_code", "items", function() {
 return {
 query: "erpnext.controllers.queries.item_query",
 filters: frm.doc.enquiry_type === "Maintenance" ?
 {"is_service_item": "Yes"} : {"is_sales_item": "Yes"}
 };
});
```


#### Custom Method

The custom method should return a list of items for auto select. If you want to send additional data, you can send multiple columns in the list.

Parameters to the custom method are:

```py
def custom_query(doctype, txt, searchfield, start, page_len, filters)
```

**Example:**

```py
# searches for leads which are not converted
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def lead_query(doctype, txt, searchfield, start, page_len, filters):
 return frappe.db.sql("""
 SELECT name, lead_name, company_name
 FROM `tabLead`
 WHERE docstatus < 2
 AND ifnull(status, '') != 'Converted'
 AND ({key} LIKE %(txt)s
 OR lead_name LIKE %(txt)s
 OR company_name LIKE %(txt)s)
 {mcond}
 ORDER BY
 IF(LOCATE(%(_txt)s, name), LOCATE(%(_txt)s, name), 99999),
 IF(LOCATE(%(_txt)s, lead_name), LOCATE(%(_txt)s, lead_name), 99999),
 IF(LOCATE(%(_txt)s, company_name), LOCATE(%(_txt)s, company_name), 99999),
 name, lead_name
 LIMIT %(start)s, %(page_len)s
 """.format(**{
 'key': searchfield,
 'mcond':get_match_cond(doctype)
 }), {
 'txt': "%{}%".format(txt),
 '_txt': txt.replace("%", ""),
 'start': start,
 'page_len': page_len
 })
```

**Note:** `@frappe.whitelist()` is used to expose `lead_query` to the client-side
and `@frappe.validate_and_sanitize_search_inputs` decorator is used to validate and sanitize user inputs sent through API or client-side request to avoid possible SQLi.

For more examples see:

[https://github.com/frappe/erpnext/blob/develop/erpnext/controllers/queries.py](https://github.com/frappe/erpnext/blob/develop/erpnext/controllers/queries.py)

<!-- page: framework/framework__user__en__guides__app-development__running-background-jobs.md -->
---
title: "Running Background Jobs\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/running-background-jobs"
updated: "2026-02-17"
---


Sometimes you may not want a user request to be executed immediately but added to a queue that will be executed by a background worker. The advantage of doing this is that your web workers remain free to execute other requests and longer jobs do not eat up all of your resources.

Frappe uses Python RQ to run background jobs. The following example illustrates how you can enqueue a job:

```python
import frappe

def long_job(arg1, arg2):
 frappe.publish_realtime('msgprint', 'Starting long job...')
 # this job takes a long time to process
 frappe.publish_realtime('msgprint', 'Ending long job...')

def enqueue_long_job(arg1, args2):
 frappe.enqueue('myapp.mymodule.long_job', arg1=arg1, arg2=arg2)
```

This will enqueue `long_job` to the queue `default`. Other available queues are `long` and `short`. You should choose the appropriate queue based on how long you estimate your enqueued job to execute.

Starting Version 14, you can also enqueue jobs at front of the queue by passing `at_front` as `True` in your enqueue call.

#### Called delayed actions on Document objects

You can also called delayed actions on document objects, for example in Stock Reconciliation if there are more than 100 items, it is executed as a background job.

Example: you can call `doc.queue_action('submit')`

Note: This only works for `save`, `submit`, `cancel`

You can also push certain actions to the background if you anticipate the execution is very large.

For example:

```python
def submit(self):
 if len(self.items) > 100:
  self.queue_action('submit')
 else:
  self._submit()
```

#### Debugging

If you are on `bench start`

You will see logs in your terminal.

Note: default worker does not auto restart, so you will have to kill bench and start again after you make changes.

<!-- page: framework/framework__user__en__guides__app-development__single-type-doctype.md -->
---
title: "Single Type Doctype\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/single-type-doctype"
updated: "2026-02-17"
---


DocTypes have a table associated with them. For example DocType **Customer** will have a table `tabCustomer` associated with it.

**Single** type DocTypes have no table associated and there is only one Document for it. This is similar to the Singleton pattern in Java. Single DocTypes are ideal for saving Settings (that are globally applicable) and for wizard / helper type forms that have no documents, but when the DocType is used for the Form UI.

The data in Single DocType is stored in `tabSingles` (`doctype`, `field`, `value`)

#### Examples

In Frappe, Single types are **System Settings** and **Customize Form**

<!-- page: framework/framework__user__en__guides__app-development__trigger-event-on-deletion-of-grid-row.md -->
---
title: "Trigger Event On Deletion Of Grid Row\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/trigger-event-on-deletion-of-grid-row"
updated: "2026-02-17"
---


To trigger an event when a row from a Child Table has been deleted (when user clicks on `delete` button), you need to add a handler the `fieldname_remove` event to Child Table, where fieldname is the fieldname of the Child Table in Parent Table declaration.

For example:

Assuming that your parent DocType is named `Item` has a Table Field linked to `Item Color` DocType with decloration name `color`.

In order to "catch" the delete event:

```js
frappe.ui.form.on('Item Color', {
 color_remove: function(frm) {
 // You code here
 // If you console.log(frm.doc.color) you will get the remaining color list
 }
);
```

The same process is used to trigger the add event (when user clicks on `add row` button):

```js
frappe.ui.form.on('Item Color', {
 color_remove: function(frm) {
 // You code here
 // If you console.log(frm.doc.color) you will get the remaining color list
 },
 color_add: function(frm) {}
});
```

Notice that the handling is be made on Child DocType Table `form.ui.on` and not on Parent Doctype so a minimal full example is:


```js
frappe.ui.form.on('Item',{
 // Your client side handling for Item
});

frappe.ui.form.on('Item Color', {
 color_remove: function(frm) {
 // Deleting is triggered here
 }
);
```

Handlers are:

1. fieldname_add
1. fieldname_move
1. fieldname_before_remove
1. fieldname_remove

<!-- page: framework/framework__user__en__guides__app-development__using-html-templates-in-javascript.md -->
---
title: "Using Html Templates In Javascript"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/app-development/using-html-templates-in-javascript"
updated: "2026-05-10"
---

Often while building javascript interfaces, there is a need to render DOM as an HTML template. Frappe Framework uses John Resig's Microtemplate script to render HTML templates in the Desk application.

&gt; Note 1: In Frappe we use the Jinja-like `{% raw %}{%{% endraw %}` tags to embed code rather than the standard `&lt;%`

&gt; Note 2: Never use single quotes `'` inside the HTML template.

To render a template,

1. Create a template `html` file in your app. e.g. `address_list.html`
2. Add it to `build.json` for your app (you can include it in `frappe.min.js` or your own javascript file).
3. To render it in your app, use `frappe.render(frappe.templates.address_list, {[context]})`

#### Example Template:

From `erpnext/public/js/templates/address_list.js`


```
<p>
    <button class="btn btn-sm btn-default btn-address">New Address</button>
</p>

{% for(var i=0, l=addrlist.length; i&lt;l; i++) { %}
    &lt;hr&gt;
    {%= _("Edit") %}
    {%= addr_list[i].address_type %}

    {% if(addr_list[i].is_primary_address) { %}
        {%= __("Primary") %}
    {% } %}

    {% if(addr_list[i].is_shipping_address) { %}
        {%= __("Shipping") %}
    {% } %}

    {%= addr_list[i].display %}
{% } %}

{% if(!addrlist.length) { %}
    {%= _("No address added yet.") %}
{% } %}
```

<!-- page: framework/framework__user__en__guides__automated-testing.md -->
---
title: "Automated Testing\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/automated-testing"
updated: "2026-02-17"
---


Frappe Provides you a test framework to write and execute tests that can be run directly on a Continuous Integration Tool like Travis

You can write server-side unit tests or UI tests

<!-- page: framework/framework__user__en__guides__automated-testing__integration-testing.md -->
---
title: "UI Integration Testing\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/automated-testing/integration-testing"
updated: "2026-02-17"
---


You can write integration tests using [Cypress](https://cypress.io). It is a NodeJS based full-stack testing framework which doesn't rely on Selenium.

To write integration tests, create a `.js` file in the `cypress/integration` directory.

### Example

Here is an example of an integration test to check insertion of a To Do

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

Cypress uses any chromium based browser installed on your system to run tests. Every app has it's own cypress test suite.
For example, to run test for the `frappe` app, run the following commands

```sh
cd ~/frappe-bench/apps/frappe
yarn cypress:open
```

This will open the Cypress Electron shell where you can run any test manually or run all of the tests.

[Screenshot on the live page]

<!-- page: framework/framework__user__en__guides__automated-testing__qunit-testing.md -->
---
title: "UI Testing with Frappe API\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/automated-testing/qunit-testing"
updated: "2026-02-17"
---


You can either write integration tests, or directly write tests in Javascript using [QUnit](http://api.qunitjs.com/)

QUnit helps you write UI tests using the QUnit framework and native frappe API. As you might have guessed, this is a much faster way of writing tests.

### Test Runner

To write QUnit based tests, add your tests in the `tests/ui` folder of your application. Your test files must begin with `test_` and end with `.js` extension.

To run your files, you can use the **Test Runner**. The **Test Runner** gives a user interface to load all your QUnit tests and run them in the browser.

In the CI, all QUnit tests are run by the **Test Runner** using `frappe/tests/test_test_runner.py`

[Screenshot on the live page]

### Running Tests

To run a Test Runner based test, use the `run-ui-tests` bench command by passing the name of the file you want to run.

 bench run-ui-tests --test frappe/tests/ui/test_list.js

This will pass the filename to `test_test_runner.py` that will load the required JS in the browser and execute the tests

### Debugging Tests

To debug a test, you can open it in the **Test Runner** from your UI and run it manually to see where it is exactly failing.

### Test Sequence

In Frappe UI tests are run in a fixed sequence to ensure dependencies.

The sequence in which the tests will be run will be in `tests/ui/tests.txt`
file.

### Running All UI Tests

To run all UI tests together for your app run

 bench run-ui-tests --app [app_name]

This will run all the files in your `tests/ui` folder one by one.

### Example QUnit Test

Here is the example of the To Do test in QUnit

 QUnit.test("Test quick entry", function(assert) {
 assert.expect(2);
 let done = assert.async();
 let random_text = frappe.utils.get_random(10);

 frappe.run_serially([
 () => frappe.set_route('List', 'ToDo'),
 () => frappe.new_doc('ToDo'),
 () => frappe.quick_entry.dialog.set_value('description', random_text),
 () => frappe.quick_entry.insert(),
 (doc) => {
 assert.ok(doc && !doc.__islocal);
 return frappe.set_route('Form', 'ToDo', doc.name);
 },
 () => assert.ok(cur_frm.doc.description.includes(random_text)),

 // Delete the created ToDo
 () => frappe.tests.click_page_head_item('Menu'),
 () => frappe.tests.click_dropdown_item('Delete'),
 () => frappe.tests.click_page_head_item('Yes'),

 () => done()
 ]);
 });

### Writing Test Friendly Code with Promises

Promises are a great way to write test-friendly code. If your method calls an aysnchronous call (ajax), then you should return an `Promise` object. While writing tests, if you encounter a function that does not return a `Promise` object, you should update the code to return a `Promise` object.

<!-- page: framework/framework__user__en__guides__automated-testing__unit-testing.md -->
---
title: "Unit Testing"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/guides/automated-testing/unit-testing"
updated: "2026-03-06"
---

## 1.Introduction

Frappe provides some basic tooling to quickly write automated tests. There are some basic rules:

1. Test can be anywhere in your repository but must begin with `test_` and should be a `.py` file.
2. Tests must run on a site that starts with `test_`. This is to prevent accidental loss of data.
3. Test stubs are automatically generated for new DocTypes.
4. Frappe test runner will automatically build test records for dependant DocTypes identified by the `Link` type field (Foreign Key)
5. Tests can be executed using `bench run-tests`
6. For non-DocType tests, you can write simple unittests and prefix your file names with `test_`.

## Writing Tests for DocTypes

### 2.1. Writing DocType Tests:

1. Test cases are in a file named `test_[doctype].py`
2. You must create all dependencies in the test file
3. Create a Python module structure to create fixtures / dependencies

#### Example (for `test_event.py`):

```
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
import frappe.defaults

from frappe.tests.utils import FrappeTestCase


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
    "subject":"_Test Event 2",
    "starts_on": "2014-01-01",
    "event_type": "Private"
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


class TestEvent(FrappeTestCase):
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

    def test_allowed_private_if_in_event_user(self):
        doc = frappe.get_doc("Event", frappe.db.get_value("Event",
        {"subject":"_Test Event 3"}))

        frappe.set_user("test1@example.com")
        self.assertTrue(frappe.has_permission("Event", doc=doc))

    def test_event_list(self):
        frappe.set_user("test1@example.com")
        res = frappe.get_list("Event", filters=[["Event", "subject", "like", "_Test Event%"]], fields=["name", "subject"])
        self.assertEqual(len(res), 2)
        subjects = [r.subject for r in res]
        self.assertTrue("_Test Event 1" in subjects)
        self.assertTrue("_Test Event 3" in subjects)
        self.assertFalse("_Test Event 2" in subjects)
```

## 2. Running Tests

This function will build all the test dependencies and run your tests.  
You should run tests from "frappe_bench" folder. Without options all tests will be run.

 bench run-tests

If you need more information about test execution - you can use verbose log level for bench.

 bench --verbose run-tests

### Options:

```
 --app <appname>
 --doctype <doctype>
 --test <specifictest>
 --module <module> (Run a particular module that has tests)
 --profile (Runs a Python profiler on the test)
 --junit-xml-output<pathtoxml> (The command provides test results in the standard XUnit XML format)
```

#### 2.1. Example for app:

All applications are located in folder: "~/frappe-bench/apps".  
We can run tests for each application.

- frappe-bench/apps/erpnext/
- frappe-bench/apps/erpnext_demo/
- frappe-bench/apps/frappe/

```
 bench run-tests --app erpnext
 bench run-tests --app erpnext_demo
 bench run-tests --app frappe
```

#### 2.2. Example for doctype:

```
 frappe@erpnext:~/frappe-bench$ bench run-tests --doctype "Activity Cost"
 .
 ----------------------------------------------------------------------
 Ran 1 test in 0.008s

 OK
```

#### 2.3. Example for test:

Run a specific case in User:

```
 frappe@erpnext:~/frappe-bench$ bench run-tests --doctype User --test test_get_value
 .
 ----------------------------------------------------------------------
 Ran 1 test in 0.005s

 OK
```

#### 2.4. Example for module:

If we want to run tests in the module:

 /home/frappe/frappe-bench/apps/erpnext/erpnext/support/doctype/issue/test_issue.py

We should use module name like this (related to application folder)

 erpnext.support.doctype.issue.test_issue

##### Example:

```
 frappe@erpnext:~/frappe-bench$ bench run-tests --module "erpnext.stock.doctype.stock_entry.test_stock_entry"
 ...........................
 ----------------------------------------------------------------------
 Ran 27 tests in 30.549s
```

#### 2.5. Example for profile:

```
 frappe@erpnext:~/frappe-bench$ bench run-tests --doctype "Activity Cost" --profile
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
```

#### 2.6 Running Tests without creating fixtures or before_tests hook

- When you are building a feature it is useful to write tests without building test dependencies (i.e build fixtures for linked objects), with `--skip-test-records`  
- You can also skip the test initialisation script with `--skip-before-tests`

Example  

```
bench --site school.erpnext.local run-tests --doctype "Student Group" --skip-test-records --skip-before-tests
```

### 3.0 FrappeTestCase

`FrappeTestCase` is Frappe Framework specific TestCase class extended from `unittest.TestCase`. Inherting this class in your tests ensures:  



1. `frappe.local.flags` and other most used local proxies are reset after test case runs.
2. database - a new [database transaction](https://frappeframework.com/docs/v14/user/en/api/database#database-transaction-model) is started before testcase begins and rolled back after tests are finished.

Usage 

```python
# app/doctype/dt/test_dt.py  
  
from frappe.tests.utils import FrappeTestCase  
  
class TestDt(FrappeTestCase):  
 @classmethod  
 def setUpClass(cls):  
 super().setUpClass() # important to call super() methods when extending TestCase.   
 ...
```

## Writing XUnit XML Tests

##### How to run:

```
bench run-tests --junit-xml-output=/reports/junit_test.xml
```

##### Example of test report:

```
 <testsuite tests="3">
 <testcase classname="foo1" name="ASuccessfulTest">
 <testcase classname="foo2" name="AnotherSuccessfulTest">
 <testcase classname="foo3" name="AFailingTest">
 <failure type="NotEnoughFoo"> details about failure </failure>
 </testcase>
 </testcase></testcase></testsuite>
```

It’s designed for the CI Jenkins, but will work for anything else that understands an XUnit-formatted XML representation of test results.

#### Jenkins configuration support:

1. You should install xUnit plugin - [https://wiki.jenkins-ci.org/display/JENKINS/xUnit+Plugin](https://wiki.jenkins-ci.org/display/JENKINS/xUnit+Plugin)
2. After installation open Jenkins job configuration, click the box named “Publish JUnit test result report” under the "Post-build Actions" and enter path to XML report:

(Example: *reports/*.xml*)
