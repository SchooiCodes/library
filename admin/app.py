#!/usr/bin/env python3
"""Tech Library Admin Panel — manage pages, preview changes, control content."""
import os, json, hashlib, uuid, time
from pathlib import Path
from flask import (
    Flask, render_template, request, redirect,
    url_for, session, abort, jsonify, flash,
)

SITE_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = Path(__file__).resolve().parent / "config.json"

app = Flask(__name__)

# ---------- config ----------
def load_config():
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text())
    return {"username": "admin", "password": "admin123", "secret": uuid.uuid4().hex}

def save_config(cfg):
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2))

cfg = load_config()
app.secret_key = cfg.get("secret", uuid.uuid4().hex)

# ---------- auth ----------
def require_auth():
    if not session.get("logged_in"):
        return redirect(url_for("login_page"))

def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

@app.route("/login", methods=["GET", "POST"])
def login_page():
    if session.get("logged_in"):
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        u = request.form.get("username", "")
        p = request.form.get("password", "")
        if u == cfg["username"] and hash_pw(p) == hash_pw(cfg["password"]):
            session["logged_in"] = True
            session["username"] = u
            return redirect(url_for("dashboard"))
        return render_template("login.html", error=True)
    return render_template("login.html", error=False)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login_page"))

# ---------- helpers ----------
def get_pages_data():
    pages = []
    for f in sorted(SITE_ROOT.rglob("*.html")):
        if "admin" in str(f):
            continue
        rel = str(f.relative_to(SITE_ROOT))
        try:
            mtime = f.stat().st_mtime
            size = f.stat().st_size
            content = f.read_text(encoding="utf-8", errors="replace")
            word_count = len(content.split())
        except Exception:
            mtime, size, word_count = 0, 0, 0
        pages.append({
            "path": rel,
            "name": f.stem,
            "dir": str(f.relative_to(SITE_ROOT).parent) if f.relative_to(SITE_ROOT).parent != Path(".") else "",
            "size": size,
            "mtime": mtime,
            "words": word_count,
        })
    priority_map = {"": 0, "tutorials": 1, "docs": 2, "resources": 3, "programming": 4}
    return sorted(pages, key=lambda p: (priority_map.get(p["dir"], 5), p["path"]))

def get_file_content(path):
    full = SITE_ROOT / path
    if not full.exists() or not full.is_file():
        return None
    return full.read_text(encoding="utf-8", errors="replace")

def save_file(path, content):
    full = SITE_ROOT / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content, encoding="utf-8")
    return True

def get_site_css():
    css_path = SITE_ROOT / "assets" / "style.css"
    if css_path.exists():
        return css_path.read_text(encoding="utf-8", errors="replace")
    return ""

# ---------- routes ----------
@app.route("/")
def dashboard():
    resp = require_auth()
    if resp: return resp

    pages = get_pages_data()
    total = len(pages)
    dirs = len(set(p["dir"] for p in pages))
    total_words = sum(p["words"] for p in pages)
    # "recent" = last 20 modified
    recent = sorted(pages, key=lambda p: p["mtime"], reverse=True)[:20]

    page_groups = {}
    for p in pages:
        page_groups.setdefault(p["dir"], []).append(p)

    priority = {"", "tutorials", "docs", "resources", "programming"}
    sorted_groups = sorted(
        page_groups.items(),
        key=lambda x: (0 if x[0] in priority else 1, x[0]),
    )

    return render_template(
        "dashboard.html",
        user=session.get("username"),
        total=total,
        dirs=dirs,
        total_words=total_words,
        page_groups=sorted_groups,
        recent=recent,
        all_pages=pages,
    )

@app.route("/api/pages")
def api_pages():
    resp = require_auth()
    if resp: return resp
    pages = get_pages_data()
    q = request.args.get("q", "").lower()
    if q:
        pages = [p for p in pages if q in p["path"].lower() or q in p["name"].lower()]
    return jsonify(pages)

@app.route("/edit/", defaults={"path": ""})
@app.route("/edit/<path:path>")
def edit_page(path):
    resp = require_auth()
    if resp: return resp
    if not path:
        return redirect(url_for("dashboard"))
    content = get_file_content(path)
    if content is None:
        return render_template("edit.html", path=path, content="", error="File not found", all_pages=get_pages_data(), site_css=get_site_css())
    return render_template("edit.html", path=path, content=content, error=None, all_pages=get_pages_data(), site_css=get_site_css())

@app.route("/save/<path:path>", methods=["POST"])
def save_page(path):
    resp = require_auth()
    if resp: return resp
    content = request.form.get("content", "")
    save_file(path, content)
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify({"ok": True})
    return redirect(url_for("edit_page", path=path, saved=1))

@app.route("/new", methods=["GET", "POST"])
def new_page():
    resp = require_auth()
    if resp: return resp
    if request.method == "POST":
        path = request.form.get("path", "").strip()
        content = request.form.get("content", "")
        if not path:
            return render_template("new.html", error="Path is required", path=path, content=content, all_pages=get_pages_data())
        full = SITE_ROOT / path
        if full.exists():
            return render_template("new.html", error="File already exists", path=path, content=content, all_pages=get_pages_data())
        save_file(path, content)
        return redirect(url_for("edit_page", path=path))
    return render_template("new.html", error=None, path="", content="", all_pages=get_pages_data())

@app.route("/delete/<path:path>", methods=["POST"])
def delete_page(path):
    resp = require_auth()
    if resp: return resp
    full = SITE_ROOT / path
    if full.exists() and full.is_file():
        full.unlink()
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify({"ok": True})
    return redirect(url_for("dashboard"))

@app.route("/rename/<path:path>", methods=["POST"])
def rename_page(path):
    resp = require_auth()
    if resp: return resp
    data = request.get_json(silent=True) or {}
    new_path = data.get("new_path", "").strip()
    if not new_path:
        return jsonify({"ok": False, "error": "No target path"}), 400
    full_old = SITE_ROOT / path
    full_new = SITE_ROOT / new_path
    if not full_old.exists():
        return jsonify({"ok": False, "error": "Source not found"}), 404
    if full_new.exists():
        return jsonify({"ok": False, "error": "Target already exists"}), 409
    full_new.parent.mkdir(parents=True, exist_ok=True)
    full_old.rename(full_new)
    return jsonify({"ok": True, "path": new_path})

@app.route("/settings", methods=["GET", "POST"])
def settings():
    resp = require_auth()
    if resp: return resp
    global cfg
    message = None
    if request.method == "POST":
        new_user = request.form.get("username", "").strip()
        current_pass = request.form.get("current_password", "")
        new_pass = request.form.get("new_password", "").strip()
        confirm_pass = request.form.get("confirm_password", "").strip()

        if not hash_pw(current_pass) == hash_pw(cfg["password"]):
            message = "Current password is incorrect."
        else:
            if new_user:
                cfg["username"] = new_user
            if new_pass:
                if new_pass != confirm_pass:
                    message = "New passwords do not match."
                elif len(new_pass) < 4:
                    message = "Password must be at least 4 characters."
                else:
                    cfg["password"] = new_pass
            if not message:
                cfg["secret"] = uuid.uuid4().hex
                save_config(cfg)
                app.secret_key = cfg["secret"]
                session.clear()
                return redirect(url_for("login_page"))

    return render_template("settings.html", user=cfg["username"], message=message, all_pages=get_pages_data())

@app.route("/page-info/<path:path>")
def page_info(path):
    resp = require_auth()
    if resp: return resp
    content = get_file_content(path)
    if content is None:
        return jsonify({"ok": False}), 404
    full = SITE_ROOT / path
    stat = full.stat()
    return jsonify({
        "ok": True,
        "size": stat.st_size,
        "mtime": stat.st_mtime,
        "lines": content.count("\n") + 1,
        "words": len(content.split()),
        "chars": len(content),
    })

if __name__ == "__main__":
    print("=" * 54)
    print("  ⚡ Tech Library Admin Panel")
    print("  ─────────────────────────────")
    print(f"  URL:   http://127.0.0.1:5050")
    print(f"  Login: {cfg['username']} / {cfg['password']}")
    print("=" * 54)
    app.run(host="127.0.0.1", port=5050, debug=True)
