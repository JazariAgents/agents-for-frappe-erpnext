<!-- Frappe documentation: framework, part 22 of 24. Index: docs/INDEX.md -->

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

[Screenshot on the live page]

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
