<!-- Frappe documentation: learning, part 1 of 2. Index: docs/INDEX.md -->

<!-- page: learning/learning__add-a-chapter.md -->
---
title: "Add a Chapter\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "Learning"
url: "https://docs.frappe.io/learning/add-a-chapter"
updated: "2026-05-12"
---

**A chapter** forms the second layer in the hierarchy. It is used to group lessons that belong to the same topic. You can upload [SCORM](https://scorm.com/scorm-explained/one-minute-scorm-overview/) (Sharable Content Object Reference Model) as chapters in Frappe Learning if you are migrating content from other LMS platforms.

---

## Types of Chapters

In Frappe Learning, you can create two types of chapters:

- **Chapter with Lesson content**
- **SCORM Chapters**

---

### Chapter with Lesson Content

This is the standard chapter used to group individual lessons.

1. Inside your Course, click the `+ Add` button on the right side of the screen.

![](https://docs.frappe.io/files/Screenshot%202026-02-23%20at%2011.08.53%E2%80%AFAM.png)
*Add Chapter Modal *

2. Enter the `Title` for your chapter.
3. Click `Create` to save. You can now start adding lessons to this chapter.

---

### SCORM Chapter

:::caution
SCORM packages typically include HTML and JavaScript that run with the user's session, which introduces inherent security risks from scripted content. This can't be fully mitigated for the Course Creator role, as session access is required for SCORM to function.
:::



Use this option if you have an existing SCORM Chapter you wish to add.

1. Click the `+ Add` button.
2. Toggle the `SCORM Package` switch.
3. Enter your `Title` and upload your **SCORM ZIP file**.

![](https://docs.frappe.io/files/Screenshot%202026-02-23%20at%2011.14.44%E2%80%AFAM.png)
*Uploading SCORM Chapter *

4. Click `Create` and visit your chapter to see it.

![](https://docs.frappe.io/files/Screenshot%202026-02-23%20at%2011.14.26%E2%80%AFAM.png)
*SCORM Chapter View *

:::note
In SCORM Chapters, you cannot add individual lessons; the uploaded package serves as the entire content for that chapter.
:::

<!-- page: learning/learning__add-a-program.md -->
---
title: "Add a Program"
space: "Learning"
url: "https://docs.frappe.io/learning/add-a-program"
updated: "2026-02-24"
---

### Learning Paths

Learning Paths allow instructors to group multiple courses into structured Programs. This makes it easier for students to follow a guided sequence of courses and track their overall progress.

### Creating a Program

1. Navigate to the Programs section.
2. Click on the **+ New** button.
3. Enter a Title for your Program.
4. Add Courses to the Program.
5. Check the Enable Course Order option only if you want to enforece the order
6. You can also publish the program from here now or at any later point.

![](/files/programmoderator.mp4)



### Managing Enrollment

There are two ways students can join Programs:

1. Published Programs: Students can view the Program, enroll themselves, and progress through its courses.
2. Private Programs: Instructors can manually enroll selected students without making the Program public.

### Student Experience

1. Students will see a Programs list they are enrolled in or other that are published.
2. Each Program displays its courses in sequence.
3. Students can click on a course to enroll and begin learning.
4. If Enforce Course Order is enabled, students must complete one course before moving to the next.
5. Progress is tracked and displayed on the Program page.

![](/files/program details.mp4)



### Tracking Progress

Instructors can view a Progress Summary for the Programs, giving them insight into student engagement and completion rates.

<!-- page: learning/learning__assessments__programming-exercise.md -->
---
title: "Programming Exercises"
space: "Learning"
url: "https://docs.frappe.io/learning/assessments/programming-exercise"
updated: "2026-02-24"
---

In Frappe Learning, Programming Exercises allow you to test a student's coding skills in a live, auto-graded environment. These can be integrated into your courses to provide hands-on practice.

---

## Creating a Programming Exercise

To manage your exercises, click on the **Programming Exercises** section in the sidebar to access the exercise list.

1. **Start Creation:** Click the `+ Create` button.
2. **Basic Info:** Enter a `Title` for the exercise and click `Save`.

![](https://docs.frappe.io/files/Screenshot 2026-02-24 at 12.41.50 AM.png)

3. **Configuration:** After saving, you can define the technical parameters:

- **Language:** Select the programming language (e.g., Python).
- **Problem Statement:** Use the text editor to provide the problem statement and requirements.
- **Test Cases:** Give Input and Expected Output for the tests to run.

---

## The Student Environment

When a student opens a Programming Exercise, they are presented with an in-browser code editor.

![](https://docs.frappe.io/files/Screenshot 2026-02-24 at 12.48.04 AM.png)

1. **Writing Code:** Students write their solution directly in the portal.
2. **Running Tests:** Students can click `Run` to see how their code performs against the test cases.

---

## Reviewing Submissions

Instructors can access the `Submission List` from the top of the Programming Exercise form.

<!-- page: learning/learning__assignments.md -->
---
title: "Assignments\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "Learning"
url: "https://docs.frappe.io/learning/assignments"
updated: "2026-02-24"
---

In Frappe Learning, you can add assignments to both courses and batches.

Click on the Assignments section on the sidebar. You now see the Assignment List. From here, you can either edit an existing assignment or create a new one.

![](/files/Screenshot%202025-02-07%20at%204.54.53%E2%80%AFPM.png)

## Creating an Assignment

To create a new assignment, click on the **+ Create** button. In the form that opens up, enter the following information.

1. **Title:** Give a title to the assignment.
2. **Type:** Select the type of assignment. You can choose from PDF, Image, Document, URL and Text. The type you select will determine the kind of submission students can make.
3. **Question:** Enter the question for the assignment.

Once you have entered all the information, click on the Save button to save the assignment.

![](/files/Screenshot%202025-02-07%20at%204.55.06%E2%80%AFPM.png)

### Grading an Assignment

On top of the Assignment form, you will see a button called Submission List. It opens up all the submissions for the assignment.  
When you open a submission, you see the question and the attachment/answer that the student submitted for it. You can grade the submission as either Pass or Fail. You can also leave some comments which the students get to see.

![](/files/Screenshot%202025-02-07%20at%204.55.36%E2%80%AFPM.png)

<!-- page: learning/learning__badges.md -->
---
title: "Badges\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "Learning"
url: "https://docs.frappe.io/learning/badges"
updated: "2026-02-24"
---

Admins can create badges with rules in the learning system. When a user completes the actions defined in the rules the badge gets assigned to them.

There are 3 types of events on which badges get assigned to learners. Let us understand them with examples.

### Assign a badge when a learner completes a quiz

You can assign a badge to learners when they complete a quiz. Each time a learner submits a quiz, a new record gets created under LMS Quiz Submission. So this is your event to assign the badge.

![Screenshot 2024-06-06 at 5.32.27 PM](/files/Screenshot 2024-06-06 at 5.32.27 PM.png)



So when creating a badge for this, you enter a title and description for the badge. You also attach the badge image.

Then you select the Event as **New** and select the DocType on which this rule applies. As this badge would be assigned on quiz submission, you select the DocType as LMS Quiz Submission.

You can also add a specific condition to it. For example, we want the badge to be assigned only if the learner gets 100% correct answers for a quiz.

Then you select the user who should receive this badge. In most DocTypes of Learning, the learner is scored in a field called Member. The same is true for quiz submission. So we select the user as **Member**.

Once you have entered all this information you save the document. Now each time a learner submits a quiz and scores 100% they would be assigned this badge.

If you want this badge to be assigned to the learner only once and not each time they submit the quiz, you enabled the option **Grant only once**.

### Assign a badge when the user completes a course

To create this badge the rules would be a bit different. When a student enrolls for a course, a new entry gets created in the LMS Enrollment doctype. Then each time they make progress in that course, the progress percentage gets updated in the same document. So you should select **LMS Enrollment** as the Reference Document Type and the event will be **Value Changed**.

The User Field would be **Member** and the Field To Check would be **progress**.

Then we need to apply a condition to check if the course is completed or not which is indicated by progress percentage. So we add this as the condition **doc.progress == float("100.0")**.

You can then add a relevant title and image and enable the badge to start using it.

![](/files/Screenshot%202025-02-06%20at%203.22.47%E2%80%AFPM.png)

### Assign a badge when a student completes a training

Trainings are done with the help of Batches. As such there is no progress tracking for an individual batch, such badges can be auto assigned. 

So select the Event as **Auto Assign**. Reference Document Type would be **Batch Student** as this is the child table where the students of a batch are stored. User Field would be **Student**. 

For condition we need to tell it which batch do these students belong to. For this we enter condition as a json where we specify the batch name as parent.

**{**  
    **"parent": "CLS-03050"**  
**}**



![](/files/Screenshot%202025-02-06%20at%203.22.54%E2%80%AFPM.png)

<!-- page: learning/learning__basic-settings__branding.md -->
---
title: "Branding and Customization"
space: "Learning"
url: "https://docs.frappe.io/learning/basic-settings/branding"
updated: "2026-02-25"
---

You can tailor the portal’s appearance to match your brand identity through the **LMS Settings**.

## Visual Branding

Navigate to `Settings` and then go to `Branding` in the Settings Sidebar to update:

- **Brand Name:** The name displayed in the sidebar heading.
- **Logo & Favicon:** Upload your organization's logo for the sidebar and the favicon for browser tabs.

![](/files/Screenshot 2026-02-24 at 1.29.55 AM.png)
*Branding Section in Settings*

---

## Sidebar Customization

- **Menu Links:** In `Settings` > `Sidebar`, you can toggle which default links appear in the sidebar.
- **Custom Links:** In `Sidebar`, Use the `More` button configuration to add other website links.

<!-- page: learning/learning__basic-settings__navigating-learning-portal.md -->
---
title: "Navigating the Learning Portal"
space: "Learning"
url: "https://docs.frappe.io/learning/basic-settings/navigating-learning-portal"
updated: "2026-05-06"
---

Frappe Learning operates across two distinct interfaces to separate student-facing content from administrative backend tasks.

1. **The Learning Portal:** The primary student and instructor-facing website where learning and content creation happen.
2. **The Desk:** The administrative backend.

---

## Interface Access & Switching

You can jump between these two environments at any time:

- **To Portal:** Click the `Learning` icon on your Desk Dashboard, or navigate to your base URL (default is `/lms`).
- **To Desk:** Click on your `User Profile Icon` **>** `Apps` **>** `Desk`. Alternatively, go to `/desk` URL.

:::note
All basic functionalities are available in the Learning Portal, which is where you will be spending most of your time.
:::







---

## Navigating Learning Portal

- **The Sidebar:** Located on the left, this contains quick links to Courses, Programs, and Batches.
- **Instructor/Student Toggle:** Located at the top of the homepage. This allows creators to preview exactly how content appears to a learner.
- **User Menu:** Click your avatar to access Theme Settings (Light/Dark mode), Account Settings, etc.
- **Help Center:** Click on the help icon on bottom center of your sidebar. This will take you to `Getting Started` wizard if it is incomplete or to `Help Center` if that is done.

![](/files/Screenshot 2026-02-24 at 1.06.14 AM.png)

<!-- page: learning/learning__core-concepts__courses.md -->
---
title: "Learning Hierarchy"
space: "Learning"
url: "https://docs.frappe.io/learning/core-concepts/courses"
updated: "2026-02-25"
---

This is the structure that a course in Frappe Learning follows. A course contains chapters. Chapters contain lessons.

![Screenshot 2024-05-16 at 4.03.52 PM](/files/Screenshot 2024-05-16 at 4.03.52 PM831306.png)
*Structure of Courses, Chapters and Lessons in Frappe Learning*

<!-- page: learning/learning__course-creation__add-a-preview-video.md -->
---
title: "Add a Preview Video"
space: "Learning"
url: "https://docs.frappe.io/learning/course-creation/add-a-preview-video"
updated: "2026-02-25"
---

A preview video acts as a teaser for guest users.

1. In the Course form, locate the `Preview Video` field.
2. To use a YouTube video: Go to YouTube, click the `Share` button under the video, and copy the link provided.
  ![](https://docs.frappe.io/files/Screenshot 2026-02-23 at 10.53.10 AM.png)
3. Paste the link into the field.

![](/files/Screenshot 2026-02-23 at 11.05.29 AM.png)
*Course Fields*

4. This video will appear on the Course landing page, allowing users to watch it before they enroll.
  ![](/files/Screenshot 2026-02-23 at 11.06.06 AM.png)
  *Course Preview*

<!-- page: learning/learning__course-creation__adding-a-lesson__add-interactive-content.md -->
---
title: "Interactive Content"
space: "Learning"
url: "https://docs.frappe.io/learning/course-creation/adding-a-lesson/add-interactive-content"
updated: "2026-04-08"
---

Make your lessons more engaging by adding interactive assessments and development environments.

You can add the following interactive content in Frappe Learning:

1. Quizzes
2. Assignments
3. Programming Exercises
4. CodeSandBox

---

## Quizzes

Quizzes serve as knowledge checks. You can add a quiz block to any lesson to ensure learners have understood the material before moving forward.

To add a Quiz:

1. Hover over the lesson content
2. Click the `+` icon to open the block menu
3. Select the `Quiz` block from the menu.
4. Search for and select a quiz you have already created in Learning.

![](/files/Screenshot 2026-02-24 at 12.48.14 PM.png)

---

## Assignments

Assignments are used to evaluate learners through longer-form tasks such as essays, projects, or file submissions.

To add an Assignment:

1. Hover over the lesson content
2. Click the `+` icon to open the block menu
3. Select the `Assignment` block
4. Search for and choose an assignment you have already created in Learning

![](/files/Screenshot 2026-02-24 at 1.49.15 PM.png)

---

## Programming Exercises

Programming Exercises allow learners to practice coding concepts directly within a lesson.

To add a Programming Exercise:

1. Hover over the lesson content
2. Click the `+` icon to open the block menu
3. Select the `Programming Exercise` block
4. Search for and select a programming exercise you have already created in Learning

![](/files/Screenshot 2026-02-24 at 1.49.55 PM.png)

---

## CodeSandBox

For technical and programming courses, you can embed a live IDE directly into the lesson.

To add a CodeSandBox:

1. Go to your sandbox on [CodeSandbox.io](https://CodeSandbox.io).
2. Copy the URL of your sandbox.
3. Paste it in the Lesson Editor.
4. Learners will be able to view and interact with the code without leaving the course.
5. They can also open a sandbox in CodeSandbox by clicking on `Open Sandbox`**.**

![](/files/Screenshot 2026-02-24 at 12.52.05 PM.png)

<!-- page: learning/learning__course-creation__adding-a-lesson__add-video-content.md -->
---
title: "Video Integration (Cloudflare, Vimeo, YouTube, etc.)"
space: "Learning"
url: "https://docs.frappe.io/learning/course-creation/adding-a-lesson/add-video-content"
updated: "2026-04-08"
---

Frappe Learning allows you to embed videos in lessons using popular video hosting platforms. You don’t need to upload videos directly into Frappe Learning, simply **copy the video URL** from your preferred provider and **paste it into the Lesson Editor**.

Frappe Learning automatically detects the video source and embeds it for learners.

---

## Supported Video Platforms

### 1. YouTube

YouTube videos can be embedded using the standard watch URL.

#### Supported URL format

```
https://www.youtube.com/watch?v=<video-id>
```

#### Example

```
https://www.youtube.com/watch?v=SLNSSz41v_o
```

---

### 2. Vimeo

Vimeo videos are supported using the video URL.

#### Supported URL format

```
https://vimeo.com/<video-id>
```

#### Example

```
https://vimeo.com/825334862
```

---

### 3. Cloudflare Stream

Cloudflare Stream provides secure video hosting with adaptive streaming.

#### Supported URL format

```
https://customer-<account-id>.cloudflarestream.com/<video-id>/watch
```

#### Example

```
https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/watch
```

---

### 4. Bunny Stream

Bunny Stream allows fast, global video delivery with built-in analytics.

#### Supported URL format

```
https://iframe.mediadelivery.net/play/<library-id>/<video-id>
```

#### Example

```
https://iframe.mediadelivery.net/play/579970/54b3e5a1-cf95-4f88-96d3-8387d93dc2f2
```

---

## Important Notes

- Paste **only the video URL**, not iframe embed code
- The URL must match one of the supported formats above
- Video privacy, access control, and streaming limits are managed by the video provider

<!-- page: learning/learning__course-creation__adding-a-lesson__adding-google-content.md -->
---
title: "Embedding Google Workspace (Docs, Sheets, Slides)"
space: "Learning"
url: "https://docs.frappe.io/learning/course-creation/adding-a-lesson/adding-google-content"
updated: "2026-02-24"
---

You can integrate live Google Docs, Sheets, and Slides into your lessons to provide dynamic, up-to-date documentation and presentations.

### How to Embed Google Workspace Files

1. Open your Google Doc, Sheet, or Slide.
2. Make sure your permissions are set properly (`File` > `Share` > `Share With Others`).
  ![](/files/Screenshot 2026-02-23 at 2.38.05 PM.png)
  *Permission Manager in Google*
3. Copy your URL from the top browser address bar.

![](/files/Screenshot 2026-02-23 at 2.34.07 PM.png)
*Google Docs*

4. Now paste it in your lesson.
  ![](/files/Screenshot 2026-02-23 at 2.40.59 PM.png)
  *Document rendered in lesson.*

---

### Integration Options

- **Google Slides:** Perfect for presentations. These render with full navigation controls for the student.
- **Google Sheets:** Useful for sharing live data tables or interactive calculators.
- **Google Docs:** Best for course handouts, reading material, or live-updating documentation.

<!-- page: learning/learning__course-creation__adding-a-lesson__adding-simple-content.md -->
---
title: "Add a Lesson"
space: "Learning"
url: "https://docs.frappe.io/learning/course-creation/adding-a-lesson/adding-simple-content"
updated: "2026-02-25"
---

The main content of a course resides in the **lesson**. A lesson can have various kinds of content ranging from documents to images to videos from Youtube, Vimeo, etc. We can also put quizzes or assignments to make them more interactive!

---

## Create a Lesson

1. Navigate to the **Course** you want to edit.
2. Locate the **Chapter** where you want to add content.
3. Click the `Add Lesson` button within that chapter.

![](/files/Screenshot 2026-02-23 at 12.26.55 PM.png)
*Course Settings*

4. You will be taken to the Lesson editor to add your content. Add your content here.

![](/files/Screenshot 2026-02-23 at 12.30.45 PM.png)
*Lesson Editor*

5. Enter your lesson [details](#lesson-fields-reference).

---

## Types of Lesson Content

Frappe Learning allows you to mix and match different media and tools to create a rich learning experience. By default, the type of content is text. 

Choose from the following options to build your lesson:

- **Text:** Enter any text content. This is the default block type.
- **Heading:** Add various heading levels to structure your lesson.
- **Quiz:** Add quizzes you have previously created. These act as progression gates for the learner.
- **Assignment:** Link to an assignment where students can submit files (PDF, Image, Document) or URLs for instructor review.
- **Programming Exercises:** Embed auto-graded coding tasks where students write and test code directly in the browser.
- **Upload:** Directly upload images, videos, PDFs, and audio files to be rendered within the lesson.
- **Google Slides:** Make sure it is not view restrited and simply copy the link and paste it to render the presentation.
- **Google Sheets & Docs:** Similar to Slides, use the link to embed live spreadsheets or documents.
- **Video Hosting:** Integrate videos hosted on external services like YouTube, Vimeo, Cloudflare Stream, or BunnyStream.
- **CodeSandBox:** Embed live coding environments for technical or programming lessons.

:::caution
The visibility of your embedded media (Google Docs, Videos, etc.) depends on the sharing permissions you have set on those specific external platforms.
:::









---

## Lesson Fields Reference


| Field                  | Description                                                                                                                                                                                                                                                                                                                                  | Mandatory |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| **Title**              | The name of the lesson (e.g., "Installing Python").                                                                                                                                                                                                                                                                                          | ✅         |
| **Content**            | The rich-text editor for text, images, and embedded media. When you hover on the editor, a **+** icon will appear at the left of it. Click on the icon to open the lesson menu. You can select the type of content you want to add from the menu.                                                                                            | ❌         |
| **Include in Preview** | If you want Guest users to be able to see this lesson without enrolling for the course, you can enable this option.                                                                                                                                                                                                                          | ❌         |
| **Instructor Notes**   | If there is some content that you want to share only with the instructors and moderators of the system, and don't want learners to see it, you can add such content here. These notes will only be visible to users who have Course Creator, Batch Evaluator, and Moderator roles. Any teaching or training instructions can be shared here. | ❌         |

<!-- page: learning/learning__course-creation__deleting-content.md -->
---
title: "Editing or Deleting Content"
space: "Learning"
url: "https://docs.frappe.io/learning/course-creation/deleting-content"
updated: "2026-04-08"
---

As your course evolves, you may need to update or remove content.

## Delete a Course

Go to your **Course** and click on `Settings` in the tab panel. In the top right corner, click the **trash icon** and confirm to delete the entire course.

![](https://docs.frappe.io/files/Screenshot 2026-02-23 at 4.09.06 PM.png)
*Course Settings View: course delete button is highlighted.*

---

## Edit or Delete a Chapter

- To **edit** a chapter, hover over the chapter name in the curriculum view. Click the **edit icon** that appears on the same line to change the Title or update SCORM content.
- To **delete** a chapter, hover over the chapter and click the **trash icon** on the same line. Confirm the deletion to remove the chapter and its associated lessons.

![](/files/Screenshot 2026-02-23 at 4.09.56 PM.png)
*Course Settings View: chapter edit and delete buttons are highlighted*

---

## Edit or Delete a Lesson

- To **edit** a lesson, simply click on the lesson title to open the **Lesson Editor**. From here, you can modify any blocks or settings.
- To **delete** a lesson, hover over the lesson in the curriculum list. Click the **trash icon** that appears on the same line and confirm to delete.

![](/files/Screenshot 2026-02-23 at 4.11.37 PM.png)
*Course Settings View: lesson delete button is highlighted*

<!-- page: learning/learning__course-creation__duplicating-a-course.md -->
---
title: "Duplicating a Course"
space: "Learning"
url: "https://docs.frappe.io/learning/course-creation/duplicating-a-course"
updated: "2026-04-07"
---

If you wish to duplicate a course on the same site or on another Frappe Learning site, you can do so by simply exporting a course zip. Follow the steps mentioned below:

1. Open the course that you want to duplicate.
2. Open the settings tab.
3. From the navbar, open the menu and then click on Export.



This exports the entire course along with all its chapters, lessons, assessments (quizzes, assignments, and programming exercises), and assets into a ZIP file.

![](/files/Export.mp4)





Now that you have the ZIP, you can proceed to duplicate the course on any Frappe Learning site.

1. Open the course list on the site.
2. Click on Create and then select Import via ZIP
3. In the modal that opens, select the ZIP file that you have exported earlier.
4. Once the ZIP file is selected, click on Import.

This will import the course along with all its data into the system and replicate the course in the same structure.

![](/files/import.mp4)

<!-- page: learning/learning__create-a-batch.md -->
---
title: "Create a Batch\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "Learning"
url: "https://docs.frappe.io/learning/create-a-batch"
updated: "2026-02-06"
---

A batch is a group of learners enrolled for the same set of courses at the same time. Only Moderators can create batches on the system.

![Screenshot 2024-05-17 at 3.32.21 PM](/files/Screenshot 2024-05-17 at 3.32.21 PM.png)  


To create a new batch click on the **New Batch** button. Enter the following batch details in the dialog.

**Title:** Give the batch an appropriate title.

**Description:** A short description of the batch. This information appears on the batch details page.

**Batch Details:** A detailed description of the batch. This can include the syllabus, prerequisites, etc. This appears on the batch details page.

  


**Meta Image:** This is the image that will appear when you share the batch's link on any social media platform.

**Start Date:** The date on which the batch begins.

**End Date**: The date on which the batch ends.

**Start Time:** The time when the batch session will start.

**End Time:** The time when the batch session ends.

**Seat Count:** Seat Count means the maximum number of students that will be allowed for this batch. Once the batch has this number of students, no more students will be accepted. These restrictions are applied when a user tries to enroll for the batch after payment and also when a moderator manually enrolls students.

**Medium:** The medium of instruction for the batch. It can be either Online or Offline.

**Category:** The category of the batch. You can add categories using the LMS Category doctype. These can then be used to categorize batches.

**Evaluation End Date:** If you want learners to complete their evaluations by a certain date, you can set it here. Learners will not be allowed to schedule evaluation post this date.

**Batch Details Raw:** This is the raw HTML version of the batch details. You can use this to add any custom HTML to the batch details page.

**Paid Batch:** If it's a paid batch, you can enable this. If the batch is paid, then the students will have to pay the batch fee before they can enroll for the batch.

**Amount:** The amount that students will have to pay for the batch if it's a paid batch.

**Currency:** The currency in which students will have to pay for the batch if it's a paid batch. After entering all these details, save the form. You will be redirected to the batch details page.

**Note:** Paid Courses will only work if you have setup a Payment Gateway. [Read this](https://docs.frappe.io/learning/setting-up-payment-gateway) to know more.

![screencapture-frappe-school-lms-batches-CLS-04704-edit-2024-05-17-15_51_17](/files/screencapture-frappe-school-lms-batches-CLS-04704-edit-2024-05-17-15_51_17.png)  


On the batch details page, you see all the batch information you had just entered. You can edit batch information from this page.

![Screenshot 2024-05-17 at 4.16.54 PM](/files/Screenshot 2024-05-17 at 4.16.54 PM.png)  


To manage more details of the batch, you can click on the Manage Batch button.

![Screenshot 2024-05-17 at 4.29.06 PM](/files/Screenshot 2024-05-17 at 4.29.06 PM.png)  


In the batch details are various tabs like Courses, Students, Assessments, Discussions, Live Class, etc. From the **Students** tab, you can add students manually. All you have to do is enter the Email ID of the student. The student must be a user of the system else you won't be able to add them to the batch.

![Screenshot 2024-05-17 at 4.28.39 PM](/files/Screenshot 2024-05-17 at 4.28.39 PM.png)  


You can similarly add courses to your batch. Learners will have to complete these courses as a part of this batch. You can also add evaluators for each course.

![Screenshot 2024-05-17 at 4.32.15 PM](/files/Screenshot 2024-05-17 at 4.32.15 PM.png)  


You can add two forms of assessments in a batch, quizzes and assignments. You can then check the status of the assignment and the quiz score for each student. 

From the announcements tab, moderators can send important emails to all students of the batch. The emails sent are also displayed in a list. There is also a discussions tab where learners can put in their queries and moderators and other fellow learners can help resolve these queries.

### Students Dashboard

Each student has a dashboard on the batch page. There they get to schedule evaluations. They also get to see their upcoming evaluations from this page. It also shows the students the assessments they have attempted and their scores or status for the same. 

At the bottom of the dashboard, students see a heatmap. This heatmap highlights the number of activities done by the students during the last few weeks. An activity comprises of one of the following tasks:
1. Completed a lesson
2. Submitted a quiz
3. Submitted an assignment

The heatmap is to motivate students to complete some activities every day and give them an idea of which days they were most productive.


![](/files/Screenshot%202025-02-03%20at%206.01.03%E2%80%AFPM.png)
  

<!-- page: learning/learning__create-a-course.md -->
---
title: "Create a Course\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
space: "Learning"
url: "https://docs.frappe.io/learning/create-a-course"
updated: "2026-04-08"
---

A **course** is the primary entity of the Learning app. 

You can make your courses in 2 ways:

1. Using the Learning Portal.
2. Importing them from a spreadsheet (Data Import)
3. Importing from ZIP (not a SCORM Package)

---

### Using the Learning Portal

1. Go to `Courses` on the sidebar, click the `+ Create` button, and select `New Course` from the menu.

![](https://docs.frappe.io/files/Screenshot%202026-02-23%20at%209.37.40%E2%80%AFAM.png)
*Step 1: Courses -> New Course -> New Course*

2. Fill in the basic details (Title, Short Introduction, etc.).

![](https://docs.frappe.io/files/Screenshot%202026-02-23%20at%2010.11.38%E2%80%AFAM.png)
*Course Creation Modal*

3. Click the `Create` button. You will be redirected to the `Course Settings` page, where you can fill out the [remaining details](#course-fields-reference) like metadata, images, and pricing.

---

### Importing from a Spreadsheet

Use this method to upload multiple courses at once. Note that this imports course metadata (Title, Description, etc.) but **cannot** import course content like Chapters or Lessons.

1. Go to `Courses` on the sidebar, click `+ Create`, and select `Import Course`.

![](https://docs.frappe.io/files/Screenshot%202026-02-23%20at%209.37.40%E2%80%AFAM.png)
*Step 1: Courses -> New Course -> Import Course*

2. Download Template:

- **All Fields:** To fill in every available detail.
- **Mandatory:** To get only the required fields.
- **Custom:** To select specific fields.

:::note
In custom templates, fields with Red Text are mandatory.
:::



![](https://docs.frappe.io/files/Screenshot%202026-02-23%20at%209.47.25%E2%80%AFAM.png)
*Download CSV Template options*

![](https://docs.frappe.io/files/Screenshot%202026-02-23%20at%209.48.09%E2%80%AFAM.png)
*Custom Template Download Modal*

3. Fill in your data in the spreadsheet. Leave the **ID** column empty; the system will auto-generate these.
4. Upload your Excel/CSV file. Or click the Google Sheet option and paste your URL. Make sure to copy the URL from your browser address bar. *The Google Sheet Link must end with a **gid=** parameter*.

![](https://docs.frappe.io/files/Screenshot%202026-02-23%20at%209.46.07%E2%80%AFAM.png)
*Importing from Google Sheet*

5. Map your columns if the headers don't match exactly.

![](https://docs.frappe.io/files/Screenshot%202026-02-23%20at%209.53.01%E2%80%AFAM.png)
*Map your columns*

6. Review your data and if everything is okay, click the `Import` button.

![](https://docs.frappe.io/files/Screenshot%202026-02-23%20at%2010.05.58%E2%80%AFAM.png)
*Review and Import*

7. Now scroll down to see which rows succeeded and review any errors for failed rows.

![](https://docs.frappe.io/files/Screenshot%202026-02-23%20at%2012.03.25%E2%80%AFPM.png)
*View Import Logs*

:::caution
Note that mandatory fields are compulsory and the import would fail without them (except for ID fields).
:::



---

## Course Fields Reference


| Field                        | Description                                                                                                                                                                          | Mandatory |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- |
| **Title**                    | Name of the course displayed on the course page and listings.                                                                                                                        | ✅         |
| **Short Introduction**       | Brief summary shown in course cards and search results.                                                                                                                              | ✅         |
| **Course Description**       | Detailed explanation of course content, objectives, and outcomes.                                                                                                                    | ✅         |
| **Instructors**              | Email IDs of instructors authorized to manage and teach the course.                                                                                                                  | ✅         |
| **Category**                 | Grouping category (e.g., Programming, Design) used for filtering.                                                                                                                    | ❌         |
| **Tags**                     | Keywords indicating difficulty or prerequisites to help users decide if it's right for them.                                                                                         | ❌         |
| **Course Image**             | Thumbnail image representing the course visually.                                                                                                                                    | ❌         |
| **Color**                    | Background color of the course card; fallback if no image is uploaded.                                                                                                               | ✅         |
| **Published**                | Toggle to make the course visible on the website to users. A course will appear on the website to the users only when it is published. This setting is only visible to Moderators.   | ❌         |
| **Published On**             | The date shown to learners indicating when the course went live.                                                                                                                     | ❌         |
| **Upcoming**                 | If a course is about to become available to users soon but not yet, mark it as Upcoming. Note that even for an upcoming course to be visible on the website, it should be published. | ❌         |
| **Featured**                 | Highlights the course in designated "Featured" sections of the portal.                                                                                                               | ❌         |
| **Disable Self Enrollment**  | Enable this if you don't want users to enroll themselves into the course directly but instead want the Administrator to enroll them.                                                 | ❌         |
| **Preview Video**            | Introductory video or teaser accessible before a student enrolls.                                                                                                                    | ❌         |
| **Related Courses**          | Linked courses shown as recommendations on the course page.                                                                                                                          | ❌         |
| **Paid Course**              | If enabled, students must complete payment to access the course content.                                                                                                             | ❌         |
| **Paid Certification**       | Requires an additional fee to be paid before the certificate is issued.                                                                                                              | ❌         |
| **Amount**                   | The cost of the course (only applicable if Paid Course or Paid Certification is enabled).                                                                                            | ✅*        |
| **Currency**                 | The currency in which the course price is listed (only applicable if Paid Course or Paid Certification is enabled).                                                                  | ✅*        |
| **Evaluator**                | Evaluators for course certification (only applicable if Paid Certification is enabled).                                                                                              | ✅*        |
| **Time Zone**                | Time Zone for Evaluation Schedule (only applicable if Paid Certification is enabled).                                                                                                | ✅*        |
| **Completion Certification** | Issues a certificate to the student automatically upon finishing the course.                                                                                                         | ❌         |
| **Meta Description**         | SEO-friendly description used by search engines.                                                                                                                                     | ❌         |
| **Meta Keywords**            | SEO-friendly keywords used by search engines.                                                                                                                                        | ❌         |


*Mandatory only if the related Paid/Certification features are enabled.

<!-- page: learning/learning__create-a-live-class.md -->
---
title: "Create a Live Class"
space: "Learning"
url: "https://docs.frappe.io/learning/create-a-live-class"
updated: "2026-05-06"
---

Moderators can host a live session from the batch page.

The live class can be done either through Zoom or Google Meet. Once a live class is created, all students who are a part of the batch will receive a calendar invite. All upcoming live classes will be listed on the batch page. Students can join the current session from the batch page itself.

Follow the steps below to start your own live class:

### Step 1: Configure your Google Calendar.

This is required for both Zoom and Google integration. This is what helps us send a calendar invite for the live class. You will also need to enable Google Settings and add the Google Calendar of the moderator. To enable Google Settings, follow the steps mentioned in [this document](https://docs.frappe.io/erpnext/google_calendar).

### Step 2: Connect your integration

You can either use [Zoom](#zoom-integration) or [Google Meet](#google-meet) for this.

#### Zoom Integration

To use this feature, you will have to create a Server-to-server OAuth App from the Zoom App Marketplace. You can follow [this document](https://marketplace.zoom.us/docs/guides/build/server-to-server-oauth-app/) for the same. Creating a Server-to-Server OAuth App provides you with an **Account ID**, **Client ID**, and **Client Secret**.



![Screenshot 2024-05-17 at 5.07.25 PM](/files/Screenshot 2024-05-17 at 5.07.25 PM.png)
*Zoom Settings Doctype*



You will then have to enter these values in the **Zoom Settings** DocType. Check out this video for more details.

![](/files/Zoom App.mp4)



For Auto Recording to work, ensure that Automatic Recording is enabled on your Zoom Account.

![Auto Recording](https://docs.frappelms.com/assets/auto-recording.9e7f3f7b.jpg)
*Automatic recording setting in Zoom Account*

Once the details are submitted, the live class gets saved in your Zoom Account as well as the system backend. A calendar invite also gets sent to all the students of the class.

#### Google Meet

To set up your Google Meet live class, after configuring your Google Calendar, follow the steps below

1. Go to  `Settings` -> `Google Meet` -> `+ New`
  ![](/files/image24f5ef.png)
  *New Google Meet Account Setup*
2. Enter your details in the modal

### Step 3: Create your live class

1. Navigate to the batch where you wish to add the live class and configure your `Conferencing Provider`. Fill `Google Meet Account` field for Google and `Zoom Account` field for Zoom.
2. Now, you can simply go to your `Classes` tab in your batch and create your live class
  ![](/files/imaged54fab.png)
  *Create Live Class Modal*

<!-- page: learning/learning__falcon-self-hosting-guide.md -->
---
title: "Falcon Self-Hosting Guide"
space: "Learning"
url: "https://docs.frappe.io/learning/falcon-self-hosting-guide"
updated: "2026-02-06"
---

This guide walks you through setting up and deploying your own instance of Falcon — a live code execution engine.


### Prerequisites


1. A cloud server (e.g., DigitalOcean droplet or any VPS)
2. Python 3.11+
3. Docker and Docker Compose
4. Git
5. Nginx
6. A domain

### Clone the Repository

    git clone https://github.com/fossunited/falcon
    cd falcon

Or use your own fork if needed.


### Setup Python Environment

    python3 -m venv env
    source env/bin/activate
    pip install --upgrade pip
    pip install -r dev-requirements.txt
    
Ensure you also install uvicorn[standard] for WebSocket support:


    pip install 'uvicorn[standard]'

### Pull Docker Images
Falcon uses Docker containers for sandboxed code execution. Pull the base runtimes:

    
    docker pull fossunited/falcon-python:3.9
    docker pull fossunited/falcon-golang
    docker pull fossunited/falcon-rust
    docker pull frappedevs/falcon-javascript

### Create systemd Service
Create a service file at /etc/systemd/system/falcon.service:


    [Unit]
    Description=Falcon LiveCode Service
    After=network.target
    [Service]
    User=root
    WorkingDirectory=/root/falcon
    ExecStart=/root/falcon/env/bin/uvicorn livecode_server.server:app --host 0.0.0.0 --port 8000
    Restart=always
    [Install]
    WantedBy=multi-user.target
    
Then reload and start the service:

    sudo systemctl daemon-reexec
    sudo systemctl daemon-reload
    sudo systemctl enable falcon
    sudo systemctl start falcon

Check logs:

    journalctl -u falcon -f

### Configure Nginx
Install Nginx if not already:

    
    sudo apt update
    sudo apt install nginx
    
Create a new site config under /etc/nginx/sites-available/falcon:


    server {
        listen 80;
        server_name falcon.example.com;
        location / {
            proxy_pass http://localhost:8000;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
    
Enable the site:


    sudo ln -s /etc/nginx/sites-available/falcon /etc/nginx/sites-enabled/
    sudo nginx -t
    sudo systemctl restart nginx

(Optional) Set up HTTPS with Certbot:

    sudo apt install certbot python3-certbot-nginx
    sudo certbot --nginx

### Test Your Setup
In your browser or frontend app, test a session:

First add the script on a page

    const script = document.createElement('script')
    script.src = `https://falcon.frappe.io/static/livecode.js`
    document.head.appendChild(script)

Then run the session

    const session = new LiveCodeSession({
      base_url: "https://falcon.example.com",
      runtime: "python",
      code: "print('Hello')",
      onMessage: console.log
    });
    
You should see:


    { msgtype: "welcome", message: "welcome to livecode" }


### Troubleshooting
1. 403 or 502 errors: Check journalctl -u falcon -f and nginx -t
2. WebSocket not working: Make sure uvicorn[standard] is installed and Nginx supports WebSockets.
3. Docker errors in tests: Ensure runtime images are pulled correctly.
