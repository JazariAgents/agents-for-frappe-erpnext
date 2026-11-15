<!-- Frappe documentation: framework, part 24 of 24. Index: docs/INDEX.md -->

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

[Screenshot on the live page: Dropdown for OAuth Client]  


Select "New OAuth Client" from the dropdown, and you'll be taken to a page for adding the OAuth scopes and settings for the application you want to add OAuth for.

[Screenshot on the live page: New OAuth Client]  


Here, you have to configure the:

* App Name (Grafana here)
* Open ID scopes
* Redirect URIs

The redirect URI for Grafana from their docs is `<grafana-url>/login/generic_oauth`. > If you’re on a server without a URL, you can provide the IP address of the server for the `<grafana-url>` part.

Once you have added the details in the respective fields, you will receive an `App Client ID` and `App Client Secret`. These will be used in the Grafana configuration for the OAuth setup.

[Screenshot on the live page: OAuth Client details added]  


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

[Screenshot on the live page: Signin with Frappe Grafana]  


If you have done everything correctly, you'll be logged into Grafana with the credentials from your Frappe site.

[Screenshot on the live page: Logging in with Frappe GIF]  

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

[Screenshot on the live page: Web Form]

## Creating a Web Form

To create a Web Form, type "new web form" in awesomebar and hit enter.

1. Enter Title
2. Select DocType for which the record should be created.
3. Add some introduction (Optional).
4. Click on "Get Fields" button to get all fields from selected doctype OR select fields for your web form.
5. Publish it and you are good to go.

[Screenshot on the live page: Create Web Form]

[Screenshot on the live page: Web Form Fields]

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

[Screenshot on the live page: Web Form Field Layout]

[Screenshot on the live page: Web Form Layout]

## Multi Step Webform

Updating the layout makes webform look better but still if webform has many fields it becomes lengthy.  
We can add `Page Breaks` to segregate the sections in different pages (called as Multi Step Webform).

> You can add maximum 9 Page Breaks which will only allow 10 Pages.

[Screenshot on the live page: Web Form Page Break]

[Screenshot on the live page: Step Web Form Page 1]

[Screenshot on the live page: Step Web Form Page 2]

> All the customization options mentioned below can be done from the Customization Tab of webform document.

## Submit Button Label

You can change the label of submit button on the webform.

[Screenshot on the live page: Web Form Submit Label]

## Banner Image

You can now add banner image on webform.

[Screenshot on the live page: Banner Image]

## Breadcrumbs

You can customize the breadcrumbs in a Web Form by adding JSON object.

> Breadcrumbs are only visible if the webform `[list view](/framework/v14/user/en/web-form/settings#list-settings)` is enabled.

Example:

[Screenshot on the live page: Custom Breadcrumbs]

[Screenshot on the live page: Webform Breadcrumbs]

## After Submit Page

You can give custom success title and message which will appear after user has submitted the webform.

[Screenshot on the live page: Webform Success Title & Message]

[Screenshot on the live page: Webform Success Page]

Based on the access extra buttons will be visible on the submit page like 

 See previous responses

 Edit your response

 View your response  
 & 

 Submit another response

[Screenshot on the live page: Webform Success Page]

If the Web Form is opened through a [Web Form Request](vscode-file://vscode-app/framework/user/en/web-form/web-form-request), these action links preserve the request key where needed.

Configure your webform to redirect to a specific URL after 5 seconds after it has been submitted by setting `success_url` field.

[Screenshot on the live page: Webform Breadcrumbs]



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

[Screenshot on the live page: Web Form Custom CSS]

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

[Screenshot on the live page: Web Form]



### Show List

It will enable `List View` where you can see all the submitted forms. You can only open the form that you own. 

[Screenshot on the live page: Web Form]





> If `apply_document_permissions` is enabled you can open other forms.

### Title & List Columns

You can change the title of the list and also can add/remove/arrange list view columns 

[Screenshot on the live page: Web Form]



[Screenshot on the live page: Web Form]



## Sidebar Settings

[Screenshot on the live page: Web Form]



### Show Sidebar

Show webform with sidebar. Select or create a website sidebar where you can add link to current webform and other related webforms or webpages. 

[Screenshot on the live page: Web Form]

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

[Screenshot on the live page: zero downtime migration]

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

[Screenshot on the live page: Page DocType!]

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

[Screenshot on the live page: Vue Works]
