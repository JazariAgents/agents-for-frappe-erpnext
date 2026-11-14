#!/usr/bin/env python3
"""Call a Frappe site with the API key in .frappe/credentials.txt, without the key ever reaching the output.

Every skill in this plugin uses this script for the API-key route instead of writing its own HTTP code.
It reads the key itself, sends the request, and prints the answer as JSON. The key and secret are removed
from everything it prints, including error messages and tracebacks.

    python frappe_call.py whoami
    python frappe_call.py GET  /api/v2/document/ToDo --query '{"fields": ["name", "status"], "limit": 20}'
    python frappe_call.py GET  /api/v2/document/ToDo --query '{"fields": ["name"]}' --all
    python frappe_call.py POST /api/v2/document/ToDo --data '{"description": "Call the bank"}' --write
    python frappe_call.py PUT  /api/v2/document/ToDo/abc123 --data-file change.json --write
    python frappe_call.py UPLOAD ./customers.csv --write
    python frappe_call.py snapshot --op close-todos --request "Close all test ToDos" --class reversible \\
        --doc ToDo abc123 --doc ToDo def456

Rules it enforces:
  * Anything but GET changes the site, so it is refused unless --write is given. Give --write only after the
    snapshot is taken and verified and the user has said yes (see the snapshot spec in frappe-connect).
    The ERPNext "mapper" methods (make_sales_order and the like) only return an unsaved document; they are
    POST calls, so they also need --write, and that is fine: they change nothing until the result is saved.
  * A call that changes or deletes an existing record is refused unless that exact record has a snapshot from
    the last hour. This holds for every verb and every form of the address (v1 and v2, record methods, bulk
    calls, and GET calls to methods that write). The rules are in frappe_safety.py, shared with the MCP guard.
  * A change is refused until the user has replied after its snapshot was saved (the plugin's hooks record
    the time of each message; where no hook runs, this check cannot be made). Snapshot first, then ask.
  * A call the rules do not recognise is refused. If it only reads or creates something new, tell the user the
    plugin cannot check it and stop; after their yes, repeat it with --unlisted-method (the flag works only
    after that refusal and the user's reply).
  * The answer's `data` (or `message`) is printed as JSON on standard output; --out writes the whole answer
    to a file instead and prints a one-line summary.
  * On an HTTP error it prints the status and the site's own reason, and exits 1.

Options: --site URL (default: site_url in .frappe/state.json), --credentials PATH (default
.frappe/credentials.txt), --workspace DIR (default: the current folder).
"""
import argparse
import datetime as dt
import json
import os
import random
import re
import string
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SECRETS = []


def redact(text):
    text = str(text)
    for s in SECRETS:
        if s and len(s) >= 4:
            text = text.replace(s, "****")
    return text


def die(msg, code=2):
    sys.stderr.write(redact("frappe_call: " + msg) + "\n")
    sys.exit(code)


def read_credentials(path):
    """Accepts `api_key = x` / `api_secret = y` lines (the plugin's format), `KEY=...` lines, `key:secret`,
    or a JSON object. Comment lines (#) and blank lines are ignored."""
    try:
        raw = Path(path).read_text(encoding="utf-8-sig")
    except OSError as e:
        die(f"cannot read {path}: {e.strerror}. Run the frappe-connect skill to set up the key.")
    key = secret = None
    text = raw.strip()
    if text.startswith("{"):
        try:
            j = json.loads(text)
            key, secret = j.get("api_key"), j.get("api_secret")
        except ValueError:
            pass
    if not key:
        for line in raw.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            m = re.match(r"^(?:export\s+)?([A-Za-z_]+)\s*[:=]\s*[\"']?([^\"'\s]+)[\"']?\s*$", line)
            if m:
                name, val = m.group(1).lower(), m.group(2)
                if name in ("api_key", "key", "frappe_api_key"):
                    key = val
                elif name in ("api_secret", "secret", "frappe_api_secret"):
                    secret = val
            elif re.fullmatch(r"[A-Za-z0-9]+:[A-Za-z0-9]+", line):
                key, secret = line.split(":", 1)
    for v in (key, secret):
        if v:
            SECRETS.append(v)
    if not key or not secret or "PASTE" in key.upper() or "PASTE" in secret.upper():
        die(f"{path} has no usable api_key and api_secret lines yet. The user fills them in; never ask for them in chat.")
    return key, secret


def site_url(args, ws):
    if args.site:
        return args.site.rstrip("/")
    try:
        st = json.loads((ws / ".frappe" / "state.json").read_text(encoding="utf-8"))
        url = st.get("site_url") or st.get("site")
        if url:
            return url.rstrip("/")
    except (OSError, ValueError):
        pass
    die("no --site given and no site_url in .frappe/state.json.")


EXPLAIN = {
    401: "the site rejected the key (wrong or regenerated key, or a Restrict IP list on the user).",
    403: "the API user lacks a role for this record type, method or a record it touches. Name it; do not retry.",
    404: "no such record, DocType or method on this site (the app may not be installed).",
    417: "the site refused the data (a validation error). Repeat its message to the user.",
    429: "rate limited. Wait for Retry-After; do not retry in a loop.",
}


def reason(body):
    try:
        j = json.loads(body)
    except ValueError:
        return body[:400]
    out = []
    for e in j.get("errors") or []:
        out.append(str(e.get("message") or e.get("type")))
    if j.get("_server_messages"):
        try:
            for m in json.loads(j["_server_messages"]):
                out.append(json.loads(m).get("message", m) if isinstance(m, str) and m.startswith("{") else str(m))
        except (ValueError, TypeError):
            out.append(str(j["_server_messages"]))
    if not out and j.get("exc_type"):
        out.append(j["exc_type"])
    text = " | ".join(out) or body[:400]
    return re.sub(r"<[^>]+>", "", text)


def api_path(path):
    """Git Bash on Windows turns an argument such as /api/v2/... into C:/Program Files/Git/api/v2/...
    before this script sees it. Undo that, and accept the path with or without its leading slash."""
    path = path.replace("\\", "/")
    i = path.find("/api/")
    if i > 0:
        path = path[i:]
    elif path.startswith("api/"):
        path = "/" + path
    return path if path.startswith("/") else "/" + path


def request(base, auth, method, path, query=None, data=None, raw=None, ctype=None):
    path = api_path(path)
    p, _, q = path.partition("?")
    url = base + urllib.parse.quote(urllib.parse.unquote(p))
    params = dict(urllib.parse.parse_qsl(q)) if q else {}
    for k, v in (query or {}).items():
        params[k] = v if isinstance(v, str) else json.dumps(v)
    if params:
        url += "?" + urllib.parse.urlencode(params)
    body = raw if raw is not None else (json.dumps(data).encode() if data is not None else None)
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("Authorization", auth)
    req.add_header("Accept", "application/json")
    if body is not None:
        req.add_header("Content-Type", ctype or "application/json")
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            txt = r.read().decode("utf-8", "replace")
            return r.status, (json.loads(txt) if txt.strip() else None), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace"), dict(e.headers)
    except urllib.error.URLError as e:
        die(f"could not reach {base}: {e.reason}", 1)


def fail(status, body, headers):
    msg = f"HTTP {status}: {reason(body)}"
    if status == 401 and "IP Address" in body:
        msg += "\nThe key is fine: the user has a Restrict IP list and this address is not on it."
    elif status in EXPLAIN:
        msg += "\n" + EXPLAIN[status]
    if status == 429 and headers.get("Retry-After"):
        msg += f" Retry-After: {headers.get('Retry-After')} s."
    die(msg, 1)


sys.path.insert(0, str(Path(__file__).resolve().parent))
import frappe_safety  # noqa: E402  the plugin's one set of snapshot rules, shared with the MCP guard hook


def fetch_text(base, auth, file_url):
    """An uploaded file on the connected site (an import's CSV) as text; None when it cannot be read."""
    if not str(file_url).startswith(("/private/files/", "/files/")):
        return None                             # only files stored on the site itself
    req = urllib.request.Request(base + urllib.parse.quote(urllib.parse.unquote(file_url)), method="GET")
    req.add_header("Authorization", auth)
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return r.read().decode("utf-8-sig", "replace")
    except (urllib.error.HTTPError, urllib.error.URLError):
        return None


def doctype_meta(base, auth, doctype):
    """The record type's definition as the site gives it, or None when it cannot be read."""
    if not doctype:
        return None
    st, j, _ = request(base, auth, "GET", f"/api/v2/doctype/{urllib.parse.quote(str(doctype), safe='')}/meta")
    meta = payload(j) if st == 200 else None
    return meta if isinstance(meta, dict) else None


def import_records(base, auth, data_import):
    """(records, reason). The records starting this import needs snapshots of: the import, plus every record an
    update import changes. Their IDs come from the import's dry run (it saves nothing), or from the file itself
    when the dry run does not show every row. records is None, with the reason, when they cannot be worked out."""
    di = urllib.parse.quote(str(data_import), safe="")
    st, j, _ = request(base, auth, "GET", f"/api/v2/document/Data%20Import/{di}")
    rec = payload(j) if st == 200 else None
    if not isinstance(rec, dict):
        return None, f"the import {data_import} could not be read from the site, so starting it is refused."
    preview = file_text = id_field = None
    if rec.get("import_type") == "Update Existing Records":
        meta = doctype_meta(base, auth, rec.get("reference_doctype"))
        if isinstance(meta, dict):              # a record type named by one of its fields is identified by that field
            auto = str(meta.get("autoname") or "")
            id_field = auto[len("field:"):] if auto.startswith("field:") else "name"
        st, j, _ = request(base, auth, "POST", f"/api/v2/document/Data%20Import/{di}/method/get_preview_from_template", data={})
        preview = payload(j) if st == 200 else None
        if isinstance(preview, dict) and preview.get("max_rows_exceeded"):
            name = str(rec.get("import_file") or "")
            if not name.lower().endswith(".csv"):
                return None, ("this update import has more rows than its dry run shows, and its file is not a .csv, so "
                              "the plugin cannot read every row's ID to check its snapshot. Use a .csv file for an "
                              "update import of more than 10 rows, or ask the user to start it from the Data Import screen.")
            file_text = fetch_text(base, auth, name)
    found = frappe_safety.import_targets(rec, preview, file_text, id_field)
    if found is None:
        return None, (f"cannot tell which records the import {data_import} changes (its type, or for an update import "
                      "the ID column of its rows), so starting it is refused. Check the import's dry run and its file.")
    return found, ""


def payload(j):
    if isinstance(j, dict):
        for k in ("data", "message"):
            if k in j:
                return j[k]
    return j


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("method", help="GET, POST, PUT, DELETE, UPLOAD, whoami or snapshot")
    ap.add_argument("path", nargs="?", help="API path, or the file for UPLOAD")
    ap.add_argument("--query", help="JSON object of query parameters (fields, filters, limit, start, order_by ...)")
    ap.add_argument("--data", help="JSON body")
    ap.add_argument("--data-file", help="file holding the JSON body")
    ap.add_argument("--all", action="store_true", help="GET a list: follow every page (limit 500 per page)")
    ap.add_argument("--write", action="store_true", help="allow a call that changes the site (after snapshot + yes)")
    ap.add_argument("--unlisted-method", action="store_true",
                    help="allow a call the plugin's rules do not know, after telling the user it cannot be checked and getting a yes")
    ap.add_argument("--private", action="store_true", default=True, help="UPLOAD as a private file (default)")
    ap.add_argument("--public", action="store_true", help="UPLOAD as a public file")
    ap.add_argument("--out", help="write the whole answer to this file")
    ap.add_argument("--site")
    ap.add_argument("--credentials")
    ap.add_argument("--workspace", help="the folder that holds .frappe/ (default: this folder or the nearest one above it)")
    ap.add_argument("--op", help="snapshot: short name of the operation")
    ap.add_argument("--request", help="snapshot: the user's request, word for word")
    ap.add_argument("--class", dest="rclass", help="snapshot: reversible, recreate or irreversible")
    ap.add_argument("--environment", default=None, help="snapshot: production or test")
    ap.add_argument("--doc", nargs=2, action="append", metavar=("DOCTYPE", "NAME"), help="snapshot: a record to save (repeat)")
    a = ap.parse_args()
    for stream in (sys.stdout, sys.stderr):     # the site's answer may hold any language; never fail on printing it
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    ws = Path(a.workspace).resolve() if a.workspace else (frappe_safety.find_workspace(os.getcwd()) or Path.cwd())
    key, secret = read_credentials(a.credentials or ws / ".frappe" / "credentials.txt")
    auth = f"token {key}:{secret}"
    base = site_url(a, ws)
    m = a.method.upper()

    if m == "WHOAMI":
        st, j, h = request(base, auth, "GET", "/api/method/frappe.auth.get_logged_user")
        if st != 200:
            fail(st, j if isinstance(j, str) else json.dumps(j), h)
        print(json.dumps({"site": base, "user": payload(j)}))
        return

    if m == "SNAPSHOT":
        if not (a.op and a.request and a.rclass and a.doc):
            die("snapshot needs --op, --request, --class and at least one --doc DOCTYPE NAME")
        now = dt.datetime.now()
        folder = ws / ".frappe" / "snapshots" / f"{now:%Y-%m-%d_%H%M%S}_{re.sub(r'[^a-z0-9-]+', '-', a.op.lower())}_{''.join(random.choices(string.ascii_lowercase + string.digits, k=4))}"
        records = []
        for dtp, name in a.doc:
            st, j, h = request(base, auth, "GET", f"/api/v2/document/{dtp}/{name}")
            if st != 200:
                fail(st, j if isinstance(j, str) else json.dumps(j), h)
            records.append({"doctype": dtp, "name": name, "response": j})
        (folder / "images").mkdir(parents=True, exist_ok=True)
        raw_path = folder / "raw.json"
        raw_path.write_text(redact(json.dumps(records, indent=1, ensure_ascii=False)), encoding="utf-8")
        env = a.environment
        if not env:
            try:
                env = json.loads((ws / ".frappe" / "state.json").read_text(encoding="utf-8")).get("environment")
            except (OSError, ValueError):
                env = "unknown"
        (folder / "SNAPSHOT.md").write_text(
            f"# Snapshot {folder.name}\n\n- When: {now:%Y-%m-%d %H:%M:%S}\n- Site: {base}\n- Environment: {env}\n"
            f"- Request (verbatim): {a.request}\n- Reversibility: {a.rclass}\n- Records: {len(records)}\n"
            + "".join(f"  - {r['doctype']} {r['name']}\n" for r in records)
            + "\n## Restore\nAsk the frappe-restore skill to restore this snapshot. Settings come back exactly; deleted records "
              "come back as new records; submitted or sent documents cannot be undone.\n", encoding="utf-8")
        # verify: it must read back and contain every record
        back = json.loads(raw_path.read_text(encoding="utf-8"))
        held = frappe_safety.snapshot_pairs(back)
        lost = [f"{d} {n}" for d, n in a.doc if (d, n) not in held]
        if len(back) != len(records) or not all(r["response"] for r in back) or lost:
            die(f"snapshot at {folder} did not verify" + (f" (not held in full: {', '.join(lost[:5])}; give each "
                "record's exact type and name)" if lost else "") + ". Do not make the change.", 1)
        print(json.dumps({"snapshot": str(folder.relative_to(ws)), "records": len(records), "verified": True}))
        return

    if m not in ("GET", "POST", "PUT", "DELETE", "UPLOAD", "PATCH"):
        die(f"unknown method {a.method}")
    if not a.path:
        die("a path is needed")
    query = json.loads(a.query) if a.query else None
    body_preview = None
    if a.data_file:
        body_preview = json.loads(Path(a.data_file).read_text(encoding="utf-8-sig"))
    elif a.data:
        body_preview = json.loads(a.data)
    kind, targets = ("allow", []) if m == "UPLOAD" else frappe_safety.classify_request(m, api_path(a.path), body_preview, query)
    if (m != "GET" or kind != "allow") and not a.write:
        die(f"{m} {'to this method ' if m == 'GET' else ''}changes the site. Take and verify the snapshot, tell the user "
            "the reversibility class and the count, get a clear yes, then repeat this command with --write.")
    if kind == "unnamed":
        die("this call changes records but does not say which ones (doctype and name), or names them "
            "inconsistently, so their snapshot cannot be checked and it is refused. Put each record's doctype and "
            "name in the data, or use the record's own address.")
    if kind == "unknown":
        key = m + " " + frappe_safety.split_api_path(api_path(a.path))[2]
        if isinstance(body_preview, dict) and body_preview.get("cmd"):
            key += " cmd=" + str(body_preview.get("cmd"))
        if not frappe_safety.unlisted_call_allowed(ws, key, a.unlisted_method):
            die("the plugin's rules do not know this call, so they cannot tell which records it changes, and it is "
                "refused. If it changes an existing record, use the record's own address (PUT or DELETE "
                "/api/v2/document/<DocType>/<name>, or .../method/<method>), or name the record (doctype and name) "
                "in the data, so its snapshot can be checked. If it only reads or creates something new, tell the "
                "user the plugin cannot check this call and stop. After they reply with a clear yes, repeat it with "
                "--unlisted-method. The flag works only after this refusal and the user's reply.")
    if kind == "import":
        targets, why = import_records(base, auth, targets[0][1])
        if targets is None:
            die(why)
    if kind == "allow" and m != "UPLOAD":
        # The site knows settings record types the bundled list does not. Creating one replaces its settings.
        for made in list(dict.fromkeys(frappe_safety.created_doctypes(m, api_path(a.path), body_preview, query)))[:8]:
            meta = doctype_meta(base, auth, made)
            if meta is None and frappe_safety.settings_like(made):
                die(f"could not ask the site whether {made} is a settings record type. If it is, creating it replaces "
                    "the stored settings. Snapshot it and update it with PUT instead, or check the API user can read "
                    "the record type's definition.")
            if meta and meta.get("issingle"):
                targets = targets + [(made, made)]
    missing = frappe_safety.missing_snapshots(ws, targets)
    if missing:
        docs = " ".join(f'--doc "{dt_}" "{name_}"' for dt_, name_ in missing[:40])
        what = ", ".join(f"{dt_} {name_}" for dt_, name_ in missing[:5]) + (f" and {len(missing) - 5} more" if len(missing) > 5 else "")
        die(f"no snapshot of {what} in .frappe/snapshots/ from the last hour, so this change is refused. "
            f"Run: frappe_call.py snapshot --op <name> --request \"<the user's words>\" --class <class> {docs}"
            + (" (and one --doc for each of the rest)" if len(missing) > 40 else "")
            + ", tell the user what will change, wait for their reply, then repeat this command.")
    late = frappe_safety.unconfirmed(ws, targets, strict=False)
    if late:
        what = ", ".join(f"{dt_} {name_}" for dt_, name_ in late[:5]) + (f" and {len(late) - 5} more" if len(late) > 5 else "")
        die(f"the user has not replied since the snapshot of {what} was saved, so nothing shows they said yes to "
            "this change, and it is refused. The request itself is never the yes. Tell the user what will change, "
            "how many records, and whether it can be undone; wait for their reply; then repeat this command as it "
            "is. Do not take the snapshot again.")

    if m == "UPLOAD":
        f = Path(a.path)
        if not f.is_file():
            die(f"no such file: {f}")
        bnd = "----frappecall" + "".join(random.choices(string.ascii_letters, k=12))
        priv = "0" if a.public else "1"
        body = (f"--{bnd}\r\nContent-Disposition: form-data; name=\"is_private\"\r\n\r\n{priv}\r\n"
                f"--{bnd}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{f.name}\"\r\n"
                f"Content-Type: application/octet-stream\r\n\r\n").encode() + f.read_bytes() + f"\r\n--{bnd}--\r\n".encode()
        st, j, h = request(base, auth, "POST", "/api/v2/method/upload_file", raw=body, ctype=f"multipart/form-data; boundary={bnd}")
        if st != 200:
            fail(st, j if isinstance(j, str) else json.dumps(j), h)
        print(json.dumps(payload(j), ensure_ascii=False))
        return

    data = body_preview

    if m == "GET" and a.all:
        q = dict(query or {})
        size = int(q.pop("limit", 500)) or 500
        start, rows = 0, []
        while True:
            q2 = dict(q, limit=str(size), start=str(start))
            st, j, h = request(base, auth, "GET", a.path, query=q2)
            if st != 200:
                fail(st, j if isinstance(j, str) else json.dumps(j), h)
            page = payload(j) or []
            rows += page
            if not (isinstance(j, dict) and j.get("has_next_page")) or not page:
                break
            start += len(page)
        result = rows
    else:
        st, j, h = request(base, auth, m, a.path, query=query, data=data)
        if not (200 <= st < 300):
            fail(st, j if isinstance(j, str) else json.dumps(j), h)
        result = payload(j)

    text = redact(json.dumps(result, indent=1, ensure_ascii=False, default=str))
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
        n = len(result) if isinstance(result, list) else 1
        print(json.dumps({"written": a.out, "records": n}))
    else:
        print(text)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except BaseException as e:  # noqa: BLE001 - nothing may escape with a secret in it
        sys.stderr.write(redact(f"frappe_call: {type(e).__name__}: {e}") + "\n")
        sys.exit(1)
