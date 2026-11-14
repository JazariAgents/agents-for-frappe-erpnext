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


WRITE_METHODS = ("frappe.client.submit", "frappe.client.cancel", "frappe.client.delete", "frappe.client.set_value",
                 "frappe.client.save", "frappe.client.rename_doc", "frappe.model.rename_doc")


def changes_existing(method, path, body):
    """(doctype, name) when this call changes or removes an existing record, else None.
    Creating a record, uploading a file and calling read-only or mapper methods change nothing that exists."""
    p = urllib.parse.unquote(path)
    m = re.match(r"^/api/(?:v2/document|resource)/([^/]+)/([^/]+)(?:/method/([^/?]+))?", p)
    if m and (method in ("PUT", "PATCH", "DELETE") or (method == "POST" and m.group(3))):
        if m.group(3) and m.group(3) not in ("submit", "cancel", "save", "rename", "amend") and not m.group(3).startswith(("set_", "update", "delete", "remove", "close", "reopen", "make_payment")):
            return None                         # a document method that only reads, such as get_preview_from_template
        return m.group(1), m.group(2)
    m = re.match(r"^/api/(?:v2/)?method/([A-Za-z0-9_.]+)", p)
    if m and method == "POST" and m.group(1) in WRITE_METHODS and isinstance(body, dict):
        doc = body.get("doc") if isinstance(body.get("doc"), dict) else body
        if doc.get("doctype") and doc.get("name"):
            return doc["doctype"], doc["name"]
    return None


def snapshot_has(ws, doctype, name, window=3600):
    import time
    snaps = ws / ".frappe" / "snapshots"
    if not snaps.is_dir():
        return False
    for d in snaps.iterdir():
        raw = d / "raw.json"
        try:
            if time.time() - raw.stat().st_mtime > window:
                continue
            text = raw.read_text(encoding="utf-8", errors="replace")
            json.loads(text)
        except (OSError, ValueError):
            continue
        if doctype in text and str(name) in text:
            return True
    return False


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
    ap.add_argument("--private", action="store_true", default=True, help="UPLOAD as a private file (default)")
    ap.add_argument("--public", action="store_true", help="UPLOAD as a public file")
    ap.add_argument("--out", help="write the whole answer to this file")
    ap.add_argument("--site")
    ap.add_argument("--credentials")
    ap.add_argument("--workspace", default=".")
    ap.add_argument("--op", help="snapshot: short name of the operation")
    ap.add_argument("--request", help="snapshot: the user's request, word for word")
    ap.add_argument("--class", dest="rclass", help="snapshot: reversible, recreate or irreversible")
    ap.add_argument("--environment", default=None, help="snapshot: production or test")
    ap.add_argument("--doc", nargs=2, action="append", metavar=("DOCTYPE", "NAME"), help="snapshot: a record to save (repeat)")
    a = ap.parse_args()

    ws = Path(a.workspace).resolve()
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
        ok = len(back) == len(records) and all(r["response"] for r in back)
        if not ok:
            die(f"snapshot at {folder} did not verify. Do not make the change.", 1)
        print(json.dumps({"snapshot": str(folder.relative_to(ws)), "records": len(records), "verified": True}))
        return

    if m not in ("GET", "POST", "PUT", "DELETE", "UPLOAD", "PATCH"):
        die(f"unknown method {a.method}")
    if m != "GET" and not a.write:
        die(f"{m} changes the site. Take and verify the snapshot, tell the user the reversibility class and the count, "
            "get a clear yes, then repeat this command with --write.")
    if not a.path:
        die("a path is needed")
    body_preview = None
    if a.data_file:
        body_preview = json.loads(Path(a.data_file).read_text(encoding="utf-8"))
    elif a.data:
        body_preview = json.loads(a.data)
    target = changes_existing(m, api_path(a.path), body_preview)
    if target and not snapshot_has(ws, *target):
        dt_, name_ = target
        die(f"no snapshot of {dt_} {name_} in .frappe/snapshots/ from the last hour, so this change is refused. "
            f"Run: frappe_call.py snapshot --op <name> --request \"<the user's words>\" --class <class> --doc \"{dt_}\" \"{name_}\" "
            "(one --doc per record), get the user's yes, then repeat this command.")

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

    query = json.loads(a.query) if a.query else None
    data = None
    if a.data_file:
        data = json.loads(Path(a.data_file).read_text(encoding="utf-8"))
    elif a.data:
        data = json.loads(a.data)

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
