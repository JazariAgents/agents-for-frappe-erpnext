# Capabilities — Courses and students

## Contents

- capability table (id, mode, destructive, source)
- version notes

Every row was confirmed against an official Frappe documentation page fetched on 2026-08-31 while this plugin was built. Nothing that could not be traced to a page is in this plugin at all.

| id | Capability | Mode | Destructive | Reversibility | Bundled page | Source URL |
|---|---|---|---|---|---|---|
| `lms.course` | Create a course | browser | yes | reversible | `docs/learning/learning-01.md` lines 796–917 | https://docs.frappe.io/learning/create-a-course |
| `lms.chapter` | Add chapters and lessons | browser | yes | reversible | `docs/learning/learning-01.md` lines 3–62 | https://docs.frappe.io/learning/add-a-chapter |
| `lms.batch` | Run a batch of learners | browser | yes | reversible | `docs/learning/learning-01.md` lines 702–794 | https://docs.frappe.io/learning/create-a-batch |
| `lms.liveclass` | Host a live class | browser | yes | reversible | `docs/learning/learning-01.md` lines 919–979 | https://docs.frappe.io/learning/create-a-live-class |
| `lms.quiz` | Assess learners with quizzes | browser | yes | reversible | `docs/learning/learning-01.md` lines 1503–1560 | https://docs.frappe.io/learning/quizzes |
| `lms.assignment` | Set assignments | browser | yes | reversible | `docs/learning/learning-01.md` lines 156–187 | https://docs.frappe.io/learning/assignments |
| `lms.certificate` | Issue certificates | browser | yes | irreversible | `docs/learning/learning-01.md` lines 1335–1355 | https://docs.frappe.io/learning/issue-a-certificate |
| `lms.program` | Group courses into a program | browser | yes | reversible | `docs/learning/learning-01.md` lines 64–110 | https://docs.frappe.io/learning/add-a-program |
| `lms.payments` | Charge for a course | browser | yes | reversible | `docs/learning/learning-01.md` lines 1594–1621 | https://docs.frappe.io/learning/setting-up-payment-gateway |
| `edu.student` | Enrol students | browser | yes | reversible | `docs/education/education-01.md` lines 1962–2062 | https://docs.frappe.io/education/student |
| `edu.program` | Set up programs and courses | browser | yes | reversible | `docs/education/education-01.md` lines 1321–1383 | https://docs.frappe.io/education/program |
| `edu.fees` | Collect fees | browser | yes | irreversible | `docs/education/education-01.md` lines 848–960 | https://docs.frappe.io/education/fees |
| `edu.assessment` | Run assessments | browser | yes | reversible | `docs/education/education-01.md` lines 86–105 | https://docs.frappe.io/education/assessment-introduction |

## Version notes

- In this edition these calls go through the MCP server (Frappe v16.53 and later) or frappectl (v16 and later). On an older site, work through the Desk (`browser.md`).
- ERPNext v16 and Frappe HR v16 track the framework major; CRM, Helpdesk, Insights, Builder and Learning have their own version lines.

