"""Check that every local file referenced from HTML/CSS exists and that JSON files parse."""
import json, re, sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

errors = []

class Refs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        if any(k == "onerror" for k, _ in attrs):
            return  # optional image, hidden by the page when missing
        for k, v in attrs:
            if k in ("src", "href") and v:
                self.refs.append(v)

def local(ref):
    u = urlparse(ref)
    if u.scheme or u.netloc or ref.startswith(("#", "mailto:", "javascript:", "data:", "{{")):
        return None
    return unquote(u.path) or None

def check(base, refs, src):
    for ref in refs:
        path = local(ref)
        if path:
            target = Path(path.lstrip("/")) if path.startswith("/") else base / path
            if not target.exists():
                errors.append(f"{src}: missing {ref}")

for html in Path(".").rglob("*.html"):
    p = Refs()
    p.feed(html.read_text(encoding="utf-8"))
    check(html.parent, p.refs, html)
for css in Path(".").rglob("*.css"):
    check(css.parent, re.findall(r"url\(['\"]?([^'\")]+)", css.read_text(encoding="utf-8")), css)
for j in Path(".").rglob("*.json"):
    try:
        json.loads(j.read_text(encoding="utf-8"))
    except ValueError as e:
        errors.append(f"{j}: invalid JSON ({e})")

print("\n".join(errors) or "All local references resolve.")
sys.exit(1 if errors else 0)
