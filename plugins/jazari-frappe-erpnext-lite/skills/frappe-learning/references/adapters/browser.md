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

- **The Path line is the checked one.** Lines marked *checked on v16.55* were matched against a live v16 Desk (which lives at `/desk`; old `/app` links redirect there). When a numbered step names a different menu ("Go to Accounting > …"), that is the documentation's older menu: follow the Path line, then continue from the next step.
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
- **Path (checked on v16.55 with the app installed):** https://your-site/lms → **Courses** in the sidebar → **New Course**
- **On this screen:** On a first visit Frappe Learning asks how you heard about it; choose **Skip for now**.
- **Documented steps:**
  1. Using the Learning Portal
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning-01.md` lines 796–917  (https://docs.frappe.io/learning/create-a-course)

### Add chapters and lessons
- **Path (checked on v16.55 with the app installed):** https://your-site/lms → **Courses** → open the course → **Add Chapter**
- **Documented steps:**
  1. Inside your Course, click the + Add button on the right side of the screen
  2. Enter the Title for your chapter
  3. Click Create to save. You can now start adding lessons to this chapter
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning-01.md` lines 3–62  (https://docs.frappe.io/learning/add-a-chapter)

### Run a batch of learners
- **Path (checked on v16.55 with the app installed):** https://your-site/lms → **Batches** in the sidebar
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning-01.md` lines 702–794  (https://docs.frappe.io/learning/create-a-batch)

### Host a live class
- **Path (checked on v16.55 with the app installed):** https://your-site/lms → **Batches** → open the batch → **Live Class**. It needs Zoom or Google Meet set up first, under your name → **Settings**
- **Documented steps:**
  1. Go to Settings - > Google Meet - > + New
  2. Enter your details in the modal
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning-01.md` lines 919–979  (https://docs.frappe.io/learning/create-a-live-class)

### Assess learners with quizzes
- **Path (checked on v16.55 with the app installed):** https://your-site/lms → **Quizzes** in the sidebar
- **Documented steps:**
  1. Click the + Create button
  2. In the form that appears, enter the Title of the quiz and click Save
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning-01.md` lines 1503–1560  (https://docs.frappe.io/learning/quizzes)

### Set assignments
- **Path (checked on v16.55 with the app installed):** https://your-site/lms → **Assignments** in the sidebar
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning-01.md` lines 156–187  (https://docs.frappe.io/learning/assignments)

### Issue certificates
- **Path (checked on v16.55 with the app installed):** https://your-site/lms → **Certifications** in the sidebar
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/learning/learning-01.md` lines 1335–1355  (https://docs.frappe.io/learning/issue-a-certificate)

### Group courses into a program
- **Path (checked on v16.55 with the app installed):** https://your-site/lms → **Programs** in the sidebar
- **Not checked on a live site:** the Education app was not on the test site; this path is the documentation's.
- **Documented steps:**
  1. Navigate to the Programs section
  2. Click on the + New button
  3. Enter a Title for your Program
  4. Add Courses to the Program
  5. Check the Enable Course Order option only if you want to enforece the order
  6. You can also publish the program from here now or at any later point
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning-01.md` lines 64–110  (https://docs.frappe.io/learning/add-a-program)

### Charge for a course
- **Path:** open https://your-site/lms → **Payment Gateway** in the sidebar
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/learning/learning-01.md` lines 1594–1621  (https://docs.frappe.io/learning/setting-up-payment-gateway)

### Enrol students
- **Path:** https://your-site/app → **Home > Education > Student > Student**
- **Not checked on a live site:** the Education app was not on the test site; this path is the documentation's.
- **Record type:** Student
- **Documented steps:**
  1. Go to the student list and click on New
  2. Enter the First Name, Middle Name and Last Name of the student
  3. Enter other details like Student Email Address, User ID(If Applicable) and Joining Date
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/education/education-01.md` lines 1962–2062  (https://docs.frappe.io/education/student)

### Set up programs and courses
- **Path:** https://your-site/app → **Home > Education > Masters > Program**
- **Not checked on a live site:** the Education app was not on the test site; this path is the documentation's.
- **Record type:** Program
- **Documented steps:**
  1. Go to the Program list and click on New
  2. Enter the Program Name and the Program Abbreviation
  3. Select the Department for the Program
  4. Select and add the courses within the Program
  5. Save
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/education/education-01.md` lines 1321–1383  (https://docs.frappe.io/education/program)

### Collect fees
- **Path:** https://your-site/app → **Home > Education > Fees > Fees**
- **Not checked on a live site:** the Education app was not on the test site; this path is the documentation's.
- **Record type:** Fees
- **Documented steps:**
  1. Go to the Fees list and click on New
  2. The Institution will be selected by default, which is editable, if required
  3. Select and add the Student for whom the Fees record is being made. The name of the student will be fetched simultaneously
  4. Add the Due Date of the payment of the Fees
  5. Save
- **Snapshot first** — reversibility: irreversible
- **Full page, bundled offline:** `docs/education/education-01.md` lines 848–960  (https://docs.frappe.io/education/fees)

### Run assessments
- **Path:** open https://your-site/app (the Desk) and find *Assessment* — the documentation page below shows the screen
- **Not checked on a live site:** the Education app was not on the test site; this path is the documentation's.
- **Snapshot first** — reversibility: reversible
- **Full page, bundled offline:** `docs/education/education-01.md` lines 86–105  (https://docs.frappe.io/education/assessment-introduction)

