<!-- Frappe documentation: drive, part 1 of 1. Index: docs/INDEX.md -->

<!-- page: drive/drive__file-access.md -->
---
title: "Sharing"
space: "Drive"
url: "https://docs.frappe.io/drive/file-access"
updated: "2026-01-06"
---

The most important part of any cloud is access.

Frappe Drive has three types of permissions:

- View - allowing people to view, download, comment, and share the file
- Edit - allowing people to edit a file or document
- Upload - allows people to upload files to a folder


By *default*:

- In the _Home_ folder, only you have access to the files and folders. You can share them with anyone, choosing the access you want to give.
- In a _team_, all members have view and upload access to folders and files - they don't have write access unless you explicitly give them. 

### Folders
When a folder has a specific share settings, all the items inside that folder (recursively) have the same access **until** the permissions of a folder or file inside this folder is overridden.

For example:
```
Folder A -> file.txt
         -> file2.txt
         -> Folder C -> file3.jpeg
Folder B -> file4.doc
```
At first, default permissions (private if in the "Home" view, read + comment + write for all team members if in the "Team" view). 

Then, if I share `Folder A` with a specific user with View access - then all the items within (including the "nested" file `file3.jpeg`) are *also* shared with that user with the View Access.

*However*, if I make `Folder C` private again, then that user will be able to see neither `Folder C` nor any of its items (`file3.jpeg`, in this case).

Put simply, access "bubbles" downwards. When a user tries to access an item, Drive traverses up the path checking for any sharing settings configured. If it finds one, it stops and uses that. If it doesn't, it implements default permissions.

### Sharing
You can share with specific users, specific teams, or the world:
![](/files/Permissions%20Frappe%20Build.png)

If you share an item publicly, **anyone can access the file**. They will not need to login.

<!-- page: drive/drive__files.md -->
---
title: "Files"
space: "Drive"
url: "https://docs.frappe.io/drive/files"
updated: "2026-01-06"
---

The only way to currently add files to Frappe Drive is through the client. Either by dragging the files/folder onto it or by selecting the file upload option.


> Frappe Drive saves file paths in the database, so its imperative that you do not modify contents of `/private/files/$user_hash_folder` or the `file_path` in the database. This can lead to lost files and corrupted data
> 
> 

### Special files
**Links**: these are not files at all! They are actually links to some external website. This feature is useful in cases of having a Google Sheeets, for example, or a file hosted on some other cloud solution.

That said, they are treated like files in every way - you can control access, favourite, or do anything you like.

You can add links using the dialog - or just copy a link and Drive will detect it for you. 

**Documents**: this is a beta product - Frappe Writer. It is a Google Docs equivalent.

<!-- page: drive/drive__introduction.md -->
---
title: "Introduction"
space: "Drive"
url: "https://docs.frappe.io/drive/introduction"
updated: "2026-01-06"
---

## What is Frappe Drive?

You dislike domination of Google and closed-source cloud solutions. Given the sensitivity of this structure, you expect that there is some good open source solution.

To your horror, you click through them all - NextCloud, OwnCloud - and none of them satisfy you. They are slow. The UI is subpar. They feel flaky.

And then you discover Frappe Drive.
![](/files/Frappe%20Drive%20Image.png)


Aesthetic. Powerful. Reliable. 

Sign up on [Frappe Cloud](frappecloud.com/) now.

## Why Frappe Drive?

The idea of building a drive-like application has been floating around in Frappe since atleast [2015](https://github.com/frappe/frappe/issues/8723#issuecomment-164223523). While Frappe Framework has rather robust file handling itself, the need arose for building a standalone solution. As we dug deeper, what began as a simple file-sharing platform evolved into a comprehensive collaboration tool.

## Key Features

Core — the file manager

- Large file uploads using multi-part uploads
- Folder uploads to maintain your structure in Drive
- Preview files directly in your browser, [supported file previews](https://docs.frappe.io/drive/previews)
- Stream videos directly from the server
- Search for all your files and files shared shared with you
- View activity logs of a file to glance at the changes in permissions and file metadata
- Share files and folders with users, groups, everyone on the site or publish publicly
- Add guest users who have limited and controlled access to your site
- Pool storage of all users together or assign a quota of storage to each user

Writer — the document editor

- Collaborate with other users or guests in real time
- Annotate, resolve and reply to other users to give suggestions
- Manually version your documents to always be able to go back to an older version
- Automatic versioning to make sure you never lose data
- Import docx documents into the editor


<details>
<summary><em>More screenshots</em></summary>

![Image Preview](https://github.com/user-attachments/assets/993cbd87-a96c-4e5c-8737-0c03c9222723)

![File Sharing Dialog](https://github.com/user-attachments/assets/acb1a542-53d1-4d0e-b2e2-6c9b87f04e69)

![Editor](https://github.com/user-attachments/assets/fe87dfd1-3f55-42df-94b9-f7baed03a391)

![Editor with real time editing](https://github.com/user-attachments/assets/f89a2fab-e618-4d7d-90a6-aaa2cf45fa55)

</details>

## Under the Hood

- [**Frappe Framework**](https://github.com/frappe/frappe): A full-stack web application framework written in Python and Javascript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.

- [**Frappe UI**](https://github.com/frappe/frappe-ui): A Vue-based UI library, to provide a modern user interface. The Frappe UI library provides a variety of components that can be used to build single-page applications on top of the Frappe Framework.

- [**TipTap**](https://github.com/ueberdosis/tiptap): Tiptap is a wrapper over ProseMirror that provides some friendlier APIs and defaults.

- [**ProseMirror**](https://github.com/prosemirror): ProseMirror is a flexible, extensible toolkit for building rich-text editors with precise control over document structure and behavior.

- [**YJS**](https://github.com/yjs/yjs): The Content Free Replicated Data type (CRDT) at the core of the real time collaboration in both the document and annotation system.


## Installation
Go [here](/drive/quick-start) for installation.

## Learn and Connect

- [Website](https://frappe.io/drive)
- [Telegram Public Group](https://t.me/frappedrive)
- [Discuss Forum](https://discuss.frappe.io/)
- [Documentation](https://docs.frappe.io/drive/quick-start)

<!-- page: drive/drive__microsoft-documents.md -->
---
title: "Microsoft Documents"
space: "Drive"
url: "https://docs.frappe.io/drive/microsoft-documents"
updated: "2026-01-06"
---

It's simple to get previews on Microsoft documents like Word, Excel, or PowerPoint files!

Ask your site administrator to go to `/drive/disk-settings` and set the `JWT Token` to anything they like. **This should not be released**, as it can give access to your files.

We do not currently support editing files (OnlyOffice integration) - you can upvote this feature request [here](https://github.com/frappe/drive/issues/343).

<!-- page: drive/drive__open-source.md -->
---
title: "Open Source"
space: "Drive"
url: "https://docs.frappe.io/drive/open-source"
updated: "2026-01-06"
---

The term _open source_ refers to software where the source code is freely available to the public for inspection, modification, enhancement and redistribution.

This is opposed to most propetiery software products - like Google Drive or Dropbox - which do not allow you to view their codebase. Any attempt at transparency is heavily restricted.

Frappe Drive is a *completely open source* product, published under the [Affero General Public License (aGPLv3)](https://github.com/frappe/drive?tab=AGPL-3.0-1-ov-file#readme) license.

It grants you the freedom to...

* Use the software for any purpose
* Change the software to suit your needs
* Share the software with anyone
* Share the changes you make

The source code of Frappe Drive is available on [GitHub](https://github.com/frappe/drive).

**You read that right**. You can install Frappe Drive wherever you want and use it for free. You can change it. You can do what you like.

#### More Advantages of Open Source Software

1. There is no lock-in with one specific vendor. Even if Frappe discontinues Drive tomorrow, you have the service you love in your hands.
2. You can host the application anywhere, including your own server to gain complete ownership and privacy of the data.
3. You can access a [community](https://discuss.erpnext.com/) for help.
4. You can benefit from using a polished product that has been **critiqued and used by a wide range of people**, who have reported hundreds of issues, security fixes, and suggestions. Transparent to its core.

<!-- page: drive/drive__previews.md -->
---
title: "Previews"
space: "Drive"
url: "https://docs.frappe.io/drive/previews"
updated: "2026-01-06"
---

For most common file types, Frappe Drive allows you to preview it in the browser itself.

Here is a (non-exhaustive) list of file types we support. Want something added? Please [get in touch](mailto:safwan@frappe.io) or open [an issue](github.com/frappe/drive/issues/new)!

**Office**

* `application/pdf`
* `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
* `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`

**Images**

* `image/png`
* `image/jpg`
* `image/gif`
* `image/svg`
* `image/webp`

**Videos**

Frappe Drive lacks any transcoding pipeline for now so only H264, H265*, and AV1* codecs are supported for video streaming.

* `video/mp4`
* `video/webm`
* `video/quicktime`

**Text**

Generally most text files should preview but this is ever expanding so we might miss some.

* Most mime types with starting with `text/`
* Support for this codec is [platform dependant](https://caniuse.com/hevc). For example: H265 only works on MacOS and Windows running Chrome (Safari also supports it).

<!-- page: drive/drive__quick-start.md -->
---
title: "Host Locally"
space: "Drive"
url: "https://docs.frappe.io/drive/quick-start"
updated: "2026-01-06"
---

### Docker (*recommended*)

This is the quickest way to set up Frappe Drive and take it for a test *drive*.

The Frappe Framework is multi-tenant and supports multiple apps by default. This `docker compose` is just a standalone version with Frappe Drive pre-installed. Just put it behind your desired reverse-proxy if needed, and you're good to go. 
  
If you wish to use multiple Frappe apps or need multi-tenancy. I suggest moving over to our production ready self-hosted workflow, or join us on Frappe Cloud to get first party support and hassle-free hosting.

1. Setup folder:
```
mkdir frappe-drive && cd frappe-drive
```

2. Download the required files (Docker Compose file and Frappe Bench setup script):
```
wget -O docker-compose.yml https://raw.githubusercontent.com/frappe/drive/main/docker/docker-compose.yml
wget -O init.sh https://raw.githubusercontent.com/frappe/drive/main/docker/init.sh
```
3. Run the container!

```
docker compose up -d
```

### Using Bench

This is the bare metal way to setup Drive.


1. [Install Bench.](https://frappeframework.com/docs/user/en/installation)
2. Install Frappe Drive using `bench get-app drive`.
3. Create your site - `bench new-site site.name`...
4. ... and install the app: `bench install-app drive`.
5. Install some Drive specific system packages:

*Ubuntu/Debian (apt based distros)*:
```sh 
sudo apt install ffmpeg libmagic
```

*macOS*:
```sh
brew install libmagic ffmpeg
```

6. Start up the bench if you haven't already - `bench start`.
7. Drive is now accessible at `localhost:8000` or `sitename:8000`.

<!-- page: drive/drive__storage-quota.md -->
---
title: "Storage"
space: "Drive"
url: "https://docs.frappe.io/drive/storage-quota"
updated: "2026-01-06"
---

A team has a specific total storage limit, and a per-user limit. This can be configured in Desk (in the `Drive Team` DocType).

## Storage settings
Frappe Drive offers a comprehensive breakdown of your storage. You can see both the team's and your personal files'. We also highlight the files contributing most to your storage, if you wanted to cut down on your cloud storage.

![](/files/Storage.png)

## Adding Storage
### Frappe Cloud
On Frappe Cloud your storage limit is automatically handled by the plan you select and the corresponding disk space that plan has. Additionally, you can also use a disk storage add-on to increase your disk size.

## Self-hosted
You can set your storage limit inside your `Drive Team` DocType. Under the hood it's simply updating the `site_config`.

<!-- page: drive/drive__teams.md -->
---
title: "Teams"
space: "Drive"
url: "https://docs.frappe.io/drive/teams"
updated: "2026-01-06"
---

The reason Drive is great for businesses is because of the teams feature. You can have as many te

### Create and Manage
You can create and edit teams by going to *Settings > Teams* along with managing or inviting members.

There are three types of users: 

1. normal users, 
2. *managers*. By default, only the creator of a team is a manager. You can add other managers,
3. *guests*, who only have read access

<!-- page: drive/drive__why-frappe-drive.md -->
---
title: "Frappe Drive for You"
space: "Drive"
url: "https://docs.frappe.io/drive/why-frappe-drive"
updated: "2026-01-06"
---

Drive is **completely open source** and will always be. Drive is built by [Frappe](https://frappe.io) - we've been here since 2007 and have a [suite of products](https://frappe.io/products), all of which are open source.

Drive is **great for teams**. Join multiple teams - your work and family on the same account. Have a personal view, and fly between different views with ease.

Drive has a **beautiful UI**, and is an awesome experience for users. Other open source solutions do not even come close.

Drive is **fast**. Whoosh.
