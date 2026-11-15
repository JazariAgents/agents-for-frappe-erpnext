<!-- Frappe documentation: framework, part 1 of 24. Index: docs/INDEX.md -->

<!-- page: framework/framework__assignments-and-todos.md -->
---
title: "Assignments and Todos"
space: "Framework"
url: "https://docs.frappe.io/framework/assignments-and-todos"
updated: "2026-02-17"
---

## Overview

The **ToDo** doctype in Frappe Framework helps users track and manage tasks assigned to themselves or to others. ToDos can be created independently or linked to other documents in the system, providing a centralized task management system.

## ToDo Fields

- *Status*: Can be "Open", "Closed", or "Cancelled"
- *Priority*: Set as "High", "Medium", or "Low" (default is "Medium")
- *Color*: Optional color tagging for visual identification
- *Due Date*: When the task should be completed
- *Description*: The main content of the task (required)
- *Reference Type* & *Name*: Optional link to a related document (e.g., a specific Issue, Lead, etc.)
- *Role*: Optional role assignment
- *Assigned* By: User who created or assigned the task
- *Allocated To*: User responsible for completing the task

## Creating ToDos

ToDos can be created in several ways:

1. **Direct Creation**:

   - Navigate to the ToDo list
   - Click on "Add ToDo" button
   - Fill in the required details and save

2. **Via Assignment**:

   - From any document (e.g., Issue, Task), use the "Assign To" function
   - The system creates a ToDo and links it to that document

3. **Via Email**:

   - Send emails to the system with appropriate settings
   - Email content is converted to ToDos automatically (ToDo is in the `email_append_to` settings)

4. **Via Assignment Rules**:

   - Set up automatic assignments based on conditions
   - The system creates ToDos when conditions are met (note: Assignment Rules cannot be set on the ToDo doctype itself)

## Managing ToDos

### Marking as Completed

To mark a **ToDo** as completed:

- Open the ToDo
- Change the status to "Closed"
- Save the document

Only the assignee (the user in the "Allocated To" field) can close their assigned ToDos. When done through the UI, the system will show an error if someone else tries to complete another person's ToDo.

### Cancelling ToDos

To cancel a **ToDo**:

- Open the ToDo
- Change the status to "Cancelled"
- Save the document

Cancelling differs from completion as it indicates the task won't be done rather than has been done.

### Impact of Due Date

The due date field:

- Helps in prioritizing tasks
- Provides a target completion date
- Is used in listing views to sort and filter ToDos
- Is used by Assignment Rules for automated due date management

However, the system does not automatically send reminders when due dates are approaching or have passed. If you need this, consider creating a custom **Notification**.

## Notifications

The system sends notifications in the following scenarios:

1. **When a document is assigned or the assignment is cancelled**:

   - The assignee receives a notification
   - The notification includes the task description and who assigned it, or cancelled the assignment

3. **Global Notification Counter**:

   - Open ToDos contribute to the notification counter in the Frappe interface
   - The counter helps users see at a glance how many open tasks they have

## Permissions

- Users can see ToDos assigned to them or created by them
- System Managers have access to all ToDos
- The "All" role has permission to create, read, write, and delete ToDos

## Integration with Other Documents

When a **ToDo** is linked to another document:

- A comment is added to the referenced document when the ToDo is assigned
- A comment is added when the ToDo is completed or cancelled
- The list of assigned users is updated in the referenced document's `_assign` field
- When viewing the referenced document, users can see who the document is assigned to

## Working with Assignment Rules

While Assignment Rules cannot be created for the **ToDo** doctype itself, they can create ToDos for other doctypes:

- Create rules based on document conditions
- Assign tasks using round-robin, load balancing, or field-based assignment
- Automatically set due dates based on document fields
- Close or reassign ToDos when document conditions change

Assignment Rules provide powerful automation for task management across the system.

<!-- page: framework/framework__automations.md -->
---
title: "Automations"
space: "Framework"
url: "https://docs.frappe.io/framework/automations"
updated: "1 month before 2026-11-14"
fetched: "2026-11-14"
---

An **Automation Flow** says "when this happens to this kind of record, do these things in order", without writing code. You pick a trigger, narrow it with conditions, and add a list of steps: update a field, send a notification, assign someone, call a webhook, wait two days, branch on a value.

Note

Automation Flow is in **beta**. The configuration described here is stable but the run log and internals may change in upcoming releases.

## When to use an Automation Flow

Frappe already has single-purpose tools for common jobs and they remain the right choice when one of them does exactly what you need:

| You want to… | Use |
| --- | --- |
| Send one email or system notification on an event | [Notification](/framework/notifications) |
| Post a document to an external URL on an event | [Webhook](/framework/user/en/guides/integration/webhooks) |
| Distribute new documents across a team | Assignment Rule |
| Change a document's behaviour in code | [Server Script](/framework/user/en/desk/scripting/server-script) |

Use an Automation Flow when you need what those tools can't do on their own:

- **Several steps in order**: assign the document, then email the assignee, then create a follow-up task.
- **Waiting**: do something, wait two days, then do something else, or wait until another event happens.
- **Branching**: if the deal is over 10,000 do one thing, otherwise do another.
- **Reaching linked records**: the trigger is a Communication, but the record you want to update is the Lead it belongs to.

## How it works

1. **Trigger**: a document event, a date, a schedule, a custom event from an app, or a manual run starts the flow. See [Triggers and Conditions](/framework/automations/triggers-and-conditions).
2. **Match**: the flow's match fields and condition decide whether this document qualifies.
3. **Queue**: a matching trigger is queued, not executed inline. A background worker picks it up shortly after the request commits, so a slow webhook never blocks a user's save. Repeated saves of the same document before the worker runs collapse into a single run.
4. **Run**: the worker executes the steps in order and writes an **Automation Run** record with the outcome of every step. See [Steps and Actions](/framework/automations/steps-and-actions).

Because runs happen in the background, the **scheduler and background workers must be running** for automations to fire.

Note

Only a **System Manager** can create, edit or read Automation Flows.

## Creating a flow

1. Go to **Automation Flow** in the awesome bar and click **New**.
2. Enter a **Title** and choose the **Document Type** the flow is about.
3. Choose a **Trigger Type** and fill in the fields it asks for.
4. Optionally add **Match Fields** and an **Advanced Expression using Python**.
5. Add one or more rows under **Actions**.
6. Save and click **Test Run** to try it against a real document (all changes are rolled back), then check **Enabled** and save again.

A flow can only be enabled once it has at least one action.

### Example: follow up on high-value leads

- **Document Type**: Lead
- **Trigger Type**: Doc Created
- **Match Fields**: _Annual Revenue_ \> 1,000,000
- **Actions**:

1. **Assign to User**: `sales-head@example.com`
2. **Send Notification**: Email to `sales-head@example.com`, subject `New lead: {{ doc.lead_name }}`
3. **Wait**: 2 Days
4. **Send Notification**: Email to `@assignees`, subject `Follow up on {{ doc.lead_name }}`, with a step condition `doc.status == "Lead"` so it is skipped if someone has already moved the lead on.

## Run history

Every run is saved as an **Automation Run** which is linked to the flow and to the document it ran against. Each run has a status:

- **Success**: every step succeeded or was skipped.
- **Partially Failed**: a step failed and _Stop on Error_ was off, so later steps still ran.
- **Failed**: a step failed and `Stop on Error` stopped the run or the run couldn't start.
- **Waiting**: the run is paused at a `Wait step` and resumes on its own.
- **Skipped**: the document was deleted or no longer matched when `Revalidate on Run` is on.

Open a run to see each step's status, its output, how long it took, and, for a failed step, the error message and traceback. For a skipped step, the run shows the condition and the values it read, so you can see _why_ it didn't match. Run logs are cleared after 30 days by the standard log cleanup.

## Automation Settings

**Automation Settings** holds the site-wide switches and limits:

- **Disable Automations**: stop dispatching all flows on the site. Rows already queued are not affected. To stop automations even when the database is unreachable, set `"automation_disabled": 1` in `site_config.json`.
- **Maximum Recursion Depth** (default 3): how many times a flow's actions may trigger another flow before the chain is refused. This stops two flows that update each other from looping forever.
- **Failure Threshold** (default 10): after this many consecutive failed runs, the flow is **disabled automatically** and its pending runs are skipped and its owner gets a notification. The reason is shown in the flow's _Disabled Reason_ field.
- **Allow Unregistered Events**: accept custom events that no installed app has registered. See [Extending Automations](/framework/automations/extending-automations).

The remaining settings (drain timing, retries, retention and size limits) tune the background worker and rarely need changing.

## Next steps

- [Triggers and Conditions](/framework/automations/triggers-and-conditions)
- [Steps and Actions](/framework/automations/steps-and-actions)
- [Extending Automations](/framework/automations/extending-automations), for app developers

<!-- page: framework/framework__automations__extending-automations.md -->
---
title: "Extending Automations"
space: "Framework"
url: "https://docs.frappe.io/framework/automations/extending-automations"
updated: "1 month before 2026-11-14"
fetched: "2026-11-14"
---

Apps can extend Automation Flows in three ways: **emit events** that flows trigger on or wait for, **add actions** to the step list, and **add relationships** so steps can reach records the schema doesn't link directly. Each one is registered in your app's `hooks.py`.

## Emitting events

Call `emit()` wherever something meaningful happens in your app:

```python
from frappe.automation_engine import emit

def on_deal_won(deal):
    emit("crm.deal_won", doc=deal, payload={"amount": deal.deal_value})
```

| Argument | Description |
| --- | --- |
| `event` | Event name. Use an app-prefixed, dotted name like `crm.deal_won`. |
| `doc` | The document the event is about. Custom Event flows with a Document Type run against it. |
| `payload` | A JSON-serializable dict. Flows read it as `payload` in templates and `context["payload"]` in conditions. |
| `correlation_key` | Resumes runs paused at a matching **WaitForEvent** step. |

`emit()` does two things:

1. It queues every enabled **Custom Event** flow for _that_ event.
2. If `correlation_key` is given, it resumes any run waiting for that event with the same key.

It returns `{"queued": <count>, "resumed": <count>}`. Runs start after the current transaction commits, and calling `emit()` twice for the same record before then produces a single run. Payloads larger than the **Event Payload Limit** in Automation Settings (64 KB by default) are rejected.

### Resuming a waiting flow

A flow can send an email, then **WaitForEvent**`crm.email_replied` with the correlation key `{{ doc.name }}`. When the reply arrives, your app emits the same event with the same key:

```python
emit(
    "crm.email_replied",
    doc=lead,
    payload={"communication": comm.name},
    correlation_key=lead.name,
)
```

The waiting run resumes immediately, and its later steps can read the payload from `context["event"]["payload"]`.

### Registering events

`emit()` only accepts events an installed app has registered, unless **Allow Unregistered Events** is on in Automation Settings. Register events in `hooks.py`, either as bare names or with metadata that builder UIs can show:

```python
automation_events = [\
    "crm.deal_won",\
    {\
        "crm.email_replied": {\
            "label": "Email replied",\
            "description": "A contact replied to an email sent from CRM",\
            "subject": {"doctype_key": "reference_doctype", "name_key": "reference_name", "doctypes": ["CRM Lead", "CRM Deal"]},\
        }\
    },\
]
```

`subject` tells the engine which record an event is _about_, read from the payload. With a subject, a flow on `CRM Lead` runs against the lead named in the payload even if the code that emitted the event was holding a Communication. Use `"doctype": "CRM Lead"` in place of `doctype_key` when the subject type is fixed.

## Adding actions

Subclass `AutomationAction` and implement `execute`:

```python
# my_app/automation.py
from typing import ClassVar

import frappe
from frappe.automation_engine.actions.base import AutomationAction, AutomationParamError, render_value

class PostToChannel(AutomationAction):
    action_type = "PostToChannel"
    label = "Post to Channel"
    description = "Post a message to a team channel."
    transactional = False  # it calls an external service
    params_schema: ClassVar[list] = [\
        {"fieldname": "channel", "label": "Channel", "fieldtype": "Data", "reqd": 1},\
        {"fieldname": "message", "label": "Message", "fieldtype": "Small Text", "reqd": 1},\
    ]

    def validate(self, params, doctype):
        if not params.get("channel"):
            raise AutomationParamError("Channel is required", fieldname="channel")

    def execute(self, doc, params, context):
        message = render_value(params["message"], doc, context)
        post_message(params["channel"], message)
        return f"Posted to {params['channel']}"
```

```python
# hooks.py
automation_actions = ["my_app.automation.PostToChannel"]
```

Class attributes:

| Attribute | Purpose |
| --- | --- |
| `action_type` | Unique identifier stored on the step. Don't change it after release. |
| `label`, `description` | Shown in the Action Type list and in builder UIs. |
| `params_schema` | Parameter fields: `fieldname`, `label`, `fieldtype`, `options`, `reqd`. |
| `requires_document` | Set to `False` if the action can run without a trigger document, for example on a Scheduled flow. |
| `applicable_doctypes` | Limits the action to these DocTypes. `None` means all. |
| `supported_trigger_types` | Limits the action to these trigger types. `None` means all. |
| `transactional` | Set to `False` if the action has effects a database rollback can't undo, such as HTTP calls or messages. The engine then never replays the run from the start. |

Methods:

- `validate(params, doctype)`: runs when the flow is saved and again before each execution. Raise `AutomationParamError` with a `fieldname` to point at the bad parameter.
- `execute(doc, params, context)`: does the work. Return a short string for the run log, or a dict with a `detail` key plus any output later steps should read through `context["steps"][step_key]`.
- `output_doctype(params)`: if the action creates a record, return its DocType. A step's **Output Alias** can then target the new record, and later steps are validated against it.

The action runs as the flow's **Run As** user, so normal permission checks apply. Don't call `frappe.db.commit()`; the engine owns the transaction. To pause the run from inside an action, raise `StopAutomation("reason", resume_after=seconds)`.

## Adding relationships

Link, Dynamic Link and child-table link fields become relationships automatically, in both directions. Register a provider only for connections the schema doesn't express, such as a record matched on an email address:

```python
from frappe.automation_engine.relationships import AutomationRelationshipProvider

class ContactRelationships(AutomationRelationshipProvider):
    def get_definitions(self, source_doctype):
        if source_doctype != "Communication":
            return []
        return [{\
            "name": "sender_lead",\
            "label": "Lead (by sender email)",\
            "target_doctype": "CRM Lead",\
            "cardinality": "one",\
        }]

    def resolve(self, source_doc, relationship, params):
        name = frappe.db.get_value("CRM Lead", {"email": source_doc.sender})
        return [{"doctype": "CRM Lead", "name": name}] if name else []
```

```python
# hooks.py
automation_relationships = ["my_app.automation.ContactRelationships"]
automation_relationship_ignore = ["My Log DocType"]
```

- `cardinality` is `one` or `many`. Only `one` relationships can be used as a step's target alias. `many` relationships are for related-record conditions, where overriding `query()` to filter in SQL keeps them fast on large tables.
- A definition with the same `name` as a derived relationship replaces it, which lets an app relabel a schema link.
- Every reference a provider returns is checked for existence and read permission before a step uses it.
- `automation_relationship_ignore` hides DocTypes (such as logs) from derived relationships.

## Suppressing and checking automations

```python
from frappe.automation_engine import is_enabled, skip_automations

if is_enabled():
    ...

with skip_automations():
    doc.save()  # no Automation Flow fires for this save
```

<!-- page: framework/framework__automations__steps-and-actions.md -->
---
title: "Steps and Actions"
space: "Framework"
url: "https://docs.frappe.io/framework/automations/steps-and-actions"
updated: "1 month before 2026-11-14"
fetched: "2026-11-14"
---

The **Actions** table on an Automation Flow lists the steps a run executes, top to bottom. Each row has a **Step Type** and, for action steps, an **Action Type** and its **Parameters**.

## Step types

| Step Type | What it does |
| --- | --- |
| **Action** | Runs one action, such as setting a field or sending an email |
| **Wait** | Pauses the run for a fixed time, then continues with the next step |
| **WaitForEvent** | Pauses the run until an app emits a matching event, or a timeout passes |
| **If** | Evaluates a condition and runs only the steps in the matching branch |

### Wait

Set **Parameters** to a duration:

```json
{"value": 2, "unit": "Days"}
```

`unit` is one of `Seconds`, `Minutes`, `Hours` or `Days`. While paused, the run shows as **Waiting**. When it resumes, the document is loaded fresh, so later steps see any changes made during the wait.

### WaitForEvent

Pauses until an app emits an event with a matching correlation key:

```json
{
  "event_name": "crm.email_replied",
  "correlation_key": "{{ doc.name }}",
  "timeout_value": 3,
  "timeout_unit": "Days"
}
```

The correlation key is rendered when the step is reached, and the run resumes when the app calls `emit()` with the same event and key. If the timeout passes first, the run resumes anyway. Steps after the wait can read how it ended from `context.event`: `outcome` is `Matched` or `Timed Out`, and `payload` holds the event's data.

A typical use case: send a follow-up only if the customer hasn't replied, by adding an If step after the wait with the condition `context["event"]["outcome"] == "Timed Out"`.

### If

An If step needs a **Step Condition**. Steps that belong to it set **Parent Step** to the If row's number and **Branch** to `If` (runs when the condition is true) or `Else` (runs when it's false). Steps without a Parent Step always run.

| # | Step Type | Action | Parent Step | Branch |
| --- | --- | --- | --- | --- |
| 1 | If | condition `doc.grand_total > 10000` |  |  |
| 2 | Action | Assign to User: `manager@example.com` | 1 | If |
| 3 | Action | Assign to User: `sales@example.com` | 1 | Else |
| 4 | Action | Send Notification |  |  |

If Steps can be nested. The branch is decided once, when the run first reaches the If step, and isn't re-evaluated after a Wait.

## Step conditions

Any step can have a **Step Condition**, a Python expression that must be true for the step to run. Otherwise the step is recorded as **Skipped** and the run continues. The expression can read:

- `doc`: the document that triggered the run
- `target`: the record the step acts on
- `context`: the run's state, including `context["steps"]`, the outputs of earlier steps keyed by step key

## Actions

These are the actions shipped as core framework actions. Other Apps can extend this actions via `hooks.py`, see [extending automations](/framework/automations/extending-automations) .

| Action Type | What it does | Key parameters |
| --- | --- | --- |
| **Set Field Value** | Sets one or more fields on the target and saves it | `field` \+ `value`, or `values` as a map |
| **Increment Field Value** | Adds a number to a numeric field | `field`, `amount` (negative to subtract) |
| **Create Document** | Inserts a new document of any type | `doctype`, `values` |
| **Send Notification** | Sends an email or a system notification | `channel` (`Email` or `System`), `recipients`, `subject` and `message`, or `email_template` |
| **Assign to User** | Assigns the target to one or more users | `assign_to`, `description` |
| **Call Webhook** | Sends an HTTP request | `url`, `method`, `headers`, `payload`, `timeout` |
| **Run Script** | Runs Python code | `server_script` (an API Server Script), or inline `script` |

### Examples

Set two fields at once:

```json
{"values": {"status": "Replied", "priority": "High"}}
```

Create a follow-up ToDo:

```json
{
  "doctype": "ToDo",
  "values": {
    "description": "Call {{ doc.lead_name }}",
    "reference_type": "{{ doc.doctype }}",
    "reference_name": "{{ doc.name }}",
    "allocated_to": "{{ doc.lead_owner }}"
  }
}
```

Email the document owner and assignees:

```json
{
  "channel": "Email",
  "recipients": ["@owner", "@assignees", "team@example.com"],
  "subject": "{{ doc.name }} was closed",
  "message": "<p>{{ doc.name }} was closed on {{ frappe.utils.nowdate() }}.</p>"
}
```

`@owner` and `@assignees` resolve against the document when the step runs. They read the document as it was loaded at the start of the run (or after the last Wait), so an assignment made by an earlier step in the same run isn't included yet.

## Templates

Text parameters accept Jinja. Available variables:

- `doc` / `target`: the record the step acts on
- `trigger`: the document that started the run
- `payload`: data from a custom event or schedule
- `context`: the run's state, including `context.steps.<step_key>` for earlier steps' outputs

## Acting on other records

By default a step acts on the trigger document. To act on a linked record, declare a named alias under **Relationships** and set the step's **Target** to that alias:

```json
[{"alias": "customer", "relationship": "customer"}]
```

Link, Dynamic Link and child-table link fields are available automatically, under their fieldname. Reverse links are named `<doctype>_via_<field>`, for example `crm_deal_via_lead`. Apps can register more (see [Extending Automations](/framework/automations/extending-automations)).

A **Create Document** step can also set an **Output Alias**. Later steps can then target the document it created.

## Error handling

- **Stop on Error** (on by default): the first failed step stops the run, which is marked **Failed**. Turn it off to keep going; the run is then marked **Partially Failed**.
- Each step runs inside its own savepoint, so a failed step's database changes are rolled back without undoing earlier steps.
- **Call Webhook** and **Run Script** can reach outside the database. Once one of them has run, the run is never replayed from the start, so a webhook isn't sent twice.
- **Call Webhook** refuses private and internal network addresses, and follows at most five redirects. A response status of 400 or above fails the step.
- **Run Script** needs Server Scripts enabled (`bench set-config -g server_script_enabled 1`), and only a System Manager can write an inline script. The script can read `doc`, `target`, `trigger`, `payload` and `context`, and can set keys on `result` to publish output to later steps. It can't call `frappe.db.commit()`.

## Test Run

Click **Test Run** on a saved flow and pick a document. The flow runs for real against it, and then **every change is rolled back**. The result lists each step's status, messages and the condition values it read.

During a test run, Wait steps are simulated, and Call Webhook reports the request it _would_ send without sending it.

<!-- page: framework/framework__automations__triggers-and-conditions.md -->
---
title: "Triggers and Conditions"
space: "Framework"
url: "https://docs.frappe.io/framework/automations/triggers-and-conditions"
updated: "1 month before 2026-11-14"
fetched: "2026-11-14"
---

The trigger decides **when** an Automation Flow is considered. The match fields and condition decide **whether** a particular document qualifies. Both are set on the Automation Flow form.

## Trigger types

| Trigger Type | Fires when | Needs |
| --- | --- | --- |
| **Doc Created** | A document is inserted | Document Type |
| **Doc Updated** | An existing document is saved (not on insert) | Document Type |
| **Field Value Changed** | One field changes value on save | Document Type, Trigger Field |
| **Doc Deleted** | A document is deleted | Document Type |
| **Doc Submitted** | A submittable document is submitted | Document Type |
| **Doc Cancelled** | A submittable document is cancelled | Document Type |
| **Date Based** | A date field is N days before or after today | Document Type, Date Field |
| **Scheduled** | A cron expression comes due | Cron Expression |
| **Custom Event** | An app calls `frappe.automation_engine.emit()` | Custom Event name |
| **Manual** | Someone starts the flow explicitly | — |

### Field Value Changed

Set **Trigger Field** to the field to watch. Optionally narrow it with:

- **From Value**: fire only when the old value was this.
- **To Value**: fire only when the new value is this.

Leave either empty to accept any value. For example, _Trigger Field_`status`, _To Value_`Closed` fires whenever a document is closed, whatever its previous status was.

### Date Based

Pick a **Date Field**, a **Date Offset (Days)** and a **Date Direction**:

- `3` days **Before**`renewal_date`: fires on documents whose renewal is three days from today.
- `1` day **After**`due_date`: fires on documents that became overdue yesterday.

Date Based flows are checked **hourly**. Each document fires at most once per day, however many times the check runs.

### Scheduled

Enter a standard five-field **Cron Expression**, for example `0 9 * * 1` for 09:00 every Monday. The form shows the **Next Run** time after you save.

- **Without a Document Type**, the flow runs once per schedule, with no document. Use this for periodic jobs such as a weekly digest email or calling an external API.
- **With a Document Type**, the flow runs once for **every document that matches** its match fields and condition, each time the schedule comes due.

If the scheduler was down and missed several fires, the flow catches up once for the latest one, not once for every fire it missed.

### Custom Event

Custom Event flows run when an app emits a named event, such as `crm.deal_won`. Enter the event name exactly as the app emits it in **Custom Event**. How an app emits and registers events is covered in [Extending Automations](/framework/automations/extending-automations).

If a Document Type is set, the flow only runs for events about a document of that type.

### Manual

A Manual flow never fires on its own. It runs only when an app starts it through the `frappe.automation_engine.api.run_manually` method, for example from a button in the app's UI. The caller needs write access to the flow and read access to the document.

## Match fields

**Match Fields** use the same filter editor as the list view. Add a row per field rule. The document must satisfy every rule for the flow to run.

For example, on a Lead flow:

- _Status_ = `Open`
- _Source_ is set
- _Annual Revenue_ \> `1000000`

A flow with no match fields matches every document of its type.

## Advanced condition

For logic the match fields can't express, write a Python expression in **Advanced Expression using Python**. The document is available as `doc`, and the expression is evaluated with Frappe's safe evaluator, so `frappe.utils` helpers are available.

```python
doc.status == "Open" or doc.priority == "High"
```

```python
doc.grand_total > 50000 and doc.customer_group != "Internal"
```

The match fields **and** the expression must both be true. If the expression raises an error, the document is treated as not matching and the error is written to the Error Log.

## Revalidate on Run

A trigger is matched when the document is saved, but the steps run a moment later in a background worker. Check **Revalidate on Run** to test the match fields and condition again right before executing. If the document no longer matches, the run is recorded as **Skipped**.

This is useful when a document can change quickly after the save that triggered the flow, for example a status that is set and then reverted.

## Run As

**Run As** decides whose permissions the steps run with:

- **Automation User** (default): the user in the **Automation User** field, `Administrator` unless you change it.
- **Triggering User**: the user whose action triggered the flow.
- **Document Owner**: the owner of the document the flow runs against.

Every step still runs normal permission checks as that user. If a step fails with a permission error, check whether the Run As user can read the trigger document and write the record the step changes.

Note

Set **Automation User** to a dedicated user with only the roles the flow needs, rather than leaving it as `Administrator`.

## When flows do not fire

Automation Flows are skipped during installs, migrations and patches, while **Disable Automations** is checked in Automation Settings, and when `automation_disabled` is set in `site_config.json`.

Code that must save documents without triggering flows, such as a data import, can suppress them:

```python
from frappe.automation_engine import skip_automations

with skip_automations():
    doc.save()
```

<!-- page: framework/framework__data-masking.md -->
---
title: "Data Masking"
space: "Framework"
url: "https://docs.frappe.io/framework/data-masking"
updated: "2026-02-17"
---

> Note: This feature is only available in nightly (v16) version. This feature is considered experimental.

In the Frappe Framework, permissions can be applied to control field visibility using [Perm Levels](https://docs.frappe.io/erpnext/user/manual/en/managing-perm-level).  

However, in many business scenarios, it's important to show certain fields while hiding their sensitive data. For example:  

- HR users might need to view employee details but should not see salary amounts.  
- Support staff may see customer phone numbers in a masked format like `811XXXXXXX`.
- Finance users can view bank account fields without exposing the full account number.  

This is where Data Masking comes in.  

With Data Masking, you can configure specific fields to display masked or hidden values based on the user's roles and permissions — without restricting field visibility.  
It ensures sensitive information remains protected while keeping the user interface consistent and informative.
### Enabling Data Masking

Data Masking can be enabled directly from the Doctype or through the Customize Form.

#### Steps to Enable Data Masking

1. Open the Doctype (in Developer Mode) or Customize Form where you want to enable masking.  
2. Select the field you want to mask.  
3. Check the Mask checkbox.  
4. Save and reload the form.

Once enabled, users who do not have the Mask permission for that field will see masked or hidden data, while users with the appropriate permission will see the actual value.

Here's a quick demo showing how to enable Data Masking:
[Screenshot on the live page: Enable Data Masking]


#### Supported Field Types

Data Masking can be applied only on the following field types:

`Select`, `Read Only`, `Phone`, `Percent`, `Password`, `Link`, `Int`, `Float`,  
`Dynamic Link`, `Duration`, `Datetime`, `Currency`, `Data`, and `Date`.

### For Developers

Data Masking in the Frappe Framework works seamlessly with the existing permission system.  
When a user doesn’t have the required Mask permission for a field, the framework automatically replaces the actual value with a masked version both in the UI and backend responses.

#### How It Works Internally

1. **Field Configuration**  
   Each field can have a `mask` property enabled in its DocField.  
   ```python
   {
       "fieldname": "phone_number",
       "fieldtype": "Data",
       "options": "Phone",
       "mask": 1
   }
   ```
2. **Permission Check**  
   The system checks if the current user has the `mask` permission for that field using:
   ```python
   meta.has_permlevel_access_to(fieldname=df.fieldname, df=df, permission_type="mask")
   ```
3. **Automatic Masking in Responses**
   Once the permission check fails, the framework automatically masks the field value before returning it.
   This applies to:

   * Form view data loading
   * List view queries
   * Reports using ORM or standard data fetching
   * API responses (e.g. `/api/resource/...`, `/api/method/...`)

> Note: Data Masking does **not** apply automatically to custom SQL queries or Query Reports that use raw SQL.
In such cases, developers need to explicitly apply masking logic in their query results before returning the response.

<!-- page: framework/framework__desk-reports__excel-xlsx-export-styling.md -->
---
title: "Excel (XLSX) Export Styling"
space: "Framework"
url: "https://docs.frappe.io/framework/desk-reports/excel-xlsx-export-styling"
updated: "2026-04-22"
---

> Introduced in Version 16

  
The `get_xlsx_styles` module method allows you to define custom Excel styling for report exports.

> **Note:** This method is only called when exporting standard Script Reports or Query Reports to Excel format (not CSV).

## Basic Usage

Define a `get_xlsx_styles` function in your report's Python file:  

```python
from frappe.utils.xlsxutils import XLSXMetadata, XLSXStyleBuilder

def get_xlsx_styles(metadata: XLSXMetadata) -> dict:
    builder = XLSXStyleBuilder(metadata)

    # Add your custom styles here...
    return builder.result
```



> **Note:** Default styles (header, filters, fieldtype formats, currency) are applied automatically when `XLSXStyleBuilder` is initialized.

> To disable this, pass `default_styling=False`:
>
> builder = XLSXStyleBuilder(metadata, default_styling=False)

## XLSXMetadata

The `metadata` object provides access to report data and helper methods.  

### Attributes


| Attribute             | Type                     | Description                         |
| --------------------- | ------------------------ | ----------------------------------- |
| `report_name`         | `str`                    | Name of the report                  |
| `filters`             | `dict`                   | Raw filter values                   |
| `column_map`          | `dict[int, dict]`        | Column index → column definition    |
| `row_map`             | `dict[int, dict \| list]` | Row index → row data                |
| `applied_filters_map` | `dict[int, list]`        | Filter row index → [label, value]   |
| `has_total_row`       | `bool`                   | Whether last row is a total row     |
| `has_indentation`     | `bool`                   | Whether indentation styling applies |


> **Note:** All indexes must be 0-based respecting  XlsxWriter's indexing.

## XLSXStyleBuilder

The builder provides methods to register and apply styles.

### Registering Styles

```python
# Register a style and get its ID
style_id = builder.register_style({"bold": True, "bg_color": "#FFFF00"})
```

### Applying Styles

```python
# Style an entire column
builder.style_column(col_idx, style_id)

# Style an entire row
builder.style_row(row_idx, style_id)

# Style a specific cell
builder.style_cell(row_idx, col_idx, style_id)
```

## Style Properties

### Font Styles

```python
builder.register_style({
    "bold": True,
    "italic": True,
    "underline": True,
    "font_size": 12,
    "font_color": "#FF0000",
    "font_name": "Arial",
})
```

### Background Colors

```python
builder.register_style({
    "bg_color": "#FFFF00",
})  
```

### Borders

```python
# Border thickness: 1 = thin, 2 = medium, 3 = thick
builder.register_style({
    "border": 1,
    "border_color": "#000000",
})

# Individual borders
builder.register_style({
    "left": 2,
    "right": 2,
    "top": 1,
    "bottom": 3,
})
```

### Alignment

```python
builder.register_style({
    "align": "center",           # left, center, right
    "valign": "vcenter",         # top, vcenter, bottom
    "text_wrap": True,
    "indent": 2,

})
```

### Number Formats

```python
builder.register_style({
    "num_format": "#,##0.00",    # Custom number format

})
```

## Complete Example

```python
from frappe.utils.xlsxutils import XLSXMetadata, XLSXStyleBuilder

def get_xlsx_styles(metadata: XLSXMetadata) -> dict:
    builder = XLSXStyleBuilder(metadata)

    # --- Register Styles (do this once, reuse style_id) --- #
    success_style = builder.register_style({"font_color": "#006100", "bg_color": "#C6EFCE"})
    warning_style = builder.register_style({"font_color": "#9C5700", "bg_color": "#FFEB9C"})
    error_style = builder.register_style({"font_color": "#9C0006", "bg_color": "#FFC7CE"})
    highlight_style = builder.register_style({"bold": True, "bg_color": "#DDEBF7"})
    total_row_border = builder.register_style({"border": 3, "border_color": "#15137e"})
    right_align = builder.register_style({"align": "right"})

    # --- Style entire column --- #
    amount_col_idx = builder.field_index_map.get("net_amount")

    if amount_col_idx is not None:
        builder.style_column(amount_col_idx, right_align)

    # --- Style total row with border --- #
    if metadata.has_total_row:
        builder.style_row(metadata.get_last_row_index(), total_row_border)

    # --- Conditional Cell Styling --- #
    status_col_idx = builder.field_index_map.get("status")

    for row_idx, row_data in metadata.row_map.items():
        if not isinstance(row_data, dict):
            continue

        # Status-based styling
        if status_col_idx is not None:
            status = row_data.get("status")

            if status == "Completed":
                builder.style_cell(row_idx, status_col_idx, success_style)

            elif status == "Pending":
                builder.style_cell(row_idx, status_col_idx, warning_style)

            elif status == "Cancelled":
                builder.style_cell(row_idx, status_col_idx, error_style)

        # High value highlighting
        if amount_col_idx is not None:
            amount = row_data.get("net_amount")

            if amount and amount > 10000:
                builder.style_cell(row_idx, amount_col_idx, highlight_style)

    return builder.result
```

## Example Output

[Screenshot on the live page]
*Example Export with Styles*

## Recommendations

- **Register styles once and reuse** — Avoid creating duplicate styles by registering them at the start and using the returned `style_id` throughout.

## Reference

- For all available style properties, visit the [xlsxwriter format documentation](https://xlsxwriter.readthedocs.io/format.html#format-methods-and-format-properties).

<!-- page: framework/framework__doctypes__allow-on-submit.md -->
---
title: "Allow on Submit"
space: "Framework"
url: "https://docs.frappe.io/framework/doctypes/allow-on-submit"
updated: "2026-07-02"
---

# Allow on Submit

**Allow on Submit** is a DocField property that lets a field remain editable after a document has been submitted. Submitted documents are normally locked to protect the audit trail. Use this option only for fields that can safely change without changing the meaning, value, status, or ledger impact of the submitted document.

## When to use Allow on Submit

Enable this property for fields that record additional information after submission, but do not affect validations, totals, stock, accounting, workflow decisions, or external commitments.

- Reference numbers received after submission
- Remarks, notes, or internal comments
- Tracking details or dispatch information
- Print-only labels or operational metadata

## When not to use it

Do not enable Allow on Submit for fields that affect business logic or the submitted document's financial, stock, or compliance meaning. If changing a field should change the transaction, cancel and amend the document instead.

- Amounts, quantities, rates, taxes, discounts, or totals
- Party, company, posting date, warehouse, item, account, or currency fields
- Status fields used by workflows, integrations, reports, or validations
- Any field used to create ledger entries or stock ledger entries

## Enable Allow on Submit using Customize Form

1. Go to **Customize Form**.
2. Select the DocType where the field should remain editable after submission.

The form builder opens with the fields for the selected DocType. In this example, the **ToDo** DocType is selected.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

3. In the fields table, select the field that should be editable after submission.
4. In the field properties, enable **Allow on Submit**.
5. Click **Update** to save the customization.

Use the property search to find **Allow on Submit** quickly, especially when a field has many properties.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

## Verify the behavior

1. Open a submitted document for the DocType you customized.
2. Confirm that only the intended field is editable.
3. Change the field value and save the document.
4. Check that totals, ledger entries, workflow state, and other submitted values did not change.

## Recommended practice

Before enabling Allow on Submit, check whether the field is used in controller methods, custom scripts, reports, print formats, workflows, integrations, or permission logic. If the field is used anywhere to calculate or decide something important, keep it locked after submission.

For custom apps, also review server-side validations. Allowing the field to be edited on a submitted document does not automatically make every related business rule safe. Add validations where needed so only the intended post-submit updates are allowed.

## Troubleshooting

### The field is still read-only after enabling Allow on Submit

Reload the form and check whether the field is also controlled by read-only dependencies, role permissions, workflow state, custom scripts, or server-side logic.

### The value changes on the form but does not save

Check custom validations and controller hooks for the DocType. A server-side validation may still be blocking updates on submitted documents.

### The field should affect the transaction

Do not use Allow on Submit. Cancel and amend the submitted document so the corrected transaction has a clear audit trail.

<!-- page: framework/framework__doctypes__docstatus.md -->
---
title: "Docstatus or Document Status"
space: "Framework"
url: "https://docs.frappe.io/framework/doctypes/docstatus"
updated: "2026-07-05"
---

Frappe uses the concept of a "Docstatus" to keep track of the status of transactions. The docstatus will always have one of the following three values:

1. Draft (value: 0)
2. Submitted (value: 1)
3. Cancelled (value: 2)

Documents that are _not submittable_ will always remain in the "draft" state. Documents that are _submittable_ can optionally proceed from the draft state to the "submitted", and then to the "cancelled" state.

Documents in the submitted and cancelled state cannot be edited, with one execption: for individual fields we can explicitly allow edits, even when the document is in the submitted state.

In the backend code we have a helper class `DocStatus` that can be used as follows:

```py
import frappe
from frappe.model.docstatus import DocStatus

draft_invoice_names = frappe.get_list(
 "Sales Invoice",
 filters={"docstatus": DocStatus.draft()},
 pluck="name"
)

invoice_doc = frappe.get_doc("Sales Invoice", draft_invoice_names[0])
invoice_doc.docstatus == DocStatus.draft() # -> True
invoice_doc.docstatus.is_draft() # -> True
invoice_doc.docstatus.is_submitted() # -> False
invoice_doc.docstatus.is_cancelled() # -> False

invoice_doc.submit()
invoice_doc.docstatus == DocStatus.submitted() # -> True
invoice_doc.docstatus.is_draft() # -> False
invoice_doc.docstatus.is_submitted() # -> True
invoice_doc.docstatus.is_cancelled() # -> False

invoice_doc.cancel()
invoice_doc.docstatus == DocStatus.cancelled() # -> True
invoice_doc.docstatus.is_draft() # -> False
invoice_doc.docstatus.is_submitted() # -> False
invoice_doc.docstatus.is_cancelled() # -> True
```

The docstatus gets stored as an integer value in each Doctype table of the database.
