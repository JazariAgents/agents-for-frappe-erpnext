<!-- Frappe documentation: crm, part 1 of 1. Index: docs/INDEX.md -->

<!-- page: crm/crm__assignment-rule.md -->
---
title: "Assignment Rule"
space: "CRM"
url: "https://docs.frappe.io/crm/assignment-rule"
updated: "2026-05-26"
---

Assignment Rules automate the process of assigning leads and deals to specific agents based on predefined conditions. This streamlines your workflow and ensures leads and deals are directed to the most qualified agents for faster resolution and improved customer experience.

## **Creating an Assignment Rule**

1. Go to **Settings > Assignment Rules** and click on **+New**.
  ![](/files/image253100.png)
2. **Define the Rule:** Fill in the following mandatory fields:
  - **Name:** A label to identify the rule
  - **Description:** Describe in short what the rule does
  - **Apply for:** Select for which doctype(Lead or Deal) the rule will apply
  - **Assignment condition:** Define the condition using the conditions builder for the assignment rule
    ![](/files/image7712f7.png)
  - **Users:** Choose the user(s) to whom Lead or Deal meeting the condition will be assigned.

## **Lead or Deal Routing**

Assignment Rules offer two rules for assigning Lead or Deal:

1. **Auto-rotate:** This method distributes Lead or Deal evenly among the selected users. Each user receives one assignment at a time, and the cycle repeats once all users have been assigned.
2. **Assign by workload:** This method assigns Lead or Deal to the user with the least workload, ensuring a fair distribution and preventing any single user from being overloaded.

## **Additional Fields**

**Unassignment condition:** Define a condition using the conditions builder for the unassignment rule, complex nested conditions are also supported. This will be used to unassign a Lead or Deal based on the condition specified

**Assignment Schedule:** Select the days you want the assignment rule to be active

---

By effectively utilizing Assignment Rules, you can significantly improve the efficiency and organization of your lead and deal management process.

<!-- page: crm/crm__call-log.md -->
---
title: "Call Log"
space: "CRM"
url: "https://docs.frappe.io/crm/call-log"
updated: "2026-02-05"
---

The call log page in Frappe CRM is for recording, tracking, and managing all your customer calls. It helps you to maintain a clear history of interactions, improve communication effectiveness, and gain valuable insights for better customer relationships.

Make a call
-----------

* You need to go to a Deal/Lead page
* You can make a call by clicking on the call icon in the lead details section or the activity tab by clicking on new and then making a call.


> Refer to this [page](https://docs.frappe.io/crm/twilio#make-a-call) to understand where and how to make calls in the CRM System in detail.
> 
> 

![CALL](/files/CALL.gif)  


Once your call is done you can check in the Calls tab to track all the call activity made to a Lead/Deal. Also, you can easily refer to the call recording.

![call activity](/files/call activity.gif)  


**Call Logs**
-------------

Call log view is a valuable tool for any business that relies on effective customer communication. By leveraging these reports, you can transform your call data into actionable insights, driving improved performance, customer satisfaction, and overall business success.

![Screen Recording 2024-03-31 at 2.33.58 PM (1)](/files/Screen Recording 2024-03-31 at 2.33.58 PM (1).gif)  


Frappe CRM's call log reports offer various filters and options to customize your analysis. Here are some common reporting aspects:

* **Call Details:** Filter calls by date range, time, type (inbound/outbound), duration, agent and customer, and more.
* **Agent Performance:** Analyze individual agent call volume, success rates (e.g., call-to-answer conversion), and average call duration to measure performance.
* **Customer Analysis:** Report on call volume, call topics, and customer demographics to understand customer behavior and identify trends.
* **Outcome Analysis:** Track the outcome of each call (e.g., successful sale, follow-up required) to measure conversion rates and identify areas for improvement.
* **Call Recording Analysis:** Analyze recordings to identify areas where communication can be improved or gather specific customer feedback. Analyzing call logs can help identify areas where training or coaching can be provided to enhance team communication skills and effectiveness.

  


  

<!-- page: crm/crm__capturing-leads__web-form.md -->
---
title: "Forms"
space: "CRM"
url: "https://docs.frappe.io/crm/capturing-leads/web-form"
updated: "2026-07-17"
---

Forms in Frappe CRM let you collect Leads or Deals directly from your website or by circulating web forms without writing a single line of code. 

![](/files/image99a4f3.webp)
*A sample form*

## Creating a form

Follow these simple steps to create one:

1. Open **Settings → Forms**. (You'll need the Sales Manager or System Manager role to see this.)
2. Click **New**.
3. Give it a title, choose whether submissions become a **Lead** or a **Deal**, and set the route. This becomes the last part of the form's public URL (`/crm-form/your-route`). The route fills itself in from the title until you edit it directly.
4. Click **Create form**.

![](/files/Screen Recording 2026-07-17 at 3.29.49 PM.mov)

It opens straight into the builder with a starting layout already in place – name, email, and phone for Leads, plus organization name for Deals, so there's something to look at and publish right away.

## Building the layout

The editor is a canvas of sections and columns, all drag-and-drop:

- **Add Section** starts a new labelled group. Click on the title to name it.
- Inside a section, **Add Field** searches every field on the Lead or Deal; you can select and add which you want to show on your form.
- Click a field to expand it and set:
  - **Required** - visitors can't submit without filling it in.
  - **Placeholder** - example text shown inside the empty field.
  - **Description** - helper text under the field.
- Drag the grip on the left of a section or field to reorder it.
- Remove a field with the **×**. Fields the record (Lead or Deal) itself requires (like Status) can't be removed outright — they move to a **Hidden required fields** panel instead, where you set the default value that gets applied automatically on submission. If fields are added to the hidden section, they aren't visible to the audience on the public form.

![](/files/Screen Recording 2026-07-17 at 3.38.06 PM.mov)

## Previewing

Click **Preview** to see the form as a visitor would, fill it out, and check that the success screen shows what you'd expect. Nothing here is actually saved. **Discard** or **Preview again** resets it, and **Edit** takes you back to the canvas.

![](/files/Screen Recording 2026-07-17 at 3.41.11 PM.mov)

## Settings

The Settings tab holds:

- **Route** - the public URL slug.
- **Maps to** - Lead or Deal.
- **Submit button label** -  you can edit this label as per your preference.
- **Success message** - shown after submission if there's no redirect.
- **Redirect URL** - send visitors somewhere else (a thank-you page, say) instead of showing the success message.

![](/files/image8e50bc.webp)
*Settings page in Forms*

## Publishing

Flip **Publish** on in the header to make the form live. It won't publish until every hidden required field has a default set.

Unpublishing doesn't delete anything. It just takes the public page down. As a manager, you can still open the link yourself to preview a draft; everyone else gets a 404 until it's published.

![](/files/Screenshot 2026-07-17 at 3.46.12 PM.webp)
*Enable "Publish" to make your form public*

## Sharing and embedding

Once published, the **Share** tab gives you:

- **Link** - the hosted form's own page, ready to send directly.
- **Embed** - an iframe snippet for dropping into your own site.
- **Allowed domains** - list the sites (one per line) allowed to embed the iframe. Leave it empty, and the embed only works on your CRM's own domain.

![](/files/Screenshot 2026-07-17 at 3.49.53 PM.webp)
*Share tab in Forms*

That's it. Once you have embedded the form in your website, your site visitors can fill it up and a Lead / Deal as configured will get created in your CRM with source = Web Form.

![](/files/Screen Recording 2026-07-17 at 4.15.11 PM.mov)

P.S. In case you want to add more automations and colour to your form like custom CSS, banner images, etc. you can check your form in the desk view by going to Desk -> Web form. Refer to [this link](https://docs.frappe.io/framework/user/en/web-form/customization) for more details.

<!-- page: crm/crm__comment.md -->
---
title: "Comment"
space: "CRM"
url: "https://docs.frappe.io/crm/comment"
updated: "2026-02-05"
---

The comment feature allows internal communication and information sharing related to leads and deals. It facilitates collaboration among agents by providing a dedicated space to discuss, track progress, and share details.

![](/files/e3s52jJ.png)  


### **Key Features**

* **Internal Communication:** Engage in discussions with other agents regarding leads and deals.
* **Mentions:** Use the "@" symbol followed by a username to notify specific agents about important updates or require their input within a comment.
* **Information Storage:** Store relevant details about the lead or deal within the comments section for easy reference. This can include notes from conversations, action items, or crucial milestones.

### **Add a Comment**

1. Locate the "Comment" button at the bottom on the Lead or Deal page.
2. Enter your comment in the designated text box.
3. To mention a user, type "@" followed by their username. A dropdown menu will appear with matching usernames for ease of selection.
4. Once you've crafted your comment and included any necessary mentions, click "Submit".

<!-- page: crm/crm__custom-actions.md -->
---
title: "Custom Actions"
space: "CRM"
url: "https://docs.frappe.io/crm/custom-actions"
updated: "2026-05-26"
---

# Custom Actions

Custom actions let you add buttons to the Lead or Deal page header.  You can add single buttons, group them under a dropdown, or create  labeled dropdown menus — each running your own logic when clicked.

## Creating Custom Actions

Custom actions live inside a CRM Form Script. Open **CRM Form Script** in Desk, pick your DocType (Lead or Deal), and write a class. Set `this.actions` inside `onLoad()`:

```js
class CRMDeal {
    onLoad() {
        this.actions = [
            {
                label: "Open in Desk",
                onClick: (close) => {
                    let URL = `https://frappecrm.frappe.cloud/app/crm-deal/${this.doc.name}`
                    window.open(URL, '_blank')
                }
            }
        ]
    }
}

```

This adds a button labelled "Open in Desk" that opens the current deal in a new tab.  


![](/files/Screenshot 2026-05-26 at 5.51.52 PM.png)
*"Open In Desk" Button in Top Right of the header *

### Grouped Actions (three-dot menu)

Use `group` to nest items under a single `more-horizontal` icon dropdown. Set `hideLabel: true` to hide the group heading from the dropdown menu.



```js
class CRMDeal {
    onLoad() {
        this.actions = [
            {
                group: "Add",
                hideLabel: true,
                items: [
                    { label: "Create Quotation", onClick: (close) => {} },
                    { label: "Create Sales Order", onClick: (close) => {} },
                ]
            },
            {
                group: "Delete",
                items: [
                    { label: "Delete Quotation", onClick: (close) => {} },
                    { label: "Delete Sales Order", onClick: (close) => {} },
                ]
            }
        ]
    }
}

```

![](/files/Screenshot 2026-05-26 at 5.50.39 PM.png)

### Grouped Actions with Label (dropdown button)

Add `buttonLabel` to turn the three-dot icon into a labelled dropdown button.



```js
class CRMDeal {
    onLoad() {
        this.actions = [
            {
                buttonLabel: "Create",
                group: "Add",
                hideLabel: true,
                items: [
                    { label: "Create Quotation", onClick: (close) => {} },
                    { label: "Create Sales Order", onClick: (close) => {} },
                ]
            }
        ]
    }
}

```

![](/files/Screenshot 2026-05-26 at 5.53.36 PM.png)

### Mixing Single Buttons and Groups

You can combine both styles in one array:

```js
class CRMDeal {
    onLoad() {
        this.actions = [
            {
                label: "Refresh Score",
                icon: "refresh-cw",
                onClick: (close) => { /* ... */ }
            },
            {
                group: "More",
                hideLabel: true,
                items: [
                    { label: "Export PDF", onClick: (close) => {} },
                    { label: "Duplicate", onClick: (close) => {} },
                ]
            }
        ]
    }
}
```

![](/files/Screenshot 2026-05-26 at 5.54.11 PM.png)

## What You Have Access To

Inside your script, these helpers are available without any imports:

- `this.doc` — the current document. Read and write fields directly: `this.doc.status = "Lost"`, `this.doc.deal_name`.
- `call(method, params)` — call any server-side Python method. Returns a Promise.
- `createDialog(options)` — show a confirmation dialog. Provide `title`, `message`, and `actions`.
- `formDialog(options)` — show a dialog with form fields to collect input from the user.
- `toast.success(msg)`, `toast.error(msg)`, `toast.info(msg)` — show notifications.
- `router.push(location)`, `router.replace(location)` — navigate to a different page.
- `throwError(msg)` — show a red toast and stop execution immediately.

## Examples

### Create Quotation (only for Won Deals)

This action checks if the deal is Won, then calls the server to  create a quotation. If successful, it navigates to the new quotation  page.

```js
class CRMDeal {
  onLoad() {
    this.actions = [
      {
        label: "Create Quotation",
        icon: "file-text",
        onClick: (close) => {
          if (this.doc.status !== "Won") {
            toast.info("This action is only available for Won deals");
            return;
          }

          call("crm.api.quotation.create_from_deal", {
            deal: this.doc.name,
            customer: this.doc.organization,
          }).then((data) => {
            if (data?.name) {
              router.push({ name: "Quotation", params: { name: data.name } });
              toast.success("Quotation created successfully");
            } else {
              toast.error("Could not create quotation");
            }
          });
        },
      },
    ];
  }
}

```

### Mark as Lost (with confirmation)

Asks the user to confirm, then updates the deal status directly.

```js
class CRMDeal {
  onLoad() {
    this.actions = [
      {
        label: "Mark as Lost",
        icon: "x-circle",
        onClick: (close) => {
          createDialog({
            title: "Mark Deal Lost",
            message: "Are you sure you want to mark this deal as Lost?",
            actions: [
              {
                label: "Mark Lost",
                theme: "red",
                variant: "solid",
                onClick: async ({ close: dialogClose }) => {
                  this.doc.status = "Lost";
                  toast.success("Deal marked as Lost");
                  dialogClose();
                },
              },
              {
                label: "Cancel",
                variant: "outline",
                onClick: ({ close: dialogClose }) => dialogClose(),
              },
            ],
          });
        },
      },
    ];
  }
}

```

### Schedule a Follow-up (with form dialog)

Opens a dialog with date and notes fields. When submitted, calls the server to save the follow-up.

```js
class CRMDeal {
  onLoad() {
    this.actions = [
      {
        label: "Schedule Follow-up",
        icon: "calendar",
        onClick: (close) => {
          formDialog({
            title: "Schedule Follow-up",
            fields: [
              {
                fieldname: "date",
                fieldtype: "Date",
                label: "Follow-up Date",
                reqd: 1,
              },
              { fieldname: "notes", fieldtype: "Small Text", label: "Notes" },
            ],
            submitLabel: "Schedule",
            cancelLabel: "Cancel",
            onSubmit: async (data) => {
              await call("crm.api.deal.schedule_followup", {
                deal: this.doc.name,
                date: data.date,
                notes: data.notes,
              });
              toast.success("Follow-up scheduled for " + data.date);
            },
          });
        },
      },
    ];
  }
}

```

### Delete Deal (with confirmation and redirect)

Confirms before deleting, then redirects back to the deals list.

```js
class CRMDeal {
  onLoad() {
    this.actions = [
      {
        label: "Delete Deal",
        icon: "trash-2",
        onClick: (close) => {
          createDialog({
            title: "Delete Deal",
            message: `Are you sure you want to delete "${this.doc.deal_name}"? This cannot be undone.`,
            actions: [
              {
                label: "Delete",
                theme: "red",
                variant: "solid",
                onClick: async ({ close: dialogClose }) => {
                  await call("frappe.client.delete", {
                    doctype: "CRM Deal",
                    name: this.doc.name,
                  });
                  dialogClose();
                  router.push("/deals");
                  toast.success("Deal deleted");
                },
              },
              {
                label: "Cancel",
                variant: "outline",
                onClick: ({ close: dialogClose }) => dialogClose(),
              },
            ],
          });
        },
      },
    ];
  }
}

```



## Showing and Hiding Actions Based on Field Values

Sometimes you only want certain actions to appear in certain situations. Re-set `this.actions` whenever the relevant field changes:

```js
class CRMDeal {
  onLoad() {
    this._updateActions();
  }

  // Re-run whenever status changes
  status() {
    this._updateActions();
  }

  _updateActions() {
    const isLost = this.doc.status === "Lost";

    this.actions = [
      {
        label: "Create Quotation",
        onClick: (close) => {
          /* ... */
        },
      },
      // Only show "Mark as Lost" if the deal isn't already lost
      ...(!isLost
        ? [
            {
              label: "Mark as Lost",
              icon: "x-circle",
              onClick: (close) => {
                /* ... */
              },
            },
          ]
        : []),
    ];
  }
}

```

<!-- page: crm/crm__custom-branding.md -->
---
title: "Custom Branding\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "CRM"
url: "https://docs.frappe.io/crm/custom-branding"
updated: "2026-04-20"
---

If you're setting up Frappe CRM for your company or a client, you can replace the default Frappe branding with your own. Change the name, logo, and favicon and it'll feel like your own CRM.

To get here, go to **Settings > Brand**.

![](/files/Screenshot 2026-04-20 at 5.22.26 PM.png)

Here's what you can configure:

- **Brand Name** – Shows up in the top left of the sidebar. Set it to your company name
- **Brand Logo** – Your company logo, also shown in the sidebar. Recommended size is 32x32px in PNG or SVG
- **Favicon** – The small icon that appears on your browser tab. Recommended size is 32x32px in PNG or ICO

Hit **Update** when you're done, and the changes will reflect immediately across the CRM.

<!-- page: crm/crm__custom-fields.md -->
---
title: "Custom Fields\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "CRM"
url: "https://docs.frappe.io/crm/custom-fields"
updated: "2026-02-05"
---

Frappe CRM understands that every business has unique needs. That's why it offers customization options to tailor the system to your specific workflows. This guide focuses on adding Custom Fields, a powerful tool for capturing additional data relevant to your business.

What are Custom Fields?
-----------------------

The default Lead/Deal pages in Frappe CRM come with essential fields like contact details, organization, owner etc. However, you might need to capture more information specific to your sales process. Custom Fields allow you to do just that.

![](/files/yYUeLjQ.png)  
  


Adding Custom Fields
--------------------

Here's how to add Custom Fields to Lead or Deal documents using the side panel layout builder:
![](/files/Screenshot%202024-09-28%20at%202.35.54%E2%80%AFPM.png)
  


1. **Navigate to Lead/Deal Page:** Go to Lead/Deal Page and click on the edit icon shown on the first section header in the side panel.
    ![](/files/aQCtN5Z.png)
2. **Use the Fields Layout Builder:** A modal will open where doctype will be selected automatically. The right side displays a layout builder. Drag and drop existing fields or sections to rearrange them. Use the buttons provided to add new fields or sections.
3. **Preview Your Work (Optional):** The Sidebar Fields Layout Builder offers a **Show Preview** button. Clicking this button will display a preview of how the customized sidebar panel will look for the chosen doctype. This allows you to visualize your layout changes before saving them.
    ![](/files/Screenshot%202024-09-28%20at%203.11.14%E2%80%AFPM.png)

**Important Notes:**
--------------------

* You can only edit section labels, not field labels. To edit field properties, use the framework's "Customize Form" feature.
* The "Contacts" section for CRM Deals is non-editable. You can rearrange or rename the section but cannot remove it.
* Currently, not all field types are supported in the new UI. Fields like Rating, Geolocation, and Duration will appear as data fields on the Lead/Deal page.

By effectively utilizing Custom Fields, you can personalize your Frappe CRM experience and capture the data crucial to your sales success.

<!-- page: crm/crm__custom-list-actions.md -->
---
title: "Custom List Actions"
space: "CRM"
url: "https://docs.frappe.io/crm/custom-list-actions"
updated: "2026-02-05"
---

Similar to Custom Actions, Custom List Actions allows you to add custom actions that you can perform directly from the list view of various Frappe CRM masters (e.g., Leads, Deals, Organizations). These actions enhance your workflow by allowing quick execution of specific tasks without needing to open individual records.

## Types of List Actions

There are two main categories of custom list actions:

1. **Actions:** These resemble the custom actions you find on individual lead/deal pages. They appear as buttons in the list view header beside the create button.
  Example:
    
  ![](/files/uYxvLR7.png)
    
  ![](/files/i75wZ8b.png)
    In this example, the "Delete junk deals" button was added on listview which will automatically delete all the junk deals.

You can create all types of actions (Normal Button, Grouped Actions, Grouped Actions with label and combination of all).
2. **Bulk Actions:** These are designed for performing specific tasks on multiple selected rows in the list view. This caters to situations where you need to apply the same action to a group of records simultaneously.

```
Example:

![](/files/95SvEcH.png)
![](/files/TgJvk5C.png)  


```
{
  "label": "Mark Won",
  "onClick": async ({ list, selections, unselectAll, call }) => {
    let docs = Array.from(selections)
    for (const doc of docs) {
        // Update the status of each selected Lead/Deal to "Won"
        let updated = await call('frappe.client.set_value', {
            doctype: 'CRM Deal',
            name: doc,
            fieldname: 'status',
            value: 'Won',
        })
    }
    unselectAll()
    list.reload()
  }
}
```

In this example, the "Mark Won" button iterates through each selected Lead/Deal name (`selections`) and updates its status to "Won" using the `call` method. Finally, it unselects all rows using `unselectAll` method and reloads the list view using `list.reload()`.
```

## Adding Custom List Actions

You can define custom list actions using Frappe CRM's Form Script functionality. Here's a step-by-step guide:

1. **Navigate to Desk:** Switch to Desk and navigate to CRM Form Script.
2. **Select Doctype and Apply To:** Choose the Doctype (e.g., Customer) for which you want to create the list actions. In the "Apply To" field, select "List" and save the configuration. This will generate a boilerplate code snippet.
3. **Define Actions:** The boilerplate code provides two options:
  **actions:** Here, you can specify a list of action buttons similar to custom actions on individual record pages (refer to the documentation for custom actions for detailed guidance on defining button functionality [link](https://docs.frappe.io/crm/custom-actions)). These buttons will be visible in the list view header.
   **bulk_actions:** This section allows you to define action buttons specifically designed for bulk operations on selected rows.
4. **List Context:** Both action types utilize JavaScript code to perform the desired functionalities. You'll have access to a `list` object as a parameter on `setupList` and also on `onClick` event, which provides valuable context about the list view. This object offers functionalities like reloading the list (`list.reload()`) and accessing additional information.
  Other than `list` other contexts are also passed like `$dialog`, `router`, `createToast`, and `call`. (for more details check                 [here](https://docs.frappe.io/crm/custom-actions#using-context-and-actions))
5. **Bulk Action Context:** When defining bulk actions, the `onClick` event receives additional context besides the standard parameters. This context includes:
  **selections:** This is a Set object containing the names of all currently selected rows in the list view.
   **unselectAll:** This is a function that allows you to deselect all currently chosen rows.

By effectively utilizing these custom list actions, you can streamline your workflow and enhance your data management experience within Frappe CRM.

## Leveraging Custom List Actions

Custom List Actions offer a powerful way to automate repetitive tasks on multiple Leads or Deals. You can leverage them for various purposes, such as:

- Updating statuses for a group of Leads/Deals
- Sending mass emails or notifications
- Exporting selected data for further analysis
- Triggering custom workflows based on bulk actions

<!-- page: crm/crm__custom-script.md -->
---
title: "Custom Script"
space: "CRM"
url: "https://docs.frappe.io/crm/custom-script"
updated: "2026-05-08"
---

In Frappe CRM, you can automate lead creation using the **Server Script** feature. The `Server Script` DocType allows you to write server-side Python code without creating a custom app or deploying anything.

There are four types of Server Scripts, but for this guide, we'll focus on:

1. **DocType Event**
2. **API**
3. **Scheduler Event**

## 1. Create Lead When an Email is Received (DocType Event)

Let’s say you want to create a Lead whenever an incoming email is received.

### Step 1: Go to Server Script

Navigate to:  
**Desk → Search Server Script → Add Server Script**

![](/files/Screenshot%202025-05-14%20at%204.22.39%E2%80%AFPM.png)

![](/files/Screenshot%202025-05-14%20at%204.24.06%E2%80%AFPM.png)

### Step 2: Fill in the following:


| Field           | Value         |
| --------------- | ------------- |
| **Script Type** | DocType Event |
| **Doctype**     | Communication |
| **Event**       | After Insert  |
| **Script**      | *(see below)* |


### Sample Script:

```python
if doc.communication_type == 'Communication' and doc.sent_or_received == 'Received':
    existing_lead = frappe.db.exists("CRM Lead", {"email": doc.sender})
    if not existing_lead:
        frappe.get_doc({
            "doctype": "CRM Lead",
            "first_name": doc.sender_full_name,
            "email": doc.sender,
            "source": "Email",
            "status": "New",
        }).insert(ignore_permissions=True)
```

This will automatically create a new Lead for each new incoming email, avoiding duplicates.

![](/files/Screenshot%202025-05-14%20at%204.21.07%E2%80%AFPM.png)

## 2. Create Lead via Custom API (API Script)

Sometimes you want to allow external systems to create leads by calling an API endpoint.

### Step 1: Go to Server Script

Navigate to:  
**Desk → Search Server Script → Add Server Script**

![](/files/Screenshot%202025-05-14%20at%204.22.39%E2%80%AFPM.png)

![](/files/Screenshot%202025-05-14%20at%204.24.06%E2%80%AFPM.png)

### Step 2: Fill in the following:


| Field           | Value             |
| --------------- | ----------------- |
| **Script Type** | API               |
| **API Method**  | `create_lead_api` |
| **Script**      | *(see below)*     |


### Sample Script:

```python
data = frappe.local.form_dict

if not data.get("email") or not data.get("name"):
    frappe.throw("Missing required fields: 'email' and 'name'")

existing_lead = frappe.db.exists("CRM Lead", {"email": data["email"]})
if existing_lead:
    frappe.response["message"] = f"Lead already exists: {existing_lead}"
else:
    lead = frappe.get_doc({
        "doctype": "CRM Lead",
        "first_name": data["name"],
        "email": data["email"],
        "status": "New",
        "source": "API"
    })
    lead.insert(ignore_permissions=True)
    frappe.response["message"] = f"Lead created: {lead.name}"
```

### How to Use:

Send a `POST` request to:

```
https://&lt;your-site&gt;/api/method/create_lead_api
```

With body:

```json
{
  "email": "someone@example.com",
  "name": "Someone"
}
```

![](/files/Screenshot%202025-05-14%20at%204.26.21%E2%80%AFPM.png)

## 3. Create Lead via Scheduled Job (Scheduler Event)

You may want to create leads periodically based on some logic — for example, leads from another table, or inactive users.

### Step 1: Go to Server Script

Navigate to:  
**Desk → Search Server Script → Add Server Script**

![](/files/Screenshot%202025-05-14%20at%204.22.39%E2%80%AFPM.png)

![](/files/Screenshot%202025-05-14%20at%204.24.06%E2%80%AFPM.png)

### Step 2: Fill in the following:


| Field               | Value                    |
| ------------------- | ------------------------ |
| **Script Type**     | Scheduler Event          |
| **Cron Expression** | `0 * * * *` (Every hour) |
| **Script**          | *(see below)*            |


### Sample Script:

```python
# Example: Create a test lead every hour for demo
frappe.get_doc({
    "doctype": "CRM Lead",
    "first_name": "Auto Generated Lead",
    "email": f"demo_{frappe.utils.now_datetime().strftime('%H%M%S')}@example.com",
    "source": "Scheduled Script",
    "status": "New"
}).insert(ignore_permissions=True)
```

You can replace this logic with any query, filter, or custom rule to generate leads.

![](/files/Screenshot%202025-05-14%20at%204.27.12%E2%80%AFPM.png)

## Permission Query (Skipped)

The **Permission Query** type is used to control record visibility dynamically. It’s not used for lead creation, so we’re skipping it in this guide.

## Tips

- Always test your script in a **Test Site** before using it in production.
- Use `ignore_permissions=True` cautiously.
- Use `frappe.throw()` for input validation in API scripts.

## Learn More

- [Server Scripts in Frappe Docs](https://docs.frappe.io/framework/user/en/desk/scripting/server-script)
- [CRON Format Guide](https://crontab.guru/)

<!-- page: crm/crm__custom-statuses.md -->
---
title: "Custom Statuses"
space: "CRM"
url: "https://docs.frappe.io/crm/custom-statuses"
updated: "2026-05-26"
---

# Custom Statuses

Custom statuses let you filter which status options appear in the  Lead or Deal dropdown. You can define different status lists based on  any field value on the document.

## How it works

Set `this.statuses` to an array of status **name strings**. Only statuses whose name appears in the array will be shown in the dropdown. The names must exist in the **CRM Lead Status** or **CRM Deal Status** master — add new ones in **CRM Settings → Statuses** first.

The array is set inside a CRM Form Script class for your doctype.  Because the list is just JavaScript, you can conditionally choose  statuses based on any field or logic.

## Basic Example — Static List

```js
class CRMLead {
    onLoad() {
        this.statuses = [
            "New",
            "Contacted",
            "Qualified",
            "Nurturing",
            "Lost"
        ]
    }
}
```

The dropdown will only show these five statuses, in this order.  


![](/files/Screenshot 2026-05-26 at 6.21.39 PM.png)

## Dynamic Example — Per Deal Type

Different products or services often need different sales pipelines.  Use a field change handler to swap the status list when the user changes  a field.

The deal statuses that ship by default are:


| Status             | Included in Product | Included in Service |
| ------------------ | ------------------- | ------------------- |
| Qualification      | ✓                   | —                   |
| Demo/Making        | ✓                   | —                   |
| Proposal/Quotation | —                   | ✓                   |
| Negotiation        | ✓                   | ✓                   |
| Ready to Close     | —                   | ✓                   |
| Won                | ✓                   | ✓                   |
| Lost               | ✓                   | ✓                   |




```js
class CRMDeal {
  onLoad() {
    this._updateStatuses();
  }

  custom_deal_type() {
    this._updateStatuses();
    // Reset status if the current value isn't in the new pipeline
    if (this.doc.status && !this.statuses.includes(this.doc.status)) {
      this.doc.status = this.statuses[0];
    }
  }

  _updateStatuses() {
    if (this.doc.custom_deal_type === "Product") {
      this.statuses = [
        "Qualification",
        "Demo/Making",
        "Negotiation",
        "Won",
        "Lost",
      ];
    } else {
      this.statuses = [
        "Proposal/Quotation",
        "Negotiation",
        "Ready to Close",
        "Won",
        "Lost",
      ];
    }
  }
}

```

The helper `_updateStatuses` runs on load and whenever `custom_deal_type` changes. Switching pipelines also resets `this.doc.status` to the first entry if the current value no longer exists in the new list.

## Adding Custom Status Names

If the default statuses don't fit your process, add new ones in **CRM Deal Status / CRM Lead Status**  in Desk. For example, the Product pipeline might need "Evaluation" and  the Service pipeline might need "Consultation/Inquiry". Create those  status entries first, then reference them in your script:

```js
class CRMDeal {
  onLoad() {
    this._updateStatuses();
  }
  _updateStatuses() {
    this.statuses = [
      "Consultation/Inquiry", // custom — create in CRM Settings first
      "Proposal/Quotation",
      "Negotiation",
      "Won",
      "Lost",
    ];
  }
}

```

A status name that doesn't exist in the master is silently ignored — it won't appear in the dropdown, and no error is shown.  


![](/files/Screenshot 2026-05-26 at 6.57.01 PM.png)
*New status in CRM Deal Status*

![](/files/Screenshot 2026-05-26 at 6.56.55 PM.png)

## Default Statuses

### CRM Lead Status


| Name        | Type    | Position |
| ----------- | ------- | -------- |
| New         | Open    | 1        |
| Contacted   | Ongoing | 2        |
| Nurture     | Ongoing | 3        |
| Qualified   | Won     | 4        |
| Converted   | Won     | 5        |
| Unqualified | Lost    | 6        |
| Junk        | Lost    | 7        |


### CRM Deal Status


| Name               | Type    | Position | Probability |
| ------------------ | ------- | -------- | ----------- |
| Qualification      | Open    | 1        | 10%         |
| Demo/Making        | Ongoing | 2        | 25%         |
| Proposal/Quotation | Ongoing | 3        | 50%         |
| Negotiation        | Ongoing | 4        | 70%         |
| Ready to Close     | Ongoing | 5        | 90%         |
| Won                | Won     | 6        | 100%        |
| Lost               | Lost    | 7        | 0%          |


## Reference


| Property        | Type       | Description                                                                                                |
| --------------- | ---------- | ---------------------------------------------------------------------------------------------------------- |
| `this.statuses` | `string[]` | Array of status names to show in the dropdown. Readable and writable at any point in the script lifecycle. |


### Behaviour notes

- **Order**: Statuses appear in the dropdown in the order you specify in the array.
- **Missing statuses**: Names that don't exist in the  master are silently ignored — they won't appear as options. Check your  spelling or add them in CRM Settings → Statuses.
- **Reactivity**: Updating `this.statuses` after the form has loaded (e.g. in a field change handler) re-renders the dropdown immediately.
- **Status reset**: When switching pipelines, the current `this.doc.status` is **not** automatically cleared — use the `includes` check pattern shown above to reset it explicitly.

<!-- page: crm/crm__data.md -->
---
title: "Data\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "CRM"
url: "https://docs.frappe.io/crm/data"
updated: "2026-02-05"
---

The side panel allowed quick access to frequently used fields but had limitations like excessive scrolling and no support for child tables. The new Data Tab addresses these issues, offering a cleaner, more organized way to view and manage data efficiently.

<img src="/files/Data.png">

You can customize the data fields using Tabs, Sections, and Columns. Click the Edit button to modify the layout.

> The Edit button is only visible to Sales Managers.

<img src="/files/CustomizeData.png">

<!-- page: crm/crm__deal.md -->
---
title: "Deal"
space: "CRM"
url: "https://docs.frappe.io/crm/deal"
updated: "2026-04-20"
---

A deal is a qualified opportunity you're actively working to close. It usually starts as a [lead](https://docs.frappe.io/crm/lead). Once you've figured out there's real potential, you convert it into a deal and start tracking it through your pipeline. You can also use the deal record to track upsells, cross sells and renewals too against an organization.

## The Deals List

The Deals list works just like the Leads list. Each row shows you the organization, deal value, status, email, phone, who it's assigned to, and when it was last updated.

You can filter, sort, and switch between List and Kanban view. To create a deal manually, hit **+ Create** in the top right.

![](/files/imagef5b098.png)
*The Deal List*

## Inside a Deal

When you open a deal, the layout is similar to a lead – activity on the left, details on the right. But there are a few differences.

On the right side, you'll see three sections:

- **Contacts** – A deal can have multiple contacts linked to it, unlike a lead, which is tied to one person. When a lead is converted, the contact from the lead becomes the primary contact automatically. You can add more contacts anytime using the + button
- **Forecasted Sales** – Shows up when forecasting is enabled. You can set an expected closure date, probability, and expected deal value here. If you've also enabled Auto Update Expected Deal Value, this gets calculated automatically from the products table
- **Organization Details** – The organization linked to the deal, along with website, territory, annual revenue, and deal owner

![](/files/image46af1b.png)
*Inside the Deal record*

The tabs across the top work the same as leads:

- **Activity** – Full timeline of everything that's happened on this deal
- **Emails** – Send and receive emails directly from here
- **Comments** – Leave notes for your team, tag teammates
- **Data** – All the deal fields in one place, plus a **Products** table where you can add what you're selling. Each row is a product with quantity, rate, and discount. The table calculates the total and net total automatically. You can also edit the table columns to show hidden fields — click the settings icon on the table header to do that
  ![](/files/imageb9b279.png)
  *Products table in Data tab of Deal*
- **Calls** – Call history and recordings
- **Tasks** – Tasks linked to this deal
- **Notes** – Freeform notes
- **Attachments** – Files and documents

## **Adding a new Deal Status**

At the top, you'll also see the Deal status. Some of these statuses are available out of the box. If you want to add custom statuses, you can add them by going to the Desk view (more details ++**[read here](https://docs.frappe.io/crm/setting-up#frontend-and-backend)**++) and searching for CRM Deal Status. Add the status of your choice, choose the type, and click on save. The Deal status helps you visualize your Deals through a pipeline.

![](/files/image7b8e37.png)
*Adding new CRM Deal Status*

![](/files/image1cfa53.png)

## What carries over from the Lead

When you convert a lead to a deal, all the communication history – emails, calls, comments, moves over to the deal. Nothing gets lost. 

The organization name becomes the deal name, and the contact linked to the lead becomes the primary contact on the deal.

## Forecasting

If you want to forecast revenue across your pipeline, go to **Settings > Dashboard** and enable the **Enable Forecasting** toggle. This makes the Expected Closure Date and the Expected Deal Value mandatory on every deal. You can also turn on **Auto Update Expected Deal Value** to have it calculated automatically from whatever you've added to the Products table.

![](/files/imageb5022f.png)
*Enable Forecasting in Settings*

Once enabled, the Forecasted Sales section will appear on every deal's right panel.

## Marking a Deal as Lost

When you change a deal's status to Lost, a pop-up appears asking you to fill in a Lost Reason and any additional notes. This helps you track why deals fall through and spot patterns over time.



![](/files/4f7d-1391-4a94-b8ee-3c112b70f144.mp4)

<!-- page: crm/crm__email-communication.md -->
---
title: "Email Communication"
space: "CRM"
url: "https://docs.frappe.io/crm/email-communication"
updated: "2026-02-05"
---

This feature allows you to seamlessly exchange emails with your customers directly from the Lead/Deal page within the system. All email interactions are conveniently stored and accessible, promoting efficient communication and record-keeping.

Sending Emails
--------------

1. **Locate the Reply Button:** On the Lead or Deal page, find the "Reply" button, typically situated at the bottom of the page.
2. **Compose Your Email:** A new email composition window will appear. Here, you can:
    ![](/files/4fKjcOz.png)
    * **Subject:** Craft a clear and concise subject line that summarizes the email's purpose.
    * **To:** Enter the recipient's email address in the "To" field.
    * **Cc & Bcc (Optional):** Utilize the "Cc" (Carbon Copy) field to include additional recipients who should be informed but not required to respond. The "Bcc" (Blind Carbon Copy) field allows you to send a copy to recipients without revealing their addresses to other recipients.
    * **Message Body:** Compose the main content of your email. You can leverage formatting options for better readability and include attachments if necessary.
3. **Leverage Email Templates (Optional):** Streamline communication by incorporating pre-defined email templates. Click on the "Email Template" icon and select the desired template from the available list. This pre-populates the message body, saving you time and ensuring consistency.
    ![](/files/hiOatPi.png)
4. **Hit Submit:** Once you've crafted your email, click the "Submit" button to send it to the recipient(s).

Viewing Email Communication
---------------------------

All email interactions related to a specific Lead or Deal are consolidated within the system. You can access them in two ways:

* **Activities Tab:** This tab provides a comprehensive view of all activities associated with the Lead/Deal, including emails, calls, tasks, and notes.
    ![](/files/Mo06n61.png)
* **Emails Tab:** For a focused view solely on email communication, switch to the dedicated "Emails" tab. This tab exclusively displays email threads related to the Lead/Deal, offering a clear and organized record of your email exchanges.
    ![](/files/xSfEsfR.png)

Email Account Setup
-------------------

You can sync your email account with Frappe CRM to send and receive emails from Frappe CRM.

You can manage multiple incoming and outgoing Email Accounts in Frappe CRM. There has to be at least one default outgoing account and one default incoming account. If you are on the Frappe CRM cloud, the default outgoing email is set by us.

To access Email Accounts, go to Email Account Master from the desk.

### 1. Prerequisites

Before creating an Email Account, you need an Email Domain. However, you can skip creating an Email Domain if you're using one of the services listed [here](https://docs.erpnext.com/docs/user/manual/en/email-inbox#2-create-an-email-domain).


> For detailed Email Account setup you can check ERPNext documentation [here](https://docs.erpnext.com/docs/user/manual/en/email-account)
> 
> 

### 2. How to create an Email Account

1. Go to the Email Account list, and click on New.
2. Enter the email address with the domain. Domains need to be created to create an email account. You don't need to create a domain if you're syncing an email from certain providers as listed [here](https://docs.erpnext.com/docs/user/manual/en/email-inbox#2-create-an-email-domain).
3. Enter the email account password.
4. Save. If the credentials are correct, the email account will be synced.


> For some services like Gmail, you may need to enable 2FA and use [App Passwords](https://myaccount.google.com/u/0/apppasswords).
> 
> 

### 3. Additional options when creating an Email Account

1. **Use Different Email Login ID**: To use an alternative email login and password to access this account. For example, if you have [notifications@example.com](mailto:notifications@example.com) and you want users to access this email with an alternate email ID, they should tick this checkbox. The recipients will see [notifications@example.com](mailto:notifications@example.com) as the sender.
2. **Awaiting password**: If you're creating this account on behalf of someone and the password is unknown, tick this checkbox. When the other user logs in, they'll be prompted to enter the password.
3. **Use ASCII encoding for the password**: Ticking this will use ASCII encoding for the password.

<!-- page: crm/crm__email-template.md -->
---
title: "Email Template"
space: "CRM"
url: "https://docs.frappe.io/crm/email-template"
updated: "2026-04-23"
---

Email Templates is a time-saving tool that lets you create reusable email drafts (such as introductions, follow-ups, or proposals) you frequently send to your leads and deals. With the ability to utilize Jinja templates, you can personalize emails to cater to specific recipients or contexts. 

## Create a new Email Template

To create a new email template, go to **Settings > Templates.** Click on Create, and add the:

- **Name:** A label to identify the template in your list
- **Subject:** The email subject line (Jinja variables supported)
- **For:** Whether it is for a lead or a deal
- **Content Type:** You can select how you want to format the template. There are two options: Rich Text and HTML

![](/files/image8cee4e.png)

Only "Enabled" Email Templates will be visible for further use. There is a toggle option against every template.

## Using the Email Template

You can use the Email Templates you have created in Lead and/or Deal while composing your emails by clicking on the Email Template button. When you click on Reply to compose an email, the email template button appears.

For example, as seen in the screenshot, the email template "First response to deals" is selected.

![](/files/image6ca4dd.png)

The email content is then copied, and you are free to edit the content as well to personalize it further.

![](/files/image422097.png)

<!-- page: crm/crm__erpnext.md -->
---
title: "ERPNext"
space: "CRM"
url: "https://docs.frappe.io/crm/erpnext"
updated: "2026-06-25"
---

Frappe CRM, while a standalone application, offers seamless integration with ERPNext to streamline your business processes. This integration allows you to create quotations and customers directly from deals within Frappe CRM, enhancing efficiency and reducing manual data entry.

## ERPNext Setup

Both Frappe CRM and ERPNext are installed on the same site  

![](/files/image0391fb.webp)

1. Navigate to **Settings** -> **ERPNext** -> **Enable** -> Set **Company**.
2. Create **Customer** when status change -> Set **Deal Status (Optional)**

## What gets synced

Once the integration is enabled, data flows between Frappe CRM and ERPNext as described below. Most syncing runs only when both apps are on the same site; differences for separate-site setups are called out where they apply.

### Customers

- The Customer is named after the Deal's organization (Customer Type **Company**) or after the primary contact / lead name when there is no organization (Customer Type **Individual**).
- The Deal's contacts and organization address are carried over to the new Customer.
- Territory, currency, industry and website are copied from the Deal. Territory and industry are dropped automatically if they don't exist in ERPNext.

**Two Ways:**

1. Upon marking a Deal as "Won" (or a specified status, configurable in ERPNext settings), a new customer will be created in your ERPNext instance. The Deal's contacts and organization address will be automatically linked to this newly created customer.
  ![Screenshot 2024-09-18 at 8.45.09 PM](https://docs.frappe.io/files/Screenshot%202024-09-18%20at%208.45.09%E2%80%AFPM.png)
  ![Screenshot 2024-09-18 at 9.07.32 PM](https://docs.frappe.io/files/Screenshot%202024-09-18%20at%209.07.32%E2%80%AFPM.png)
2. When a Sales Order is create in ERPNext from a Deal's Quotation.
  he Create Quotation button on a Deal opens a new Quotation in ERPNext with the Deal's data pre-filled:

- The quotation is raised against the Customer if one already exists otherwise against the CRM Deal itself. (ERPNext's Quotation To field is extended to allow Customer, Lead, Prospect and CRM Deal.)
- The Deal's primary contact and organization address are attached.
- Quotation line items are pre-filled from the Deal's products ie item code, quantity, rate and discount for every Deal product that is linked to an ERPNext Item.

The typical Deal to Sales Order flow looks like: 

![](/files/create quotation.webp)
*Create Quotation*

Quotation line items are pre-filled from the deal's products

![](/files/image9b795a.webp)
*New Quotation*

![](/files/Sales Order1eb7d4.webp)

Once the customer is created, you'll find a "View Customer" button on the deal header, allowing you to easily access the customer from deal page.

![Screenshot 2024-09-18 at 8.43.34 PM](/files/Screenshot 2024-09-18 at 8.43.34 PM.png)

### CRM Product and ERPNext Item

ERPNext Items and CRM Products are kept in sync with ERPNext as the source of truth. This sync runs on the same site only.

![](/files/sync.webp)

- Creating an Item in ERPNext automatically creates a matching CRM Product and links the two records.
- Updating an Item auto updates its CRM Product. The synced fields are: item name, rate, image, disabled status and description.
- Renaming an Item renames its CRM Product (and vice-versa) keeping both sides aligned.
- Deleting an Item deletes its linked CRM Product and deleting a CRM Product deletes its linked Item.

### Pricing

  Product rates shown in the CRM follow ERPNext's pricing rather than a static value:

- A CRM Product's rate is taken from its ERPNext Item Price in the selling price list falling back to the Item's standard rate when no Item Price exists.
- On a Deal, each product line is priced the way ERPNext prices a quotation line: the price list is derived from the Deal's customer (or the default selling price list when there is none), and the rate is looked up for the item's UOM. If no Item Price is found, the CRM Product's standard rate is used as a fallback.  
This means a customer specific price list configured in ERPNext surfaces its negotiated rates directly on the Deal.

## Customizations

The **Create Quotation** and **View Custome**r buttons on the Deal page are rendered by a standard CRM Form Script named Create Quotation from CRM Deal. It is created automatically when you enable the integration and is bound to the CRM Deal form view.

### How the script works

  On load, the script checks whether the integration is enabled and if so, it adds the actions to the Deal header:

- **Create Quotation** calls the backend to build the pre-filled quotation URL and opens it n a new tab.
- **View Customer** shown only when the Deal already has a linked ERPNext Customer. opens the Customer record in a new tab.

![](/files/imageec1372.webp)
*Form Script*

### Editing the script

Because it is a standard script, Create Quotation from CRM Deal is read-only and cannot be edited in place. This protects it from being overwritten. 

To customize the behavior:

1. Go to Desk → CRM Form Script.
2. Disable the Create Quotation from CRM Deal script.
3. Duplicate it (or create a new script on the CRM Deal form view) and make your changes there. for example: changing the conditions under which the buttons appear. Add new actions or adjust labels.
4. Enable your copy.

Your custom script then renders the buttons in place of the standard one.

**Example Script:**

```
class CRMDeal {
        onLoad() {
                if (this.doc.__newDocument) return
                call(
                        "frappe.client.get_single_value",
                        {
                                doctype: "ERPNext CRM Settings",
                                field: "enabled"
                        }
                ).then((enabled) => {
                        if (enabled) this.doc.trigger('setActions')
                })
        }
        setActions() {
                // Only offer quotation creation for qualified-or-later deals
                const allowed = ["Qualification", "Proposal/Quotation", "Negotiation"]
                if (allowed.includes(this.doc.status)) {
                        this.actions.push({
                                label: __("Create Quotation"),
                                onClick: () => {
                                        call(
                                                "crm.fcrm.doctype.erpnext_crm_settings.erpnext"
                                                {
                                                        crm_deal: this.doc.name,
                                                        organization: this.doc.organization
                                                }
                                        ).then((quotation_url) => {
                                                if (quotation_url) {
                                                        window.open(quotation_url, '_blank')
                                                } else {
                                                        toast.error("Error while creating quotation")
                                                }
                                        }).catch((e) => {
                                                toast.error(e.messages[0] || "Error while creating")
                                        });
                                }
                        })
                }
     // A custom action unrelated to the integration
            this.actions.push({
                    label: __("Copy Deal Link"),
                    onClick: () => {
                            navigator.clipboard.writeText(window.location.href);
                            toast.success(__("Deal link copied"));
                    }
            })
    }
}
```

<!-- page: crm/crm__exotel.md -->
---
title: "Exotel\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "CRM"
url: "https://docs.frappe.io/crm/exotel"
updated: "2026-02-05"
---

Exotel is a cloud telephony platform that enables businesses to manage voice calls, SMS, and communication workflows without traditional phone hardware. The integration with Frappe CRM combines these communication capabilities with customer relationship management to provide a unified system for handling customer interactions.

Make call
-----------

* **Lead page:** A call button is available in the right section above lead details. Use this button to initiate a call, but ensure the **Mobile No** field in the **Person** section includes the country code.
    ![](/files/PBAkpiy.png)
* **Deal page:** In the **Contacts** section on the right side. You can add multiple contacts and designate a primary contact. The call button will utilize the primary contact's number.  
    ![](/files/LKceTy6066660.png)
* **Contact page:** Directly initiate a call by clicking the **Mobile No** displayed below the contact's name.  
    ![](/files/9YnXfPgc03eb0.png)

> Make sure to complete your KYC on Exotel before making calls [docs](https://support.exotel.com/support/solutions/articles/110606-trial-accounts-how-do-i-test-outbound-calling-)

Call pop-up
-----------

Upon making or receiving a call, a pop-up window appears displaying:

* Caller name
* Mobile number
* Call status
* Call duration
* Note button
* Task button
* Lead/Deal button
* Action buttons (Close or Minimize)


![](/files/Screenshot%202025-01-20%20at%206.39.27%E2%80%AFPM607878.png)


This window can be minimized, allowing navigation to other screens, while remaining accessible in the far-right corner of the navbar.  

![](/files/Screenshot%202025-01-20%20at%206.38.34%E2%80%AFPM.png)


Take notes &amp; task during a call
------------------------

While on a call, you can take notes/task using the note/task button. These notes/task are saved in the Call Log for later viewing and editing.  

<div style="display: flex;">
    <img style="height: 300px;" src="/files/Screenshot%202025-01-20%20at%206.32.05%E2%80%AFPM38cf45.png">
    <img style="height: 300px;" src="/files/Screenshot%202025-01-20%20at%206.30.54%E2%80%AFPM2432c4.png">
</div>

Exotel setup
------------

To configure Exotel for use within the CRM, follow these steps:

1. **Exotel Subscription:** Obtain an active Exotel subscription (refer to Exotel's documentation for details).
2. **Exotel Credentials:** From your Exotel account, retrieve your Account SID, Subdomain, API Key, API Token and Exotel Mobile Number (Exophones).
    ![](/files/Screenshot%202025-01-20%20at%206.51.13%E2%80%AFPM.png)
    ![](/files/Screenshot%202025-01-20%20at%206.56.49%E2%80%AFPM.png)
3. **Settings**: Click the dropdown menu on the top left logo and select "Settings."
    ![](/files/LHGhoZR.png)
4. **Telephony Settings:** Navigate to Telephony Settings and enable Exotel. Add your Account SID, Subdomain, API Key, API Token and set Webhook verify token (it can be anything it will be used later in Exotel incoming call flow configuration). You can also enable call recording at this point.  
    ![](/files/Screenshot%202025-01-20%20at%206.27.24%E2%80%AFPM.png)
5. **Telephony Agent:** Go to Telephony Agent (In Desk) and add users (agents) with Exotel mobile number designated for making calls and also personal number(do not forget to mark one number as primary).

    >  Make sure the email is same in both Telephony Agent and Exotel.

    ![](/files/Screenshot%202025-01-20%20at%206.41.03%E2%80%AFPM.png)


Exotel incoming call flow configuration
------------------------

For your CRM's API to connect with Exotel, perform the following configurations within Exotel:

1. Login to your Exotel account and go to App Bazar.
2. Create a new "App" for a new flow.
    ![](/files/Screenshot%202025-01-20%20at%207.02.50%E2%80%AFPM0a6a6d.png)
3. Setup the flow as you wish it to be.
    
    * [Dial Whom](https://support.exotel.com/support/solutions/articles/3000088074-working-with-connect-applet-dial-whom-)
    * [Passthru](https://support.exotel.com/support/solutions/articles/48283-working-with-passthru-applet)
    * Check the documentation to learn about all the applets in flow builder - [Link](https://developer.exotel.com/applet)
4. Set "Dial Whom" as user group. In user group there can be multiple agents. Incoming call will be redirected to agents in this group in the order they are added.
    ![](/files/Screenshot%202025-01-20%20at%207.19.44%E2%80%AFPM.png)
    ![](/files/Screenshot%202025-01-20%20at%207.37.38%E2%80%AFPM.png)
5. You can also set how you want to distribute calls.
    ![](/files/Screenshot%202025-01-20%20at%207.44.03%E2%80%AFPM.png)
6. In your connect API under "Create popup...", copy and paste URL (Callback API) mentioned below. Here use webhook verify token which was mentioned in **Exotel Setup (point 4)**.


    ```
    https://<yoursitename>/api/method/crm.integrations.exotel.handler.handle_request?key=<webhook-verify-token>
    ```
    
    ![](/files/Screenshot%202025-01-20%20at%207.08.08%E2%80%AFPM.png)
7. After that add a "Passthru applet" under "After Call Conversation ends" and paste the same URL.
    
    ![](/files/Screenshot%202025-01-20%20at%207.20.05%E2%80%AFPM.png)
    ![](/files/Screenshot%202025-01-20%20at%207.20.46%E2%80%AFPM.png)
    > Note: Make sure to check "Make Passthru Async".

8. Similary, add another "Passthru applet" under "If nobody answers..." section and paste the same URL.
    ![](/files/Screenshot%202025-01-20%20at%207.20.14%E2%80%AFPM.png)
    ![](/files/Screenshot%202025-01-20%20at%207.24.51%E2%80%AFPM.png)
    > Note: Make sure to check "Make Passthru Async".

9. Save the flow.
10. Now assign this newly created "App" to your ExoPhone from which you receive your business calls.
    ![](/files/Screenshot%202025-01-20%20at%207.26.56%E2%80%AFPM.png)

Once this is done, you should see all new incoming calls on your exotel phone number in the "Call Log" list in your CRM instance.

![](/files/Screenshot%202025-01-20%20at%207.30.13%E2%80%AFPM.png)

<!-- page: crm/crm__general-and-defaults.md -->
---
title: "General and Defaults"
space: "CRM"
url: "https://docs.frappe.io/crm/general-and-defaults"
updated: "2026-04-20"
---

These are system-wide settings that apply across your entire CRM. You'll probably set these once and rarely touch them again. To get here, go to **Settings > General** and **Settings > Defaults**.

## General

These settings control how your CRM behaves when emails and comments come in.

![](/files/Screenshot 2026-04-20 at 5.44.28 PM.png)

- **Update timestamp on new communication** – When someone sends an email or leaves a comment on a lead or deal, this updates the "Last Modified" timestamp on that record. Useful for tracking recent activity across your pipeline. If you don't enable this, then new email activity won't affect the last modified timestamp
- **Mark lead/deal as replied on response** – When a customer replies to your email, the lead or deal is automatically marked as "Replied". Only works if SLA is enabled
- **Reopen lead/deal on new communication** – If a new email comes in on a lead or deal, it automatically sets the status back to "Open". Only works if SLA is enabled

## Defaults

These settings control how numbers, currencies, and dates are displayed across the CRM. Set these to match how your team works.

![](/files/Screenshot 2026-04-20 at 5.45.52 PM.png)

- **Currency** – The default currency for all records. Can be changed on individual records if needed
- **Currency Precision** – How many decimal places to show for currency values
- **Number Format** – How numbers are displayed, for example, with commas and decimal separators
- **Float Precision** – Decimal places for non-currency number fields
- **Date Format** – How dates appear across the CRM, for example, dd-mm-yyyy
- **Time Format** – Whether to show time with or without seconds

<!-- page: crm/crm__home-actions.md -->
---
title: "Home Actions"
space: "CRM"
url: "https://docs.frappe.io/crm/home-actions"
updated: "2026-04-20"
---

When you click on the CRM logo at the top left, a small dropdown appears. By default, it shows things like Apps, Settings, and Log out.

**Home Actions** lets you customize what shows up there. Add links to tools your team uses every day, hide things they don't need, or add separators to keep things organized.

It's a small thing, but it makes a big difference if your team is jumping between tools often.

To get here, go to **Settings > Home Actions**.

![](/files/Screenshot 2026-04-20 at 5.36.42 PM.png)

Each row in the list is one item in the dropdown. You can edit any row to configure:

- **Label** – The name that shows up in the dropdown
- **Type** – Either a Route (a link) or a Separator (a divider line to group things)
- **Route** – The URL or internal path the link points to
- **Icon** – Use a Feather icon name like `settings` or `book-open`, or paste in custom SVG code
- **Open in new window** – Opens the link in a new tab
- **Hidden** – Hides the item from the dropdown without deleting it

Click **Add Row** to add a new link. Hit **Update** when you're done.

<!-- page: crm/crm__introduction.md -->
---
title: "Introduction"
space: "CRM"
url: "https://docs.frappe.io/crm/introduction"
updated: "2026-04-20"
---

## What is Frappe CRM

If you're here, you're probably outgrowing a spreadsheet, paying too much for a CRM that charges per seat, or just overwhelmed by features you never use. We've heard this a lot.

When we built Frappe CRM, we had two things in mind. Keep it simple enough that your sales team actually enjoys using it. And keep it open source, so it's always yours to own and adapt.

Most CRMs are built for enterprise teams with dedicated admins and big budgets. Frappe CRM is built for everyone else – founders tracking their first pipeline, sales managers who want their team focused on selling, and growing businesses that don't want to rethink their tooling every time they hire someone new.

## What it does

Frappe CRM gives you everything a sales team needs to manage their pipeline without the clutter.

- **Leads and Deals** – Track every prospect and opportunity in one place. Add notes, log calls, set tasks, and keep the full context of every relationship right where you need it.
- **Communication** – Send and receive emails directly from a lead or deal. Use templates to move faster. Your team can leave comments and tag each other so nothing falls through the cracks.
- **Views and Reports –** Work on a simple list or a Kanban board, whatever fits how your team thinks. Filter, sort, and save your view. Pin the ones you use every day.
- **Automation** – Set up assignment rules to route leads automatically. Define SLAs so every lead gets followed up on time.
- **Customization** – Add custom fields, statuses, and actions to adapt it as per your workflow.
- **Integrations** – Connect with Twilio, Exotel, Meta, WhatsApp, and ERPNext to extend your CRM. You can also integrate with any third-party app via APIs.

## Is it for me?

Frappe CRM works well if you are:

- A small or mid-sized sales team that wants things simple and easy
- A business that likes to stay in control of its own data
- A team that’s outgrowing spreadsheets (finally 😄)
- Someone tired of per-seat pricing on other CRMs

If you need a highly complex enterprise CRM with deep out-of-the-box integrations, Frappe CRM might feel lightweight. But if you want something your team will actually use, it's worth a try.

## Ready to get started?

Head over to the [Installation page](https://docs.frappe.io/crm/introduction/installation) to get Frappe CRM up and running.

## Learning and Community

Got stuck or want to connect with others using Frappe CRM?

- [Telegram Public Group](https://t.me/frappecrm)
- [Discuss Forum](https://discuss.frappe.io/c/frappe-crm)
- [Website](https://frappe.io/crm)
- [YouTube](https://www.youtube.com/channel/UCn3bV5kx77HsVwtnlCeEi_A)

<!-- page: crm/crm__introduction__installation.md -->
---
title: "Installation"
space: "CRM"
url: "https://docs.frappe.io/crm/introduction/installation"
updated: "2026-04-21"
---

Frappe CRM can be installed in multiple ways, depending on your requirements. You can either use **Frappe Cloud** for a fully managed experience or install CRM on your own server.

The following sections explain each installation method in detail.

---

## Managed Hosting (Frappe Cloud)

You can install Frappe CRM with a single click using **[Frappe Cloud](https://frappecloud.com/crm/signup)**, the managed hosting platform for Frappe applications.

- Sign up [here](https://frappecloud.com/crm/signup) to get started
- Your CRM instance will be ready in a few minutes

If you already have a Frappe Cloud site, you can install Frappe CRM directly from the **[Frappe Cloud Marketplace](https://cloud.frappe.io/marketplace/apps/crm)**.

:::tip
Recommendation: We strongly recommend trying Frappe Cloud before opting for self-hosting.
:::





---

## Self Hosting

### Production Setup

Follow these steps to set up Frappe CRM in production:

**Step 1**: Download the easy install script

```
wget https://frappe.io/easy-install.py
```

**Step 2**: Run the deployment command

```
python3 ./easy-install.py deploy \
    --project=crm_prod_setup \
    --email=email.example.com \
    --image=ghcr.io/frappe/crm \
    --version=stable \
    --app=crm \
    --sitename subdomain.domain.tld
```

Replace the following parameters with your values:

- `your_email.example.com`: Your email address
- `subdomain.domain.tld`: Your domain name where CRM will be hosted

The script will set up a production-ready instance of Frappe CRM with all the necessary configurations in about 5 minutes.

:::note
If hosting on a public server, make sure your DNS A record points to your server's IP and if hosting locally, map your domain to 127.0.0.1 in your /etc/hosts file to avoid 404 Page Not Found error.
:::





---

### Development Setup

#### Docker Setup

To run CRM using Docker, ensure the following are installed:

- Docker
- Docker Compose
- Git

Refer to [Docker documentation](https://docs.docker.com/). After that, follow the steps below:

**Step 1**: Create a directory and download the required files

```bash
mkdir frappe-crm
cd frappe-crm

# Download the docker-compose file
wget -O docker-compose.yml https://raw.githubusercontent.com/frappe/crm/develop/docker/docker-compose.yml

# Download the setup script
wget -O init.sh https://raw.githubusercontent.com/frappe/crm/develop/docker/init.sh
```

**Step 2**: Start the containers

```
docker compose up -d
```

**Step 3**: Access the application.

The site [http://crm.localhost:8000/crm](http://crm.localhost:8000/crm) should now be available. The default credentials are:

```
Username: Administrator
Password: admin
```

:::tip
Security note: Recommend changing the default password after login.
:::





#### Local Setup (Bench)

1. [Setup Bench](https://docs.frappe.io/framework/user/en/installation).
2. In the frappe-bench directory, run `bench start` and keep it running.
3. Open a new terminal session and cd into `frappe-bench` directory and run following commands:
  ```
  $ bench get-app crm
  $ bench new-site sitename.localhost --install-app crm
  $ bench browse sitename.localhost --user Administrator
  ```
4. Access the crm page at `sitename.localhost:8000/crm` in your web browser.

**For Frontend Development**

1. Open a new terminal session and cd into `frappe-bench/apps/crm`, and run the following commands:
  ```
  yarn install
  yarn dev

  ```
2. Now, you can access the site on the Vite dev server at `http://sitename.localhost:8080`

**Note:** You'll find all the code related to Frappe CRM's frontend inside `frappe-bench/apps/crm/frontend`

<!-- page: crm/crm__inviting-your-team.md -->
---
title: "Inviting Your Team"
space: "CRM"
url: "https://docs.frappe.io/crm/inviting-your-team"
updated: "2026-04-20"
---

Frappe CRM works best when your whole team is in. Once everyone's set up, you can assign leads, track deals together, and collaborate without things falling through the cracks.

To invite someone, go to **Settings > Invite User**.

![](/files/Screenshot 2026-04-20 at 5.04.48 PM.png)

There are two situations here:

**New users** – People who don't have a Frappe account yet. Add their email, pick a role, and hit **Send Invites**. They'll get an email asking them to set up their account and log in. If you're inviting multiple people at once, just separate their emails with commas.



**Existing site users** – If someone already has an account on your Frappe site (maybe they use another Frappe app like HRMS or Helpdesk), they're not automatically part of the CRM. You can add them directly from **Settings > Users** without sending a new invite. Just add them and assign a role.

![](/files/Screenshot 2026-04-20 at 5.14.42 PM.png)

There are three roles to choose from:

- **Sales User** – Your day-to-day sales reps. They can work on leads and deals assigned to them
- **Manager** – Can see and manage the whole team's leads and deals, not just their own
- **Admin** – Full access. Can configure the CRM, manage users, and change settings

Once someone is in, they'll show up under **Settings > Users**. You can change anyone's role anytime from there.

<!-- page: crm/crm__lead-syncing__meta.md -->
---
title: "Facebook / Instagram"
space: "CRM"
url: "https://docs.frappe.io/crm/lead-syncing/meta"
updated: "2026-03-09"
---

### Prerequisites

Before you begin, you must have atleast one Facebook page and a lead generation form. You can follow [this guide](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/) to obtain an access token for your account.

> Note: This feature is in beta, if you find any bugs, please report [here](https://github.com/frappe/crm).

### Adding a new Lead Sync Source

Open **Settings** from the dropdown menu on top-left corner of the CRM dashboard:

![Settings from Sidebar](/files/CleanShot%202025-11-11%20at%2017.09.58@2x.png)

Click on the **Lead Syncing** tab and then click on the `+ New` button to add a new Source:

![Lead Syncing Settings](/files/CleanShot%202025-11-11%20at%2017.15.57@2x4d3c60.png)

### Configuring Lead Sync Source

Now follow these steps:

1. Select **Facebook** as the source type
2. Give your source a relevant name
3. Select a frequency for scheduled syncing: how frequently the leads should be automatically synced
4. Paste the Access token obtained from Meta

![New Lead Sync Source](/files/CleanShot%202025-11-11%20at%2017.18.55@2x047f4a.png)

Now click **Create**. It will take a few seconds since we are pulling the pages and forms from Facebook. But once it is done, you can select the page and the form from where the leads will be pulled in from:

![Select Page and corresponding form](/files/CleanShot%202025-11-11%20at%2018.00.30@2x.png)

As soon as you select the form, you will see a mapping table:

![CRM Mapping Table](/files/CleanShot%202025-11-11%20at%2018.00.49@2x.png)

This table let's you easily map fields of your Facebook form to fields in Frappe CRM. Apart from this, we also store the Lead ID and Form ID in CRM Lead document. Once you are done configuring the field mapping, click on **Update**, and that is it! Your leads will start syncing in the background in some time.

:::tip
You can use Meta's [Graph API Explorer](https://developers.facebook.com/tools/explorer/) to test your token.
:::





### Sync Now

You can also manually trigger a lead sync by clicking on the **Sync Now** button.

### Failure Logs & Retry

If your leads don't appear in your CRM, go to the **Failure Logs** tab, and check the logs. The failure log contains the reason for failure (e.g. Duplicate), the lead data we received from Facebook, and also error traceback if available:

![Sync Failure Log](/files/CleanShot%202025-11-11%20at%2018.16.07@2xc169ec.png)

You can click on the **Retry Sync** button to retry syncing of this particular lead. 

> Note: A new failure log will get created if a resync fails too.

<!-- page: crm/crm__lead.md -->
---
title: "Lead"
space: "CRM"
url: "https://docs.frappe.io/crm/lead"
updated: "2026-04-20"
---

A lead is someone who has shown interest in your product or service but hasn't become a customer yet. It could be someone who filled out a form on your website, someone you met at an event, or a referral from an existing customer. The lead stage is where you figure out if they're worth pursuing further.

## The Leads List

When you click on Leads in the sidebar, you see all your leads in one place. Each row shows you the key details at a glance – name, organization, status, email, phone, who it's assigned to, and when it was last updated.

You can filter, sort, and search across your leads from here. 

![](/files/image7ce865.png)
*List View*

You can also switch between List and Kanban view depending on how you like to work.

![](/files/imageef81e1.png)
*Kanban View*



To create a new lead, hit **+ Create** in the top right. This is the manual way to create a lead. 

## Capturing Leads

There are a few ways to get leads into Frappe CRM without adding them manually one by one. You can embed a web form on your website, sync leads from Facebook and Instagram ads, bulk import them from Excel/spreadsheets, or write custom scripts to pull leads from other sources.

These are covered in detail in the [Capturing Leads](https://docs.frappe.io/crm/web-form) section.

## Inside a Lead

When you open a lead, everything about that person lives in one place.

![](/files/imagef3ab15.png)

On the right side are the lead's details – their name, email, phone, organization, job title, source, industry, and who owns the lead. You can edit any of these inline. 

On the left is the activity panel, with tabs across the top:

- **Activity** – A full timeline of everything that's happened. Emails, comments, calls, field changes — all in one feed
- **Emails** – Send and receive emails directly from here. No switching tabs
- **Comments** – Leave notes for your team, tag teammates, keep the conversation in context
- **Data** – Additional fields and information about the lead
- **Calls** – Log and view call history
- **Tasks** – Create and track tasks related to this lead
- **Notes** – Freeform notes that don't need to be part of the activity feed
- **Attachments** – Files, documents, anything relevant

## Adding a new Lead Status

At the top, you'll also see the Lead status. Some of these statuses are available out of the box. If you want to add custom statuses, you can add them by going to the Desk view (more details [read here](https://docs.frappe.io/crm/setting-up#frontend-and-backend)) and searching for CRM Lead Status. Add the status of your choice, choose the type, and click on save.

![](/files/imaged07f73.png)
*Adding new CRM Lead Status*

It should then appear as a newly added status in the frontend view too.

![](/files/image9ac94b.png)



You can see who the lead is assigned to, what status it's in, and a **Convert to Deal** button for when you're ready to move them forward.

## Converting a Lead to a Deal

When a lead is qualified and ready to move forward, hit **Convert to Deal**. You'll get the option to create a new Contact and Organization from the lead's details, or link to existing ones if they're already in your CRM. Also, choose the status you want your Deal to be in. 

![](/files/17e1-b1cb-4f43-b6b2-bd435b2f7a64.mp4)





Once converted, the lead becomes a Deal and moves into your sales pipeline.

<!-- page: crm/crm__mobile-app-installation.md -->
---
title: "Mobile App Installation"
space: "CRM"
url: "https://docs.frappe.io/crm/mobile-app-installation"
updated: "2026-02-05"
---

Frappe CRM offers a mobile-friendly interface through a Progressive Web App (PWA). This means you can access all the CRM functionalities directly on your phone.

Supported Devices and Browsers
------------------------------

The Frappe CRM PWA works on most modern smartphones and tablets. Here's a quick note about browser compatibility:

* **Android:** Chrome is recommended for the best experience.
* **iOS:** Safari is recommended.

> NOTE: Firefox currently doesn't support PWA installation without additional plugins.
 

How to Install
--------------

Here's how to install the Frappe CRM mobile app on your phone:

**Open the App URL:**

In your mobile browser (Chrome or Safari), navigate to the following URL, replacing `<sitename>` with your actual Frappe CRM website address:


```
https://<sitename>/crm
```

**Example:**

If your Frappe CRM site address is <https://frappecrm.frappe.cloud>, the mobile app URL would be:


```
https://frappecrm.frappe.cloud/crm
```
Devices
-------

### Android (Chrome)

1. On Android, you will get a prompt to install the app on this URL.
2. If you do not see the prompt, tap on the hamburger menu (three dots), and tap on Install app from the list of options.
3. Tap on Install, and wait for a few seconds.
4. You will then be able to find the Frappe CRM app in your applications. You can login to this app with your site credentials.

    <video controls data-setup="{}" height="auto" preload="auto" style="border-radius: 10px;
 border: 2px solid;" width="300">
<source src="https://docs.frappe.io/files/AndroidPWAInstall.mp4" type="video/mp4">
</video>

1. On iOS, if you're using Safari, tap on the share button shown in the video below.
2. Scroll down the list of options, then tap Add to Home Screen.
3. If you do not see "Add to Home Screen", click on "Edit Actions" and you should find the option.
4. The icon will then appear on your home screen. You can login to this app with your site credentials.

    <video controls data-setup="{}" height="auto" preload="auto" style="border-radius: 10px;
 border: 2px solid;" width="300">
<source src="https://docs.frappe.io/files/IOSPWAInstall.mp4" type="video/mp4">
</video>

**Congratulations! You've successfully installed the Frappe CRM PWA on your mobile device.**

<!-- page: crm/crm__note.md -->
---
title: "Note"
space: "CRM"
url: "https://docs.frappe.io/crm/note"
updated: "2026-04-21"
---

Notes are for capturing anything important about a lead or deal that doesn't fit neatly into a form field. A key thing a prospect mentioned on a call, something to remember before the next meeting, internal context for your team, or anything worth writing down.

## The Notes View

Click on Notes in the sidebar to see all notes across your CRM in one place, shown as cards. Each card shows the title, content, who wrote it, and when. You can filter and search to find what you need.

![](/files/image3d95de.png)
*The Notes View*

Every note is also linked back to the lead or deal it belongs to, so you can jump straight to the record from here.

![](/files/image348688.png)
*Inside a Note - linked to a Lead / Deal*

## Notes inside a Lead or Deal

Each lead and deal has its own Notes tab. Notes created here are tied to that specific record. They won't show up on other leads or deals. To add one, go to the Notes tab and hit **+ New Note**. Give it a title and write whatever you need.



![](/files/imaged9af76.png)
*Notes tab inside a Lead / Deal*

You can edit a note anytime by clicking on it.

## Creating a Note from the Activity tab

You can also create a note directly from the Activity tab inside a lead or deal using the **+ New** button. It'll show up in the Notes tab and in the activity feed.

![](/files/Screen Recording 2026-04-21 at 7.59.36 AM.mov)

<!-- page: crm/crm__notification.md -->
---
title: "Notification"
space: "CRM"
url: "https://docs.frappe.io/crm/notification"
updated: "2026-02-05"
---

Stay informed about important activities within your CRM system using the Notifications feature. This page serves as a central hub for all your CRM-related alerts and updates.

![](/files/4pVP4rV.png)  


Accessing Notifications
-----------------------

1. Locate the **Notifications** option in the sidebar.
2. Click to open the **Notifications Panel**.

Understanding Notifications
---------------------------

The Notifications Panel displays a list of alerts related to your CRM activities. These alerts currently includes:

* Mentions in comment
* Task assignments/unassignment (changing assigned user)
* Lead/Deal assignments/unassignment

Managing Notifications
----------------------

Within the Notifications Panel, you can perform the following actions:

* **Open a Notification:** Click on an individual notification to view the specific comment or activity it refers to. This action will also mark the notification as read.
* **Mark All as Read:** Click the dedicated button at the top of the panel to mark all your current notifications as read.

<!-- page: crm/crm__organization.md -->
---
title: "Organization"
space: "CRM"
url: "https://docs.frappe.io/crm/organization"
updated: "2026-04-21"
---

If you're in B2B sales, you're rarely dealing with just one person at a company. There might be multiple deals happening with the same organization at the same time – a new product, an upsell, a renewal, a cross-sell. Organizations give you a place to track all of it in one view.

## Inside an Organization

When you open an organization, you'll see its details on the left – name, website, territory, industry, number of employees, and address.

On the right, you get two tabs:

- **Deals** – Every deal linked to this organization, with the amount and current status. At a glance, you can see where each opportunity stands
  ![](/files/image02ff87.png)
  *Linked Deals to an Organization - could be a new Deal, Upsell/Cross-sell, Renewal*
- **Contacts** – Everyone at this organization who's in your CRM, with their email and phone
  ![](/files/image36fbcf.png)
  *Multiple stakehoders of an Organization shown as Contacts*



This makes it easy for a sales rep to walk into a conversation fully prepared. They know what's been discussed, what's open, and who else on their team has been talking to this account.

## How Organizations get created

Just like contacts, organizations are created automatically when a lead is created or converted to a deal. You can also create them manually or link an existing organization to a deal during the conversion process. Read about it more [here](https://docs.frappe.io/crm/lead#converting-a-lead-to-a-deal).

<!-- page: crm/crm__pinned-view.md -->
---
title: "Pinned View"
space: "CRM"
url: "https://docs.frappe.io/crm/pinned-view"
updated: "2026-05-21"
---

Pinned Views let you quickly access frequently used saved views directly from the sidebar. You can create custom filters, sorting, and column configurations, save them as views, and pin them for instant access whenever needed.

## How to pin a view

1. Prerequisite: Create a [saved view](https://docs.frappe.io/crm/view). If you already have an existing saved view, go to the next step.
2. Go to the **List** dropdown and navigate to the view you want to pin.
3. Hover over the desired view and click on the three-dot (...) menu.
4. From the menu that appears, select **Pin View**.

![](/files/Screenshot 2026-05-21 at 6.40.20 PM.png)

## Managing pinned views

Once you've pinned a view, it will be displayed in a dedicated "Pinned Views" section within the sidebar. You can access this view with a single click whenever needed.

![](/files/image53f4b2.png)

## Unpinning views

To remove a view from the pinned section and revert it to a regular saved view, follow the same steps mentioned above. Access the three-dot menu for the pinned view and select **Unpin View.**

<!-- page: crm/crm__profile-and-preferences.md -->
---
title: "Profile and Preferences"
space: "CRM"
url: "https://docs.frappe.io/crm/profile-and-preferences"
updated: "2026-04-20"
---

Every user in Frappe CRM has their own profile and preferences. These are personal to you. Changing them won't affect anyone else on your team.

To get here, click your name at the top left of the sidebar and go to **Settings**.

## Profile

This is your personal account page. Keep it up to date, especially if you're communicating with leads and deals directly from the CRM.

![](/files/Screenshot 2026-04-20 at 4.55.23 PM.png)

- **Name** – How you appear to your teammates inside the CRM
- **Email & Signature** – Click Configure to open your Email Settings. Here you can set up two things: 
  - **Signature** – Write your email signature once, and it'll automatically appear at the bottom of every email you send from the CRM
  - **Emails** – If your team has multiple email accounts set up, you can choose which one to send from when composing an email. Useful if you handle both a personal inbox and a shared team inbox like [sales@yourcompany.com](mailto:sales@yourcompany.com)
    ![](/files/Screenshot 2026-04-20 at 4.57.12 PM.png)
- **Password** – Change your password anytime from here.

## Preferences

This is where you make the CRM feel like yours.

- **Theme** – Light, Dark, or System. System follows whatever your OS is set to, so it switches automatically if you use dark mode at night
- **Language** – Change the language of the application. This will be only applicable to your user account, so your sales team is free to pick theirs
- **Timezone** – Set this to your local timezone so dates and times always show up correctly for you

Once you've set this up, you are now set to invite more of your team members to Frappe CRM. Check the next page to learn how to do this.

<!-- page: crm/crm__public-view.md -->
---
title: "Public View"
space: "CRM"
url: "https://docs.frappe.io/crm/public-view"
updated: "2026-05-21"
---

Public Views are [saved views](https://docs.frappe.io/crm/view) that are accessible to every sales user in the system. They function similarly to your personal saved views, but instead of being confined to your workspace, they become a shared resource accessible to everyone.

## When to use public views

Public Views are ideal for situations where a specific filter or layout needs to be consistently used by your entire team. Here are some examples:

- A view that filters leads/deals by a particular source or industry.
- A view that prioritizes high-value deals that require immediate attention.
- A view that displays specific customer information relevant to the sales team.

By creating Public Views for these commonly used scenarios, you can ensure everyone has access to the same information and is working from the same perspective.

## Who can create a public view

Only users with the **Sales Manager and Admin** roles can create Public Views. This helps maintain control over what information is shared publicly within the CRM system.

## Creating a public view

1. Prerequisite: Create a [saved view](https://docs.frappe.io/crm/view). If you already have an existing saved view, go to the next step.
2. Go to the **List** dropdown and navigate to the saved view you want to make public.
3. Hover over the desired view and click on the three-dot (...) menu.
4. From the menu that appears, select **Make Public**.
  ![](/files/image7615eb.png)

This will convert your saved view into a Public View, making it accessible to all users in the sidebar under the **Public Views** section.

## Making a public view private

Public Views can be reverted to private views at any time. Simply follow the same steps mentioned above and select **Make Private** from the three-dot menu.

<!-- page: crm/crm__quick-entry-layout.md -->
---
title: "Quick Entry Layout"
space: "CRM"
url: "https://docs.frappe.io/crm/quick-entry-layout"
updated: "2026-02-05"
---

The Quick Entry Layout Builder allows you to customize the layout of quick entry forms in Frappe CRM, similar to how you can add custom sections and fields to Lead and Deal pages. This gives you more control over the data capture process for different document types.
![](/files/Screenshot%202024-09-28%20at%203.15.58%E2%80%AFPM.png)


Steps
-----

1. **Navigate to Lead/Deal ListView:** Go to Lead/Deal ListView and click on the "Create" to open quick entry modal. Click on the edit button.
    ![](/files/Screenshot%202024-09-28%20at%203.14.48%E2%80%AFPM.png)
2. **Select the Doctype:** A modal will open and doctype will be selected automatically but can still choose the doctype for which you want to add or edit fields in the quick entry form.
3. **Utilize the Quick Entry Layout Builder:** Once you've selected the doctype, the Quick Entry Layout Builder interface for that doctype will appear. This interface provides functionalities for:
	* Adding new sections to the quick entry form.
	* Adding fields within these sections.
	* Dragging and dropping fields to reposition them within sections or between sections.
	* Rearranging sections by dragging and dropping.
	* Editing section labels to provide clear descriptions.
	* and more
4. **Preview Your Work (Optional):** The Quick Entry Layout Builder offers a **Show Preview** button. Clicking this button will display a preview of how the customized quick entry form will look for the chosen doctype. This allows you to visualize your layout changes before saving them.
    ![](/files/Screenshot%202024-09-28%20at%203.15.34%E2%80%AFPM.png)

By following these steps, you can effectively customize quick entry forms in Frappe CRM to better suit your specific data collection requirements for different document types.

<!-- page: crm/crm__service-level-agreement.md -->
---
title: "Service Level Agreement"
space: "CRM"
url: "https://docs.frappe.io/crm/service-level-agreement"
updated: "2026-05-07"
---

An SLA (Service Level Agreement) is a formal agreement outlining the level of service a provider commits to deliver and the expectations a customer has for that service. In Frappe CRM, SLAs establish response time benchmarks for communication related to Leads and Deals.

### Prerequisites

Before creating an SLA, ensure you have a **Holiday List** configured. This list is linked to the SLA to exclude holidays from response time calculations. You can create one under **Settings > Holiday List**.

### Creating an SLA

1. Go to **Settings > SLA Policies** and click on **+New**
  ![](/files/image115486.png)
2. **Define SLA details:** Fill in the following information:
  - **Name**: A label to identify the policy
  - **Apply on:** Whether it is for a lead or a deal
  - **Rolling Response:** If you want to set an SLA for subsequent responses
  - **Assignment Conditions:**
    - Set as Default SLA: Enable if you want this to be fetched as the default SLA
    - Add custom conditions: You can specify which conditions this SLA applies to. For example, you want to set an SLA for leads coming in from Europe. Add the field, the condition, and the value)  
    lid From: Set the date range during which the SLA will be active

![](/files/imagea13a3f.png)

3. **Response & Follow up:** To set the response time duration
4. **Work Schedule & Holidays:** Set working hours for each day. Only communications received during these hours will count toward response time calculations. Link your Holiday List here to automatically exclude public holidays.

![](/files/image7d4776.png)

5. **Enable the SLA:** Once you've configured the SLA details, ensure it's enabled.

### **Benefits of Using SLAs**

SLAs offer several advantages for your sales team:

- **Improved Response Times:** By establishing clear response time goals, SLAs encourage prompt communication with potential and existing customers, leading to better engagement and conversion rates.
- **Enhanced Customer Satisfaction:** Timely responses demonstrate your commitment to customer service, fostering trust and positive client relationships.
- **Streamlined Workflow:** SLAs help prioritize communication tasks, ensuring your team focuses on the most critical leads and deals within designated timeframes.
- **Performance Measurement:** SLAs provide a benchmark for evaluating your team's responsiveness and identifying areas for improvement.

By effectively utilizing SLAs in Frappe CRM, you can empower your sales team to deliver exceptional customer service and achieve optimal sales performance.

<!-- page: crm/crm__setting-up.md -->
---
title: "Setting Up Your Workspace"
space: "CRM"
url: "https://docs.frappe.io/crm/setting-up"
updated: "2026-04-20"
---

Once you've installed Frappe CRM, you'll be walked through a quick setup before you land in your workspace. It takes about two minutes.

### Step 1: Set your preferences

You'll start with a Welcome screen. Pick your language, confirm your country, set your timezone, and choose your currency. These make sure dates, times, and deal values show up correctly across your CRM.

Hit Next when you're done.

![](/files/Screenshot 2026-04-20 at 3.57.04 PM.png)
*Setting up your preferences*



### Step 2: Set up your account

Enter your full name and email address. Your email will be your login ID going forward, so use one you actively check.

Hit Complete Setup, and you're in.

![](/files/Screenshot 2026-04-20 at 3.57.40 PM.png)
*Setting up your first user (you)*

## Frontend and backend

What you're looking at is the CRM frontend. This is what your sales team will use every day. It's clean, focused, and built for speed. When you first land inside the frontend, you'll see some demo data already in place – a few sample leads with names, organizations, and statuses. 

![](/files/Screenshot 2026-04-20 at 4.07.33 PM.png)

But as the admin, you also have access to a more powerful backend view called **Desk**. 

To get there, click on the **CRM logo** at the top left, then go to **Apps > Desk**.

![](/files/image14f801.png)
*To navigate to desk view, click on Apps → Desk*

![](/files/Screenshot 2026-04-20 at 4.11.15 PM.png)
*The backend view which shows all the apps installed installed on your site*

You'll need it for things like writing scripts, adding custom fields, and some advanced configuration. To navigate around Desk, use the search bar (Command + Shift + K) to quickly find what you're looking for.

We're working on bringing more of this into the frontend, but for now, it's good to know it's there.

## What's next?

Once you're comfortable with the basics, the next step is inviting your team and configuring your CRM to match your sales process. The next few pages cover that.

<!-- page: crm/crm__settings__sales-hierarchy.md -->
---
title: "Sales Hierarchy"
space: "CRM"
url: "https://docs.frappe.io/crm/settings/sales-hierarchy"
updated: "2026-06-02"
---

Arrange your sales team into a reporting tree so managers see the leads and deals owned by their team while everyone else sees only their own.

> Only Admins Can edit the Sales Hierarchy. For others, they can only view it in read-only mode

### Enable Sales Hierarchy

Go to Settings > User Management >  Click on "Enable" button to enable sales hierarchy for your site.

![](/files/image5c50e8.png)
*Enable Sales Hierarchy*

Once enabled:

- Sales Managers see leads and deals owned by themselves and anyone below them in the tree
- Sales Users see only what they own

Note:

- A user with Sales Manager Role cannot directly report to a Sales User
- A Sales Manager who has reportees cannot be demoted to Sales User from the frontend

---

### Adding Users

Click on the "Add User" button from the top right corner to select the users which you want to add to the hierarchy. These users will be added at the top level of the tree. 

![](/files/imaged83629.png)
*Add users*

**Add direct reports**

Reportees can be added to a manager by clicking the `+` icon. Using this you can bulk assign reportees to a manager to create a hierarchy. 

![](/files/Screen Recording 2026-05-22 at 3.46.28 PM.mov)



---

### Removing Users from hierarchy

The are three ways to remove users from the hierarchy. The options depend based on whether the user has someone reporting to them or not. 

#### **Delete**

A user who does not have any reportee can be removed without unlinking by clicking on the delete button

![](/files/Screen Recording 2026-05-22 at 3.47.53 PM.mov)



#### **Reassign And remove**

Moves their direct reports up to their own manager and then removes them from the hierarchy

![](/files/Screen Recording 2026-05-22 at 3.50.25 PM.mov)



#### **Remove with reports**

Removes the user and everyone reporting to them from the hierarchy. 

![](/files/Screen Recording 2026-05-22 at 3.52.30 PM.mov)



---

### **Managing users**

Quickly drag and drop users you want to change reporting for.

![](/files/Screen Recording 2026-05-22 at 3.54.57 PM.mov)



#### **Move a user to top level**

A Manger who reports to another manager can be moved to top level along with their reportees. 

![](/files/Screen Recording 2026-05-22 at 3.56.30 PM.mov)

<!-- page: crm/crm__task.md -->
---
title: "Task"
space: "CRM"
url: "https://docs.frappe.io/crm/task"
updated: "2026-04-21"
---

If you or your team are still tracking follow-ups on a spreadsheet or a sticky note, you have a better place to do so now.

Tasks are how you make sure things actually get done. Send a proposal, schedule a demo, follow up on a trial, anything with a clear action and a deadline can be a task. They're linked to leads and deals, so everything stays in context.

## The Tasks List

Click on Tasks in the sidebar to see all tasks across your CRM. Each row shows the title, status, priority, due date, and who it's assigned to. You can filter by assignee, priority, status, or due date to focus on what matters right now.

![](/files/image14bb92.png)
*Inside a Task*

## Tasks inside a Lead or Deal

Each lead and deal has its own Tasks tab. Tasks created here are tied to that specific record. Hit **+ New Task** to create one.

![](/files/image15816a.png)
*Task tab inside a Lead / Deal*

Each task has:

- **Title** – What needs to be done
- **Description** – Any additional context or details
- **Status** – Backlog, Todo, In Progress, Done, or Cancelled
- **Assignee** – Who's responsible for it
- **Due Date** – When it needs to be done by
- **Priority** – High, Medium, or Low

## Task Reminders

Frappe CRM will automatically send you a reminder once a day, starting a day before the due date, and again an hour before. Reminders come in as both an in-app notification and an email, so nothing slips through.

![](/files/imagefcbd91.png)
*Task reminder send via Email*

<!-- page: crm/crm__twilio.md -->
---
title: "Twilio"
space: "CRM"
url: "https://docs.frappe.io/crm/twilio"
updated: "2026-02-05"
---

Twilio is a cloud communications platform that allows businesses to integrate voice, video, messaging, and authentication functionalities into their applications. This integration enables you to make calls directly from various pages within the CRM.

## Make call

- **Lead page:** A call button is available in the right section above lead details. Use this button to initiate a call, but ensure the **Mobile No** field in the **Person** section includes the country code.
  ![](/files/PBAkpiy.png)
- **Deal page:** In the **Contacts** section on the right side. You can add multiple contacts and designate a primary contact. The call button will utilize the primary contact's number.  
  ![](/files/LKceTy6066660.png)
- **Contact page:** Directly initiate a call by clicking the **Mobile No** displayed below the contact's name.  
  ![](/files/9YnXfPgc03eb0.png)

## Call pop-up

Upon making or receiving a call, a pop-up window appears displaying:

- Caller name
- Mobile number
- Call status
- Call duration
- Mute button
- Note button
- Action buttons (Accept, Reject, Cancel Call)

![](/files/0YK8bE59c3b83.png)

This window can be minimized, allowing navigation to other screens, while remaining accessible in the far-right corner of the navbar.  

![](/files/wVW5MoF.png)

## Take notes during a call

While on a call, you can take notes using the note button. These notes are saved in the Call Log for later viewing and editing.  

![](/files/tB05yerf82d8d.png)

## Twilio setup

To configure Twilio for use within the CRM, follow these steps:

1. **Twilio Subscription:** Obtain an active Twilio subscription (refer to Twilio's documentation for details).
2. **Twilio Credentials:** From your Twilio account, retrieve your Account SID, Auth Token, and Twilio Mobile Number.
3. **Settings**: Click the dropdown menu on the top left logo and select "Settings."
  ![](/files/LHGhoZR.png)
4. **Telephony Settings:** Navigate to Telephony Settings, enable Twilio and add your Account SID and Auth Token. You can also enable call recording at this point.
  ![](/files/Screenshot%202025-01-20%20at%207.51.35%E2%80%AFPM.png)
5. **Telephony Agent:** Go to Telephony Agent (In Desk) and add users (agents) with Twilio mobile numbers designated for making calls.
  Make sure the Twilio number added does not contain spaces and special characters (it can still have + at the start)  
  ![](/files/Screenshot%202025-01-20%20at%207.55.01%E2%80%AFPM.png)

## Twilio API configuration

For your CRM's API to connect with Twilio, perform the following configurations within Twilio:

1. **Incoming Call API URL:** Under **Phone Numbers** > **Manage** > **Active Numbers**, select your mobile number. Locate the **Voice Configuration** form and within the "**A call comes in**" section, add the following **URL** to the URL field:
  ```
    "https://<yoursitename>/api/method/crm.integrations.twilio.api.twilio_incoming_call_handler"
  ```
  ![](/files/HB0TwYk.png)
    This URL is responsible for handling incoming calls.
2. **Outgoing Call API URL:** Navigate to **Phone Numbers** > **Manage** > **TwiML apps** and select your app. In the **Voice Configuration** > **Request URL** field, enter the following URL:
  ```
    "https://<yoursitename>/api/method/crm.integrations.twilio.api.voice"
  ```
  ![](/files/IVSDMAF.png)
    This URL is used for making outbound calls.

:::note
Please refer to Twilio's official guide for any additional Twilio configuration requirements.
:::

<!-- page: crm/crm__view.md -->
---
title: "Saved View"
space: "CRM"
url: "https://docs.frappe.io/crm/view"
updated: "2026-05-21"
---

Saved Views help you personalize list views by saving your preferred filters, sorting, and columns. This allows you to quickly access frequently used lists and data configurations without setting them up each time. You can also consider them as reports.

## What are Views?

A View is a combination of:

- **Filters:** Show records that match specific conditions.
- **Sorting:** Arrange the data in a particular order (ascending, descending, etc.) 
- **Columns:** Choose which fields are visible in the list view.

> **Important Note:** Saved Views are personal by default and only visible to the user who created them. We'll discuss making views public in the next page.

## How to create a View

There are two ways to create a view:

**1. Default View:** You can add filters, sorting, and columns by clicking on **+Add** (as shown in the video below).

![](/files/DefaultView.mp4)







- Any changes you make to the default list view, such as applying filters, sorting, or adding/removing columns, are automatically saved.
- When you return to the list view, your personalized configuration will be retained.

**2. Creating a Named View:** 

![](/files/Untitled designca1a07.gif)

1. Apply your desired filters, sorting, and column selections.
2. Click the **List** view in the header, then click **+Create View.**
3. Give your Saved View a descriptive name, then click **Create.**

Your newly created Saved View will be accessible from the list view dropdown menu.

## Saved View Actions

The three-dot menu (...) on a Saved View provides additional actions:

- **Duplicate**: Make a copy of the saved view.
- **Edit:** Modify the name and set a custom icon for your saved view.
- **Pin View** (covered on next page): Pin the saved view in the sidebar.
- **Make Public** (covered on next page): Share your saved view with other users. It will be accessible to all users.
- **Delete:** Remove the Saved View from the list.

<!-- page: crm/crm__whatsapp.md -->
---
title: "WhatsApp"
space: "CRM"
url: "https://docs.frappe.io/crm/whatsapp"
updated: "2026-03-09"
---

WhatsApp integration allows you to send and receive WhatsApp messages from within the lead and deal pages in Frappe CRM. This streamlines communication and keeps all interaction history centralised for better customer relationship management.

![wiki-hero2](https://frappe.io/files/CRMWhatsApp.png)



A dedicated WhatsApp tab is available on both Lead and Deal pages, providing a real-time chat window for efficient communication.

- **Lead:** The mobile number field of a Lead is used to initiate and receive WhatsApp messages.
- **Deal:** The primary contact number associated with a Deal is used for WhatsApp communication.

## Installation

WhatsApp integration requires a separate app called "Frappe WhatsApp" developed by [Shridhar](https://github.com/shridarpatil/frappe_whatsapp/commits?author=shridarpatil).

- **Frappe Cloud Marketplace:** The app is available on the Frappe Cloud marketplace for easy installation.  
  ![](/files/kB9ij9C.png)
- **Manual Installation:** Clone the app's repository from Github: [[https://github.com/shridarpatil/frappe_whatsapp](https://github.com/shridarpatil/frappe_whatsapp)]

## Configuration Steps

To enable WhatsApp integration in Frappe CRM, follow these steps:

1. **Obtain WhatsApp Business Credentials:** Refer to the official WhatsApp guide for creating a WhatsApp Business account and acquiring the necessary credentials [WhatsApp Business Account Creation Guide](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started).
  ![](/files/Bq2cxlF.png)
2. **Configure WhatsApp Settings:**
  ![](/files/aN42xJe.png)
   Click the dropdown menu on the top left logo and select "Settings."  
   Locate the **WhatsApp Settings**.  
   Enter the credentials obtained in step 1.  
   Enable the WhatsApp integration.
3. **Set up the Webhook:**
  ![](/files/RyzN5w3.png)
    A webhook URL is required to establish communication between Frappe CRM and WhatsApp Business. Use the following URL format, replacing `<yoursitename>` with your actual Frappe CRM site name and including the **Webhook Verify Token** you created in the **WhatsApp Settings** in **Verify token** field
    
  ![](/files/YWmf85N.png)
4. **Subscribe to webhook fields**:
  Subscribe all webhook fields (recommended - whatsapp docs) but atleast subscribe to `messages` &amp; `message_template_status_update`
    
  ![](/files/Screenshot%202025-03-05%20at%202.18.24%E2%80%AFPM.png)

## Creating WhatsApp Templates

To ensure compliance and streamline communication, Frappe CRM utilizes WhatsApp templates. These pre-approved messages can be created and managed within the system.

![](/files/vWv1LiQ.png)

![](/files/mNauYNf.png)



1. Navigate to the **WhatsApp Templates** DocType.
2. Click on **Add WhatsApp Template**.
3. Fill in the required details for your template message.
4. Save the template.

With these configurations in place, you're ready to leverage WhatsApp Business for efficient communication with your leads and deal contacts directly within Frappe CRM.

> **Important Note:** Due to WhatsApp Business limitations, you can only initiate communication by sending a pre-approved WhatsApp template. You can only send regular messages after receiving a reply from the customer.
