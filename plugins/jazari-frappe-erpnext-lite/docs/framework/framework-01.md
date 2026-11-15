<!-- Frappe documentation: framework, part 1 of 6. Index: docs/INDEX.md -->

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
![Enable Data Masking](/files/data-masking.gif)


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

![](/files/image0ecd7d.png)
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

<!-- page: framework/framework__doctypes__doctype-layout.md -->
---
title: "DocType Layout"
space: "Framework"
url: "https://docs.frappe.io/framework/doctypes/doctype-layout"
updated: "2026-06-03"
---

# DocType Layout



DocType Layout lets you create multiple form views for the same DocType — each with different field labels, visibility rules, and defaults — **without modifying the DocType itself**. Layouts activate automatically based on document state, so the right view appears with no manual action.

**Common use cases**

- A simplified data-entry view that hides advanced fields
- A read-heavy review view that relabels fields for clarity
- Auto-switching to a "Return" layout when `doc.is_return == 1`
- State- or context-specific layouts driven by conditions or workspace links

## Creating a Layout



Go to the **DocType Layout** list and click **New**.


| Field                      | Description                                                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Title**                  | Display name shown in the layout indicator and breadcrumb (e.g. *Compact View*).                                          |
| **Document Type**          | The DocType this layout applies to. Set once and cannot change.                                                           |
| **Condition**              | Optional JS expression. When truthy, this layout activates automatically on form refresh.                                 |
| **Based On**               | Inherit field configuration from another layout of the same DocType.                                                      |
| **Is Child Table**         | Mark this layout as a child-table layout. When checked, it appears in the Child Layout selector of other DocType Layouts. |
| **Default Print Format**   | Pre-selects this print format when the layout is active.                                                                  |
| **Default Email Template** | Pre-selects this email template when the layout is active.                                                                |


After selecting a **Document Type**, click **Sync Fields** to pull in all fields from the DocType. A visual form builder opens in the **Parent Layout** tab where you can reorder and configure fields.

## Overriding Field Properties



In the form builder, select any field to override its properties. The following properties can be set **per layout** without affecting the base DocType:


| Property               | Effect                                        |
| ---------------------- | --------------------------------------------- |
| `label`                | Rename the field for this layout              |
| `hidden`               | Hide the field                                |
| `reqd`                 | Make the field mandatory                      |
| `read_only`            | Make the field read-only                      |
| `bold`                 | Emphasize the label                           |
| `allow_in_quick_entry` | Include the field in the Quick Entry dialog   |
| `in_list_view`         | Show the field as a column in the List View   |
| `in_standard_filter`   | Include the field in the Standard Filters bar |
| `default`              | Set a default value for new documents         |
| `description`          | Override the help text                        |
| `depends_on`           | Conditional visibility expression             |
| `mandatory_depends_on` | Conditional required expression               |
| `read_only_depends_on` | Conditional read-only expression              |


Properties not set in the layout fall back to the base DocType definition.

## Automatic Layout Switching



Layout selection is **entirely condition-driven** — there is no manual switcher. Set a **Condition** to make a layout activate automatically when the expression evaluates to truthy after a form refresh:

```
// Activates for return transactions
doc.is_return == 1

// Activates for high-value orders
doc.grand_total > 100000

// Activates for a specific status
doc.status === "Closed"
```

When a condition matches, the layout is applied and the URL is updated with `?layout=<name>`. The first matching layout wins; layouts are evaluated in the order they appear in the list. A layout indicator badge appears next to the document title whenever a non-default layout is active.

## Breadcrumb Navigation



When a layout is active, the breadcrumb bar reflects it:

- On the **form view**, the layout title appears as a clickable crumb between the DocType and the document name. Clicking it opens the list **filtered by the layout's condition** (parsed from `doc.field OP value` expressions).
- On that **filtered list**, the layout title appears as a non-clickable crumb so the active context stays visible.
- Clicking the **DocType crumb** while a layout is active clears all filters and removes the layout crumb, returning to the unfiltered list.

## Child Table Layouts



A layout can specify different layouts for its child tables. In the **Child Layouts** tab, add a row for each child table you want to customize:


| Field               | Description                                                            |
| ------------------- | ---------------------------------------------------------------------- |
| **Table Fieldname** | The fieldname of the child table in the parent DocType                 |
| **Child Layout**    | A DocType Layout whose Document Type matches the child table's DocType |


When the parent layout is active, each child table grid automatically renders using its assigned child layout — applying the same field-level overrides as a parent layout would.

**Important.** The child layout's **Document Type** must match the child table's DocType (e.g. `Sales Invoice Item`), not the parent DocType. Create a separate layout for the child table first, then reference it here.

The same field properties available on a parent layout — `label`, `hidden`, `reqd`, `read_only`, `depends_on`, column order, and so on — apply inside the grid when the child layout is active.

**Example.** A *Finance View* parent layout maps the items table to a *Compact Items* child layout that hides `description`, `uom`, and other detail columns, leaving only `item_code`, `qty`, and `amount` visible. Switching to the parent layout automatically compacts the grid — no extra action required from the user.

## Layout Inheritance



Use **Based On** to inherit the field configuration of another layout for the same DocType. The child layout starts with the parent's field order and overrides, and can further customize individual fields or add new ones.

This is useful for creating a family of related layouts: define a *Base Layout* with common field order, then create specialized layouts (e.g. *Sales View*, *Finance View*) that inherit and tweak it.

## Keeping Fields in Sync



The **Sync Fields** button compares the layout's field list against the current DocType definition and reports:

- **Added** — fields present in the DocType but missing from the layout (added to the end)
- **Removed** — fields in the layout that no longer exist in the DocType (removed)

Run this after modifying the underlying DocType to keep the layout consistent.

## Workspace Integration



Any DocType link in the sidebar workspace can be tied to a specific layout. Open the workspace in edit mode, select a DocType link, and set the **DocType Layout** field to the layout you want. Clicking that link opens the list pre-scoped to that layout (the URL carries `?layout=<name>`), and new documents created from the list open under that layout.

## For Developers: Standard Layouts



Layouts can be shipped as part of an app by setting **Is Standard** and selecting a **Module**. In developer mode, saving a standard layout automatically exports it as a JSON file to:

{app}/{module}/doctype/{doctype}/doctype_layout/{layout_name}.json

This file is included in migrations and deployed automatically via `bench migrate`. Standard layouts are **read-only** on production instances (outside developer mode).

<!-- page: framework/framework__document-queue.md -->
---
title: "Document Queue"
space: "Framework"
url: "https://docs.frappe.io/framework/document-queue"
updated: "2026-07-02"
---

Document Queue is a framework-level document intake workflow for files that need to be reviewed before creating a Frappe document. It stores one uploaded source file, extracts text from it, and lets the user open a target DocType with the source preview beside the native form.

Document Queue is generic. It does not map fields by itself and does not contain ERPNext-specific logic. Apps such as ERPNext can build document-specific mapping, validation, or automation on top of completed Document Queue records.

## When To Use It

Use Document Queue when users receive documents first and decide or create the target record afterwards.

Examples:

- Uploading a vendor invoice PDF before creating a Purchase Invoice in another app.
- Uploading an expense receipt before creating an Expense Claim.
- Uploading a signed form, identity document, or application PDF before creating a custom DocType record.
- Collecting files from an email inbox or bulk upload flow for later review.

Document Queue is useful when the framework should handle file intake, extraction, and review, while the app or user decides what the extracted content means.

## How It Works

A Document Queue record represents one source file. The record stores extraction status, extracted text, raw extraction output, error details, and the target document created during review.

The usual flow is:

1. A user uploads a PDF or image into Document Queue.
2. The user clicks **Extract**, or the file is extracted as part of an upload-first flow.
3. Frappe extracts readable text and stores it on the queue record.
4. The record becomes **Ready for Review**.
5. The user clicks **Start Review** and chooses a target DocType if one is not already set.
6. Frappe opens a new target document with a left-side review panel.
7. The user manually enters values into the native form using the preview and extracted text.
8. When the target document is saved, Frappe links the queue record to that document, marks the queue record **Completed**, and moves the source attachment to the target document.

## Statuses

Document Queue records use these statuses:


| Status           | Meaning                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------ |
| Draft            | The record exists but extraction has not started.                                          |
| Queued           | Extraction has been queued as a background task.                                           |
| Processing       | Extraction is currently running.                                                           |
| Ready for Review | Extraction completed and the record can be reviewed into a target document.                |
| Completed        | A target document was saved and linked to the queue record.                                |
| Failed           | Extraction failed or the file type is unsupported. Error details are stored on the record. |


Completed records cannot be started for review again. This keeps one Document Queue record tied to one completed target document.

## Extraction

Document Queue supports PDF and image extraction.

For PDFs, Frappe uses `pdfplumber` as the primary extractor. The extracted text is stored in **Extracted Text** and the detailed extraction result is stored in **Raw Extraction JSON**.

For each PDF page, the raw JSON can include:

- page number
- page width and height
- plain text
- layout text
- words with coordinates
- tables detected by `pdfplumber`

If the embedded PDF text is not useful, Frappe attempts OCR fallback with Tesseract, when the required system tools are available.

For images, Frappe uses Tesseract OCR when available. OCR words and coordinates are stored in the raw JSON.

Unsupported files are marked **Failed** and the error is stored in **Error Message**. Debug details, such as skipped OCR because `tesseract` is not available, are stored in **Debug Output**.



## Manual Document Queue Flow

To create a queue record manually:

1. Open **Document Queue**.
2. Create a new record.
3. Attach a PDF or image in **Source File**.
4. Save the record.
5. Click **Extract**.

If extraction succeeds, the record moves to **Ready for Review**.

To create a target document from the queue:

1. Open a **Ready for Review** Document Queue record.
2. Click **Start Review**.
3. If **Document Type** is not set, choose a target DocType.
4. Frappe opens a new target document.
5. Use the left review panel while filling the native form on the right.
6. Save the target document.

After save, the Document Queue record is marked **Completed**, linked to the target document, and the source file is attached to the target document.



## Review Panel

The review panel appears on the left side of the target document form.

It has two tabs:

- **Preview**: Shows the uploaded PDF or image.
- **Extraction**: Shows the extracted text.

The right side remains the native Frappe form. Users enter data manually, using the preview and extracted text as reference.

The preview pane can be resized. Frappe remembers the preferred width in the browser.

If the user leaves the new target document without saving, no target document is linked and the Document Queue record remains resumable.



## Upload Document Flow For Target DocTypes

Administrators can enable an upload-first workflow for any non-child DocType.

When enabled, new records for that DocType show an **Upload Document** banner. Users can upload a PDF or image before filling the form. Frappe creates a Document Queue record, extracts the file, and opens the same review experience for the new target document.

To enable it:

1. Open the DocType record.
2. Enable **Upload First Workflow**.
3. Save the DocType.

Only DocTypes with **Upload First Workflow** enabled are shown in the Document Queue target DocType selector.



## Ready For Review Banner

When a DocType has **Upload First Workflow** enabled, its list view can show a thin banner such as:

> 3 Documents ready for review

The banner includes a **View** action that opens Document Queue filtered to records for that target DocType in **Ready for Review** status.



## Permissions

By default:

- **System Manager** can create, read, write, delete, export, print, email, report, and share Document Queue records.
- **Desk User** can create records and can read, export, print, email, report, and share records they own.

Users also need permission to create and save the target DocType used during review.

## Developer API

### Queue Extraction

Use `enqueue_document_extraction` to run extraction as a background task.

```python
from frappe.core.doctype.document_queue.document_queue import enqueue_document_extraction

task = enqueue_document_extraction(document_queue_name)
```

This marks the record **Queued** and creates a Background Task that extracts that one Document Queue record.

### Extract Immediately

Use `extract_document_queue_record` when extraction should run immediately in the current request or test.

```python
from frappe.core.doctype.document_queue.document_queue import extract_document_queue_record

result = extract_document_queue_record(document_queue_name)
```

The result includes:

```python
{
    "extraction_method": "pdfplumber",
    "extracted_text": "...",
    "raw_extraction_json": {
        "file": "invoice.pdf",
        "extraction_method": "pdfplumber",
        "pages": [],
    },
    "debug_output": [],
}
```

### Get Review Context

Use `get_document_review_context` to fetch the data needed by a review UI.

```python
from frappe.core.doctype.document_queue.document_queue import get_document_review_context

context = get_document_review_context(document_queue_name)
```

Example response:

```python
{
    "queue_name": "abc123",
    "status": "Ready for Review",
    "document_type": "Address",
    "created_document": None,
    "source_file": "/private/files/source.pdf",
    "source_file_url": "/private/files/source.pdf?fid=...",
    "extracted_text": "Extracted text...",
    "raw_extraction_json": {},
    "debug_output": "",
}
```

### Link A Queue Record To A Target Document

Use `link_to_document` after the target document is saved.

```python
from frappe.core.doctype.document_queue.document_queue import link_to_document

link_to_document(
    document_queue=document_queue_name,
    document_type="Address",
    document_name=address_name,
)
```

This marks the Document Queue record **Completed**, stores the target document link, and attaches the source file to the target document.

### Count Records Ready For Review

Use `get_ready_for_review_count` to show a badge or banner for enabled target DocTypes.

```python
from frappe.core.doctype.document_queue.document_queue import get_ready_for_review_count

count = get_ready_for_review_count("Address")
```

The count is returned only for DocTypes that have **Upload First Workflow** enabled.

## Building On Document Queue

Document Queue intentionally stops at extraction and review. It does not infer field mappings or create accounting, buying, selling, HR, or domain-specific documents by itself.

Downstream apps can build on top of it by:

- consuming **Completed** Document Queue records
- reading `extracted_text` for simple search or manual copy flows
- reading `raw_extraction_json` for word coordinates, page data, and tables
- adding app-specific field suggestions
- adding app-specific validation before or after the target document is saved
- adding email or bulk-upload intake that creates queue records

For example, an ERP app can filter completed queue records where `document_type` is `Purchase Invoice`, read the raw extraction JSON, and apply invoice-specific mapping in that app. The mapping logic stays outside Frappe Framework.

## Limitations

- Document Queue does not perform AI or LLM-based field extraction.
- Document Queue does not map extracted text into target DocType fields.
- CSV and spreadsheet extraction are not supported by the built-in extractor.
- OCR requires system tools such as `tesseract`; PDF OCR fallback also requires `pdftoppm`.
- Extraction quality depends on the source document. Digital PDFs usually extract better than scanned or low-resolution images.

<!-- page: framework/framework__get_query.md -->
---
title: "frappe.qb.get_query"
space: "Framework"
url: "https://docs.frappe.io/framework/get_query"
updated: "2026-02-17"
---

The `frappe.qb.get_query` function provides a modern, safe, and expressive way to build database queries in Frappe. It leverages the power of the [Pypika](https://pypika.readthedocs.io/en/latest/) library while integrating seamlessly with Frappe's DocType metadata, permissions, and conventions. This guide will walk you through using `frappe.qb.get_query` from basic usage to more advanced scenarios.

## Introduction

While `frappe.db.get_list` and `frappe.db.get_all` have served Frappe well for many years and are capable of handling complex queries, their underlying code has grown complex over time, making them harder to maintain and extend. `frappe.qb.get_query` represents a modern approach to achieve similar results, built with better extensibility and maintainability in mind.

## Getting Started

### Basic Query Structure

To get started, you need to understand the basic structure of a query:

```python
# Get a query builder instance for the 'User' DocType
query = frappe.qb.get_query("User")

# Execute the query and fetch results
users = query.run(as_dict=True)
```

By default, if no `fields` are specified, it selects **only the `name` field**.

### Simple Example

```python
# Get all user names and emails
query = frappe.qb.get_query("User", fields=["name", "email"])
users = query.run(as_dict=True)
# users will be like: [{'name': 'Administrator', 'email': 'admin@example.com'}, ...]
```

## Field Selection

### Basic Field Selection

Use the `fields` argument to specify which columns you want.

```python
# Select specific fields
query = frappe.qb.get_query("User", fields=["name", "email"])

# You can also pass fields as a comma-separated string
query = frappe.qb.get_query("User", fields="name, email")

# Or select all fields using '*'
query = frappe.qb.get_query("User", fields="*")
```

### Using Aliases

Use `as` within the field string to give fields aliases in the output.

```python
query = frappe.qb.get_query(
    "User",
    fields=["name as user_name", "email as user_email"]
)
users = query.run(as_dict=True)
# users will be like: [{'user_name': 'Administrator', 'user_email': 'admin@example.com'}, ...]
```

### Linked Document Fields

If you have a Link field, you can fetch fields from the linked document using dot notation: `link_fieldname.target_fieldname`. The query builder automatically adds the necessary `LEFT JOIN`.

```python
# Get Sales Order customer name (assuming 'customer' is a Link field to Customer DocType)
query = frappe.qb.get_query(
    "Sales Order",
    fields=["name", "customer.customer_name as customer_name"],
    filters={"name": "SO-00001"}
)
so_data = query.run(as_dict=True)
# so_data might be: [{'name': 'SO-00001', 'customer_name': 'Test Customer'}]
```

### Child Table Fields

You can access fields within a Child Table using dot notation: `child_table_fieldname.child_doc_fieldname`.

```python
# Get item code from Sales Order Item (assuming 'items' is the child table fieldname)
query = frappe.qb.get_query(
    "Sales Order",
    fields=["name", "items.item_code"],
    filters={"name": "SO-00001"}
)
# This will likely return multiple rows if SO-00001 has multiple items
so_items = query.run(as_dict=True)
# so_items might be: [{'name': 'SO-00001', 'item_code': 'ItemA'}, {'name': 'SO-00001', 'item_code': 'ItemB'}]
```

**Important:** When selecting fields from child tables this way, the query performs a `LEFT JOIN`, potentially resulting in multiple rows for each parent document if the child table has multiple entries.

### Fetching Child Table Records

A more structured way to fetch child table data:

```python
# Get Sales Orders and their associated items
query = frappe.qb.get_query(
    "Sales Order",
    fields=[
        "name",
        "customer",
        {"items": ["item_code", "qty", "rate"]} # Fetch from 'items' child table
    ],
    filters={"docstatus": 1},
    limit=5
)

results = query.run(as_dict=True)

# Example result structure:
# [
#   {
#     'name': 'SO-00001',
#     'customer': 'Customer A',
#     'items': [
#       {'item_code': 'ItemA', 'qty': 2.0, 'rate': 100.0},
#       {'item_code': 'ItemB', 'qty': 1.0, 'rate': 50.0}
#     ]
#   },
#   {
#     'name': 'SO-00002',
#     'customer': 'Customer B',
#     'items': [
#       {'item_code': 'ItemC', 'qty': 5.0, 'rate': 20.0}
#     ]
#   }
# ]
```

This approach performs a separate query for the child records after fetching the parent records, efficiently grouping them by parent.


### SQL Functions in Fields

To use SQL functions in your select clauses, you can use dictionary-based syntax within the `fields` argument.

#### Aggregation Functions

```python
# COUNT - Count rows or non-null values
query = frappe.qb.get_query(
    "User",
    fields=["user_type", {"COUNT": "name", "as": "total_users"}],
    group_by="user_type"
)

# COUNT(*) - Count all rows including nulls
query = frappe.qb.get_query(
    "Sales Invoice",
    fields=[{"COUNT": "'*'", "as": "total_invoices"}]
)

# SUM - Calculate sum of numeric values
query = frappe.qb.get_query(
    "Sales Invoice",
    fields=[{"SUM": "grand_total", "as": "total_sales"}],
    filters={"docstatus": 1}
)

# AVG - Calculate average of numeric values
query = frappe.qb.get_query(
    "Sales Invoice",
    fields=[{"AVG": "grand_total", "as": "avg_invoice_amount"}],
    group_by="customer"
)

# MAX - Find maximum value
query = frappe.qb.get_query(
    "User",
    fields=[{"MAX": "creation", "as": "latest_user_date"}]
)

# MIN - Find minimum value
query = frappe.qb.get_query(
    "User",
    fields=[{"MIN": "creation", "as": "earliest_user_date"}]
)
```

#### Scalar Functions

```python
# ABS - Absolute value
query = frappe.qb.get_query(
    "Journal Entry Account",
    fields=[{"ABS": "debit_in_account_currency", "as": "abs_amount"}]
)

# IFNULL - Handle null values (takes two arguments)
query = frappe.qb.get_query(
    "User",
    fields=[{"IFNULL": ["first_name", "'Unknown'"], "as": "display_name"}]
)

# CONCAT - Concatenate strings (takes multiple arguments)
query = frappe.qb.get_query(
    "User",
    fields=[{"CONCAT": ["first_name", "' '", "last_name"], "as": "full_name"}]
)

# EXTRACT - Extract part of date/time (takes two arguments: unit and date)
query = frappe.qb.get_query(
    "User",
    fields=[{"EXTRACT": ["'YEAR'", "creation"], "as": "creation_year"}]
)

# NOW - Current timestamp (no arguments)
query = frappe.qb.get_query(
    "User",
    fields=[{"NOW": None, "as": "current_time"}]
)
```


## Filtering

### Basic Filters

The `filters` argument allows you to add `WHERE` clauses.

#### Dictionary Filters (Equality)

This is the simplest and often preferred way for equality checks.

```python
# Get users with first_name 'Admin'
query = frappe.qb.get_query(
    "User",
    fields=["name", "email"],
    filters={"first_name": "Admin"} # Simple key-value implies '='
)
```

#### Dictionary Filters (Other Operators)

For operators other than `=`, use a dictionary where the value is a list `[operator, value]`.

```python
# Get users created after a certain date
query = frappe.qb.get_query(
    "User",
    fields=["name", "creation"],
    filters={"creation": [">", "2023-01-01 00:00:00"]}
)

# Get users whose name is like 'test%'
query = frappe.qb.get_query(
    "User",
    fields=["name"],
    filters={"name": ["like", "test%"]}
)

# Get users whose name is in a list
query = frappe.qb.get_query(
    "User",
    fields=["name"],
    filters={"name": ["in", ["test1@example.com", "test2@example.com"]]}
)

# Get users whose name is NOT in a list
query = frappe.qb.get_query(
    "User",
    fields=["name"],
    filters={"name": ["not in", ["Administrator", "Guest"]]}
)
```

#### List Filters (Alternative Format)

You can also provide a list containing filter lists `[[fieldname, operator, value]]`.

```python
# Get users created after a certain date (using list format)
query = frappe.qb.get_query(
    "User",
    fields=["name", "creation"],
    filters=[["creation", ">", "2023-01-01 00:00:00"]]
)

# Multiple filters (combined with AND)
query = frappe.qb.get_query(
    "User",
    fields=["name"],
    filters=[
        ["enabled", "=", 1],
        ["user_type", "=", "System User"]
    ]
)
```

### Filter Operators

`frappe.qb.get_query` supports various operators:

| Operator String    | SQL Equivalent | Example Usage (Dictionary Format)                    | Example Usage (List Format)                               |
| :----------------- | :------------- | :--------------------------------------------------- | :-------------------------------------------------------- |
| `=`                | `=`            | `{"name": "Test"}`                                   | `[["name", "=", "Test"]]`                                 |
| `!=`               | `!=`           | `{"name": ["!=", "Test"]}`                           | `[["name", "!=", "Test"]]`                                |
| `>`                | `>`            | `{"creation": [">", "2023-01-01"]}`                 | `[["creation", ">", "2023-01-01"]]`                       |
| `<`                | `<`            | `{"creation": ["<", "2023-01-01"]}`                 | `[["creation", "<", "2023-01-01"]]`                       |
| `>=`               | `>=`           | `{"age": [">=", 18]}`                               | `[["age", ">=", 18]]`                                     |
| `<=`               | `<=`           | `{"age": ["<=", 65]}`                               | `[["age", "<=", 65]]`                                     |
| `like`             | `LIKE`         | `{"subject": ["like", "%urgent%"]}`                 | `[["subject", "like", "%urgent%"]]`                       |
| `not like`         | `NOT LIKE`     | `{"subject": ["not like", "spam%"]}`                | `[["subject", "not like", "spam%"]]`                      |
| `in`               | `IN`           | `{"status": ["in", ["Open", "Pending"]]}`           | `[["status", "in", ["Open", "Pending"]]]`                 |
| `not in`           | `NOT IN`       | `{"role": ["not in", ["Guest"]]}`                   | `[["role", "not in", ["Guest"]]]`                         |
| `is`               | `IS NULL` or `IS NOT NULL` | `{"customer": ["is", "set"]}` or `{"email": ["is", "not set"]}` | `[["customer", "is", "set"]]` or `[["email", "is", "not set"]]` |
| `descendants of`   | (Nested Set)   | `{"parent_account": ["descendants of", "Assets"]}`  | `[["parent_account", "descendants of", "Assets"]]`        |
| `ancestors of`     | (Nested Set)   | `{"location": ["ancestors of", "Room 101"]}`        | `[["location", "ancestors of", "Room 101"]]`              |
| `not descendants of` | (Nested Set)   | `{"category": ["not descendants of", "Internal"]}` | `[["category", "not descendants of", "Internal"]]`         |
| `not ancestors of` | (Nested Set)   | `{"territory": ["not ancestors of", "West Coast"]}` | `[["territory", "not ancestors of", "West Coast"]]`       |

**Note on `is set` / `is not set`:** These check if a field has a value (`IS NOT NULL` and `IS NULL` respectively).

### Filtering on Linked Document Fields

You can filter based on fields in linked documents using dot notation: `link_fieldname.target_fieldname`.

```python
# Get Sales Orders where the linked Customer's territory is 'North America'
query = frappe.qb.get_query(
    "Sales Order",
    fields=["name", "customer"],
    filters={"customer.territory": "North America"} # Filter on linked field
)
north_america_orders = query.run(as_dict=True)
```

### Filtering by Child Table Fields

You can filter parent records based on values in their child table records using dot notation: `child_table_fieldname.target_fieldname`.

```python
# Get Sales Orders that contain 'Item A' in their items table
# Use distinct=True to ensure each Sales Order appears only once
query = frappe.qb.get_query(
    "Sales Order",
    fields=["name", "customer"],
    filters={"items.item_code": "Item A"}, # Filter based on child table field
    distinct=True
)
orders_with_item_a = query.run(as_dict=True)
```

**Important:** When filtering based on child table fields, use `distinct=True` if you only want unique parent records.

### Nested Set Filters

For DocTypes that are trees (using `lft` and `rgt` columns, like Account, Territory, Warehouse, etc.), you can use special filters:

```python
# Get all accounts under 'Assets'
query = frappe.qb.get_query(
    "Account",
    fields=["name"],
    filters={"parent_account": ["descendants of", "Assets"]}
)

# Get the parent territories of 'West Coast'
query = frappe.qb.get_query(
    "Territory",
    fields=["name"],
    filters={"parent_territory": ["ancestors of", "West Coast"]}
)
```

### Logical Operators (AND/OR)

For complex conditions, structure your `filters` as a list combining conditions with `'and'` or `'or'`.

```python
# Find users who are enabled AND have first name 'Admin'
filters_and = [
    ["enabled", "=", 1],
    "and",
    ["first_name", "=", "Admin"],
]
query = frappe.qb.get_query("User", filters=filters_and)

# Find users who have first name 'Admin' OR 'Guest'
filters_or = [
    ["first_name", "=", "Admin"],
    "or",
    ["first_name", "=", "Guest"],
]
query = frappe.qb.get_query("User", filters=filters_or)

# Combine AND and OR (use nested lists for grouping)
# Find users who are enabled AND (have first name 'Admin' OR 'Guest')
filters_nested = [
    ["enabled", "=", 1],
    "and",
    [
        ["first_name", "=", "Admin"],
        "or",
        ["first_name", "=", "Guest"],
    ]
]
query = frappe.qb.get_query("User", filters=filters_nested)
```

## Query Execution

### Basic Execution

Once you have the `query` object, execute it using `.run()`:

```python
# Returns a list of tuples by default
results = query.run()

# Returns a list of dictionaries
results = query.run(as_dict=True)

# Returns a list of lists
results = query.run(as_list=True)

# If selecting a single field, returns a flat list of values
results = query.run(pluck=True)

# Print the generated SQL query and execution time
results = query.run(debug=True)
```

### Getting the SQL String

You can get the generated SQL string without executing:

```python
# Get the SQL string with values directly substituted (for debugging)
sql_string = query.get_sql()
print(sql_string)
# Example Output: SELECT `name`, `email` FROM `tabUser` WHERE `first_name`='Admin'
```

### Using Iterators for Large Datasets

When dealing with large datasets, use `as_iterator=True` to process results row by row without loading everything into memory:

```python
# Process a large number of tasks without loading all into memory
query = frappe.qb.get_query(
    "Task",
    fields=["name", "subject", "status"],
    filters={"status": "Open"}
)

# Use unbuffered_cursor for optimal memory usage with the iterator
with frappe.db.unbuffered_cursor():
    task_iterator = query.run(as_iterator=True, as_dict=True)

    processed_count = 0
    for task in task_iterator:
        # Process each task dictionary one by one
        print(f"Processing Task: {task['name']} - {task['subject']}")
        processed_count += 1
        if processed_count % 1000 == 0:
            print(f"Processed {processed_count} tasks...")
```

**Requirements:**

- You must use `as_iterator=True` with either `as_dict=True` or `as_list=True`
- For optimal memory efficiency, use within `frappe.db.unbuffered_cursor()` context manager

## Ordering, Grouping, and Pagination

### Ordering Results

Use the `order_by` argument to sort results:

```python
# Order users by creation date, ascending
query = frappe.qb.get_query("User", fields=["name", "creation"], order_by="creation asc")

# Order by multiple fields
query = frappe.qb.get_query(
    "Sales Invoice",
    fields=["name", "customer", "grand_total"],
    order_by="customer asc, grand_total desc"
)
```

### Grouping Results

Use `group_by` for aggregation:

```python
# Count invoices per customer
query = frappe.qb.get_query(
    "Sales Invoice",
    fields=["customer", {"COUNT": "'*'", "as": "invoice_count"}],
    filters={"docstatus": 1},
    group_by="customer"
)
results = query.run(as_dict=True)
# results: [{'customer': 'Cust A', 'invoice_count': 5}, {'customer': 'Cust B', 'invoice_count': 3}, ...]
```

### Pagination

Use `limit` and `offset` for pagination:

```python
# Get the first 10 users
query = frappe.qb.get_query("User", limit=10)

# Get the next 10 users (page 2)
query = frappe.qb.get_query("User", limit=10, offset=10)
```

### Distinct Results

Use `distinct=True` to get unique rows:

```python
# Get distinct customers from submitted Sales Invoices
query = frappe.qb.get_query(
    "Sales Invoice",
    fields=["customer"],
    filters={"docstatus": 1},
    distinct=True
)
```

## Permissions

### The `ignore_permissions` Flag

By default, `frappe.qb.get_query` **ignores** permissions (`ignore_permissions=True`). To enforce permissions, set `ignore_permissions=False`:

```python
# This query bypasses all permission checks (default behavior)
query_ignore = frappe.qb.get_query("DocType", fields=["name"], filters={"istable": 1})

# This query enforces standard Frappe permissions for the current user
query_enforce = frappe.qb.get_query(
    "DocType",
    fields=["name"],
    filters={"istable": 1},
    ignore_permissions=False # Explicitly enable permission checks
)

try:
    results = query_enforce.run()
except frappe.PermissionError:
    print("User does not have permission to read DocType!")
```

### How Permissions are Applied

When `ignore_permissions=False`:

1. **Role Permissions:** Checks if the user has 'read' or 'select' permission based on their roles.
2. **User Permissions:** Applies User Permissions (Allow/Restrict) defined for the DocType and linked DocTypes.
3. **Sharing:** Includes documents explicitly shared with the user.
4. **Owner Constraint:** If the role permissions only grant access `if_owner`, the query restricts results to documents owned by the user.
5. **Permission Query Conditions:** Applies conditions defined via Hooks or Server Scripts.
6. **Field Level Security:** Filters the selected `fields`, and does not allow fields used in `filters`, `group_by`, `order_by` if user does not have permlevel access. Also checks fields in `link_field.target_field` and `child_field.target_field` notations.

### Field-Level Security

When `ignore_permissions=False`:

- **`fields`:** Only fields accessible at the user's maximum permitted permlevel are included. Requesting inaccessible fields will **silently remove** the field from the selection.
- **`filters`:** Filtering is **only allowed** on fields the user has permission to access. Attempting to filter on an inaccessible field **will raise** a `frappe.PermissionError`.
- **`group_by`:** Grouping is **only allowed** on fields the user has permission to access. Attempting to group by an inaccessible field **will raise** a `frappe.PermissionError`.
- **`order_by`:** Ordering is **only allowed** on fields the user has permission to access. Attempting to order by an inaccessible field **will raise** a `frappe.PermissionError`.
- **Linked and Child Table Fields:** When using `link_field.target_field` or `child_field.target_field` notation in any of the above clauses, the system checks permissions for both the link/child field itself and the target field in the linked/child DocType.

```python
# Assume 'published' field in Blog Post has permlevel 1
# User 'test@example.com' only has permlevel 0 access

# This works, but 'published' field is silently removed from results
query = frappe.qb.get_query(
    "Blog Post",
    fields=["name", "title", "published"], # 'published' requested but inaccessible
    ignore_permissions=False,
    user="test@example.com"
)
# result will contain 'name' and 'title', but NOT 'published'

# This FAILS because filtering on 'published' is not allowed for this user
try:
    query = frappe.qb.get_query(
        "Blog Post",
        fields=["name"],
        filters={"published": 1}, # Filtering on restricted field
        ignore_permissions=False,
        user="test@example.com"
    )
    query.run()
except frappe.PermissionError as e:
    print(f"Permission error: {e}")
```

### Specifying User and Parent Context

```python
# Check permissions for a specific user
query = frappe.qb.get_query(
    "Task",
    ignore_permissions=False,
    user="test@example.com" # Check permissions for this user
)

# Provide parent context for child DocTypes
query = frappe.qb.get_query(
    "Sales Order Item",
    fields=["item_code", "qty"],
    filters={"parent": "SO-00001"},
    ignore_permissions=False,
    parent_doctype="Sales Order" # Specify parent context for permission checks
)
```

## Advanced Features

### Using Pypika Objects

For complex scenarios involving subqueries, advanced conditions, or functions not available in the dictionary syntax, you can use Pypika objects directly.

#### Pypika Objects in Fields

```python
from frappe.query_builder import Field, functions, Query

# Define Pypika objects
user_table = frappe.qb.DocType("User")
todo_table = frappe.qb.DocType("ToDo")

# Build a subquery to count open ToDos for each user
open_todo_subquery = (
    Query.from_(todo_table)
    .select(functions.Count("*"))
    .where(todo_table.owner == user_table.name) # Correlated subquery
    .where(todo_table.status == "Open")
).as_("open_todos_count")

# Use Pypika objects in fields
query = frappe.qb.get_query(
    "User",
    fields=[
        user_table.name,
        user_table.email,
        open_todo_subquery # Using the subquery object
    ],
    filters={"user_type": "System User"}
)
users_with_counts = query.run(as_dict=True)
```

#### Pypika Objects in Filters

```python
from frappe.query_builder import Field, functions

# Define Pypika objects
task_table = frappe.qb.DocType("Task")
modified_field = task_table.modified
creation_field = task_table.creation
subject_field = task_table.subject
status_field = task_table.status

# Build complex criterion
complex_filter = (
    (modified_field > creation_field) & (functions.Length(subject_field) > 10)
) | (status_field == "Cancelled")

# Use the Criterion object in filters
query = frappe.qb.get_query(
    "Task",
    fields=["name", "subject", "status", "creation", "modified"],
    filters=complex_filter
)
results = query.run(as_dict=True)
```

### Record Locking

For use within database transactions where you need to prevent other transactions from modifying specific rows:

#### Basic Locking

```python
# Lock specific Stock Ledger Entries
query = frappe.qb.get_query(
    "Stock Ledger Entry",
    fields=["name", "qty_after_transaction"],
    filters={"item_code": "ITEM001", "warehouse": "WH001"},
    for_update=True # Adds FOR UPDATE clause, will wait if rows are locked
)
entries = query.run(as_dict=True)
```

#### Skip Locked Rows

```python
# Skip rows that are already locked by another transaction
query = frappe.qb.get_query(
    "ToDo",
    fields=["name", "description"],
    filters={"status": "Pending"},
    limit=5,
    order_by="creation asc",
    for_update=True,
    skip_locked=True # Skip locked rows
)
available_tasks = query.run(as_dict=True)
```

#### Non-Blocking Lock Attempt

```python
# Fail immediately if rows are already locked
try:
    query = frappe.qb.get_query(
        "System Settings",
        fields=["name"],
        filters={"name": "System Settings"},
        for_update=True,
        wait=False # Don't wait for locks
    )
    settings = query.run(as_dict=True)
except Exception as e:
    print(f"Could not acquire lock immediately: {e}")
```

## Security Considerations

`frappe.qb.get_query` is designed with security in mind:

- **Field Validation:** Field names are validated against strict patterns to prevent SQL injection.
- **Parameterization:** Filter values are parameterized by the database driver.
- **Permission Enforcement:** Using `ignore_permissions=False` leverages Frappe's robust permission system.

Always ensure that any dynamic values used to construct filter keys or field names are properly sanitized if they originate from untrusted sources. **Always rely on passing user input as filter values.**


Written by Claude Sonnet 4. Reviewed by human.

<!-- page: framework/framework__guides-app-development__updating-a-field-from-a-linked-doctype.md -->
---
title: "Updating a Field from a Linked Doctype"
space: "Framework"
url: "https://docs.frappe.io/framework/guides-app-development/updating-a-field-from-a-linked-doctype"
updated: "2026-07-05"
---

ERPNext lets you fetch a value from a linked document into another field by using the **Fetch From** property. This is useful when one field should automatically show information from a selected linked record.

For example, when a user selects a **Customer**, you may want to automatically show the customer's territory, tax ID, customer group, or another field from the Customer master. Instead of writing a Client Script, you can configure this using **Fetch From** in the field settings.



[https://www.youtube.com/watch?v=78Yp_OdXnBI](https://www.youtube.com/watch?v=78Yp_OdXnBI)

## How Fetch From Works

Fetch From works with a **Link** field.

The format is:

```text
link_fieldname.field_to_fetch
```

Where:

- `link_fieldname` is the fieldname of the Link field in the current DocType.
- `field_to_fetch` is the fieldname from the linked DocType.

When the user selects a value in the Link field, ERPNext reads the selected linked document and copies the specified field value into the current field.

## Example

Suppose you have a custom field on **Sales Order** called **Customer Territory**, and you want it to automatically fetch the territory from the selected Customer.

In this case:

- The Link field on Sales Order is `customer`.
- The field to fetch from Customer is `territory`.
- The Fetch From value should be:

```text
customer.territory
```

When a user selects a Customer in the Sales Order, ERPNext fetches the Customer's Territory and fills it in the Customer Territory field.

## Steps To Configure Fetch From

1. Go to **Customize Form**.
2. Select the DocType where you want to show the fetched value.
3. Add or select the target field where the fetched value should appear.
4. In the field settings, enter the **Fetch From** value using this format:

```text
link_fieldname.field_to_fetch
```

5. Save the customization.
6. Reload the form and test by selecting a linked document.

## Another Example

If you want to fetch the **Supplier Group** from the selected Supplier into a custom field on Purchase Order:

- Link field: `supplier`
- Field to fetch: `supplier_group`
- Fetch From value:

```text
supplier.supplier_group
```

When the Supplier is selected, ERPNext fetches the Supplier Group into the target field.

## Important Notes

- Fetch From works only when the source field is available on the linked DocType.
- Use the **fieldname**, not the field label. For example, use `customer_group`, not `Customer Group`.
- The target field should have a compatible field type. For example, fetch text into a Data field, dates into a Date field, and linked records into a Link field where appropriate.
- Fetch From is best for simple one-way fetching. If the value needs complex conditions, calculations, or multiple dependent updates, use a Client Script instead.
- If the value in the linked document changes later, existing documents may not update automatically unless the link field is changed or the document is refreshed and saved according to the form behavior.

## Common Mistakes

- **Using the label instead of fieldname:** `customer.Customer Group` will not work. Use `customer.customer_group`.
- **Using the wrong link field:** The first part must be the fieldname of the Link field on the current form.
- **Fetching from a field that does not exist:** Check the linked DocType to confirm the exact fieldname.
- **Expecting complex logic:** Fetch From copies a value. It is not a replacement for business logic or validation.

## When To Use Fetch From

Use Fetch From when:

- A field should show a value from a selected Customer, Supplier, Item, Employee, Project, or another linked record.
- The value is informational and follows the selected linked document.
- You want a no-code configuration instead of a Client Script.
- The fetching rule is simple and does not require conditions or calculations.

## Related Topics

- [Customize Form](https://docs.frappe.io/erpnext/customize-form)
- [Custom Field](https://docs.frappe.io/erpnext/custom-field)
- [Client Script](https://docs.frappe.io/erpnext/customization/custom-scripts)
- [DocType](https://docs.frappe.io/framework/user/en/basics/doctypes)
- [Link Field](https://docs.frappe.io/framework/user/en/basics/doctypes/fieldtypes)

<!-- page: framework/framework__help__event-streaming.md -->
---
title: "Event Streaming"
space: "Framework"
url: "https://docs.frappe.io/framework/help/event-streaming"
updated: "2026-07-04"
---

Event Streaming was a Frappe feature used to publish document changes from one Frappe site and consume them on another site. It was useful when selected DocTypes needed to be synchronized between sites without building a separate integration for every record type.

## How Event Streaming Worked

In a typical setup, one site acted as the **Event Producer** and another site acted as the **Event Consumer**. When selected documents were created or updated on the producer site, events were recorded and then consumed by the other site. This made it possible to replicate masters, transactions, or custom DocTypes across Frappe sites.

## Status In Version 15 And Later

Event Streaming is not supported as a maintained core feature from Frappe/ERPNext version 15 onward. In Frappe version 14, Event Streaming existed inside the framework source under `frappe/event_streaming`. In version 15, Frappe added a removal patch for the Event Streaming module and its DocTypes, including Event Producer, Event Consumer, Event Update Log, and related mapping DocTypes.

## Separate App

The feature was separated into its own app: [frappe/event_streaming](https://github.com/frappe/event_streaming). However, the app is not actively maintained. The GitHub repository was archived by Frappe on December 6, 2024, is now read-only, and has no published releases. Treat it as unsupported for new production implementations unless your team is ready to test and maintain it independently.

## Recommended Alternatives

- **REST API:** Use Frappe's REST API for explicit integrations between ERPNext and other systems.
- **Webhooks:** Use webhooks when another system should be notified after a document is created or updated.
- **Background Jobs:** Use scheduled or queued jobs for sync logic that needs retries, logs, and error handling.
- **Custom Integration Apps:** Build a custom app when data mapping, conflict handling, or business rules need to be controlled carefully.

## When To Be Careful

Avoid planning new implementations around Event Streaming on version 15 or later. For current ERPNext integrations, prefer APIs, webhooks, and integration-specific queues so ownership, retry behavior, and failure handling are clear.

## Related Topics

- [frappe/event_streaming on GitHub](https://github.com/frappe/event_streaming)
- [Frappe version 15 Event Streaming removal patch](https://github.com/frappe/frappe/blob/version-15/frappe/patches/v15_0/remove_event_streaming.py)
- [Frappe REST API](https://docs.frappe.io/framework/user/en/api/rest)
- [Webhooks](https://docs.frappe.io/framework/user/en/guides/integration/webhooks)
- [Background Jobs](https://docs.frappe.io/framework/user/en/api/background_jobs)

<!-- page: framework/framework__keyboard-shortcuts.md -->
---
title: "Keyboard Shortcuts"
space: "Framework"
url: "https://docs.frappe.io/framework/keyboard-shortcuts"
updated: "2026-07-04"
---

# Keyboard Shortcuts

Keyboard shortcuts help you move around Frappe Desk without switching between the keyboard and mouse. Use them to open pages, search for records, save forms, open help, and view the complete shortcuts list from anywhere in Desk.

The shortcuts shown in Desk follow your operating system. On macOS, Desk shows **Command** as **⌘** and **Option** as **⌥**. On Windows and Linux, use the equivalent **Ctrl** and **Alt** keys where applicable.

## View keyboard shortcuts

Press **Shift + /** to open the Keyboard Shortcuts panel. The panel lists the global shortcuts available in Desk.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

## Global shortcuts


| Shortcut          | Action                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------- |
| **⌘ + S**         | Trigger the primary action on the current page. On a form, this is usually the save action. |
| **⌘ + K**         | Open the Awesomebar.                                                                        |
| **⌘ + G**         | Open the Awesomebar.                                                                        |
| **⌥ + S**         | Open Settings.                                                                              |
| **Shift + /**     | Show Keyboard Shortcuts.                                                                    |
| **⌥ + H**         | Open Help.                                                                                  |
| **Shift + ⌘ + R** | Clear cache and reload.                                                                     |
| **Shift + T**     | Open the console.                                                                           |
| **Shift + ⌘ + G** | Switch theme.                                                                               |


Press **Alt** to reveal additional shortcuts in the menu and sidebar.

## Open pages with the Awesomebar

Press **⌘ + K** or **⌘ + G** to open the Awesomebar. Start typing the page, report, document type, or record you want to open, then use the arrow keys to move through results and press **Enter** to select one.



*(screenshot — not bundled; see the live page URL in this file's front matter)*

## Navigate search results

- Use the **Up** and **Down** arrow keys to move through results.
- Press **Enter** to open the selected result.
- Press **Esc** to close the Awesomebar or shortcut panel.

## When shortcuts do not work

Some browser, operating system, or extension shortcuts may take priority over Desk shortcuts. If a shortcut does not work, click inside the Desk page and try again. If the cursor is inside a text field, close the field or move focus back to the page before using a global shortcut.

<!-- page: framework/framework__notifications.md -->
---
title: "Notifications"
space: "Framework"
url: "https://docs.frappe.io/framework/notifications"
updated: "2026-02-17"
---

The **Notification** doctype in Frappe Framework provides a powerful way to automate notifications across different channels when specific events occur in your system. This guide explains how to configure and use notifications effectively.

## General Settings

- **Enabled**: Toggle to activate or deactivate a notification.
- **Channel**: Select the delivery method for your notification:
  - **Email**: Send notifications via email
  - **Slack**: Send notifications to a Slack channel
  - **System Notification**: Display notifications within the Frappe interface
  - **SMS**: Send notifications via SMS (requires SMS Settings configuration)
- **Is Standard**: For developer mode; marks the notification as part of a standard module

## Event Triggers

Notifications can be triggered based on various events:

### Document Events

- **New**: Triggered when a new document is created
- **Save**: Triggered when a document is saved
- **Submit**: Triggered when a document is submitted
- **Cancel**: Triggered when a document is cancelled

### Date-Based Events

- **Days Before**: Triggered a specific number of days before a date field value
- **Days After**: Triggered a specific number of days after a date field value
- When using these events:
  - **Reference Date**: Select the date field to monitor
  - **Days Before or After**: Specify number of days before/after the date to trigger

### Value-Based Events

- **Value Change**: Triggered when a specific field's value changes
  - **Value Changed**: Select the field to monitor for changes

### Method-Based Events

- **Method**: Triggered when a specific document method is called
  - **Trigger Method**: Specify the method name (e.g., "before_insert", "after_update")

### Custom Events

- **Custom**: For programmatically triggered notifications

## Conditional Triggers

You can make notifications more targeted by adding conditions:

- **Condition**: A Python expression that must evaluate to `True` for the notification to be sent
- The condition has access to:
  - `doc`: The document that triggered the notification
  - `nowdate()`: Current date function
  - `frappe.utils`: Utility functions

### Examples

- The _Status_ of the document is "Open"

    ```python
    doc.status=="Open"
    ```

- The document's _Due Date_ matches the current date

    ```python
    doc.due_date==nowdate()
    ```

- The total is bigger than 40,000

    ```python
    doc.total > 40000
    ```

## Recipients Configuration

### Email, System Notification, and SMS Channels

Configure recipients using the Recipients table:

1. **Receiver Type**:

   - **By Document Field**: Select a field containing email addresses/phone numbers
   - **By Role**: Select a role whose users will receive the notification
   - **Custom**: Specify custom recipients

2. **Additional Options**:

   - **CC/BCC**: For email notifications
   - **Condition**: Python expression to conditionally include recipients
   - **Send to All Assignees**: Include all users assigned to the document

### For Slack Channel

- Select a predefined Slack Webhook URL from the dropdown

## Message Configuration

### Subject (for Email, Slack, and System Notifications)

- Enter the subject line text
- Support for Jinja templates: `{{ doc.name }} Delivered`

### Message Body

- **Message Type**: Select between HTML, Markdown, or Plain Text (available in developer mode only)
- **Message**: Enter the notification content
- Uses Jinja templating for dynamic content

### Templating Variables

- `{{ doc }}`: Access any field from the triggering document (e.g., `{{ doc.customer }}`)
- `{{ comments }}`: Access document comments (e.g., `{{ comments[-1].comment }}`)
- `{% if %}...{% endif %}`: Conditional logic
- `{{ nowdate() }}`: Current date

### Template Example

```html
<h3>Order Overdue</h3>

<p>Transaction {{ doc.name }} has exceeded Due Date. Please take necessary action.</p>

<!-- show last comment -->
{% if comments %}
Last comment: {{ comments[-1].comment }} by {{ comments[-1].by }}
{% endif %}

<h4>Details</h4>

<ul>
<li>Customer: {{ doc.customer }}
</li><li>Amount: {{ doc.grand_total }}
</li></ul>
```

## Advanced Options

### Attachment Settings

- **Attach Print**: Attach a PDF printout of the document
    - **Print Format**: Select a specific print format for the attached PDF
- **Attach Files**:
    - "All": sends all files that are attached to the record that triggered the notification
    - "From Field": sends a file from a specific attachment field
        - **From Attach Field**: Select the field that holds the attachment you want to send

### Post-Notification Actions

- **Set Property After Alert**: Update a field after sending the notification
- **Value To Be Set**: The value to set in the specified field

## Best Practices

1. **Test your notifications**: Use the "Get Alerts for Today" button to test date-based notifications.
2. **Keep conditions specific**: Make sure your conditions are targeted to avoid notification fatigue.
3. **Use templating wisely**: Make messages clear and include only relevant information.
4. **Verify recipient fields**: Ensure fields contain valid email addresses or phone numbers.
5. **Consider permission levels**: Recipients must have permission to access documents referenced in notifications.

## Troubleshooting

- If notifications aren't sending, check that the document meets all conditions.
- For email notifications, verify email settings are properly configured.
- For SMS notifications, ensure SMS settings are configured.
- For Slack notifications, verify webhook URL is valid and active.
- Check server logs for any errors related to notification delivery.

## Technical Notes

- Notifications are processed asynchronously to avoid impact on system performance.
- Date-based events are checked daily via a scheduled job.
- Document-event notifications are triggered in real-time when the associated action occurs.
- Conditions and templates are evaluated in a restricted environment for security.

By effectively configuring the Notification doctype, you can keep users informed about important events and automate communication across your Frappe application.

<!-- page: framework/framework__oauth2.md -->
---
title: "OAuth2"
space: "Framework"
url: "https://docs.frappe.io/framework/oauth2"
updated: "2026-02-17"
---

Frappe Framwork uses [`oauthlib`](https://github.com/oauthlib/oauthlib) to manage OAuth2 requirements. A Frappe instance can function as all of these:

1. **Resource Server**: contains resources, for example the data in your DocTypes.
2. **Authorization Server**: server that issues tokens to access some resource.
3. **Client**: app that requires access to some resource on a resource server.

DocTypes pertaining to the above roles:

1. **Common**
   - **OAuth Settings**: allows configuring certain OAuth features pertaining to the three roles.
2. **Authorization Server**
   - **OAuth Client**: keeps records of _clients_ registered with the frappe instance.
   - **OAuth Bearer Token**: tokens given out to registered _clients_ are maintained here.
   - **OAuth Authorization Code**: keeps track of OAuth codes a client responds with in exchange for a token.
   - **OAuth Provider Settings**: allows skipping authorization. `[DEPRECATED]` use **OAuth Settings** instead.
3. **Client**
   - **Connected App**: keeps records of _authorization servers_ against whom this frappe instance is registered as a _client_ so some resource can be accessed. Eg. a users Google Drive account.
   - **Social Key Login**: similar to **Connected App**, but for the purpose of logging into the frappe instance. Eg. a users Google account to enable "Login with Google".
   - **Token Cache**: tokens received by the Frappe instance when accessing a **Connected App**.

### Features

Additional features over `oauthlib` that have implemented in the Framework:

- **Dynamic Client Registration**: allows a client to register itself without manual configuration by the resource owner. [RFC7591](https://datatracker.ietf.org/doc/html/rfc7591)
- **Authorization Server Metadata Discovery**: allows a client to view the instance's auth server (itself) metadata such as auth end points. [RFC8414](https://datatracker.ietf.org/doc/html/rfc8414)
- **Resource Server Metadata Discovery**: allows a client to view the instance's resource server metadata such as documentation, auth servers, etc. [RFC9728](https://datatracker.ietf.org/doc/html/rfc9728)

### Additional Docs

Documentation of various OAuth2 features:

1. [How to setup OAuth 2?](https://docs.frappe.io/framework/user/en/guides/integration/how_to_set_up_oauth)
2. [OAuth 2](https://docs.frappe.io/framework/user/en/guides/integration/rest_api/oauth-2)
3. [Token Based Authentication](https://docs.frappe.io/framework/user/en/guides/integration/rest_api/token_based_authentication)
4. [Using Frappe as OAuth Service](https://docs.frappe.io/framework/user/en/using_frappe_as_oauth_service)
5. [Social Login Key](https://docs.frappe.io/framework/user/en/guides/integration/social_login_key)
6. [Connected App](https://docs.frappe.io/framework/user/en/guides/app-development/connected-app)

> **Warning**
>
> Some of these pages might be outdated, it is always recommended to check the
> code when in doubt.

### OAuth Settings

A Single doctype that allows configuring OAuth2 related features. It is
recommended to open the DocType page itself as each field has a
sufficiently descriptive help text.

The settings allow toggling the following features:

- Authorization check when active token is present using the _Skip Authorization_ field. _**Note**: Keep this unchecked in production._
- **Authorization Server Metadata Discovery**: by toggling the _Show Auth Server Metadata_ field.
- **Dynamic Client Registration**: by toggling the _Enable Dynamic Client Registration_ field.
- **Resource Server Metadata Discovery**: by toggling the _Show Protected Resource Metadata_.

The remaining fields (in the **Resource** section) are used only when responding to requests on `/.well-known/oauth-protected-resource`

> **Regarding Public Clients**
>
> Public clients, for example an SPA, have restricted access by default. This
> restriction is applied by use of CORS.
>
> To side-step this restriction for certain trusted clients, you may add their
> hostnames to the **Allowed Public Client Origins** field.

<!-- page: framework/framework__permission-types.md -->
---
title: "Permission Types"
space: "Framework"
url: "https://docs.frappe.io/framework/permission-types"
updated: "2026-02-17"
---

> Note: This feature is available v16 onwards.

Custom Permission Types let you create permission flags beyond the built-in ones `read`, `write`, `create`, `delete`, `submit`). Use them for action-specific permissions like "approve record", "download file", or "impersonate user".

## How it works

There are three steps:

1. **Developer creates the permission type** in dev mode for a DocType
2. **Developer adds permission checks** in code where the action happens
3. **System Manager assigns the permission to roles** in the Desk UI

The permission type is saved as a fixture and shipped with your app.

## Example: Creating an "approve" permission on Invoice

### Step 1: Create the permission type (Developer)

1. Enable developer mode and log in as Administrator
2. Create a new **Permission Type** record
3. Set **Perm Type** as `approve` and **DocType** as `Invoice`
4. Save

The permission type is now created and will be exported with your app.

### Step 2: Add permission checks in your code (Developer)

In your Invoice controller or in functions that handle approvals, check for the permission:

```python
@frappe.whitelist()
def approve_invoice(invoice_name):
    invoice = frappe.get_doc("Invoice", invoice_name)
    if not frappe.has_permission(invoice, "approve"):
        frappe.throw("Not permitted to approve", frappe.PermissionError)
    invoice.approval_status = "Approved"
    invoice.save()
```

You can also check without throwing an error:

```python
if frappe.has_permission(invoice, "approve"):
    # show approve button on frontend
```

### Step 3: Assign to roles (System Manager)

After your app is installed, system managers assign the permission to roles:

1. Open **Role Permission Manager**
2. Select the Invoice DocType
3. For each role, check or uncheck the "Approve" column, just like other permissions
4. The permission is now applied to all users with that role

That's it. Users with the "approve" permission can now perform the action. Users without it will see an error.

## How to check the permission

Use `frappe.has_permission()` in your Python code:

```python
# Check document-level permission
if frappe.has_permission(invoice_doc, "approve"):
    # User can approve this invoice

# Check DocType-level permission
if frappe.has_permission("Invoice", "approve"):
    # User can approve any invoice
```

<!-- page: framework/framework__portal-web-form__web-form-request.md -->
---
title: "Web Form Request"
space: "Framework"
url: "https://docs.frappe.io/framework/portal-web-form/web-form-request"
updated: "2026-06-26"
---

## Web Form Request

A **Web Form Request** creates a private request link for a **Web Form**.

Use it when a form should not be fully public, but the respondent should still be able to submit it without having a user account. For example, you can send a customer satisfaction survey link to a customer, pre-fill customer-specific values, and keep internal fields hidden from the browser.

## When to Use

Use a **Web Form Request** when:

1. The respondent should open the form through a private link.
2. The respondent may not have a user account.
3. The form should include respondent-specific values.
4. The target document needs hidden values that should not be exposed in the web page.

## Creating a Request

Create a **Web Form Request** and select the *Web Form* it belongs to. A URL-safe key is generated automatically.

The request can define:

- *Expires On*: expiry date and time for the request key.
- *Web Form Values*: JSON values shown in the web form and editable by the respondent.
- *Doc Values*: JSON values applied to the target document on submission, but not sent to the browser.

The request key is used in the web form URL:

```text
/your-web-form-route/new?web_form_request_key=<key>
```

You can copy this URL from the **Web Form Request** form.

## Requiring a Key

Enable *Key required* on the **Web Form** to require a valid **Web Form Request** key.

If *Key required* is enabled and no valid key is provided, the web form cannot be opened or submitted.

If *Login required* is also enabled, both conditions apply: the user must be logged in and must provide a valid request key.

## Pre-filled and Hidden Values

Use *Web Form Values* for fields that should be visible to the respondent. These fields must be included in the **Web Form** fields table.

Use *Doc Values* for fields that should be set on the created document but should not be visible to the respondent. These fields must exist on the target DocType.

The JSON keys must use the underlying field names, for example `customer` or `survey_source`.

Example:

```json
{
 "customer": "CUST-0001",
 "survey_source": "Partner CSAT"
}
```

## Expiry and Usage

If *Expires On* is set, the request key cannot be used after that date and time.

For a single-response web form, the request is marked as used after successful submission and links to the created target document. This allows the same key to be used later for editing or deleting that response if the **Web Form** settings allow it.

For a **Web Form** with *Allow multiple responses* enabled, the request key can be reused for multiple submissions and does not link to a single target document.

## Related Web Form Settings

- *Allow Multiple Responses:*  
If enabled, the same request key can submit multiple responses. In this mode, the **Web Form Request** cannot have a *Reference Docname*, because one request may create many documents.
- *Allow Editing After Submit:*  
If enabled, a request key linked to a response can open and edit that response.
- *Allow Delete:*  
If enabled, a request key linked to a response can delete that response.

<!-- page: framework/framework__sqlite-search.md -->
---
title: "SQLite Search"
space: "Framework"
url: "https://docs.frappe.io/framework/sqlite-search"
updated: "2026-02-17"
---

SQLite Search is a full-text search framework for Frappe applications that provides advanced search capabilities using SQLite's FTS5 (Full-Text Search) engine. It offers features like spelling correction, time-based recency scoring, custom ranking, permission-aware filtering, and extensible scoring pipelines.

## Table of Contents

- [Quick Start](#quick-start)

- [How It Works](#how-it-works)

- [Configuration](#configuration)

- [Features &amp; Customization](#features--customization)

- [API Reference](#api-reference)

## Quick Start

### 1. Create a Search Class

Create a search implementation by extending `SQLiteSearch`:

```python

# my_app/search.py

from frappe.search.sqlite_search import SQLiteSearch

class MyAppSearch(SQLiteSearch):

    # Database file name

    INDEX_NAME = "my_app_search.db"

    # Define the search schema

    INDEX_SCHEMA = {

        "metadata_fields": ["project", "owner", "status"],

        "tokenizer": "unicode61 remove_diacritics 2 tokenchars '-_'",

    }

    # Define which doctypes to index and their field mappings

    INDEXABLE_DOCTYPES = {

        "Task": {

            "fields": ["name", {"title": "subject"}, {"content": "description"}, "modified", "project", "owner", "status"],

        },

        "Issue": {

            "fields": ["name", "title", "description", {"modified": "last_updated"}, "project", "owner"],

            "filters": {"status": ("!=", "Closed")},  # Only index non-closed issues

        },

    }

    def get_search_filters(self):

        """Return permission filters for current user"""

        # Get projects accessible to current user

        accessible_projects = frappe.get_all(

            "Project",

            filters={"owner": frappe.session.user},

            pluck="name"

        )

        if not accessible_projects:

            return {"project": []}  # No access

        return {"project": accessible_projects}

```

### 2. Register the Search Class

Add your search class to hooks.py:

```python

# my_app/hooks.py

sqlite_search = ['my_app.search.MyAppSearch']

```

### 3. Create API Endpoint

Create a whitelisted method to expose search functionality:

```python

# my_app/api.py

import frappe

from my_app.search import MyAppSearch

@frappe.whitelist()

def search(query, filters=None):

    search = MyAppSearch()

    result = search.search(query, filters=filters)

    return result

```

### 4. Build the Index

Build the search index programmatically or via console:

```python

from my_app.search import MyAppSearch

search = MyAppSearch()

search.build_index()

```

## How It Works

### 1. Indexing Process

#### Full Index Building

When you call `build_index()`, the framework performs a complete index rebuild:

1. **Database Preparation**: Creates a temporary SQLite database with FTS5 tables configured according to your schema

2. **Document Collection**: Queries all specified doctypes using the configured field mappings and filters

3. **Document Processing**: For each document:

   - Extracts and maps fields according to `INDEXABLE_DOCTYPES` configuration

   - Cleans HTML content using BeautifulSoup to extract plain text

   - Applies custom document preparation logic if `prepare_document()` is overridden

   - Validates required fields (title, content) are present

4. **Batch Insertion**: Inserts processed documents into the FTS5 index in batches for performance

5. **Vocabulary Building**: Constructs a spelling correction dictionary from all indexed text

6. **Atomic Replacement**: Replaces the existing index database with the new one atomically

#### Individual Document Indexing

For real-time updates using `index_doc()` or `remove_doc()`:

1. **Single Document Processing**: Retrieves and processes one document using the same field mapping logic

2. **Incremental Update**: Updates the existing FTS5 index by inserting, updating, or deleting the specific document

3. **Vocabulary Update**: Updates the spelling dictionary with new terms from the document

### 2. Search Process

When a user performs a search using `search()`, the framework executes these steps:

1. **Permission Filtering**: Calls `get_search_filters()` to determine what documents the current user can access

2. **Query Preprocessing**:

   - Validates the search query is not empty

   - Combines user-provided filters with permission filters

3. **Spelling Correction**:

   - Analyzes query terms against the vocabulary dictionary

   - Uses trigram similarity to suggest corrections for misspelled words

   - Expands the original query with corrected terms

4. **FTS5 Query Execution**:

   - Constructs an FTS5-compatible query string

   - Executes the full-text search against the SQLite database

   - Applies metadata filters (status, owner, project, etc.)

   - Retrieves raw results with BM25 scores

5. **Results Processing**:

   - **Custom Scoring**: Applies the scoring pipeline to calculate final relevance scores

     - Base BM25 score processing

     - Title matching boosts (exact and partial matches)

     - Recency boosting based on document age

     - Custom scoring functions (doctype-specific, priority-based, etc.)

   - **Ranking**: Sorts results by final scores and assigns rank positions

   - **Content Formatting**: Generates content snippets and highlights matching terms

## Configuration

### INDEX_SCHEMA

Defines the structure of your search index:

```python

INDEX_SCHEMA = {

    # Text fields that will be searchable (defaults to ["title", "content"])

    "text_fields": ["title", "content"],

    # Metadata fields stored alongside text content for filtering

    "metadata_fields": ["project", "owner", "status", "priority"],

    # FTS5 tokenizer configuration

    "tokenizer": "unicode61 remove_diacritics 2 tokenchars '-_@.'"

}

```

### INDEXABLE_DOCTYPES

Specifies which doctypes to index and how to map their fields:

```python

INDEXABLE_DOCTYPES = {

    "Task": {

        # Field mapping

        "fields": [

            "name",

            {"title": "subject"},        # Maps subject field to title

            {"content": "description"},  # Maps description field to content

            {"modified": "creation"},    # Use creation instead of modified for recency boost

            "project",

            "owner"

        ],

        # Optional filters to limit which records are indexed

        "filters": {

            "status": ("!=", "Cancelled"),

            "docstatus": ("!=", 2)

        }

    }

}

```

### Field Mapping Rules

- **String fields**: Direct mapping `"field_name"`

- **Aliased fields**: Dictionary mapping `{"schema_field": "doctype_field"}`

- **Required fields**: `title` and `content` fields must be present or explicitly mapped (e.g., `{"title": "subject"}`)

- **Auto-added fields**: `doctype` and `name` are automatically included

- **Modified field**: Added automatically if used in any doctype configuration. Used for recency boosting - if you want to use a different timestamp field (like `creation` or `last_updated`), map it to `modified` using `{"modified": "creation"}`

## Features &amp; Customization

### Permission Filtering

Implement `get_search_filters()` to control access:

```python

def get_search_filters(self):

    """Return filters based on user permissions"""

    user = frappe.session.user

    if user == "Administrator":

        return {}  # No restrictions

    # Example: User can only see their own and public documents

    return {

        "owner": user,

        "status": ["Active", "Published"]

    }

```

### Custom Scoring

Create custom scoring functions to influence search relevance:

```python

class MyAppSearch(SQLiteSearch):

    ...

    @SQLiteSearch.scoring_function

    def *get*priority_boost(self, row, query, query_words):

        """Boost high-priority items"""

        priority = row.get("priority", "Medium")

        if priority == "High":

            return 1.5

        if priority == "Medium":

            return 1.1

        return 1.0

```

### Recency Boosting

The framework automatically provides time-based recency boosting using the `modified` field:

```python

# The modified field is used for calculating document age

# Recent documents get higher scores:

# - Last 24 hours: 1.8x boost

# - Last 7 days: 1.5x boost

# - Last 30 days: 1.2x boost

# - Last 90 days: 1.1x boost

# - Older documents: gradually decreasing boost

# If your doctype uses a different timestamp field, map it to modified:

INDEXABLE_DOCTYPES = {

    "GP Discussion": {

        "fields": ["name", "title", "content", {"modified": "last_post_at"}, "project"],

    },

    "Article": {

        "fields": ["name", "title", "content", {"modified": "published_date"}, "category"],

    }

}

```

### Document Preparation

Override `prepare_document()` for custom document processing:

```python

def prepare_document(self, doc):

    """Custom document preparation"""

    document = super().prepare_document(doc)

    if not document:

        return None

    # Add computed fields

    if doc.doctype == "Task":

        # Combine multiple fields into content

        content_parts = [

            doc.description or "",

            doc.notes or "",

            "\n".join([comment.content for comment in doc.get("comments", [])])

        ]

        document["content"] = "\n".join(filter(None, content_parts))

        # set fields that might be stored in another table

        document["category"] = get_category_for_task(doc)

    return document

```

### Spelling Correction

The framework includes built-in spelling correction using trigram similarity:

```python

# Spelling correction happens automatically

search_result = search.search("projetc managment")  # Will find "project management"

# Access correction information

print(search_result["summary"]["corrected_words"])

# Output: {"projetc": "project", "managment": "management"}

```

### Content Processing

HTML content is automatically cleaned and processed using BeautifulSoup:

```python

# Complex HTML content like this:

html_content = """

<div class="article">

    <h1>API Documentation</h1>

    <p>Learn how to integrate with our <a href="/api">REST API</a>.</p>

    <img src="/images/api-flow.png" alt="API workflow diagram">

    <ul>

        <li><strong>Authentication:</strong> Use <code>Bearer tokens</code></li>

        <li>Rate limiting: <em>1000 requests/hour</em></li>

    </ul>

    <blockquote>See our <a href="/examples">code examples</a> for details.</blockquote>

    <table><tbody><tr><td>Method</td><td>POST</td></tr></tbody></table>

    <script>analytics.track('page_view');</script>

    <style>.hidden { display: none; }</style>

</div>

"""

# Is automatically converted to clean, searchable plain text:

"""

API Documentation

Learn how to integrate with our REST API.

Authentication: Use Bearer tokens

Rate limiting: 1000 requests/hour

See our code examples for details.

Method POST

"""

# The cleaning process:

# 1. Removes all HTML tags (<div>, <h1>, <strong>, <code>, etc.)

# 2. Strips out scripts, styles, and non-content elements

# 3. Extracts link text while removing href URLs

# 4. Normalizes whitespace and line breaks

```

### Title-Only Search

```python

results = search.search("project update", title_only=True)

```

### Advanced Filtering

```python

accessible_projects = ['PROJ001', 'PROJ002', ...]

filters = {

    "project": accessible_projects,     # Multiple values (IN clause)

    "owner": current_user,              # Single value (= clause)

}

results = search.search("bug fix", filters=filters)

```

### Automatic Index Handling

The framework handles index building and maintenance automatically when you register your search class:

```python

# hooks.py

sqlite_search = ['my_app.search.MyAppSearch']

```

**What the framework does automatically:**

1. **Post-Migration Index Building**: Builds the search index automatically after running `bench migrate`

2. **Periodic Index Verification**: Checks every 15 minutes that the index exists and rebuilds if missing

3. **Real-time Document Updates**: Automatically calls `index_doc()` and `remove_doc()` on document lifecycle events (insert, update, delete) for all doctypes defined in your `INDEXABLE_DOCTYPES`

### Manual Index Handling

If you prefer to have manual control over the lifecycle of indexing, then you can simply opt out of automatic index handling by not registering the search class in `sqlite_search` hook.

```python

from my_app.search import MyAppSearch

def build_index_in_background():

    """Manually trigger background index building"""

    search = MyAppSearch()

    if search.is_search_enabled() and not search.index_exists():

        frappe.enqueue("my_app.search.build_index", queue="long")

# hooks.py

scheduler_events = {

    # Custom scheduler (if you want different timing)

    "daily": ["my_app.search.build_index_if_not_exists"],

}

```

## API Reference

#### `search(query, title_only=False, filters=None)`

Main search method that returns formatted results.

**Parameters:**

- `query` (str): Search query text

- `title_only` (bool): Search only in title fields

- `filters` (dict): Additional filters to apply

**Returns:**

```python

{

    "results": [

        {

            "doctype": "Task",

            "name": "TASK-001",

            "title": "Fix login bug",

            "content": "User cannot login after password reset...",

            "score": 0.85,

            "original_rank": 3, # original bm25 rank

            "rank": 1, # modified rank after custom scoring pipeline

            # ... other metadata fields

        }

    ],

    "summary": {

        "duration": 0.023,

        "total_matches": 15,

        "returned_matches": 15,

        "corrected_words": {"loggin": "login"},

        "corrected_query": "Fix login bug",

        "title_only": False,

        "filtered_matches": 15,

        "applied_filters": {"status": ["Open"]}

    }

}

```

#### `build_index()`

Build the complete search index from scratch.

#### `index_doc(doctype, docname)`

Index a single document.

#### `remove_doc(doctype, docname)`

Remove a single document from the index.

#### `is_search_enabled()`

Check if search is enabled (override to add disable logic).

#### `index_exists()`

Check if the search index exists.

#### `get_search_filters()`

**Must be implemented by subclasses.** Return filters for the current user.

**Returns:**

```python

{

    "field_name": "value",           # Single value

    "field_name": ["val1", "val2"],  # Multiple values

}

```

#### `scoring_function()`

Use the `@SQLiteSearch.scoring_function` decorator to mark a function as a scoring function.

<!-- page: framework/framework__user__en__api.md -->
---
title: "Developer API\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api"
updated: "2026-02-17"
---

## Python

Frappe aims to achieve minimum cognitive load for its users. Hence, you can find
the most used methods and utilities in the `frappe` namespace itself. It's the
only import you need (most of the time) in a Python file.

1. [Document](/framework/user/en/api/document)
2. [Database](/framework/user/en/api/database)
3. [Jinja](/framework/user/en/api/jinja)
4. [Common Utilities](/framework/user/en/api/utils)
5. [Router](/framework/user/en/python-api/routing-and-rendering)
6. [Response](/framework/user/en/python-api/response)
7. [Language Resolution](/framework/v14/user/en/python-api/language)
8. [Search](/framework/user/en/python-api/search)
9. [Hooks](/framework/user/en/python-api/hooks)
10. [REST API](/framework/user/en/api/rest)
11. [Full Text Search](/framework/user/en/api/full-text-search)
12. [Dialog API](/framework/user/en/api/py-dialog)
13. [Query Builder](/framework/user/en/api/query-builder)

## Javascript

Frappe attaches itself to the `window` object under the `frappe` namespace. You
will find most of the Client API under the `frappe` object. All of these methods
are only available inside the Desk. A good way to explore these APIs is from the
browser console.

1. [Form](/framework/user/en/api/form)
2. [Controls](/framework/user/en/api/controls)
3. [Page](/framework/user/en/api/page)
4. [Tree](/framework/user/en/api/tree)
5. [Server Calls (AJAX)](/framework/user/en/api/server-calls)
6. [Common Utilities](/framework/user/en/api/js-utils)
7. [Dialog API](/framework/user/en/api/dialog)
8. [Chart API](/framework/user/en/api/chart)
9. [Scanner API](/framework/user/en/api/scanner)

## Other

1. [REST API](/framework/user/en/api/rest)
2. [Jinja API](/framework/user/en/api/jinja)

<!-- page: framework/framework__user__en__api__background_jobs.md -->
---
title: "Background Jobs"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/background_jobs"
updated: "2026-02-17"
---

Frappe ships with a system for running jobs in the background. It is implemented by using the [schedule package](https://pypi.org/project/schedule/) and a simple long-running infinite [while loop](https://github.com/frappe/frappe/blob/d0efa8e3ff734268a30b4804427641d2a5ed643e/frappe/utils/scheduler.py#L36-L46).

You can enqueue a python method to run in the background by using the `frappe.enqueue` method:


```
def long_running_job(param1, param2):
    # expensive tasks
    pass

# directly pass the function
frappe.enqueue(long_running_job, queue='short', param1='A', param2='B')

# or pass the full module path as string
frappe.enqueue('app.module.folder.long_running_job', queue='short', param1='A', param2='B')
```
Here are all the possible arguments you can pass to the `enqueue`:


```
frappe.enqueue(
    method, # python function or a module path as string
    queue="default", # one of short, default, long
    timeout=None, # pass timeout manually
    is_async=True, # if this is True, method is run in worker
    now=False, # if this is True, method is run directly (not in a worker) 
    job_name=None, # specify a job name
    enqueue_after_commit=False, # enqueue the job after the database commit is done at the end of the request
    at_front=False, # put the job at the front of the queue
    **kwargs, # kwargs are passed to the method as arguments
)
```
You can also enqueue a [Document](https://frappeframework.com/docs/v14/user/en/api/document) method by using `frappe.enqueue_doc`:


```
frappe.enqueue_doc(
    doctype,
    name,
    "do_something", # name of the controller method
    queue="long",
    timeout=4000,
    param="value"
)
```
Queue
-----

There are 3 default queues that are configured with the framework: `short`, `default`, and `long`. Each queue has a default timeout as follows:

* short: 300 seconds
* default: 300 seconds
* long: 1500 seconds

You can also pass a custom timeout to the `enqueue` method.

### Custom Queues

You can add custom queues by configuring them in `[common_site_config.json](https://frappeframework.com/docs/v14/user/en/basics/site_config#common-site-config)`:


```
{
    ...
    "workers": {
        "myqueue": {
            "timeout": 5000, # queue timeout
            "background_workers": 4, # number of workers for this queue
        }   
    }
}
```
Workers
-------

By default Frappe sets up 3 worker types for consuming from each queue. The default configuration looks like this:


```
bench worker --queue short
bench worker --queue default
bench worker --queue long
```
In production these 3 worker processes are replicated to configured number of background workers to handle higher workloads.

NOTE: This way of mapping workers to single queue is just a convention and it's not necessary to follow it.

### Multi-queue consumption

You can specify more than one queue for workers to consume from by specifying a comma separate string of queue names.

Example: If you wanted to combine short and default workers and only use two types of workers instead of default configuration then you can modify your worker configuration like this:


```
bench worker --queue short,default
bench worker --queue long
```
NOTE: The examples shown here are for Procfile format but they can be applied to supervisor or systemd configurations easily too.

### Burst Mode using `--burst`


```
bench worker --queue short --burst
```
This command will spawn a tempoary worker that will start consuming short queue and quit once queue is empty. If you periodically need higher amount of workers then you can use your OS's crontab to setup burst workers at specific times.

Scheduler Events
----------------

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
**app/scheduled_tasks.py**


```
def update_database_usage():
    pass
```

> After changing any scheduled events in hooks.py, you need to run bench migrate for changes to take effect.
> 
> 

### Available Events

* `hourly`, `daily`, `weekly`, and `monthly`

These events will trigger every hour, day, week, and month respectively.
* `hourly_long`, `daily_long`, `weekly_long`, `monthly_long`

Same as above but these jobs are run in the [long worker](https://frappeframework.com/docs/v14/user/en/basics/directory-structure#worker_long) suitable for long-running jobs.
* `all`

The `all` event is triggered every 4 minutes. This can be configured via the `scheduler_interval` key in [common_site_config.json](https://frappeframework.com/docs/v14/user/en/basics/sites#scheduler_tick_interval)
* `cron`

A valid cron string that can be parsed by [croniter](https://pypi.org/project/croniter/).

Usage Examples:


```
scheduler_events = {
    "daily": [
        "app.scheduled_tasks.manage_recurring_invoices"
    ],
    "daily_long": [
        "app.scheduled_tasks.take_backups_daily"
    ],
    "cron": {
        "15 18 * * *": [
            "app.scheduled_tasks.delete_all_barcodes_for_users"
        ],
        "*/6 * * * *": [
            "app.scheduled_tasks.collect_error_snapshots"
        ],
        "annual": [
            "app.scheduled_tasks.collect_error_snapshots"
        ]
    }
}
```


Configurable Scheduler Events
----------------

On scenarios that require a user configurable trigger interval, Create a `Scheduler Event` record and create a `Scheduled Job Type` entry against that record. This doesn't require `scheduler_event` hook.

Example:
```
# Create `Scheduler Event` record
sch_eve = frappe.new_doc("Scheduler Event")
sch_eve.scheduled_against = "Process Payment Reconciliation"
sch_eve.save()

# Create `Scheduled Job Type`
job = frappe.new_doc("Scheduled Job Type")
job.frequency = "Cron"
job.scheduler_event = sch_eve.name
job.cron_format = "0/5 * * * *"     # runs every five minutes
job.save()
```

The `Scheduled Job Type`s trigger interval can be modified later, which persits across bench migration.

> The jobs triggered by scheduler are run by **Administrator** user. This also means any docs you create via scheduled job will be owned by the **Administrator** user unless specified otherwise.
> 
> 

<!-- page: framework/framework__user__en__api__chart.md -->
---
title: "Chart API\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/chart"
updated: "2026-02-17"
---


Frappe provides easy-to-use and fully configurable SVG charts. You can learn about them in the Frappe Chart's [documentation](https://frappe.io/charts).

## frappe.ui.RealtimeChart

`new frappe.ui.RealtimeChart(dom_element, event_name, max_label_count, data)`

Creates a new RealtimeChart instance that adds real-time data update functionality on top of the Frappe Chart API.

`dom_element`: HTML Element to be used to render the Chart.
`event_name`: Socket event which will provide the data stream.
`max_label_count`: Maximum number of labels allowed on the x-axis.
`data`: Data for the chart to be initialized with.

```js
// Empty data array
const data = {
 datasets: [
 {
 name: "Some Data",
 values: [],
 },
 ],
};

// Realtime Chart initialization
let chart = new frappe.ui.RealtimeChart("#chart", "test_event", 8, {
 title: "My Realtime Chart",
 data: data,
 type: "line",
 height: 250,
 colors: ["#7cd6fd", "#743ee2"]
});
```

Here is the sample client code to render a chart over the specified socket event.

The following python code can be executed as a cron job using [Hook](https://frappeframework.com/docs/v14/user/en/python-api/hooks) functionality.

```py
data = {
 'label': 1,
 'points': [10]
}
frappe.publish_realtime('test_event', data)
```

The `label` key specifies the label to be appended in the Chart. The `points` key specifies the array of points to be plotted. The number of values in the `points` array depends on the number of datasets.

This would produce a Chart like

![RealtimeChart](/files/realtime-chart.png)

### frappe.ui.RealtimeChart.start_updating

`frappe.ui.RealtimeChart.start_updating()`

Start listening to the specified socket event and update the RealtimeChart accordingly.

```js
frappe.ui.RealtimeChart.start_updating();
```

![RealtimeChart](/files/realtime-chart-demo.gif)
_frappe.ui.RealtimeChart.start_updating_

### frappe.ui.RealtimeChart.stop_updating

`frappe.ui.RealtimeChart.stop_updating()`

Stop listening to the socket event that RealtimeChart was initialized with.

```js
frappe.ui.RealtimeChart.stop_updating();
```

### frappe.ui.RealtimeChart.update_chart

`frappe.ui.update_chart(label, data)`

Manually updates RealtimeChart by appending the label and associated data to the end of the chart.

```js
frappe.ui.update_chart(2, [30]);
```

<!-- page: framework/framework__user__en__api__controls.md -->
---
title: "Controls\n"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/controls"
updated: "2026-02-17"
---


## frappe.ui.form.make_control
`frappe.ui.form.make_control({ parent, df })`

Makes a frappe control based on `df` properties and appends into `parent`
container.

```js
frappe.ui.form.make_control({
 parent: $wrapper.find('.my-control'),
 df: {
 label: 'Due Date',
 fieldname: 'due_date',
 fieldtype: 'Date'
 },
 render_input: true
})
```

Here are the `df` properties for most of frappe control types.

```js
// Attach
{
 label: 'Attachment',
 fieldname: 'attachment',
 fieldtype: 'Attach'
}

// Attach Image
{
 label: 'User Image',
 fieldname: 'user_image',
 fieldtype: 'Attach Image'
}

// Autocomplete
{
 label: 'Select User',
 label: 'user',
 fieldtype: 'Autocomplete',
 options: [
 'faris@erpnext.com',
 'suraj@erpnext.com'
 ]
}

// Barcode
{
 label: 'Item Barcode',
 fieldname: 'item_barcode',
 fieldtype: 'Barcode'
}

// Check
{
 label: 'Enable feature',
 fieldname: 'enable_feature',
 fieldtype: 'Check'
}

// Code
{
 label: 'JS Script',
 fieldname: 'script',
 fieldtype: 'Code',
 // for syntax highlighting
 options: 'Javascript' // JS, HTML, CSS, Markdown, SCSS, JSON,
 // wrap code
 wrap: true,
 // changing `max_lines` will set the max-height of the editor
 max_lines: 10,
 // changing `min_lines` will set the min-height of the editor
 min_lines: 5
}

// Color
{
 label: 'Your favorite color',
 fieldname: 'user_color',
 fieldtype: 'Color'
}

// Currency
{
 label: 'Amount',
 fieldname: 'amount',
 fieldtype: 'Currency',
 options: 'INR' // or name of field which holds currency
}

// Data
{
 label: 'First Name',
 fieldname: 'first_name',
 fieldtype: 'Data',
 options: 'Email' // 'Name', 'Phone', 'URL', 'Barcode'
}

// Date Range
{
 label: 'Select Date Range',
 fieldname: 'date_range',
 fieldtype: 'Date Range'
}

// Date
{
 label: 'Birth Date',
 fieldname: 'birth_date',
 fieldtype: 'Date'
}

// Datetime
{
 label: 'Submission Date and Time',
 fieldname: 'submission',
 fieldtype: 'Datetime'
}

// Dynamic Link
{
 label: 'Party',
 fieldname: 'party',
 fieldtype: 'Dynamic Link',
 options: 'party_type' // fieldname which holds the Link type
}

// Float
{
 label: 'Threshold',
 fieldname: 'threshold',
 fieldtype: 'Float'
}

// Geolocation
{
 label: 'Meeting Place',
 fieldname: 'meeting_place',
 fieldtype: 'Geolocation'
}

// HTML Editor
{
 label: 'Custom HTML',
 fieldname: 'custom_html',
 fieldtype: 'HTML Editor'
}

// Int
{
 label: 'No of days',
 fieldname: 'no_of_days',
 fieldtype: 'Int'
}

// Link
{
 label: 'Select User',
 fieldname: 'user',
 fieldtype: 'Link',
 options: 'User' // name of doctype
}

// Markdown Editor
{
 label: 'Blog Content',
 fieldname: 'content',
 fieldtype: 'Markdown Editor'
}

// MultiCheck
{
 label: 'Blog Content',
 fieldname: 'content',
 fieldtype: 'MultiCheck',
 options: [
 'Option 1',
 'Option 2',
 'Option 3',
 'Option 4',
 ],
 columns: 2 // break into 2 columns
}

// MultiSelect
{
 label: 'Select Users',
 fieldname: 'users',
 fieldtype: 'MultiSelect',
 options: [
 'faris@erpnext.com',
 'suraj@erpnext.com',
 'shivam@erpnext.com'
 ]
}

// Password
{
 label: 'New Password',
 fieldname: 'password',
 fieldtype: 'Password'
}

// Rating
{
 label: 'Rate your experience',
 fieldname: 'rating',
 fieldtype: 'Rating'
}

// Select
{
 label: 'Status',
 fieldname: 'status',
 fieldtype: 'Select',
 options: [
 'Open',
 'Closed',
 'Cancelled'
 ]
}

// Signature
{
 label: 'Status',
 fieldname: 'status',
 fieldtype: 'Signature'
}

// Text Editor
{
 label: 'Description',
 fieldname: 'description',
 fieldtype: 'Text Editor'
}

// Time
{
 label: 'In Time',
 fieldname: 'in_time',
 fieldtype: 'Time'
}

// Button
{
 label: 'Fetch',
 fieldname: 'fetch',
 fieldtype: 'Button',
 btn_size: 'xs' // xs, sm, lg
}

//Icon
{
 label: 'Page Icon',
 fieldname: 'page_icon',
 fieldtype: 'Icon'
}
```

## Adding Custom Formatters

You can add custom formatters for text type objects (Data, Select, Text etc) by adding them to the `docfield` object in `frappe.meta.docfield_map`

Example:

```
frappe.meta.docfield_map['DocField'].fieldtype.formatter = (value) => {
 if (value==='Section Break') return '🔵 Section Break';
 else return value;
}
```

<!-- page: framework/framework__user__en__api__database.md -->
---
title: "Database API"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/database"
updated: "2026-02-17"
---

*Version 16* onwards has some [breaking changes](https://github.com/frappe/frappe/wiki/query-builder-migration) in `get_list` and `get_all`

## frappe.db.get_list

`frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length, run)`

- Also aliased to `frappe.get_list`

Returns a list of records from a `doctype` table. ORM Wrapper for a `SELECT` query. Will also apply user permissions for the records for the session user. Only returns the document names if the `fields` keyword argument is not given. By default this method returns a list of `dict`s, but, you can pluck a particular field by giving the `pluck` keyword argument:

```
frappe.db.get_list('Employee')

# output
[{'name': 'HR-EMP-00008'},
 {'name': 'HR-EMP-00006'},
 {'name': 'HR-EMP-00010'},
 {'name': 'HR-EMP-00005'}
]

# with pluck
frappe.db.get_list('Employee', pluck='name')

# output
['HR-EMP-00008',
 'HR-EMP-00006',
 'HR-EMP-00010',
 'HR-EMP-00005'
]
  

```

Combining filters and other arguments:

```
frappe.db.get_list('Task',
    filters={
        'status': 'Open'
    },
    fields=['subject', 'date'],
    order_by='date desc',
    start=10,
    page_length=20,
    as_list=True
)

# output
(('Update Branding and Design', '2019-09-04'),
('Missing Documentation', '2019-09-02'),
('Fundraiser for Foundation', '2019-09-03'))

# Tasks with date after 2019-09-08
frappe.db.get_list('Task', filters={
    'date': ['>', '2019-09-08']
})

# Tasks with date between 2020-04-01 and 2021-03-31 (both inclusive)
frappe.db.get_list('Task', filters=[[
    'date', 'between', ['2020-04-01', '2021-03-31']
]])

# Tasks with subject that contains "test"
frappe.db.get_list('Task', filters={
    'subject': ['like', '%test%']
})

# Count number of tasks grouped by status
frappe.db.get_list('Task',
    fields=['count(name) as count', 'status'],
    group_by='status'
)

# For version 16 +
frappe.db.get_list('Task',
    fields=[{'COUNT': 'name', 'as': 'count'}, 'status'],
    group_by='status'
)

# output
[{'count': 1, 'status': 'Working'},
 {'count': 2, 'status': 'Overdue'},
 {'count': 2, 'status': 'Open'},
 {'count': 1, 'status': 'Filed'},
 {'count': 20, 'status': 'Completed'},
 {'count': 1, 'status': 'Cancelled'}]
  
```

Prior to version 16, setting `run=False` would return the SQL query instead of running it. From version 16 onwards, you'd get a query builder object instead. You can call `.get_sql()` to get the SQL query like earlier, otherwise you can mutate the query as desired before running it (`query.run()`)

## frappe.db.get_all

`frappe.db.get_all(doctype, filters, or_filters, fields, order_by, group_by, start, page_length, run)`

- Also aliased to `frappe.get_all`

Same as `frappe.db.get_list` but will fetch all records without applying permissions.

## frappe.db.get_value

`frappe.db.get_value(doctype, name, fieldname)` or `frappe.db.get_value(doctype, filters, fieldname)`

- Also aliased to `frappe.get_value` and `frappe.db.get_values`

Returns a document's field value or a list of values.

```
# single value
subject = frappe.db.get_value('Task', 'TASK00002', 'subject')

# multiple values
subject, description = frappe.db.get_value('Task', 'TASK00002', ['subject', 'description'])

# as dict
task_dict = frappe.db.get_value('Task', 'TASK00002', ['subject', 'description'], as_dict=1)
task_dict.subject
task_dict.description

# with filters, will return the first record that matches filters
subject, description = frappe.db.get_value('Task', {'status': 'Open'}, ['subject', 'description'])
  

```

## frappe.db.getsinglevalue

`frappe.db.get_single_value(doctype, fieldname)`

Returns a field value from a Single DocType.

```
timezone = frappe.db.get_single_value('System Settings', 'timezone')
  

```

## frappe.db.set_value

`frappe.db.set_value(doctype, name, fieldname, value)`

- Also aliased to `frappe.db.update`

Sets a field's value in the database, does not call the ORM triggers but updates the modified timestamp (unless specified not to).

```
# update a field value
frappe.db.set_value('Task', 'TASK00002', 'subject', 'New Subject')

# update multiple values
frappe.db.set_value('Task', 'TASK00002', {
    'subject': 'New Subject',
    'description': 'New Description'
})

# update without updating the `modified` timestamp
frappe.db.set_value('Task', 'TASK00002', 'subject', 'New Subject', update_modified=False)
  

```

> This method won't call ORM triggers like `validate` and `on_update`. Use this method to update hidden fields or if you know what you are doing.

## frappe.db.exists

`frappe.db.exists(doctype, name)`

Returns true if a document record exists.

Pass doctype and docname:

```
frappe.db.exists("User", "jane@example.org", cache=True)
  

```

Pass a dict of filters including the `"doctype"` key:

```
frappe.db.exists({"doctype": "User", "full_name": "Jane Doe"})
  

```

Pass the doctype and a dict of filters:

```
frappe.db.exists("User", {"full_name": "Jane Doe"})
  

```

## frappe.db.count

`frappe.db.count(doctype, filters)`

Returns number of records for a given `doctype` and `filters`.

```
# total number of Task records
frappe.db.count('Task')

# total number of Open tasks
frappe.db.count('Task', {'status': 'Open'})
  

```

## frappe.db.delete

`frappe.db.delete(doctype, filters)`

Delete `doctype` records that match `filters`. This runs a DML command, which means it can be rolled back. If no filters specified, all the records of the doctype are deleted.

```
frappe.db.delete("Route History", {
    "modified": ("<=", last_record_to_keep[0].modified),
    "user": user
})

frappe.db.delete("Error Log")
frappe.db.delete("__Test Table")
  

```

You may pass the doctype name or an internal table name. Conventionally, internal tables in Frappe are prefixed with `__`. The API follows this. The above commands run an unconditional `DELETE` query over tables **tabError Log** and **__Test Table**.

## frappe.db.truncate

`frappe.db.truncate(doctype)`

Truncate a table in the database. This runs a DDL command `TRUNCATE TABLE`, a commit is triggered before the statement is executed. This action cannot be rolled back. You may want to use this for clearing out log tables periodically.

```
frappe.db.truncate("Error Log")
frappe.db.truncate("__Test Table")
  

```

The above commands run a `TRUNCATE` query over tables **tabError Log** and **__Test Table**.

## frappe.db.commit

`frappe.db.commit()`

Commits current transaction. Calls SQL `COMMIT`.

> In most cases you don't need to commit manually. Refer Frappe's [Database transaction model](#database-transaction-model) below.

## frappe.db.savepoint

`frappe.db.savepoint(save_point)`

Create a named savepoint to which you can later roll back to.

## frappe.db.rollback

`frappe.db.rollback()`

Rollbacks current transaction. Calls SQL `ROLLBACK`.

> Frappe will automatically run `frappe.db.rollback()` if an exception is thrown during a Web Request of type `POST` or `PUT`. Use this if you have to rollback early in a transaction.

`frappe.db.rollback(save_point="save_point_name")`

Rollback to a specific savepoint instead rolling back full transactions. This rollback won't undo changes done to filesytem and any other rollback watchers.

## frappe.db.sql

`frappe.db.sql(query, values, as_dict)`

Execute an arbitrary SQL query. This may be useful for complex server side reports with join statements, adjusting the database to new features, etc.

Example:

```
values = {'company': 'Frappe Technologies Inc'}
data = frappe.db.sql("""
 SELECT
 acc.account_number
 gl.debit
 gl.credit
 FROM `tabGL Entry` gl
 LEFT JOIN `tabAccount` acc
 ON gl.account = acc.name
 WHERE gl.company = %(company)s
""", values=values, as_dict=0)

```

> Avoid using this method as it will bypass validations and integrity checks. It's always better to use [frappe.get_doc](https://frappeframework.com/docs/v14/user/en/api/document#frappeget_doc), [frappe.db.get_list](#frappedbget_list), etc., if possible.

## frappe.db.multisql

`frappe.db.multisql({'mariadb': mariadb_query, 'postgres': postgres_query})`

Execute the suitable SQL statement for any supported database engine.

## frappe.db.rename_table

`frappe.db.rename_table(old_name, new_name)`

Executes a query to change table name. Specify the DocType or internal table's name directly to rename the table.

Example:

```
frappe.db.rename_table("__internal_cache", "__temporary_cache")
frappe.db.rename_table("todo", "ToDo")
  

```

The second example should be used only if you understand the ramifications of it.

> Don't use this to rename DocType tables. Use `frappe.rename_doc` for that instead

## frappe.db.describe

`frappe.db.describe(doctype)`

Returns a tuple of the table description for given DocType.

## frappe.db.changecolumntype

`frappe.db.change_column_type(doctype, column, new_type)`

Changes the type of column for specified DocType.

## frappe.db.add_index

`frappe.db.add_index(doctype, fields, index_name)`

Creates indexes for doctypes for the specified fields.

> Note: if you want an index on a TEXT or a BLOB field, you must specify a fixed length to do that.

Example:

```
frappe.db.add_index("Notes", ["id(10)", "content(500)"], index_name)
```

## frappe.db.add_unique

`frappe.db.add_unique(doctype, fields, constraint_name=None)`

Creates unique constraint for doctypes for the specified fields.

Example:

```
frappe.db.add_unique("DoctypeName",["field1","field2"])
```

## frappe.db.bulk_update

`frappe.db.bulk_update(doctype, doc_updates, *, chunk_size=100, modified=None, modified_by=None, update_modified=True, debug=False)`

Bulk update multiple documents in batches using a single SQL UPDATE with CASE expressions.

Example:

```
frappe.db.bulk_update(
    "Task",
    {
        "TASK-0001": {"status": "Closed", "description": "Completed by QA"},
        "TASK-0002": {"status": "Open", "description": "Pending assignment"},
    },
    chunk_size=200,
    modified_by="admin@example.com",
    update_modified=True,
    debug=True,
)
```

doc_updates format:

```
{
    "DOC-0001": {"field1": "value1", "field2": "value2"},
    "DOC-0002": {"field1": "valueA", "field2": "valueB"},
}
```

**Notes:**

- Direct DB update; Document events/validations are not triggered.
- Unspecified fields remain unchanged.

## Database transaction hooks

> Note: This API is introduced in v15.

Frappe provides hooks for running callbacks before/after transaction commands like commit/rollback are issued. These hooks are useful for:

- Rolling back changes that are done outside of the database if the transaction is rolled back
- Flushing changes outside of the database only if the transaction is committed.

These hooks are :

- `frappe.db.before_commit.add(func: Callable)`
- `frappe.db.after_commit.add(func: Callable)`
- `frappe.db.before_rollback.add(func: Callable)`
- `frappe.db.after_rollback.add(func: Callable)`

Example usage:

```
def create_file(self):
    self.write_file()
    # This ensures rollback if DB transaction is rolledback
    frappe.db.after_rollback.add(self.rollback_file)

def rollback_file(self):
    self.delete_file()
```

## Database transaction model

Frappe's database abstractions implement a sane transaction model by default. So in most cases, you won't have to deal with SQL transactions manually. A broad description of this model is described below:

### Web requests

- While performing `POST` or `PUT`, if any writes were made to the database, they are committed at end of the successful request.
- AJAX calls made using `frappe.call` are `POST` by default unless changed.
- `GET` requests do not cause an implicit commit.
- Any **uncaught** exception during handling of request will rollback the transaction.

### Background/scheduled Jobs

- Calling a function as background or scheduled job will commit the transaction after successful completion.
- Any **uncaught** exception will cause rollback of the transaction.

### Patches

- Successful completion of the patch's `execute` function will commit the transaction automatically.
- Any **uncaught** exception will cause rollback of the transaction.

### Unit tests

- Transaction is committed after running one test module. Test module means any python test file like `test_core.py`.
- Transaction is also committed after finishing all tests.
- Any **uncaught** exception will exit the test runner, hence won't commit.

> Note: If you're catching exceptions anywhere, then database abstraction does not know that something has gone wrong hence you're responsible for the correct rollback of the transaction.

<!-- page: framework/framework__user__en__api__dialog.md -->
---
title: "Dialog API"
space: "Framework"
url: "https://docs.frappe.io/framework/user/en/api/dialog"
updated: "2026-02-17"
---

Frappe provides a group of standard, interactive and flexible dialogs that are easy to configure and use. There's also an API for [Python](/framework/v14/user/en/api/py-dialog).

### frappe.ui.Dialog

`new frappe.ui.Dialog({ title, fields, primary_action })`

Creates a new Dialog instance.

```
let d = new frappe.ui.Dialog({
    title: 'Enter details',
    fields: [
        {
            label: 'First Name',
            fieldname: 'first_name',
            fieldtype: 'Data'
        },
        {
            label: 'Last Name',
            fieldname: 'last_name',
            fieldtype: 'Data'
        },
        {
            label: 'Age',
            fieldname: 'age',
            fieldtype: 'Int'
        }
    ],
    size: 'small', // small, large, extra-large 
    primary_action_label: 'Submit',
    primary_action(values) {
        console.log(values);
        d.hide();
    }
});

d.show();
  

```

![Dialog](/files/dialog-api-custom-dialog.png)

 *frappe.ui.Dialog*

### frappe.msgprint

`frappe.msgprint(message)` or `frappe.msgprint({ title, message, indicator })`

Show `message` in a modal.

```
// only message
frappe.msgprint(__('Document updated successfully'));

// with options
frappe.msgprint({
    title: __('Notification'),
    indicator: 'green',
    message: __('Document updated successfully')
});
  

```

![Msgprint](/files/dialog-api-msgprint.png)

 *frappe.msgprint*

You can also bind a primary action to this dialog by passing `action`(as a method) within `primary_action`. Alternatively, `primary_action` can contain `server_action` **or** `client_action`.

The `server_action` and `client_action` are dotted paths to the respective methods which will execute on clicking the primary button.

```
// with primary action
 frappe.msgprint({
    title: __('Notification'),
    message: __('Are you sure you want to proceed?'),
    primary_action:{
        action(values) {
            console.log(values);
        }
    }
});

// with server and client action
frappe.msgprint({
    title: __('Notification'),
    message: __('Are you sure you want to proceed?'),
    primary_action: {
    'label': 'Proceed',
    // either one of the actions can be passed
    'server_action': 'dotted.path.to.method',
    'client_action': 'dotted_path.to_method',
    'args': args
    }
});
  

```

![Msgprint with Primary Action](/files/dialog-api-msgprint-with-primary-action.png)

 *frappe.msgprint with primary action bound*

### frappe.throw

`frappe.throw(error_message)`

Show `error_message` in a modal and `throw` exception.

```
frappe.throw(__('This is an Error Message'))
  

```

![Throw](/files/dialog-api-throw.png)

 *frappe.throw*

### frappe.prompt

`frappe.prompt(label)` or `frappe.prompt(df)` or `frappe.prompt(fields)`

Prompt user for a value or list of values.

```
// prompt for single value of type Data
frappe.prompt('First Name', ({ value }) => console.log(value))

// Set title and button label
frappe.prompt('First Name', console.log, 'Enter First Name', 'Submit');

// prompt for single value of any type
frappe.prompt({
    label: 'Birth Date',
    fieldname: 'date',
    fieldtype: 'Date'
}, (values) => {
    console.log(values.date);
})

// prompt for multiple values
frappe.prompt([
    {
        label: 'First Name',
        fieldname: 'first_name',
        fieldtype: 'Data'
    },
    {
        label: 'Last Name',
        fieldname: 'last_name',
        fieldtype: 'Data'
    },
], (values) => {
    console.log(values.first_name, values.last_name);
})
  

```

![Prompt](/files/dialog-api-prompt.png)

 *frappe.prompt*

### frappe.confirm

`frappe.confirm(message, if_yes, if_no)`

Show a confirmation modal, executes `if_yes` if confirmation is given else executes `if_no`.

```
frappe.confirm('Are you sure you want to proceed?',
    () => {
        // action to perform if Yes is selected
    }, () => {
        // action to perform if No is selected
    })
  

```

![Prompt](/files/dialog-api-confirm.png)

 *frappe.confirm*

### frappe.warn

`frappe.warn(title, message_html, proceed_action, primary_label, is_minimizable)`

Show a warning modal, executes `proceed_actiion` if confirmation is given. It can be set as `minimizable` which allows the dialog to be minimized.

```
frappe.warn('Are you sure you want to proceed?',
    'There are unsaved changes on this page',
    () => {
        // action to perform if Continue is selected
    },
    'Continue',
    true // Sets dialog as minimizable
)
  

```

![Prompt](/files/dialog-api-warn.png)

 *frappe.confirm*

### frappe.showalert

`frappe.show_alert(message, seconds)` or `frappe.show_alert({message, indicator}, seconds)`

Alert Dialog is used for showing non-obstructive messages.

Its parameters include `message`, which can contain the indicator color as well, and its display duration. The default is **7 seconds**.

```
frappe.show_alert('Hi, you have a new message', 5);

//show_alert with indicator
frappe.show_alert({
    message:__('Hi, you have a new message'),
    indicator:'green'
}, 5);
  

```

![Show Alert](/files/dialog-api-show-alert.png)

 *frappe.showalert*

### frappe.showprogress

`frappe.show_progress(title, count, total, description)`

Displays a progress bar with `count` (as current progress) and `total` (as maximum progress value).

```
frappe.show_progress('Loading..', 70, 100, 'Please wait');
  

```

![Show Progress](/files/dialog-api-progress.png)

 *frappe.showprogress*

### frappe.newdoc

`frappe.new_doc(doctype, route_options, init_callback)`

Opens a new form of the specified DocType that allows to edit and save it. If "Quick Entry" is enabled for the DocType (that allows to enter the most important fields) the "Quick Entry" pop-up window will be shown. Otherwise you will be redirected to the usual document entry form.

For example, let's create a new **Task**:

```
frappe.new_doc("Task");
  

```

Often when you are creating a new document in the user interface you want to initialize some of its fields based on the user interaction that triggered the creation. The other two arguments can be used for such initialization.

Specifically, the `route_options` argument is a quick and convenient way to set any field of type Link, Select, Data, or Dynamic Link in the new document. Its value should be an object whose keys are the desired field names and whose values are the initial values.

```
frappe.new_doc("Task", {subject: "New Task"});
  

```

If you need to do any other initialization of the new document that is not possible with `route_options`, `init_callback` gives you full control. It should be a function of one argument. If the doctype is initialized with a "Quick Entry" form, the callback is called with the "Quick Entry" dialog object just before control is released back to the user. Otherwise, the callback is called with the new document just before the user is allowed to edit it in the standard form.

```
frappe.new_doc("Task", {subject: "New Task"},
                doc => {doc.description = "Do what's necessary";});
  

```

Note that `subject` is a field of type "Data", so we are able to take advantage of the `route_options` argument to set it. `description` is a field of type "Text Editor", so if we want to initialize it, that must be done in the callback.

For a slightly more complex example, here's a call that creates a new **Journal Entry** of type "Bank Entry" and populates one side of the transaction:

```
frappe.new_doc("Journal Entry", {"voucher_type": "Bank Entry"}, doc => {
    doc.posting_date = frappe.datetime.get_today();
    let row = frappe.model.add_child(doc, "accounts");
    row.account = 'Bank - A';
    row.account_currency = 'USD';
    row.debit_in_account_currency = 100.0;
    row.credit_in_account_currency = 0.0;
});
  

```

### frappe.ui.form.MultiSelectDialog

`new frappe.ui.form.MultiSelectDialog({ doctype, target, setters, date_field, get_query, action })`

A MultiSelectDialog consists of filter fields followed by a multiple selection list. The primary button will perform the passed `action` on the selected options.

By default, the **Search Term** field and **Date Range** field will compose the filter fields.

The argument list includes:

- `doctype`: The source to fetch and display selection entries from.
- `target`: The target where the modal is to be displayed.
- `setters`: These will compose the filter fields and values to populate them with. These also translate to custom columns for the selection list.
- `read_only_setters`: If you want to make setters (filters) read only so that users can't change the value of the filters then add those fields in the "read_only_setters".
- `add_filters_group`: A boolean value to add/remove the filter group in the dialog below `setters`. The filter group is same as the list view filters.
- `date_field`: It is necessary to pass the `date_field` of the DocType in consideration.
- `get_query`: A function that returns `query` and `filters` to query the selection list. A custom server side method can be passed via `query`, and `filters` will be passed to that method.
- `action`: Contains the primary action to be performed on the selected options. It takes `selections` as a parameter, which comprises of the selected options.
- `columns`: An array of fields returned by custom query which will become columns in result datatable. Only works with the custom query (`get_query` argument returning a `query`).

Let us assume we want to fetch Material Requests into our dialog. We can then go on to invoke the MultiSelectDialog in the following manner:

```
new frappe.ui.form.MultiSelectDialog({
    doctype: "Material Request",
    target: this.cur_frm,
    setters: {
        schedule_date: null,
        status: 'Pending'
    },
    add_filters_group: 1,
    date_field: "transaction_date",
    get_query() {
        return {
            filters: { docstatus: ['!=', 2] }
        }
    },
    action(selections) {
        console.log(selections);
    }
});

// MultiSelectDialog with custom query method
let query_args = {
    query:"dotted.path.to.method",
    filters: { docstatus: ["!=", 2], supplier: "John Doe" }
}

new frappe.ui.form.MultiSelectDialog({
    doctype: "Material Request",
    target: this.cur_frm,
    setters: {
        schedule_date: null,
        status: 'Pending'
    },
    add_filters_group: 1,
    date_field: "transaction_date",
    columns: ["name", "transaction_date", "status"],
    get_query() {
        return query_args;
    },
    action(selections) {
        console.log(selections);
    }
});
  

```

![MultiSelectDialog](/files/dialog-api-multiselectdialog.png)

 *frappe.ui.form.MultiSelectDialog*

Here all the Material Requests that fulfill the filter criteria will be fetched into the selection area. The setter `company` is added to the filter fields along with its passed value. The `date_field` will be used to fetch and query dates from the DocType mentioned.

The **Make Material Request** (or `Make {DocType}`) secondary action button will redirect you to a new form in order to make a new entry into the DocType passed.

Now, if we want to only select particular item from a Material Request, then we can use optional `child_selection_mode` to enable child selection

```

// MultiSelectDialog for individual child selection
new frappe.ui.form.MultiSelectDialog({
    doctype: "Material Request",
    target: this.cur_frm,
    setters: {
        schedule_date: null,
        status: null
    },
    add_filters_group: 1,
    date_field: "transaction_date",
    allow_child_item_selection: 1,
    child_fieldname: "items", // child table fieldname, whose records will be shown &amp; can be filtered
    child_columns: ["item_code", "qty"], // child item columns to be displayed
    get_query() {
        return {
            filters: { docstatus: ['!=', 2] }
        }
    },
    action(selections, args) {
        console.log(args.filtered_children); // list of selected item names
    }
});
  

```

![MultiSelectDialog](/files/dialog-api-multiselectdialog-child-selection.png)

 *frappe.ui.form.MultiSelectDialog*

Here you will see a checkbox **Select Individual Items** to toggle between child item selection & parent selection. Once you toggle it, all the individual Material Requests Items are listed from the all the queried Material Request, you can now filter these items for selection.

To access the selected children, you can use `args.filtered_children` list which contains selected child item names.

### Table / Grid in a Dialog

A table can be added to a dialog, just like any other field as follows:

```
const dialog = new frappe.ui.Dialog({
  title: __("Create Logs"),
  fields: [
      {
          fieldname: "logs",
          fieldtype: "Table",
          label: __("Logs"),
          in_place_edit: true,
          reqd: 1,
          fields: [
              {
                  fieldname: "log_type",
                  label: __("Log Type"),
                  fieldtype: "Select",
                  options: "
IN
OUT",
                  in_list_view: 1,
                  reqd: 1,
              },
              {
                  fieldname: "time",
                  label: __("Time"),
                  fieldtype: "Time",
                  in_list_view: 1,
                  reqd: 1,
              }
          ],
          on_add_row: (idx) => {
            // idx = visible idx of the row starting from 1
            // eg. set `log_type` as alternating IN/OUT in the table on row addition
              let data_id = idx - 1;
              let logs = dialog.fields_dict.logs;
              let log_type = (data_id % 2) == 0 ? "IN" : "OUT";

              logs.df.data[data_id].log_type = log_type;
              logs.grid.refresh();
          },
      },
  ],
  primary_action: (values) => { ... },
  primary_action_label: __("Create"),
});
```

`on_add_row`: An event that gets triggered on adding a row to the table. You can perform an action like data manipulation or some other sort of calculation by adding your functionality to this event hook.
