#!/usr/bin/env python3
"""ERPNext Pulse - read a Frappe/ERPNext site and build a one-file dashboard.

    pulse.py demo    --out pulse.html                     the dashboard on bundled demo data
    pulse.py collect --site https://erp.example.com --out data.json
    pulse.py build   --data data.json --out pulse.html
    pulse.py run     --site https://erp.example.com --out pulse.html     collect + build
    pulse.py run     --via frappectl --profile erp --out pulse.html      the same, signed in through frappectl

READ-ONLY BY CONSTRUCTION: with an API key every request goes through Site.get(), which only ever
sends GET; through frappectl only `doc list` and `api ... -X GET` are run, which a read-only profile
allows. Nothing on the site is created, changed or deleted.

The Agents screen is built from the workspace file .frappe/activity.jsonl (see frappe-connect,
"Activity log"); pass --activity to read it from somewhere else.

Credentials come from the environment (FRAPPE_API_KEY / FRAPPE_API_SECRET) or from a file given
with --credentials that holds `api_key = ...` and `api_secret = ...` lines. They are sent only to
--site, and are never printed or written to any output file.

Uses the v1 REST paths (/api/resource, /api/method), which every Frappe version serves.
Python 3.8+, standard library only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shlex
import shutil
import statistics
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

VERSION = "1.0.2"
HERE = Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "assets" / "pulse.template.html"
SAMPLE = HERE.parent / "assets" / "sample-data.json"
PLACEHOLDER = "__PULSE_DATA__"
PAGE = 500          # rows per request
MAX_ROWS = 10000    # per list; beyond this the figure is marked partial

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="backslashreplace")
    except Exception:
        pass


class Fatal(Exception):
    """The whole run cannot continue (site unreachable, key rejected)."""


class Unavailable(Exception):
    """One metric cannot be read; the dashboard says why and carries on."""


class Site:
    def __init__(self, base: str, key: str, secret: str, timeout: int = 30):
        self.base = base.rstrip("/")
        self._auth = f"token {key}:{secret}"
        self.timeout = timeout
        self.requests = 0

    def get(self, path: str, params: dict | None = None):
        """The only way this script talks to the site. GET, nothing else."""
        url = self.base + path
        if params:
            url += "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, method="GET",
                                     headers={"Authorization": self._auth, "Accept": "application/json"})
        self.requests += 1
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 401:
                try:
                    said = e.read().decode("utf-8", "replace")
                except Exception:  # noqa: BLE001 - the body is only used to explain the refusal
                    said = ""
                if "IP Address" in said:
                    # Frappe 16.33 and later apply a user's Restrict IP list to API keys too.
                    raise Fatal("the site refused this computer's address (HTTP 401): the API user has a Restrict IP "
                                "list and this address is not on it. Add the address on the User record, or use a "
                                "key from a user without that restriction. The key itself is fine.")
                raise Fatal("the site rejected the API key (HTTP 401). Generate a new key and secret for the user.")
            raise
        except urllib.error.URLError as e:
            raise Fatal(f"could not reach {self.base}: {e.reason}")
        except json.JSONDecodeError:
            raise Fatal(f"{self.base} did not answer with JSON. Is this the site's base URL?")

    def _guard(self, what: str, fn):
        try:
            return fn()
        except urllib.error.HTTPError as e:
            if e.code == 403:
                raise Unavailable(f"The API user has no read permission on {what}.")
            if e.code == 404:
                raise Unavailable(f"{what} does not exist on this site. The app that provides it may not be installed.")
            if e.code == 417:
                raise Unavailable(f"The site refused the query on {what} (HTTP 417). A field may not exist in this version.")
            raise Unavailable(f"Reading {what} failed with HTTP {e.code}.")

    def rows(self, doctype: str, fields: list, filters: list, order_by: str | None = None):
        """Every matching row, paged. Returns (rows, truncated)."""
        def run():
            out, start = [], 0
            while True:
                p = {"fields": json.dumps(fields), "filters": json.dumps(filters),
                     "limit_page_length": PAGE, "limit_start": start}
                if order_by:
                    p["order_by"] = order_by
                page = self.get("/api/resource/" + urllib.parse.quote(doctype), p).get("data") or []
                out.extend(page)
                start += PAGE
                if len(page) < PAGE:
                    return out, False
                if len(out) >= MAX_ROWS:
                    return out, True
        return self._guard(doctype, run)

    def count(self, doctype: str, filters: list) -> int:
        return self._guard(doctype, lambda: int(self.get(
            "/api/method/frappe.client.get_count",
            {"doctype": doctype, "filters": json.dumps(filters)}).get("message") or 0))

    def method(self, dotted: str):
        return self._guard(dotted, lambda: self.get("/api/method/" + dotted).get("message"))


def _unwrap(o):
    """frappectl prints the API result; depending on the endpoint it may still be inside data/message."""
    while isinstance(o, dict) and o and set(o) <= {"data", "message", "has_next_page"} and ("data" in o or "message" in o):
        o = o["data"] if "data" in o else o["message"]
    return o


class CtlSite:
    """The same three reads through Frappe's own `frappectl` client (an OAuth or keyring profile).

    Only read commands are run: `doc list` and `api ... -X GET`. A read-only profile allows both.
    """

    def __init__(self, profile: str | None, timeout: int = 180):
        cmd = [c.strip(chr(34)) for c in shlex.split(os.environ.get("FRAPPECTL", "frappectl"), posix=(os.name != "nt"))]
        if not (shutil.which(cmd[0]) or Path(cmd[0]).exists()):
            raise Fatal("frappectl is not installed. The user can install it with `uv tool install frappectl` "
                        "or `pip install frappectl`, then sign in with `frappectl auth login <site> --oauth --read-only`.")
        self._cmd = cmd + (["-s", profile] if profile else [])
        self._env_key = bool(not profile and os.environ.get("FRAPPE_API_KEY"))   # frappectl's sign-in without a profile
        self.base = profile or os.environ.get("FRAPPE_SITE") or "frappectl default profile"
        self.timeout = timeout
        self.requests = 0

    def _run(self, args: list, what: str):
        self.requests += 1
        try:
            r = subprocess.run(self._cmd + args, capture_output=True, text=True, encoding="utf-8",
                               errors="replace", timeout=self.timeout)
        except subprocess.TimeoutExpired:
            raise Unavailable(f"Reading {what} through frappectl timed out.")
        if r.returncode != 0:
            lines = [x for x in (r.stderr or r.stdout or "").strip().splitlines() if x.strip()]
            low = " ".join(lines).lower()
            if "401" in low or "not logged in" in low or "auth login" in low or "unauthorized" in low:
                if self._env_key or "api key" in low:
                    raise Fatal("the site refused frappectl's sign-in (401). If frappectl uses a profile, the user "
                                "signs in again with: frappectl auth login <site> --oauth --read-only. If it uses "
                                "FRAPPE_API_KEY and FRAPPE_API_SECRET, that key or secret is wrong.")
                raise Fatal("frappectl is not signed in to this site. The user signs in with: "
                            "frappectl auth login <site> --oauth --read-only")
            if "403" in low or "permission" in low or "not permitted" in low:
                raise Unavailable(f"The signed-in user has no read permission on {what}.")
            if "404" in low or "not found" in low or "does not exist" in low:
                raise Unavailable(f"{what} does not exist on this site. The app that provides it may not be installed.")
            raise Unavailable(f"Reading {what} through frappectl failed: {(lines[-1] if lines else 'no message')[:200]}")
        try:
            return _unwrap(json.loads(r.stdout))
        except json.JSONDecodeError:
            raise Unavailable(f"frappectl did not return JSON for {what}.")

    def rows(self, doctype: str, fields: list, filters: list, order_by: str | None = None):
        args = ["doc", "list", doctype, "--fields", ",".join(fields), "--all", "--json"]
        if filters:
            args += ["--filters-json", json.dumps(filters)]
        out = self._run(args, doctype)
        if not isinstance(out, list):
            raise Unavailable(f"frappectl returned an unexpected shape for {doctype}.")
        return out, False

    def count(self, doctype: str, filters: list) -> int:
        return len(self.rows(doctype, ["name"], filters)[0])

    def method(self, dotted: str):
        return self._run(["api", "method/" + dotted, "-X", "GET"], dotted)


# ----------------------------------------------------------------------------- agents

ROLES = {"Rukaz": "Setup & Configuration", "Wafir": "Bulk Import & Migration", "Imran": "App Builder & Customizer",
         "Dhukhr": "Inventory & Stock", "Mizan": "Accounting, Tax & Reporting", "Zahir": "Marketing & Website",
         "Hazim": "Sales Operations & Projects", "Anees": "Customers, Support & People", "Urwah": "API, Bench & Automation"}
OUTCOMES = ("done", "partial", "failed", "refused")


def agents_section(path: str | None, days: int = 30):
    """Summarise .frappe/activity.jsonl. Returns (section or None, note or None).

    The log is written by the agents themselves, one line per finished request. It is a record of
    what they reported, not a check against the site, and the page says so.
    """
    p = Path(path) if path else Path(".frappe") / "activity.jsonl"
    if not p.exists():
        return None, ("No agent activity has been logged yet. The page fills in as the agents work: each finished "
                      "request adds one line to .frappe/activity.jsonl.")
    now = dt.datetime.now().astimezone()
    cutoff = now - dt.timedelta(days=days)
    entries, skipped = [], 0
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            r = json.loads(line)
            ts = dt.datetime.fromisoformat(str(r["ts"]).replace("Z", "+00:00"))
            if ts.tzinfo is None:
                ts = ts.astimezone()
            if r.get("outcome") not in OUTCOMES:
                raise ValueError
        except Exception:
            skipped += 1
            continue
        if ts >= cutoff:
            entries.append((ts, r))
    entries.sort(key=lambda e: e[0])
    tot = Counter(r["outcome"] for _, r in entries)
    changing = [r for _, r in entries if num(r.get("changed")) > 0]
    blank = lambda a, role: {"agent": a, "role": role, "tasks": 0, "done": 0, "refused": 0, "failed": 0, "changed": 0, "last": None}
    per = {a: blank(a, role) for a, role in ROLES.items()}
    for ts, r in entries:
        a = str(r.get("agent") or "Unknown")[:40]
        row = per.setdefault(a, blank(a, ""))
        row["tasks"] += 1
        row["done"] += r["outcome"] == "done"
        row["refused"] += r["outcome"] == "refused"
        row["failed"] += r["outcome"] in ("failed", "partial")
        row["changed"] += int(num(r.get("changed")))
        row["last"] = ts.astimezone().date().isoformat()
    day_list = [(now.date() - dt.timedelta(days=i)).isoformat() for i in range(13, -1, -1)]
    per_day = Counter(ts.astimezone().date().isoformat() for ts, _ in entries)
    secs = [num(r.get("seconds")) for _, r in entries if num(r.get("seconds")) > 0]
    section = {
        "window_days": days, "total": len(entries),
        "done": tot["done"], "partial": tot["partial"], "failed": tot["failed"], "refused": tot["refused"],
        "records_changed": int(sum(num(r.get("changed")) for r in changing)),
        "changes": len(changing), "snapshotted": sum(1 for r in changing if r.get("snapshot") is True),
        "median_seconds": round(statistics.median(secs)) if secs else None,
        "by_agent": sorted(per.values(), key=lambda x: (-x["tasks"], x["agent"])),
        "by_day": {"days": day_list, "counts": [per_day[d] for d in day_list]},
        "by_adapter": [{"name": k, "count": v} for k, v in Counter(str(r.get("adapter") or "unknown") for _, r in entries).most_common()],
        "recent": [{"ts": ts.isoformat(timespec="minutes"), "agent": str(r.get("agent") or "")[:40],
                    "skill": str(r.get("skill") or "")[:60], "task": str(r.get("task") or "")[:80],
                    "outcome": r["outcome"], "changed": int(num(r.get("changed")))} for ts, r in entries[-12:][::-1]],
    }
    note = f"{skipped} line(s) of the activity log could not be read and were left out." if skipped else None
    return section, note


# ----------------------------------------------------------------------------- helpers

def month_list(today: dt.date, n: int) -> list:
    out, y, m = [], today.year, today.month
    for _ in range(n):
        out.append(f"{y:04d}-{m:02d}")
        y, m = (y - 1, 12) if m == 1 else (y, m - 1)
    return out[::-1]


def num(v) -> float:
    try:
        return float(v or 0)
    except (TypeError, ValueError):
        return 0.0


def by_month(rows, months, date_field, value_field) -> list:
    tot = defaultdict(float)
    for r in rows:
        tot[str(r.get(date_field) or "")[:7]] += num(r.get(value_field))
    return [round(tot[m], 2) for m in months]


def read_credentials(path: str | None) -> tuple:
    key, secret = os.environ.get("FRAPPE_API_KEY"), os.environ.get("FRAPPE_API_SECRET")
    if path:
        for line in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.match(r"\s*(api[_ ]?key|api[_ ]?secret)\s*[:=]\s*(\S+)", line, re.I)
            if m and "PASTE" not in m.group(2).upper():
                val = m.group(2).strip("\"'")
                if "secret" in m.group(1).lower():
                    secret = val
                else:
                    key = val
    if not key or not secret:
        raise Fatal("no API key and secret found. Set FRAPPE_API_KEY and FRAPPE_API_SECRET, or pass "
                    "--credentials <file> with `api_key = ...` and `api_secret = ...` lines.")
    return key, secret


# ----------------------------------------------------------------------------- collect

def collect(site, company: str | None, months_n: int, lang: str, activity: str | None = None) -> dict:
    today = dt.date.today()
    months = month_list(today, months_n)
    start = months[0] + "-01"
    tday = today.isoformat()
    notes, truncated = {}, []

    try:
        companies = site.rows("Company", ["name", "default_currency"], [])[0]
    except Unavailable as e:
        raise Fatal(f"cannot read the Company list, so there is nothing to report on. {e}")
    if not companies:
        raise Fatal("the site has no Company yet. Finish the ERPNext setup wizard first.")
    if company is None:
        if len(companies) > 1:
            raise Fatal("the site has several companies; pass --company with one of: "
                        + ", ".join(sorted(c["name"] for c in companies)))
        company = companies[0]["name"]
    comp = next((c for c in companies if c["name"] == company), None)
    if comp is None:
        raise Fatal(f"no company named {company!r} on this site.")

    def attempt(key, fn, default=None):
        try:
            return fn()
        except Unavailable as e:
            notes[key] = str(e)
            return default

    def listed(label, doctype, fields, filters):
        rows, cut = site.rows(doctype, fields, filters)
        if cut:
            truncated.append(label)
        return rows

    co = ["company", "=", company]

    system = {}

    def apps():
        v = site.method("frappe.utils.change_log.get_versions") or {}
        system["apps"] = [{"name": k, "version": (d or {}).get("version") or "?", "branch": (d or {}).get("branch")}
                          for k, d in v.items()]
    attempt("system.apps", apps)
    installed = {a["name"] for a in system.get("apps") or []}

    def needs_hr(key, fn):
        """Leave, attendance, expense claims and payroll live in the Frappe HR app (hrms)."""
        if installed and "hrms" not in installed:
            notes[key] = "Frappe HR (the hrms app) is not installed on this site."
            return None
        return attempt(key, fn)

    # ---- finance
    fin = {"months": months}
    si = attempt("finance.invoiced.sales", lambda: listed("sales invoices", "Sales Invoice",
                 ["posting_date", "base_net_total", "customer_name"],
                 [["docstatus", "=", 1], co, ["posting_date", ">=", start]]))
    pi = attempt("finance.invoiced.purchases", lambda: listed("purchase invoices", "Purchase Invoice",
                 ["posting_date", "base_net_total"], [["docstatus", "=", 1], co, ["posting_date", ">=", start]]))
    if si is not None and pi is not None:
        fin["sales_invoiced"] = by_month(si, months, "posting_date", "base_net_total")
        fin["purchases_invoiced"] = by_month(pi, months, "posting_date", "base_net_total")
    else:
        fin["months"] = None
    si_note, pi_note = notes.pop("finance.invoiced.sales", ""), notes.pop("finance.invoiced.purchases", "")
    if si_note or pi_note:
        notes["finance.invoiced"] = " ".join(x for x in (si_note, pi_note) if x)

    def receivables():
        rows = listed("unpaid sales invoices", "Sales Invoice",
                      ["name", "customer_name", "due_date", "outstanding_amount", "conversion_rate"],
                      [["docstatus", "=", 1], co, ["outstanding_amount", ">", 0]])
        buckets = Counter()
        open_rows = []
        for r in rows:
            amt = num(r.get("outstanding_amount")) * (num(r.get("conversion_rate")) or 1.0)
            due = str(r.get("due_date") or tday)[:10]
            days = (today - dt.date.fromisoformat(due)).days
            b = "not_due" if days <= 0 else "d1_30" if days <= 30 else "d31_60" if days <= 60 else "d61_90" if days <= 90 else "d90_plus"
            buckets[b] += amt
            if days > 0:
                open_rows.append({"invoice": r.get("name"), "customer": r.get("customer_name"),
                                  "due_date": due, "days_overdue": days, "amount": round(amt, 2)})
        total = sum(buckets.values())
        fin["receivables"] = {
            "total": round(total, 2), "overdue": round(total - buckets["not_due"], 2),
            "count": len(rows), "overdue_count": len(open_rows),
            "aging": [{"bucket": b, "amount": round(buckets[b], 2)} for b in ("not_due", "d1_30", "d31_60", "d61_90", "d90_plus")]}
        fin["top_overdue"] = sorted(open_rows, key=lambda r: -r["amount"])[:8]
    attempt("finance.receivables", receivables)

    def payables():
        rows = listed("unpaid purchase invoices", "Purchase Invoice",
                      ["due_date", "outstanding_amount", "conversion_rate"],
                      [["docstatus", "=", 1], co, ["outstanding_amount", ">", 0]])
        total = over = 0.0
        n_over = 0
        for r in rows:
            amt = num(r.get("outstanding_amount")) * (num(r.get("conversion_rate")) or 1.0)
            total += amt
            if str(r.get("due_date") or tday)[:10] < tday:
                over += amt
                n_over += 1
        fin["payables"] = {"total": round(total, 2), "overdue": round(over, 2), "count": len(rows), "overdue_count": n_over}
    attempt("finance.payables", payables)

    def cash():
        rows = listed("payment entries", "Payment Entry", ["posting_date", "payment_type", "base_paid_amount"],
                      [["docstatus", "=", 1], co, ["posting_date", ">=", start], ["payment_type", "in", ["Receive", "Pay"]]])
        fin["cash_in"] = by_month([r for r in rows if r.get("payment_type") == "Receive"], months, "posting_date", "base_paid_amount")
        fin["cash_out"] = by_month([r for r in rows if r.get("payment_type") == "Pay"], months, "posting_date", "base_paid_amount")
    attempt("finance.cash", cash)

    # ---- sales
    sales = {}
    if si is not None:
        per = defaultdict(float)
        for r in si:
            per[r.get("customer_name") or "?"] += num(r.get("base_net_total"))
        sales["top_customers"] = [{"name": k, "amount": round(v, 2)} for k, v in sorted(per.items(), key=lambda kv: -kv[1])[:8]]
    else:
        notes["sales.top_customers"] = si_note

    def orders():
        rows = listed("sales orders", "Sales Order", ["status", "base_net_total"],
                      [["docstatus", "=", 1], co, ["transaction_date", ">=", start]])
        agg = defaultdict(lambda: [0, 0.0])
        for r in rows:
            a = agg[r.get("status") or "?"]
            a[0] += 1
            a[1] += num(r.get("base_net_total"))
        sales["orders_by_status"] = [{"status": k, "count": v[0], "amount": round(v[1], 2)}
                                     for k, v in sorted(agg.items(), key=lambda kv: -kv[1][0])]
        opened = [v for k, v in agg.items() if k in ("To Deliver and Bill", "To Bill", "To Deliver", "On Hold")]
        sales["open_orders"] = {"count": sum(v[0] for v in opened), "amount": round(sum(v[1] for v in opened), 2)}
    attempt("sales.orders", orders)

    def quotations():
        rows = listed("quotations", "Quotation", ["base_net_total"], [["docstatus", "=", 1], co, ["status", "=", "Open"]])
        sales["open_quotations"] = {"count": len(rows), "amount": round(sum(num(r.get("base_net_total")) for r in rows), 2)}
    attempt("sales.quotations", quotations)

    def customers():
        sales["customers_total"] = site.count("Customer", [["disabled", "=", 0]])
        rows = listed("customers", "Customer", ["creation"], [["creation", ">=", start + " 00:00:00"]])
        c = Counter(str(r.get("creation") or "")[:7] for r in rows)
        sales["new_customers"] = [c[m] for m in months]
    attempt("sales.customers", customers)

    # ---- people
    people = {}

    def employees():
        rows = listed("employees", "Employee", ["status", "department", "date_of_joining", "relieving_date"], [co])
        active = [r for r in rows if r.get("status") == "Active"]
        dep = Counter((r.get("department") or "No department").split(" - ")[0] for r in active)
        people["headcount"] = len(active)
        people["by_department"] = [{"name": k, "count": v} for k, v in dep.most_common(12)]
        people["joined_12m"] = sum(1 for r in rows if str(r.get("date_of_joining") or "") >= start)
        people["left_12m"] = sum(1 for r in rows if r.get("status") == "Left" and str(r.get("relieving_date") or "") >= start)
    attempt("people.employees", employees)

    def leave():
        people["leave_requests_open"] = site.count("Leave Application", [co, ["status", "=", "Open"], ["docstatus", "=", 0]])
        people["on_leave_today"] = site.count("Leave Application", [co, ["status", "=", "Approved"], ["docstatus", "=", 1],
                                                                    ["from_date", "<=", tday], ["to_date", ">=", tday]])
    needs_hr("people.leave", leave)

    def attendance():
        rows = listed("attendance", "Attendance", ["status"], [co, ["docstatus", "=", 1], ["attendance_date", "=", tday]])
        c = Counter(r.get("status") or "?" for r in rows)
        people["attendance_today"] = [{"status": k, "count": v} for k, v in c.most_common()]
        if not rows:
            notes["people.attendance"] = "No attendance has been marked for today yet."
    needs_hr("people.attendance", attendance)

    def claims():
        rows = listed("expense claims", "Expense Claim", ["total_claimed_amount"], [co, ["docstatus", "=", 0]])
        people["expense_claims_pending"] = {"count": len(rows), "amount": round(sum(num(r.get("total_claimed_amount")) for r in rows), 2)}
    needs_hr("people.claims", claims)

    def payroll():
        since = (today - dt.timedelta(days=92)).isoformat()
        rows = listed("salary slips", "Salary Slip", ["start_date", "gross_pay", "net_pay"],
                      [co, ["docstatus", "=", 1], ["start_date", ">=", since]])
        if not rows:
            raise Unavailable("No salary slip was submitted in the last three months.")
        last = max(str(r.get("start_date"))[:10] for r in rows)
        cur = [r for r in rows if str(r.get("start_date"))[:10] == last]
        people["payroll_last"] = {"period": last[:7], "employees": len(cur),
                                  "gross": round(sum(num(r.get("gross_pay")) for r in cur), 2),
                                  "net": round(sum(num(r.get("net_pay")) for r in cur), 2)}
    needs_hr("people.payroll", payroll)

    # ---- system

    def scheduler():
        st = site.method("frappe.utils.scheduler.get_scheduler_status") or {}
        system["scheduler"] = st.get("status") if isinstance(st, dict) else str(st)
    attempt("system.scheduler", scheduler)

    def errors():
        days = [(today - dt.timedelta(days=i)).isoformat() for i in range(13, -1, -1)]
        rows = listed("error log", "Error Log", ["creation"], [["creation", ">=", days[0] + " 00:00:00"]])
        c = Counter(str(r.get("creation") or "")[:10] for r in rows)
        system["errors_by_day"] = {"days": days, "counts": [c[d] for d in days]}
        cutoff = (dt.datetime.now() - dt.timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")
        system["errors_24h"] = sum(1 for r in rows if str(r.get("creation") or "") >= cutoff)
    attempt("system.errors", errors)

    def jobs():
        cutoff = (dt.datetime.now() - dt.timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")
        rows = listed("scheduled job log", "Scheduled Job Log", ["scheduled_job_type"],
                      [["status", "=", "Failed"], ["creation", ">=", cutoff]])
        c = Counter(r.get("scheduled_job_type") or "?" for r in rows)
        system["failed_jobs_24h"] = [{"job": k, "count": v} for k, v in c.most_common(10)]
    attempt("system.jobs", jobs)

    def email():
        system["email_queue"] = {"not_sent": site.count("Email Queue", [["status", "=", "Not Sent"]]),
                                 "error": site.count("Email Queue", [["status", "=", "Error"]])}
    attempt("system.email", email)

    def users():
        system["users"] = {"enabled": site.count("User", [["enabled", "=", 1], ["name", "!=", "Guest"]]),
                           "system": site.count("User", [["enabled", "=", 1], ["user_type", "=", "System User"]])}
    attempt("system.users", users)

    notes.setdefault("system.backups", "Backup status cannot be read over the REST API. Check it with bench on the "
                                       "server, or on the Frappe Cloud dashboard.")

    agents, agents_note = agents_section(activity)
    if agents_note:
        notes["agents"] = agents_note

    return {
        "meta": {"company": company, "site": urllib.parse.urlparse(site.base).netloc or site.base, "currency": comp.get("default_currency") or "",
                 "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
                 "period_from": start, "period_to": tday, "demo": False, "lang": lang, "collector": VERSION,
                 "truncated": sorted(set(truncated))},
        "finance": fin, "sales": sales, "people": people, "system": system, "agents": agents, "notes": notes,
        "sources": json.loads(SAMPLE.read_text(encoding="utf-8"))["sources"],
    }


# ----------------------------------------------------------------------------- build

def build(data: dict, fmt: str) -> str:
    tpl = TEMPLATE.read_text(encoding="utf-8")
    if PLACEHOLDER not in tpl:
        raise Fatal(f"{TEMPLATE.name} has no {PLACEHOLDER} placeholder.")
    # "</" must not appear inside a <script> block; "<" is the same character to a JSON parser
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    page = tpl.replace(PLACEHOLDER, payload)
    if fmt == "artifact":
        return page                      # the Artifact tool wraps a fragment in its own document
    lang = (data.get("meta") or {}).get("lang") or "en"
    return ("<!doctype html>\n<html lang=\"%s\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            "<style>body{margin:0}</style>\n</head>\n<body>\n%s\n</body>\n</html>\n" % (lang, page))


def main() -> int:
    ap = argparse.ArgumentParser(description="Build the ERPNext Pulse dashboard. Read-only.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("demo", "collect", "build", "run"):
        p = sub.add_parser(name)
        p.add_argument("--out", required=True)
        p.add_argument("--lang", choices=("en", "ar"), default="en")
        if name in ("demo", "build", "run"):
            p.add_argument("--format", choices=("file", "artifact"), default="file",
                           help="file: a complete page to open in a browser. artifact: a fragment for Claude's Artifact tool.")
        if name == "build":
            p.add_argument("--data", required=True)
        if name in ("collect", "run"):
            p.add_argument("--site", default=os.environ.get("FRAPPE_URL") or os.environ.get("FRAPPE_SITE"))
            p.add_argument("--via", choices=("api", "frappectl"), default="api",
                           help="api: API key and secret. frappectl: a signed-in frappectl profile (OAuth or keyring).")
            p.add_argument("--profile", help="frappectl profile name; the default profile when omitted.")
            p.add_argument("--activity", help="path to the agents' activity log (default .frappe/activity.jsonl)")
            p.add_argument("--credentials")
            p.add_argument("--company")
            p.add_argument("--months", type=int, default=12)
    a = ap.parse_args()
    try:
        if a.cmd == "demo":
            data = json.loads(SAMPLE.read_text(encoding="utf-8"))
            data["meta"]["lang"] = a.lang
        elif a.cmd == "build":
            data = json.loads(Path(a.data).read_text(encoding="utf-8"))
        else:
            if a.via == "frappectl":
                site = CtlSite(a.profile)
            else:
                if not a.site:
                    raise Fatal("pass --site https://your-site (or set FRAPPE_URL), or use --via frappectl.")
                if a.site.startswith("http://") and not re.match(r"http://(localhost|127\.0\.0\.1|\[::1\])(:|/|$)", a.site):
                    print("WARNING: --site is plain http; the API key travels unencrypted. Use https outside your own machine.", file=sys.stderr)
                key, secret = read_credentials(a.credentials)
                site = Site(a.site, key, secret)
            data = collect(site, a.company, max(2, min(24, a.months)), a.lang, a.activity)
            print(f"read {site.base} with {site.requests} read requests; "
                  f"{len(data['notes'])} metric(s) unavailable; partial lists: {data['meta']['truncated'] or 'none'}")
            for k, v in sorted(data["notes"].items()):
                print(f"  - {k}: {v}")
        if a.cmd == "collect":
            Path(a.out).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        else:
            Path(a.out).write_text(build(data, a.format), encoding="utf-8", newline="\n")
        print(f"wrote {a.out}")
        return 0
    except Fatal as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
