# Automation Flows — "when this happens, do that", without code

## Contents

- what an Automation Flow is, and when to use something simpler
- before you build one: three questions to ask
- the safe order: build off, test-run, then turn on
- the calls, as tested
- triggers
- steps and the exact action names
- who the flow acts as
- reading the run history
- undoing a flow
- what goes wrong

An **Automation Flow** is a record that says: when something happens to this kind of record, do
these steps in order. It can wait, branch, reach linked records, send email and call other systems.
It arrived in Frappe **v16.36**. A site older than that has no `Automation Flow` DocType; say so and
offer a Notification, a Webhook or an Assignment Rule instead.

This file was checked against a live Frappe **16.56** site on 2026-11-14: every call below was run
and behaved as written. The official pages are bundled:

- `docs/framework/framework__automations.md` — overview, run history, settings
- `docs/framework/framework__automations__triggers-and-conditions.md`
- `docs/framework/framework__automations__steps-and-actions.md`
- `docs/framework/framework__automations__extending-automations.md` — for app developers

## Use the simplest tool that does the job

| The user wants… | Use |
|---|---|
| one email or alert when something happens | a Notification |
| to post a record to another system when something happens | a Webhook (this skill) |
| to share new records out across a team | an Assignment Rule |
| several steps in order, a wait, a branch, or to change a linked record | **an Automation Flow** |

## Before you build one: three questions

Ask these in plain words and wait for the answers. Do not guess them.

1. **What starts it?** A new record, a change to one field, a date coming up, a schedule.
2. **Which records count?** All of them, or only some (for example "only invoices over 10,000").
3. **What should happen, in order?** One line per step.

Then say back, in one sentence, what the flow will do and **what it will do on its own once it is
on** (send email to real people, change records, call another system). That sentence is the thing
the user approves.

## The safe order

1. **Create it switched off.** A new flow is off unless `enabled` is set. Creating one changes
   nothing on the site. Reversibility: safe.
2. **Test-run it** against one real record. The site runs every step and then rolls everything
   back; a webhook is shown, not sent. Show the user each step's result. Reversibility: safe.
3. **Turn it on** only after a clear yes. Switching it on changes an existing record: save a snapshot of
   the flow first, ask, end your turn, and switch it on only after the user's reply. From this moment it
   acts without anyone watching.
   Reversibility: **irreversible** — an email it sends or a webhook it calls cannot be recalled,
   even though the flow itself can be switched off again in a second.
4. **Check the first real run** in the run history and report it.

Never turn a flow on in the same breath as creating it. Never build a flow that deletes records,
and never use **Run Script** unless the user asked for a script by name and is a System Manager.

## The calls, as tested

The paths are the ordinary document calls from `adapters/api.md`, plus three methods.

| Step | Call |
|---|---|
| What can a flow on this DocType use? | `GET /api/v2/method/frappe.automation_engine.api.get_automation_capabilities?doctype=<DocType>` — returns the trigger types, the DocType's fields, its linked records and the action list with each action's parameters |
| Create (off) | `POST /api/v2/document/Automation%20Flow` |
| Test-run | `POST /api/v2/method/frappe.automation_engine.api.trial_run` with `{"automation": "<flow name>", "docname": "<a real record>"}` |
| Turn on / off | `PUT /api/v2/document/Automation%20Flow/<flow name>` with `{"enabled": 1}` or `{"enabled": 0}` |
| Runs for one record | `GET /api/v2/method/frappe.automation_engine.api.get_runs?reference_doctype=<DocType>&reference_name=<name>` |
| All runs | `GET /api/v2/document/Automation%20Run` |

Through Frappe's MCP server the same things are `call_method` (for the three methods) and
`create_document` / `update_document` on `Automation Flow`. In the Desk, type **Automation Flow**
in the search bar; the form has a **Test Run** button.

A flow that works, exactly as it was sent:

```json
{
  "title": "Urgent to-dos get high priority",
  "document_type": "ToDo",
  "trigger_type": "Doc Created",
  "filters": "[[\"ToDo\", \"description\", \"like\", \"%urgent%\"]]",
  "actions": [
    {"step_type": "Action", "action_type": "SetFieldValue",
     "params": "{\"field\": \"priority\", \"value\": \"High\"}"}
  ]
}
```

- `filters` and `params` are JSON **text**, not nested objects.
- The site names the flow itself (`AUTO-00001`). Use that name in the later calls.
- The answer to the test run lists every step with `status`, `detail`, and, for a skipped step,
  the condition and the values it read. Read it to the user in plain words.

## Triggers

`trigger_type` is one of: `Doc Created`, `Doc Updated`, `Field Value Changed` (needs
`trigger_field`; optional `from_value`, `to_value`), `Doc Deleted`, `Doc Submitted`,
`Doc Cancelled`, `Date Based` (needs `date_field`, `date_offset`, `date_direction` Before or
After; checked hourly, each record fires at most once a day), `Scheduled` (needs
`cron_expression`), `Custom Event` (needs `custom_event`) and `Manual`.

Narrow it with `filters` (the same filters as a list view; every rule must hold) and, when filters
cannot say it, `condition` — one Python expression over `doc`. Set `revalidate_on_run` when the
record may change again right after the save that triggered the flow.

## Steps and the exact action names

Each row of `actions` has a `step_type`: `Action`, `Wait`, `WaitForEvent` or `If`.

For an `Action`, `action_type` must be the **stored name**, written without spaces. The label the
Desk shows ("Set Field Value") is refused with *Unknown automation action*.

| Label in the Desk | `action_type` | `params` |
|---|---|---|
| Set Field Value | `SetFieldValue` | `field` and `value`, or `values` (a map of several) |
| Increment Field Value | `IncrementFieldValue` | `field`, `amount` |
| Create Document | `CreateDocument` | `doctype`, `values` |
| Send Notification | `SendNotification` | `channel` (`Email` or `System`), `recipients`, then `subject` and `message`, or `email_template` |
| Assign to User | `AssignToUser` | `assign_to`, `description` |
| Call Webhook | `CallWebhook` | `url`, `method`, `headers`, `payload`, `timeout` |
| Run Script | `RunScript` | `server_script` or inline `script` |

An app can add its own actions, so read the list from `get_automation_capabilities` on the user's
site rather than trusting this table alone.

- `Wait`: `params` is `{"value": 2, "unit": "Days"}`; the unit is Seconds, Minutes, Hours or Days.
- `If`: give it a `step_condition`; the steps that belong to it carry `parent_step` (the If row's
  number) and `branch` (`If` or `Else`).
- Text parameters accept `{{ doc.fieldname }}`. Recipients accept `@owner` and `@assignees`.
- To act on a linked record instead of the one that triggered the flow, declare it under
  `relationships` and set the step's `target`. The bundled *Steps and Actions* page shows how.

## Who the flow acts as

`run_as` defaults to **Automation User**, and that user defaults to **Administrator**. So a new
flow acts with full rights unless told otherwise. Say this to the user before turning a flow on,
and offer `Triggering User` or `Document Owner`, or a named user with only the roles the steps
need. Each step still passes the ordinary permission checks as that user.

## Reading the run history

Every run is an **Automation Run** with a status: `Success`, `Partially Failed`, `Failed`,
`Waiting` or `Skipped`. `get_runs` gives the runs for one record. On the test site a matching
record's run finished about three seconds after the save; a record that did not match the filter
was left alone. Run logs are cleared after 30 days.

Runs happen in a background worker. **If the scheduler or the workers are stopped, no flow fires**
— check with "Diagnose the scheduler" in this skill before blaming the flow.

After **Failure Threshold** failed runs in a row (10 unless changed in Automation Settings) the
site switches the flow off by itself and writes why in `disabled_reason`.

## Undoing a flow

- **Switch it off**: `{"enabled": 0}`. Nothing new fires. This is the undo.
- **Deleting** a flow that has already run is refused (*Cannot delete … linked with Automation
  Run*). Leave it switched off. Do not delete its run history to force the deletion.
- What a flow already did stays done. Records it changed need restoring from their own snapshots;
  email it sent cannot be unsent. Say this before turning a flow on, not after.
- To stop **every** flow on the site at once, a System Manager ticks **Disable Automations** in
  Automation Settings.

## What goes wrong

| What you see | Why | Do this |
|---|---|---|
| *Unknown automation action: Set Field Value* | the label was sent, not the stored name | use the name from the table above |
| the flow cannot be switched on | it has no actions yet | add at least one step |
| it is on but nothing happens | scheduler or workers stopped, **Disable Automations** ticked, or the record does not match | check the scheduler, then test-run against that record and read the condition values |
| a step fails with a permission error | the `run_as` user may not read the record or write the target | name the user and the missing permission |
| 404 on `Automation Flow` | the site is older than v16.36 | offer a Notification, Webhook or Assignment Rule |
| a webhook step fails at once | it refuses private and internal addresses; a reply of 400 or above fails the step | use a public https address and check the receiving side |
| flows do not fire during an import | they are skipped during installs, migrations and patches by design | nothing to fix |
