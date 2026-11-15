<!-- Frappe documentation: crm, part 1 of 3. Index: docs/INDEX.md -->

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
