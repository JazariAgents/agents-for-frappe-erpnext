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

