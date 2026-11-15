<!-- Frappe documentation: framework, part 6 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__user__en__api__query-builder.md -->
---
title: "Query Builder\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/query-builder"
updated: "2026-04-23"
---

`frappe.qb` is a query builder written around PyPika to build a single interface for cross-db queries

While developing apps, you'll often need to retrieve some specific data from the database. One way to do this is to use `frappe.db.sql` and write raw SQL queries.

Maybe something like

```python
result = frappe.db.sql(
 f"""
 SELECT `path`,
 COUNT(*) as count,
 COUNT(CASE WHEN CAST(`is_unique` as Integer) = 1 THEN 1 END) as unique_count
 FROM `tabWeb Page View`
 WHERE `creation` BETWEEN {some_date} AND {some_later_date}
 """
)
```

The query builder API makes this easier by providing a simple pythonic API to build SQL queries without limiting the flexibility of handwritten SQL.

The same query in the query builder would look something like

```python
import frappe
from frappe.query_builder import DocType
from frappe.query_builder.functions import Count
from pypika.terms import Case

WebPageView = DocType("Web Page View") # you can also use frappe.qb.DocType to bypass an import

count_all = Count('*').as_("count")
case = Case().when(WebPageView.is_unique == "1", "1")
count_is_unique = Count(case).as_("unique_count")

result = (
 frappe.qb.from_(WebPageView)
 .select(WebPageView.path, count_all, count_is_unique)
 .where(Web_Page_View.creation[some_date:some_later_date])
).run()
```

## frappe.qb

Returns a Pypika query object which lets you build queries. Queries built using this object will be a  
type from `pypika.dialects`, sprinkled with some Frappe sugar. Some of its methods are:

### frappe.qb.from_(doctype)

lets you construct a from query to select data

**Select query**

```python
query = frappe.qb.from_('Customer').select('id', 'fname', 'lname', 'phone')
```

The SQL query built is

```sql
SELECT `id`,`fname`,`lname`,`phone` FROM `tabCustomer`
```

**A complex Select example**

```python
customers = frappe.qb.DocType('Customer')
q = (
 frappe.qb.from_(customers)
 .select(customers.id, customers.fname,customers.lname, customers.phone)
 .where((customers.fname == 'Max') | (customers.id.like('RA%')) )
 .where(customers.lname == 'Mustermann')
)
```

The SQL query built is

```sql
SELECT `id`,`fname`,`lname`,`phone` FROM `tabCustomer` WHERE (`fname`='Max' OR `id` LIKE 'RA%') AND `lname`='Mustermann'
```

Some noteworthy things

- We have created a `customers` variable to refer to the table in the query.
- Select can take any number of arguments, selecting various Fields.
- The '|' (pipe) or '&' (ampersand) operators can be used to refer to 'OR' or 'AND'.
- Chaining the `where()` method appends 'AND' by default

You can read more about the other functions at the [Pypika](https://github.com/kayak/pypika) repo.

### frappe.qb.Doctype(name_of_table)

Returns a PyPika table object which can be used elsewhere. It will automatically add 'tab' if necessary.

### frappe.qb.Table(name_of_table)

Does the same thing as `frappe.qb.DocType` but will not append 'tab'. It's intended to be used with '__Auth' like tables.

> Note: You should only use this if you know what you are doing.

### frappe.qb.Field(name_of_coloum)

Return a PyPika field object, this represents a column. They are usually used to compare columns with values.

One example would be

```python
lname = frappe.qb.Field("lname")
q = frapppe.qb.from_("customers").select("*").where(lname == 'Mustermann')
```

## Executing queries

Queries built using the `frappe.qb` namespace are PyPika objects. They will have to be converted to string objects so that your database management system can recognize them.

To check how your query object translates, you can type cast it with `str` or use the `.get_sql` method they come with.

```python
query = frappe.qb.from_('Customer').select('id', 'fname', 'lname', 'phone')

str(query)
# SELECT "id","fname","lname","phone" FROM "tabCustomer"

query.get_sql()
# SELECT "id","fname","lname","phone" FROM "tabCustomer"

str(query) == query.get_sql()
# True
```

### Walk method

All queries built through `frappe.qb` are parameterized by default. All input fields, raw values, and functions are separated as Named parameters and sent to the database as a dictionary. Parameterization is done to sanitize queries which would prevent SQL injections.

You use the `walk` method to check out which parts are parameterized. It returns the parameterized query and the corresponding dictionary.

```py
doctype = frappe.qb.DocType("DocType")

frappe.qb.from_(doctype).select('*').where(doctype.name == "somename").walk()
# ('SELECT * FROM `tabDocType` WHERE `name`=%(param1)s', {'param1': 'somename'})
```

### Run method

This is the most preferred method to execute your queries. Every valid query has the `run` method which you  
may use to execute the query with.

```python
frappe.qb.from_('Customer').select('id', 'fname', 'lname', 'phone').run()
```

The `run` method accepts `kwargs` which will be passed on while the query is being executed. You may pass whatever options are available in `frappe.db.sql`, through the `run` method.

To run debug on your query, or get the result in the form of List[Dict], you may use the following respectively:

```python
In [7]: frappe.qb.from_('ToDo').select('name').run(debug=True)
SELECT "name" FROM "tabToDo"
Execution time: 0.0 sec
Out[7]: [('8d765f73a2',)]

In [8]: frappe.qb.from_('ToDo').select('name').run(as_dict=True)
Out[8]: [{'name': '8d765f73a2'}]
```

> The `run` method internally calls the lower level `frappe.db.sql` API.

### frappe.db.sql

ou may choose to directly pass your query objects to `frappe.db.sql` too. This ignores permisions and paramaterisation of queries.

```python
query = frappe.qb.from_('Customer').select('id', 'fname', 'lname', 'phone')
frappe.db.sql(query)
```

## frappe.query_builder.functions

This module provides standard functions you might need while building queries, like `Count()` and `Sum().`

### Joins and Sub-queries

You can check [pypika documentation](https://pypika.readthedocs.io/en/latest/2_tutorial.html#joining-tables-and-subqueries) to join tables and add subqueries. Instead of `Table`, use `frappe.qb.DocType`

Example:

```
HasRole = frappe.qb.DocType('Has Role')
CustomRole = frappe.qb.DocType('Custom Role')

query = (frappe.qb.from_(HasRole)
 .inner_join(CustomRole)
 .on(CustomRole.name == HasRole.parent)
 .select(CustomRole.page, HasRole.parent, HasRole.role))
```

### Simple functions

Say you want to count all the entries in a Notes table. You could do something like

```python
from frappe.query_builder.functions import Count

Notes = frappe.qb.DocType("Notes")
count_pages = Count(Notes.content).as_("Pages")

result = frappe.qb.from_(Notes).select(count_pages).run(as_dict=True)
```

### JSON functions

> Note: This is available on v16+

These helpers make JSON queries portable across MariaDB and Postgres by mapping to the correct SQL dialect internally. 

Use cases:

1. Read JSON object values by path
2. Read scalar/text values for filtering
3. Check whether JSON object/array contains a value

Available helpers:

1. `JSONExtract(field, path)`
2. `JSONValue(field, path)`
3. `JSONContains(target, candidate)`

Example: JSON object field

```python
import frappe
from frappe.query_builder.functions import JSONExtract, JSONValue

CustomerProfile = frappe.qb.DocType("Customer Profile")

# preferences_json:
# {"notifications": {"email": true, "sms": false}, "language": "en"}

query = (
    frappe.qb.from_(CustomerProfile)
    .select(
        CustomerProfile.customer_name,
        JSONValue(CustomerProfile.preferences_json, "$.language").as_("preferred_language"),
        JSONValue(CustomerProfile.preferences_json, "$.notifications.email").as_("email_notifications"),
    )
    .where(JSONValue(CustomerProfile.preferences_json, "$.notifications.email") == "true")
)
```

Example: JSON list field

```
import frappe
from frappe.query_builder.functions import JSONContains, JSONExtract

SalesOrder = frappe.qb.DocType("Sales Order")

# applied_discounts_json:
# {"codes": ["WELCOME10", "FREESHIP", "VIP"]}

query = (
    frappe.qb.from_(SalesOrder)
    .select(SalesOrder.name, SalesOrder.customer)
    .where(JSONContains(JSONExtract(SalesOrder.applied_discounts_json, "$.codes"), "FREESHIP"))
)
```

### Custom Functions

`frappe.query_builder.functions` is a superset of `pypika.functions`, so it has all PyPika functions and some custom ones we made. You can make your custom functions by importing the `CustomFunction` class from PyPika

One implementation of the DateDiff function

```python
from pypika import CustomFunction

customers = Tables('Customer')
DateDiff = CustomFunction('DATE_DIFF', ['interval', 'start_date', 'end_date'])

q = Query.from_(customers).select(
 DateDiff('day', customers.created_date, customers.updated_date)
)
```

If we print `q`, we would get

```SQL
SELECT DATE_DIFF('day',"created_date","updated_date") FROM "Customer"
```

> Notice how we specify arguments and the actual SQL text. The exact format might not work for more complex functions. The advanced section covers more complicated methods.

### Constant Column

`ConstantColumn` is a class to define a pseudo column with a constant value. 

```py
from frappe.query_builder.custom import ConstantColumn

frappe.qb.from_("DocType").select("name", ConstantColumn("john").as_("user"))
# SELECT `name`,'john' `user` FROM `tabDocType`
```

Here we define a column user with the value "john."

## Advanced

### Special functions

One such function is [Match Against](https://mariadb.com/kb/en/match-against/). It's different because it has a chained against argument. To implement something like this you need to inherit from PyPika's `DistinctOptionFunction` class.

The current MATCH class looks something like

```python

from pypika.functions import DistinctOptionFunction
from pypika.utils import builder

class MATCH(DistinctOptionFunction):
 def __init__(self, column: str, *args:
 super(MATCH, self)._init_(" MATCH", column, *args)
 self._Against = False

 def get_function_sql(self, **kwargs):
 s = super(DistinctOptionFunction, self).get_function_sql(**kwargs)

 if self._Against:
 return f"{s} AGAINST (f'+{self._Against}*') IN BOOLEAN MODE)"
 return s

 @builder
 def Against(self, text: str):
 self._Against = text
```

- The `__init__()` method works similar to CustomFunction class above. You mention all the arguments and the SQL text.
- The `Against()` method only stores a value that will be used in the `get_function_sql()`
- It also has the `@builder` wrapper. In short, it lets these functions be chainable by making a copy of the object.
- We have wrapped the `get_function_sql()` method, which allows us to append the required SQL text for Against.
- this can further be extended to use any number other chains.

In use, the Match class looks like this

```python
from frappe.query_builder.functions import Match

match = Match("Coloum name").Against("Some_text_match")
# MATCH('Coloum name') AGAINST ('+Some_text_match*' IN BOOLEAN MODE)
```

### Utils

**ImportMapper(dict)**

In the rare case where you have different functions for different SQL dialects, Which do the same thing, you can use the ImportMapper Utility. It maps functions based on the SQL dialect, so one query works across different SQL dialects.

It takes in a dict which maps functions to databases.

For example the the mapping for GroupConat looks like this

```python

from frappe.query_builder.utils import ImportMapper, db_type_is
from frappe.query_builder.custom import GROUP_CONCAT, STRING_AGG

GroupConcat = ImportMapper(
 {
 db_type_is.MARIADB: GROUP_CONCAT,
 db_type_is.POSTGRES: STRING_AGG
 }
)
```

<!-- page: framework/framework__user__en__api__realtime.md -->
---
title: "Realtime (socket.io)"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/realtime"
updated: "2026-06-12"
---

Frappe ships with an API for realtime events based on [socket.io](https://socket.io/). Since socket.io needs a Node server to run, we run a Node process in parallel to the main web server.

## Client APIs (JavaScript)

## frappe.realtime.on

To listen to realtime events on the client (browser), you can use the `frappe.realtime.on` method:

```
frappe.realtime.on('event_name', (data) => {
    console.log(data)
})
```

## frappe.realtime.off

Stop listening to an event you have subscribed to:

```
frappe.realtime.off('event_name')
```

## Server APIs (Python)

## frappe.publish_realtime

To publish a realtime event from the server, you can use the `frappe.publish_realtime` method:

```
frappe.publish_realtime('event_name', data={'key': 'value'})
```

## frappe.publish_progress

You can use this method to show a progress bar in a dialog:

```
frappe.publish_progress(25, title='Some title', description='Some description')
```

[Screenshot on the live page: frappe publish realtime]

## **Custom Event Handlers (Python)**

> Note: This feature is only available in nightly version. This feature is considered experimental.

You can implement custom real-time event handlers by creating a file `your_app/your_app/realtime/handlers.py` in your custom app. The syntax is fairly similar with API whitelists.



```python
from frappe.realtime import realtime

@realtime.on(
  "project_subscribe",
  frappe_context=False,   # open a Frappe context (DB + session) for the handler body
  allow_guest=False,      # if False, the event is dropped when socket.user == "Guest"
)
```

Defaults: `frappe_context=False`, `allow_guest=False`

### **Example**

```python
import frappe
from frappe.realtime import Socket, realtime

@realtime.on("project_subscribe")
def project_subscribe(socket: Socket, project: str) -> None:
    if socket.has_permission("Project", project):
        socket.join(f"project:{project}")
```



The first argument is always the typed `Socket`. The rest are the payload the client sent, positionally. The event name `"project_subscribe"` is what the browser emits with `frappe.realtime.emit(...)`.

### **Working example with frappe_context=True**

With `frappe_context=True` the full ORM is available in the handler body — `frappe.get_doc`, `frappe.local.site`, `frappe.session.user` are all populated and reflect the authenticated socket user.



This example handler loads a doc, checks permission, and emits the result back to the client:  

```python
@realtime.on("test_get_doc", frappe_context=True)
def test_get_doc(socket: Socket, doctype: str, docname: str) -> None:
    import frappe
    try:
        doc = frappe.get_doc(doctype, docname)
        doc.check_permission()
        socket.emit(
            "test_get_doc_result",
            {
                "ok": True,
                "site": frappe.local.site,
                "user": frappe.session.user,
                "doctype": doc.doctype,
                "name": doc.name,
                "modified": str(doc.get("modified")),
            },
        )
    except Exception as e:
        socket.emit("test_get_doc_result", {"ok": False, "error": f"{type(e).__name__}: {e}"})
```



From the browser:

```js
frappe.realtime.on("test_get_doc_result", (r) => console.log(r));
frappe.realtime.emit("test_get_doc", "User", "Administrator");
```

See [Permission checks](#permission-checks-two-ways)  section for the cost and when to prefer the cheap HTTP based permission check instead.



A handler runs only if its owning app is installed on the connecting site. The owning app is detected automatically from the import.

You may have to restart the socketio server to see code changes take effect. See the [Socket.IO docs](https://socket.io/docs/v4/) for more on writing custom event handlers.

### **Socket object**

Read-only identity, populated at connect:

```python
socket.site            # the site this socket is on
socket.user            # "Guest" for anonymous
socket.user_type       # e.g. "System User"
socket.installed_apps  # list of installed apps
```



Rooms, emit and transient state:

```python
socket.join(room)                        # add this socket to a room
socket.leave(room)                       # remove it
socket.emit(event, data=None, room=None) # emit to a room, or to this client if room is None
socket.get(key, default=None)            # read transient per-socket state
socket.set(key, value)                   # persist transient per-socket state (cleared on disconnect)
```



**Permission checks**

There are two ways to perform doctype permission checks.



**A. HTTP (default, recommended)** : `socket.has_permission(doctype, name)` asks the web process, exactly like the core handlers. No DB connection in the realtime process. Cheap. Use this unless you have a reason not to.

```python
if socket.has_permission("Project", project):
    socket.join(f"project:{project}")
```



B. **In-process (`frappe_context=True`)** : opens a full Frappe context for the handler body so you can call `frappe.has_permission(...)`, query the DB, etc. directly. Cost: every such event pays `frappe.init -> connect -> set_user -> commit/rollback -> destroy` and forces a DB connection into the realtime process. Use sparingly.

```python
@realtime.on("project_subscribe", frappe_context=True)
def project_subscribe(socket: Socket, project: str) -> None:
    if frappe.has_permission("Project", doc=project, ptype="read"):
        socket.join(f"project:{project}")
```

Full reference: ++[https://github.com/frappe/frappe/blob/develop/frappe/realtime/README.md](https://github.com/frappe/frappe/blob/develop/frappe/realtime/README.md)++

## **Custom Event Handlers (NodeJS)**

> **Available from v16.**  Considered experimental. This is the previous implementation and will be phased out in newer version. 
>
> Socket.IO server path; new apps should prefer the Python handlers above.



You can implement custom real-time event handlers by creating a `handlers.js` file in the `realtime` folder of your app.

You need a single export from this file — a function that sets up event handlers on the socket instance. E.g. for an app called "chat":

```javascript
// bench/apps/chat/realtime/handlers.js

function chat_app_handlers(socket) {
    socket.on("hello_chat", () => {
        console.log("hello world!");
    });
}

module.exports = chat_app_handlers;
```

Trigger this event from client-side code with `frappe.realtime.emit("hello_chat")`. You may have to restart the socketio server to see code changes take effect. See the [Socket.IO docs](https://socket.io/docs/v4/) for more on writing custom event handlers.

## **Pushing events to clients**

You do not emit from the web process directly — you publish through Redis, and the realtime server bridges it to the connected sockets. The room string you publish to must match the room your handler `join`-ed.

```python
from frappe.realtime import publish_to_room
publish_to_room("project:PROJ-0001", "project_updated", {"status": "Open"})
```



Other named helpers, each thin wrapper over `publish_realtime`.

```python
publish_to_user(user, event, message=None)
publish_to_doc(doctype, docname, event, message=None)
publish_to_doctype(doctype, event, message=None)
publish_task_progress(task_id, message=None)
publish_to_website(event, message=None)
publish_to_all(event, message=None)
publish_to_room(room, event, message=None)
```

Full reference: ++[https://github.com/frappe/frappe/blob/develop/frappe/realtime/README.md](https://github.com/frappe/frappe/blob/develop/frappe/realtime/README.md)++



# **Custom Client**

You can write a custom client to connect to the socket.io server if you're developing a SPA or a mobile app that doesn't use the Desk interface. Refer to the official [Socket.IO client docs](https://socket.io/docs/v4/client-initialization/).



Example custom clients:

- [gameplan/frontend/src/socket.js](https://github.com/frappe/gameplan/blob/9f9332cf29496afe5e912e4f1734fbf1142cb18c/frontend/src/socket.js#L13)
- [frappe/socketio_client.js](https://github.com/frappe/frappe/blob/8093a1d0a54900fe4b43b01ae6ffc0adf855da43/frappe/public/js/frappe/socketio_client.js#L49)

## **Authorization in custom clients**

Two ways to authenticate a connection with the socket.io server:

- **Cookies** — in a browser-like environment, the connection automatically sends cookies and the socketio server authenticates using them.
- **Authorization header** — if cookies are unavailable (e.g. mobile apps), use an `Authorization` header just like API requests. See the [REST API authentication docs](https://frappeframework.com/docs/user/en/api/rest#authentication) and [Socket.IO extraHeaders](https://socket.io/docs/v4/client-options/#extraheaders).



# **Implementation Notes**

- Realtime server uses the socket.io server, written in node.js, found in the `/realtime` directory.
- The realtime client is a wrapper around the socket.io client library, found in `public/js/frappe/socketio_client.js`.
- Python processes publish events to the node server over a Redis pub-sub channel. The realtime server subscribes to the Redis channel and republishes to all subscribed clients.
- The realtime server is multi-tenant: all site traffic is namespaced by sitename. Namespaces are created dynamically as `/{sitename}`, where `sitename` is the  site's folder name in the `sites` directory (or `frappe.local.site`).
- The realtime server uses the main Frappe web server to authenticate connections. The SID cookie or authorization header is passed to the client and used to ensure the connection is a valid user that can subscribe to DocTypes/documents per permissions.

## **Available rooms**


| Room                 | Access                                                                                                   |
| -------------------- | -------------------------------------------------------------------------------------------------------- |
| all                  | Connected by default for all System Users                                                                |
| website              | Accessible to any user, including Guests                                                                 |
| user:{username}      | Per-user room. Allowed without permission checks                                                         |
| doctype:{doctype}    | Per-DocType room. Only users with DocType permission may join; auto-subscribed on opening list/form view |
| doc:{doctype}/{name} | Per-document room. Only users with document permission may join; auto-subscribed on opening form view    |

<!-- page: framework/framework__user__en__api__rest.md -->
---
title: "REST API"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/rest"
updated: "2026-05-10"
---

Frappe framework generates REST API for all of your DocTypes out of the box. You can also run arbitrary python methods using their dotted module path.

Authentication
--------------

There are two ways to authenticate through Frappe REST API. Token based authentication and password based authentication.

### 1. Token Based Authentication

A token is a pair of API Key and API Secret. To generate these tokens follow these steps:

1. Go to User list and open a user.
2. Click on the "Settings" tab. (skip this step if you don't see tabs)
3. Expand the API Access section and click on Generate Keys.
4. You will get a popup with the API Secret. Copy this value and keep it somewhere safe (Password Manager).
5. You will also see another field "API Key" in this section.

The token is generated by concatenating `api_key` and `api_secret` with a colon `:`. Pass the string `token api_key:api_secret` to the `Authorization` header in the request.


```
fetch('http://&lt;base-url&gt;/api/method/frappe.auth.get_logged_user', {
    headers: {
        'Authorization': 'token api_key:api_secret'
    }
})
.then(r =&gt; r.json())
.then(r =&gt; {
    console.log(r);
})

```

```
➜ curl http://&lt;base-url&gt;/api/method/frappe.auth.get_logged_user -H "Authorization: token api_key:api_secret"

```
Every request you make with these tokens will be logged against the user you selected in Step 1. This also means that roles will be checked against this user. You can also create a new user just for API calls.

### 2. Password Based Authentication

Password based authentication relies on cookies and session data to maintain authentication in subsequent requests. In most cases, the library you are using to issue REST calls will handle session data, but if it doesn't you should use Token based authentication.


```
fetch('http://&lt;base-url&gt;/api/method/login', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        usr: 'username or email',
        pwd: 'password'
    })
})
.then(r =&gt; r.json())
.then(r =&gt; {
    console.log(r);
})

```

```
➜ curl --cookie-jar snowcookie --request POST "http://&lt;base-url&gt;/api/method/login" -H 'Content-Type: application/json' -H 'Accept: application/json' --data-raw "{ "usr" : "&lt;username&gt;", "pwd": "&lt;password&gt;" }"
{"message":"Logged In","home_page":"/app","full_name":"&lt;user:full_name&gt;","dashboard_route":"/sites"}

➜ curl --cookie snowcookie --request POST "http://&lt;base-url&gt;/api/method/frappe.auth.get_logged_user" -H 'Accept: application/json'
{"message":"&lt;username&gt;"}

```
### 3. Access Token

Refer documentation for [How to setup OAuth](/framework/v14/user/en/guides/integration/how_to_set_up_oauth).

Use the generated `access_token` in request header.


```
fetch('http://&lt;base-url&gt;/api/method/frappe.auth.get_logged_user', {
    headers: {
        'Authorization': 'Bearer access_token'
    }
})
.then(r =&gt; r.json())
.then(r =&gt; {
    console.log(r);
})

```
Listing Documents
-----------------

To get a list of records of a DocType, send a GET request at `/api/resource/:doctype`. By default, it will return 20 records and will only fetch the name of the records. The result for the query can be found under `data` of the payload.

We'll be using the ToDo DocType to show example responses for the queries below.


```
GET /api/resource/:doctype

```
Response


```
{
  "data":[
    {"name":"f765eef382"},
    {"name":"2a26fa1c64"},
    {"name":"f32c68060f"},
    {"name":"9065fa9832"},
    {"name":"419082fc38"},
    {"name":"6234d15099"},
    {"name":"62f2181ee0"},
    {"name":"a50afbbfaa"},
    ...
  ]
}

```
You can specify which fields to fetch in the `fields` param. It should be a JSON array.


```
GET /api/resource/:doctype?fields=["field1", "field2"]

```
Response


```
{
  "data":[
    {"description":"Business worker talk society. Each try theory prove notice middle. Crime couple trouble guy project hit.","name":"f765eef382"},
    {"description":"This reveal as look near sister. Car staff bar specific address.","name":"2a26fa1c64"},
    {"description":"Wear bag some walk. Movie partner new class tough run. Brother Democrat imagine.","name":"f32c68060f"},
    {"description":"Break laugh apply reveal new now focus heavy. Outside local staff research total. Else point try despite.","name":"9065fa9832"},
    {"description":"Truth reduce baby artist actually model. Cost phone us others himself wife almost. Language thing wonder share talk. Factor glass significant could window certain yet.","name":"419082fc38"},
    {"description":"Tv memory understand opportunity window beat physical.","name":"6234d15099"},
    {"description":"Should floor situation in response sell. Our assume company mean red majority shoulder.","name":"62f2181ee0"},
    {"description":"Performance seem sign recent. Court form me tonight simple trouble. Address job garden play teach. Happy speech amount offer change then.","name":"a50afbbfaa"},
    ...
  ]
}

```

You can specify which fields to expand in the `expand` param. It should be a JSON array.

```
GET /api/resource/:doctype?expand=["priority"]

```
Response


```
{
  "data":[
    {
        "name":"f765eef382"
        "priority": {
            "name":"a1b2c3", 
            "title": "Medium", 
            "creation": "2025-11-05 19:02:19.106966",
        },
    },
    {
        "name":"f765eef393"
        "priority": {
            "name":"a1b2c4", 
            "title": "High", 
            "creation": "2025-11-05 20:02:19.106966",
        },
    },
    ...
  ]
}

```

You can filter the records by passing `filters` param. Filters should be an array, where each filter is of the format: `[field, operator, value]`


```
GET /api/resource/:doctype?filters=[["field1", "=", "value1"], ["field2", "&gt;", "value2"]]

```
Response


```
{
  "data":[
    {"name":"f765eef382"},
    {"name":"2a26fa1c64"},
    {"name":"f32c68060f"},
    {"name":"9065fa9832"},
    {"name":"419082fc38"},
    {"name":"6234d15099"},
    {"name":"62f2181ee0"},
    {"name":"a50afbbfaa"},
    ...
  ]
}

```
`filters` parameter joins all the specified filters using `AND` SQL operator, if you want `OR` filters you can use the `or_filters` param. Syntax for `or_filters` is same as `filters.

You can also provide the sort field and order. It should be of the format `fieldname asc` or `fieldname desc`. The space should be URL encoded. In the following line, we're taking fieldname to be `title`.


```
GET /api/resource/:doctype?order_by=title%20desc

```
You can also page the results by providing the `limit_start` and `limit_page_length` params.


```
GET /api/resource/:doctype?limit_start=5&amp;limit_page_length=10

```
Response


```
{
  "data": [
    {"name":"6234d15099"},
    {"name":"62f2181ee0"},
    {"name":"a50afbbfaa"},
    {"name":"aa12a5cf71"},
    {"name":"6ac9800d4e"},
    {"name":"4bcf8b701c"},
    {"name":"aee15f4c20"},
    {"name":"6ba753afef"},
    ...
  ]
}

```
`limit` is an alias for `limit_page_length` for accessing `/api/resource` in Version 13. This means the following should also return the same payload as the above query.


```
GET /api/resource/:doctype?limit_start=5&amp;limit=10

```
By default, you will receive the data as `List[dict]`. You can retrieve your data as `List[List]` by passing `as_dict=False`.


```
GET /api/resource/:doctype?limit_start=5&amp;limit=5&amp;as_dict=False

```
Response


```
{
  "data": [
    ["6234d15099"],
    ["62f2181ee0"],
    ["a50afbbfaa"],
    ["aa12a5cf71"],
    ["6ac9800d4e"]
  ]
}

```
To debug the query built for your reqeusts, you can pass `debug=True` with the request. This returns the executed query and execution time under `exc` of the payload.


```
GET /api/resource/:doctype?limit_start=10&amp;limit=5&amp;debug=True

```
Response


```
{
  "data": [
    {"name":"4bcf8b701c"},
    {"name":"aee15f4c20"},
    {"name":"6ba753afef"},
    {"name":"f4b7e24abc"},
    {"name":"bd9156096c"}
  ],
  "exc": "[\"select `tabToDo`.`name`\\n\\t\\t\\tfrom `tabToDo`\\n\\t\\t\\t\\n\\t\\t\\t\\n\\t\\t\\t order by `tabToDo`.`modified` DESC\\n\\t\\t\\tlimit 5 offset 10\", \"Execution time: 0.0 sec\"]"
}

```
CRUD Operations
---------------

Frappe generates REST endpoints for CRUD operations for all DocTypes automatically. Make sure you set the following headers in your requests so that you get proper JSON responses.


```
{
    "Accept": "application/json",
    "Content-Type": "application/json",
}

```
### Create

Create a new document by sending a `POST` request to `/api/resource/:doctype`. Send the document as JSON in the Request Body.


```
POST /api/resource/:doctype

# Body
{"description": "New ToDo"}

```
Response


```
{
  "data": {
    "name": "af2e2d0e33",
    "owner": "Administrator",
    "creation": "2019-06-03 14:19:00.281026",
    "modified": "2019-06-03 14:19:00.281026",
    "modified_by": "Administrator",
    "idx": 0,
    "docstatus": 0,
    "status": "Open",
    "priority": "Medium",
    "description": "New ToDo",
    "doctype": "ToDo"
  }
}

```
### Read

Get a document by sending a `GET` request to `/api/resource/:doctype/:name`.


```
GET /api/resource/:doctype/:name

```
Response


```
{
  "data": {
    "name": "bf2e760e13",
    "owner": "Administrator",
    "creation": "2019-06-03 14:19:00.281026",
    "modified": "2019-06-03 14:19:00.281026",
    "modified_by": "Administrator",
    "idx": 0,
    "docstatus": 0,
    "status": "Open",
    "priority": "Medium",
    "description": "<p>Test description</p>",
    "doctype": "ToDo"
  }
}

```
Expand all link fields by sending a `GET` request to `/api/resource/:doctype/:name?expand_links=True`.

```
GET /api/resource/:doctype/:name?expand_links=True

```
Response


```
{
  "data": {
    "name": "bf2e760e13",
    "owner": "Administrator",
    "creation": "2019-06-03 14:19:00.281026",
    "modified": "2019-06-03 14:19:00.281026",
    "modified_by": "Administrator",
    "idx": 0,
    "docstatus": 0,
    "status": "Open",
    "priority": {
        "name":"a1b2c3", 
        "title": "Medium", 
        "creation": "2025-11-05 19:02:19.106966",
    },
    "description": "<p>Test description</p>",
    "doctype": "ToDo"
  }
}

```

### Update

Update a document by sending a `PUT` request to `/api/resource/:doctype/:name`. You don't need to send the whole document, instead you can just send the fields that you want to update.


```
PUT /api/resource/:doctype/:name

# Body
{"description": "New description"}

```
Response


```
{
  "data": {
    "name": "bf2e760e13",
    "owner": "Administrator",
    "creation": "2019-06-03 14:19:00.281026",
    "modified": "2019-06-03 14:21:00.785117",
    "modified_by": "Administrator",
    "idx": 0,
    "docstatus": 0,
    "status": "Open",
    "priority": "Medium",
    "description": "New description",
    "doctype": "ToDo"
  }
}

```
### Delete

Delete a document by sending a `DELETE` request to `/api/resource/:doctype/:name`.


```
DELETE /api/resource/:doctype/:name

```
Response


```
{"message": "ok"}

```
Remote Method Calls
-------------------

Frappe allows you to trigger arbitrary python methods using the REST API for handling custom logic. These methods must be marked as *whitelisted* to make them accessible via REST.

To run a whitelisted python method at `frappe.auth.get_logged_user`, send a request to the endpoint `/api/method/frappe.auth.get_logged_user`.


```
GET /api/method/frappe.auth.get_logged_user

```
Response


```
{
  "message": "john@doe.com"
}

```
* If your method returns some values, you should send a `GET` request.
* If your method changes the state of the database, use `POST`. After a successful `POST` request, the framework will automatically call `frappe.db.commit()` to commit the changes to the database.
* A successful response will return a JSON object with a `message` key.
* An errored response will return a JSON object with `exc` key which contains the stack trace and `exc_type` which contains the thrown Exception.
* The return value of the method will be converted to a JSON and sent as the response.

File Uploads
------------

There is a dedicated method `/api/method/upload_file` that accepts binary file data and uploads it into the system.

Here is the curl command for it:


```
➜ curl -X POST \
  http://&lt;base-url&gt;/api/method/upload_file \
  -H 'Accept: application/json' \
  -H 'Authorization: token xxxx:yyyy' \
  -F file=@/path/to/file/file.png

```
If you are using client side Javascript to upload files, you can append the uploaded files as FormData and send an XHR request. Here is the [implementation code](https://github.com/frappe/frappe/blob/421f070e78ee1186e7f2f4b2575d8be1d3e2d646/frappe/public/js/frappe/file_uploader/FileUploader.vue#L381-L401) in Frappe Desk.

<!-- page: framework/framework__user__en__api__scanner.md -->
---
title: "Scanner API\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/scanner"
updated: "2026-02-17"
---


Frappe uses the open-source library [Html5-QRCode](https://github.com/mebjas/html5-qrcode) to provide a flexible way to handle inputs like Barcodes, QRCodes, etc. using the device camera.



## frappe.ui.Scanner

```
new frappe.ui.Scanner({ ... })
```

Creates a new Scanner instance that can be used to scan single or multiple barcodes.

Options:

- `container`: Dom element under which video feed from the camera will be shown.
- `dialog`: If set as `true`, will open a dialog to show video feed from the camera.
- `multiple`: If set as `false`, will stop scanning after one successful scan.
- `on_scan`: Callback method to handle the scanned input.

Here is a sample client code to scan one single barcode and log it to the console.

```js
new frappe.ui.Scanner({
 dialog: true, // open camera scanner in a dialog
 multiple: false, // stop after scanning one value
 on_scan(data) {
 console.log(data.decodedText);
 }
});
```

The below code can be used to continously scan and handle the scanned input.

```js
const scanner = new frappe.ui.Scanner({
 dialog: true, // open camera scanner in a dialog
 multiple: true, // stop after scanning one value
 on_scan(data) {
 handle_scanned_barcode(data.decodedText);
 }
});
```

To stop the scanning, you can either close the dialog or use `scanner.stop_scan();`

<!-- page: framework/framework__user__en__api__server-calls.md -->
---
title: "Server Calls (AJAX)\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/server-calls"
updated: "2026-04-18"
---

## frappe.call

`frappe.call(method, args)`

Makes an AJAX request to the server, where the `method` which is the dotted path  
to a whitelisted Python method, is executed and it's return value is sent as the  
response.

```js
// call with no parameters
frappe.call('ping')
 .then(r => {
 console.log(r)
 // {message: "pong"}
 })

// call with a single parameter
frappe.call('frappe.core.doctype.user.user.get_role_profile', {
 role_profile: 'Test'
}).then(r => {
 console.log(r.message)
})

// call with all options
frappe.call({
 method: 'frappe.core.doctype.user.user.get_role_profile',
 args: {
 role_profile: 'Test'
 },
 // disable the button until the request is completed
 btn: $('.primary-action'),
 // freeze the screen until the request is completed
 freeze: true,
 callback: (r) => {
 // on success
 },
 error: (r) => {
 // on error
 }
})
```

## frappe.db.get_doc

`frappe.db.get_doc(doctype, name, filters)`

Returns the Document object of `doctype` and `name`. If `name` is not provided,  
gets the first document matched by `filters`.

```js
// get doc by name
frappe.db.get_doc('Task', 'TASK00002')
 .then(doc => {
 console.log(doc)
 })

// get doc by filters
frappe.db.get_doc('Task', null, { status: 'Open' })
 .then(doc => {
 console.log(doc)
 })
```

## frappe.db.get_list

`frappe.db.get_list(doctype, { fields, filters })`

Returns a list of records of `doctype` with `fields` and `filters`.

```js
frappe.db.get_list('Task', {
 fields: ['subject', 'description'],
 filters: {
 status: 'Open'
 }
}).then(records => {
 console.log(records);
})
```

## frappe.db.get_value

`frappe.db.get_value(doctype, name, fieldname)`

Returns a document's field value or a list of values.

```js
// single value
frappe.db.get_value('Task', 'TASK00004', 'status')
 .then(r => {
 console.log(r.message.status) // Open
 })

// multiple values
frappe.db.get_value('Task', 'TASK00004', ['status', 'subject'])
 .then(r => {
 let values = r.message;
 console.log(values.status, values.subject)
 })

// using filters
frappe.db.get_value('Task', {status: 'Open'}, 'subject')
 .then(r => {
 let values = r.message;
 console.log(values.subject)
 })
```

## frappe.db.get_single_value

`frappe.db.get_single_value(doctype, field)`

Returns a field value from a Single DocType.

```js
frappe.db.get_single_value('System Settings', 'time_zone')
 .then(time_zone => {
 console.log(time_zone);
 })
```

## frappe.db.set_value

`frappe.db.set_value(doctype, docname, fieldname, value, callback)`

Sets a document's property using `frappe.get_doc` and `doc.save` on server.

```js
// update a field's value
frappe.db.set_value('Task', 'TASK00004', 'status', 'Open')
 .then(r => {
 let doc = r.message;
 console.log(doc);
 })

// update multiple fields
frappe.db.set_value('Task', 'TASK00004', {
 status: 'Working',
 priority: 'Medium'
}).then(r => {
 let doc = r.message;
 console.log(doc);
})
```

## frappe.db.insert

`frappe.db.insert(doc)`

Insert a new document.

```js
frappe.db.insert({
 doctype: 'Task',
 subject: 'New Task'
}).then(doc => {
 console.log(doc);
})
```

## frappe.db.count

`frappe.db.count(doctype, filters)`

Returns number of records for a given `doctype` and `filters`.

```js
// total number of Task records
frappe.db.count('Task')
 .then(count => {
 console.log(count)
 })

// total number of Open Tasks
frappe.db.count('Task', {
 filters: {
 status: 'Open'
 }
}).then(count => {
 console.log(count);
})
```

## frappe.db.delete_doc

`frappe.db.delete_doc(doctype, name)`

Delete a document identified by `doctype` and `name`.

```js
frappe.db.delete_doc('Task', 'TASK00004')
```

## frappe.db.exists

`frappe.db.exists(doctype, name)`

Returns true if a document record exists.

```js
frappe.db.exists('Task', 'TASK00004')
 .then(exists => {
 console.log(exists) // true
 })
```

<!-- page: framework/framework__user__en__api__tree.md -->
---
title: "Tree\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/tree"
updated: "2026-02-17"
---

The Tree View is generated for all DocTypes that has Is Tree enabled.

[Screenshot on the live page: Tree View]
*Tree View*

## Standard Tree JS

To customize the Tree View you must have a `{doctype}_tree.js` file in the doctype directory.
Below are all the options that can be customized.

For instance, if you want to configure the Account DocType, you'll have to create a file `account_tree.js` with the following contents.

```js
frappe.treeview_settings["Account"] = {
	breadcrumb: "Accounting",
	title: "Chart of Accounts",

	filters: [
		{
			fieldname: "company",
			fieldtype: "Select",
			label: "Company",
			options: "Company 1\nCompany 2",
			on_change: handle_company_change(),
		},
	],

	get_tree_nodes: "path.to.whitelisted_method.get_children",
	add_tree_node: "path.to.whitelisted_method.handle_add_account",

	fields: [
		{
			fieldtype: "Data",
			fieldname: "account_name",
			label: "New Account Name",
			reqd: true,
		},
		{
			fieldtype: "Link",
			fieldname: "account_currency",
			label: "Currency",
			options: "Currency",
		},
		{
			fieldtype: "Check",
			fieldname: "is_group",
			label: "Is Group",
		},
	],

	ignore_fields: ["parent_account"],

	menu_items: [
		{
			label: "New Company",
			action: function () {
				frappe.new_doc("Company", true);
			},
			condition: "frappe.boot.user.can_create.indexOf('Company') !== -1",
		},
	],

	onload: function (treeview) {},

	post_render: function (treeview) {},

	onrender: function (node) {},

	on_get_node: function (nodes) {},

	extend_toolbar: true,

	toolbar: [
		{
			label: "Add Child",
			condition: function (node) {
				return node && node.is_group;
			},
			click: function (node) {
				frappe.treeview_settings["Account"].add_node(node);
			},
			btnClass: "hidden-xs",
		},
	],
};
```
