# Capabilities — Courses and students

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `lms.course` | Create a course | browser | yes | reversible | `docs/learning/learning__create-a-course.md` | https://docs.frappe.io/learning/create-a-course |
| `lms.chapter` | Add chapters and lessons | browser | yes | reversible | `docs/learning/learning__add-a-chapter.md` | https://docs.frappe.io/learning/add-a-chapter |
| `lms.batch` | Run a batch of learners | browser | yes | reversible | `docs/learning/learning__create-a-batch.md` | https://docs.frappe.io/learning/create-a-batch |
| `lms.liveclass` | Host a live class | browser | yes | reversible | `docs/learning/learning__create-a-live-class.md` | https://docs.frappe.io/learning/create-a-live-class |
| `lms.quiz` | Assess learners with quizzes | browser | yes | reversible | `docs/learning/learning__quizzes.md` | https://docs.frappe.io/learning/quizzes |
| `lms.assignment` | Set assignments | browser | yes | reversible | `docs/learning/learning__assignments.md` | https://docs.frappe.io/learning/assignments |
| `lms.certificate` | Issue certificates | browser | yes | irreversible | `docs/learning/learning__issue-a-certificate.md` | https://docs.frappe.io/learning/issue-a-certificate |
| `lms.program` | Group courses into a program | browser | yes | reversible | `docs/learning/learning__add-a-program.md` | https://docs.frappe.io/learning/add-a-program |
| `lms.payments` | Charge for a course | browser | yes | reversible | `docs/learning/learning__setting-up-payment-gateway.md` | https://docs.frappe.io/learning/setting-up-payment-gateway |
| `edu.student` | Enrol students | browser | yes | reversible | `docs/education/education__student.md` | https://docs.frappe.io/education/student |
| `edu.program` | Set up programs and courses | browser | yes | reversible | `docs/education/education__program.md` | https://docs.frappe.io/education/program |
| `edu.fees` | Collect fees | browser | yes | irreversible | `docs/education/education__fees.md` | https://docs.frappe.io/education/fees |
| `edu.assessment` | Run assessments | browser | yes | reversible | `docs/education/education__assessment-introduction.md` | https://docs.frappe.io/education/assessment-introduction |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

