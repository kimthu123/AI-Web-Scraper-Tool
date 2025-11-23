# run_scraper.py
import sys, json
from scraper import scrape_arxiv, scrape_semantic

def to_front_items(arts):
    items = []
    for a in arts:
        title = a.get("title") or "Untitled"
        url = a.get("publication", {}).get("url") or a.get("sourceUrl") or ""
        authors = a.get("author", {}).get("name", "") or "Unknown"
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
            "pdf_url": ""
        })
    return items

def main():
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    q = q.strip()
    if not q:
        print(json.dumps({"items": []}, ensure_ascii=False))
        return

    results = []
    try:
        results += scrape_arxiv(q, limit)
    except Exception as e:
        results.append({"title": f"arXiv error: {e}", "publication": {"url": ""}, "author": {"name": ""}, "date": ""})
    try:
        results += scrape_semantic(q, limit)
    except Exception as e:
        results.append({"title": f"Semantic Scholar error: {e}", "publication": {"url": ""}, "author": {"name": ""}, "date": ""})

    print(json.dumps({"items": to_front_items(results)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
