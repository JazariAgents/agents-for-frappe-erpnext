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