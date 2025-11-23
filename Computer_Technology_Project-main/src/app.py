from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from scraper import scrape_arxiv, scrape_semantic

app = Flask(__name__, static_folder='.')
CORS(app)

def to_front_items(arts):
    items = []
    for a in arts:
        title = a.get("title") or "Untitled"
        pub = a.get("publication") or {}
        url = pub.get("url") or a.get("sourceUrl") or ""
        authors = (a.get("author") or {}).get("name", "") or "Unknown"
        date = a.get("date") or ""
        year = None
        if date:
            try:
                year = int(str(date).split("-")[0])
            except Exception:
                year = None
        items.append({
            "title": title,
            "doi": "",
            "url": url,
            "authors": authors,
            "year": year,
            "pdf_url": a.get("pdf_url", "")
        })
    return items

def _dedupe(items):
    """De-dupe by (url,title)."""
    seen = set()
    out = []
    for a in items:
        url = ((a.get("publication") or {}).get("url") or a.get("sourceUrl") or "").strip().lower()
        title = (a.get("title") or "").strip().lower()
        key = (url, title)
        if key in seen:
            continue
        seen.add(key)
        out.append(a)
    return out

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/search")
def search():
    q = (request.args.get("q") or "").strip()
    limit = min(max(int(request.args.get("limit", 1)), 0), 170)
    if not q:
        return jsonify({"error": "Missing query"}), 400

    results = []
    # call both sources, but don't add error placeholders
    try:
        results += scrape_arxiv(q, limit)
    except Exception as e:
        app.logger.exception("arXiv error: %s", e)
    try:
        results += scrape_semantic(q, limit)
    except Exception as e:
        app.logger.exception("Semantic error: %s", e)

    # de-dupe and CAP to limit
    results = _dedupe(results)[:limit]

    front = to_front_items(results)
    return jsonify({"count": len(front), "items": front})

if __name__ == "__main__":
    app.run(debug=True)
