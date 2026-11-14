#!/usr/bin/env python3
"""Say how this pack's knowledge compares with the versions a Frappe site is running.

    version_check.py --frappe 16.60.1 --erpnext 16.58.0 [--hrms 16.55.0]
    version_check.py --versions-json '{"frappe": {"version": "16.60.1"}, "erpnext": {"version": "16.58.0"}}'
    version_check.py --frappe 16.60.1 --json          machine-readable result

--versions-json takes the result of `frappe.utils.change_log.get_versions` as it comes back.

It reads compat.json at the plugin root, makes no network request and touches nothing. Exit code is
always 0 when it could compare; the verdict is in the output. Python 3.8+, standard library only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

COMPAT = Path(__file__).resolve().parents[3] / "compat.json"

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="backslashreplace")
    except Exception:
        pass


def parse(v) -> tuple | None:
    """'16.56.0', 'v16.56.0', '17.0.0-dev', '16.x.x-develop' -> (16, 56, 0); None when unreadable."""
    m = re.match(r"\s*v?(\d+)(?:\.(\d+))?(?:\.(\d+))?", str(v or ""))
    if not m:
        return None
    return tuple(int(x) if x is not None else 0 for x in m.groups())


def show(t: tuple) -> str:
    return ".".join(str(x) for x in t)


def check(site: dict, compat: dict) -> dict:
    """site: {"frappe": "16.60.1", "erpnext": "..."} -> verdict dict."""
    know, chk = compat["knowledge"], compat["checked"]
    apps, level = [], "in_step"
    order = {"in_step": 0, "ahead_checked": 1, "ahead_unchecked": 2, "older": 2, "other_major": 3}
    for app in ("frappe", "erpnext", "hrms"):
        sv = parse(site.get(app))
        if sv is None:
            continue
        kv, cv = parse(know.get(app)), parse(chk.get(app))
        ref = kv or cv
        if ref is None:
            continue
        if sv[0] > ref[0]:
            st = "other_major"
        elif sv[0] < ref[0]:
            st = "older"
        elif cv and sv > cv:
            st = "ahead_unchecked"
        elif kv and sv > kv:
            st = "ahead_checked"
        else:
            st = "in_step"
        apps.append({"app": app, "site": show(sv), "knowledge": show(kv) if kv else None,
                     "checked": show(cv) if cv else None, "status": st})
        if order[st] > order[level]:
            level = st

    def applies(c):
        sv, since, kv = parse(site.get(c["app"])), parse(c["since"]), parse(know.get(c["app"]))
        return bool(sv and since and sv >= since and (kv is None or since > kv))

    changes = [c for c in compat.get("changes", []) if applies(c)]
    feats = []
    for f in compat.get("features", []):
        sv, need = parse(site.get(f["app"])), parse(f["from"])
        if sv and need:
            feats.append({"name": f["name"], "available": sv >= need, "from": f["from"]})
    return {"level": level, "apps": apps, "changes": changes, "features": feats,
            "pack_version": compat.get("pack_version"), "knowledge_date": know.get("date"), "checked_date": chk.get("date")}


def say(r: dict) -> str:
    names = {"frappe": "Frappe", "erpnext": "ERPNext", "hrms": "Frappe HR"}
    site = ", ".join(f"{names[a['app']]} {a['site']}" for a in r["apps"]) or "an unknown version"
    out = [f"Your site runs {site}. This pack is version {r['pack_version']}."]
    lv = r["level"]
    if lv == "in_step":
        out.append(f"That is within what the pack was built on ({r['knowledge_date']}). Nothing to flag.")
    elif lv == "ahead_checked":
        out.append(f"Your site is newer than the pack's reference pages ({r['knowledge_date']}), but within what its "
                   f"connection, dashboard and safety rules were checked against on {r['checked_date']}.")
    elif lv == "ahead_unchecked":
        out.append(f"Your site is newer than anything this pack was checked against ({r['checked_date']}). "
                   "Where the site and the pack disagree, the site is right.")
    elif lv == "other_major":
        out.append("Your site is on a newer major version than this pack was written for. Menus, field names and "
                   "some steps will differ; treat the pack's steps as a guide and confirm each one on screen.")
    elif lv == "older":
        out.append("Your site is on an older major version than this pack was written for. Some features and paths "
                   "described here will not exist on it.")
    missing = [f for f in r["features"] if not f["available"]]
    if missing:
        out.append("Not available on this site: " + "; ".join(f"{f['name']} (needs {f['from']} or later)" for f in missing) + ".")
    todo = [c for c in r["changes"] if not c.get("covered")]
    done = [c for c in r["changes"] if c.get("covered")]
    if todo:
        out.append(f"{len(todo)} change(s) since the pack's reference pages that it does not cover yet:")
        out += [f"  - {names[c['app']]} {c['since']}: {c['what']}" for c in todo]
    if done:
        out.append(f"{len(done)} newer change(s) the pack already accounts for:")
        out += [f"  - {names[c['app']]} {c['since']}: {c['what']}" for c in done]
    if lv != "in_step":
        out.append("To get the newest pack: `claude plugin marketplace update jazari-agents` then "
                   "`claude plugin update jazari-frappe-erpnext@jazari-agents`, or turn on auto-update for the marketplace in /plugin.")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Compare this pack with a site's Frappe versions. Offline, read-only.")
    ap.add_argument("--frappe")
    ap.add_argument("--erpnext")
    ap.add_argument("--hrms")
    ap.add_argument("--versions-json", help="the result of frappe.utils.change_log.get_versions")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    a = ap.parse_args()
    site = {k: v for k, v in (("frappe", a.frappe), ("erpnext", a.erpnext), ("hrms", a.hrms)) if v}
    if a.versions_json:
        try:
            raw = json.loads(a.versions_json)
        except json.JSONDecodeError:
            print("ERROR: --versions-json is not valid JSON.", file=sys.stderr)
            return 2
        raw = raw.get("message", raw.get("data", raw)) if isinstance(raw, dict) else {}
        for app, info in (raw or {}).items():
            site.setdefault(app, info.get("version") if isinstance(info, dict) else info)
    if not parse(site.get("frappe")) and not parse(site.get("erpnext")):
        print("ERROR: give at least --frappe or --erpnext, or --versions-json.", file=sys.stderr)
        return 2
    try:
        compat = json.loads(COMPAT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"ERROR: cannot read {COMPAT.name}: {e}", file=sys.stderr)
        return 2
    r = check(site, compat)
    print(json.dumps(r, ensure_ascii=False, indent=2) if a.json else say(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
