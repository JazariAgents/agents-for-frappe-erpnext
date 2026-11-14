---
title: "What are Benches?"
space: "Cloud"
url: "https://docs.frappe.io/cloud/what-are-benches-and-bench-groups"
updated: "2026-02-27"
---

A **Bench** is a collection of apps and sites. All sites on a **Bench** share the same configuration, such as the version of apps, or version of dependencies.

Frappe Cloud creates the benches from templates which can be viewed under the **Benches** menu.

![](/files/Screenshot 2026-02-27 at 3.20.37 PM.png)

> For a more technical explanation of what a **Bench** is, see the [Bench confusion](#bench-confusion) section.

The template holds information such as:

- Which apps to install.![](/files/WtN8r0p.png)
- What common site config flags to be set for benches deployed from the current template.
- The version of dependencies to be used for the benches.

> **Private Bench"**
>
> If you are using a [private bench](https://frappecloud.com/docs/benches) then all of the above information can be set and updated by you.

### **When is a Bench created?**

A bench template by itself does not run your site. For this you have to *deploy* that template. This takes place when you click on *Deploy* or *Update Available* on your **Bench** page.

1. When you do this, a *Deploy* job (visible in the **Deploys** tab) is created. This job builds a [Docker image](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image) from the template and uploads it to the Frappe Cloud [Docker registry](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry).
  ![](/files/Screenshot 2026-02-27 at 2.44.37 PM.png)
2. After the Deploy job succeeds, a *New Bench* job (visible in the **Jobs** tab) is created. This job downloads the template’s image and runs it on the server.
  ![](/files/Screenshot 2026-02-27 at 2.52.20 PM.png)

Once the **Bench** is up and running, a new site can be created on it, or an existing site can be moved to it from another **Bench**.

## **Bench confusion**

If you are familiar with [Frappe Framework](https://frappe.io/framework) development then term "bench" may not be a new one and might cause some confusion. This is a perfectly sane response to our shortcomings when it comes to naming things. To help clear this, I'll try and differentiate between the different benches:




| **Term**       | **Context**      | **Description**                                                                                      |
| -------------- | ---------------- | ---------------------------------------------------------------------------------------------------- |
| *Frappe Bench* | Frappe Framework | Directory that holds a collection of Frappe Framework apps and sites on which they may be installed. |
| `frappe/bench` | Frappe Framework | [CLI tool](https://github.com/frappe/bench) used to manage a *Frappe Bench*.                         |
| **Bench**      | Frappe Cloud     | *Frappe Bench* running inside a container from which your site is served.                            |


In the context of Frappe, all benches are conceptually linked (unless you are talking about a [regular bench](https://en.wikipedia.org/wiki/Bench_(furniture))).