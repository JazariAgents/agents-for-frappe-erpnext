# Interface adapter — Courses and students

## Contents

- which interface each capability lives in
- ground rules
- where each action lives, step by step
- what cannot be done in the interface

Everything in this file can be done by a person clicking, with no API key. Most of it can also be done
through the API — see `api.md`. The two are alternatives, not a split of the work.

## Which interface

| Open | Which product |
|---|---|
| `https://your-site/app` | the Desk |
| `https://your-site/lms` | the Frappe Learning portal |

Frappe's apps do not share one interface. The Desk (`/app`) has the awesomebar — the search box at the
top — where typing a DocType name jumps straight to its list. Frappe CRM, Helpdesk, Insights, Learning,
Drive, Wiki, Builder and Studio are separate single-page apps with their own left sidebar and no awesomebar.
Frappe Cloud is a different site entirely. Use the base that matches the capability's row.

## Ground rules

- **Verify the label on screen before clicking.** These paths come from Frappe's documentation as it stood
  on 2026-08-31. Interfaces move. If the screen does not match, say so instead of clicking something similar.
- Ask before each change on a live system, and never type the user's password.
- **The numbered steps are the page's main procedure, not the whole page.** Prerequisites, options, and follow-on sections such as saving and submitting are in the bundled page — read it before acting.
- Where a row gives a sidebar item rather than a menu path, that is what the documentation published —
  open the product, use that sidebar entry, and follow the linked page.
- Where a row has no path at all, open the product at its base URL and follow the documentation link.
  Do not invent a menu that might not exist.

## Where each action lives

### Create a course
- **Path:** open https://your-site/lms (the Frappe Learning portal) and find *Create a Course* — the documentation page below shows the screen
- **Documented steps:**
  1. Using the Learning Portal
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning__create-a-course.md`  (https://docs.frappe.io/learning/create-a-course)

### Add chapters and lessons
- **Path:** open https://your-site/lms (the Frappe Learning portal) and find *Add a Chapter* — the documentation page below shows the screen
- **Documented steps:**
  1. Inside your Course, click the + Add button on the right side of the screen
  2. Enter the Title for your chapter
  3. Click Create to save. You can now start adding lessons to this chapter
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning__add-a-chapter.md`  (https://docs.frappe.io/learning/add-a-chapter)

### Run a batch of learners
- **Path:** open https://your-site/lms (the Frappe Learning portal) and find *Create a Batch* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning__create-a-batch.md`  (https://docs.frappe.io/learning/create-a-batch)

### Host a live class
- **Path:** open https://your-site/lms (the Frappe Learning portal) and find *Create a Live Class* — the documentation page below shows the screen
- **Documented steps:**
  1. Go to Settings - > Google Meet - > + New
  2. Enter your details in the modal
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning__create-a-live-class.md`  (https://docs.frappe.io/learning/create-a-live-class)

### Assess learners with quizzes
- **Path:** open https://your-site/lms (the Frappe Learning portal) and find *Quizzes* — the documentation page below shows the screen
- **Documented steps:**
  1. Click the + Create button
  2. In the form that appears, enter the Title of the quiz and click Save
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning__quizzes.md`  (https://docs.frappe.io/learning/quizzes)

### Set assignments
- **Path:** open https://your-site/lms (the Frappe Learning portal) and find *Assignments* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning__assignments.md`  (https://docs.frappe.io/learning/assignments)

### Issue certificates
- **Path:** open https://your-site/lms (the Frappe Learning portal) and find *Issue a Certificate* — the documentation page below shows the screen
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/learning/learning__issue-a-certificate.md`  (https://docs.frappe.io/learning/issue-a-certificate)

### Group courses into a program
- **Path:** open https://your-site/lms (the Frappe Learning portal) and find *Add a Program* — the documentation page below shows the screen
- **Documented steps:**
  1. Navigate to the Programs section
  2. Click on the + New button
  3. Enter a Title for your Program
  4. Add Courses to the Program
  5. Check the Enable Course Order option only if you want to enforece the order
  6. You can also publish the program from here now or at any later point
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning__add-a-program.md`  (https://docs.frappe.io/learning/add-a-program)

### Charge for a course
- **Path:** open https://your-site/lms → **Payment Gateway** in the sidebar
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning__setting-up-payment-gateway.md`  (https://docs.frappe.io/learning/setting-up-payment-gateway)

### Enrol students
- **Path:** https://your-site/app → **Home > Education > Student > Student**
- **Record type:** Student
- **Documented steps:**
  1. Go to the student list and click on New
  2. Enter the First Name, Middle Name and Last Name of the student
  3. Enter other details like Student Email Address, User ID(If Applicable) and Joining Date
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/education/education__student.md`  (https://docs.frappe.io/education/student)

### Set up programs and courses
- **Path:** https://your-site/app → **Home > Education > Masters > Program**
- **Record type:** Program
- **Documented steps:**
  1. Go to the Program list and click on New
  2. Enter the Program Name and the Program Abbreviation
  3. Select the Department for the Program
  4. Select and add the courses within the Program
  5. Save
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/education/education__program.md`  (https://docs.frappe.io/education/program)

### Collect fees
- **Path:** https://your-site/app → **Home > Education > Fees > Fees**
- **Record type:** Fees
- **Documented steps:**
  1. Go to the Fees list and click on New
  2. The Institution will be selected by default, which is editable, if required
  3. Select and add the Student for whom the Fees record is being made. The name of the student will be fetched simultaneously
  4. Add the Due Date of the payment of the Fees
  5. Save
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/education/education__fees.md`  (https://docs.frappe.io/education/fees)

### Run assessments
- **Path:** open https://your-site/app (the Desk) and find *Assessment* — the documentation page below shows the screen
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/education/education__assessment-introduction.md`  (https://docs.frappe.io/education/assessment-introduction)

