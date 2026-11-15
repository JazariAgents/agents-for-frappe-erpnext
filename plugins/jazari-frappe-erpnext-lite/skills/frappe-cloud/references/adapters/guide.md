# Guide adapter — Frappe Cloud — sites, benches, servers

## Contents

- what guided means here
- the topics, and what to check with the user

These are not buttons. They are decisions and concepts where Frappe's behaviour depends on a choice the
user has to make — and the wrong choice is expensive to reverse later. Claude explains the options from
the documentation, asks which case applies, and then acts through `api.md` or `browser.md` on the records
that follow from the answer.

## Topics

### Understand benches and bench groups
- **What the page says:** A **Bench** is a collection of apps and sites. All sites on a **Bench** share the same configuration, such as the version of apps, or version of dependencies.
- **It covers:** **When is a Bench created?**, **Bench confusion**
- **Read the site's current answer before advising.** Check what this site already does, say so, then explain the alternatives from the page above and let the user choose.
- **Full page, bundled offline:** `docs/cloud/cloud-03.md` lines 552–603  (https://docs.frappe.io/cloud/what-are-benches-and-bench-groups)

