import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# -----------------------------
# 🔹 GPT Topic Classifier
# -----------------------------
TOPIC_LABELS = [
    "AI for Climate Change",
    "Climate Adaptation",
    "Carbon Emissions",
    "Machine Learning",
    "AI Sustainability",
    "Green Energy",
    "Environmental AI"
]

def classify_topic_with_gpt(summary):
    prompt = f"""
You are an AI assistant helping classify research articles related to climate and AI.

Article Summary:
\"{summary}\"

Choose the best-fitting topic from the list below:
- {', '.join(TOPIC_LABELS)}

Return only the most relevant topic name.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        label = response.choices[0].message.content.strip()
        return label if label in TOPIC_LABELS else "Uncategorized"
    except Exception as e:
        print(" GPT classification error:", e)
        return "Uncategorized"

def estimate_reading_time(text):
    words = len(text.split())
    return max(1, words // 200)

# -----------------------------
# 🔹 Standard Article Format
# -----------------------------
def format_article(title, summary, link, published, author, source):
    return {
        "title": title,
        "date": published,
        "contentGroup": "Articles",
        "internalTags": [classify_topic_with_gpt(summary)],
        "author": {
            "name": author,
            "email": "",
            "organization": ""
        },
        "publication": {
            "name": source,
            "url": link
        },
        "publicTags": [],
        "summary": summary,
        "sourceUrl": link,
        "language": "en",
        "readingTime": estimate_reading_time(summary),
        "imageUrl": "",
        "relatedContent": [],
        "content": f"<p>{summary}</p>"
    }

# -----------------------------
# 🔹 arXiv Scraper
# -----------------------------
def scrape_arxiv(keyword, max_results):
    print(" Scraping arXiv...")
    url = f"http://export.arxiv.org/api/query?search_query=all:{keyword}&start=0&max_results={max_results}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")
    entries = soup.find_all("entry")

    articles = []
    for entry in entries:
        title = entry.title.text.strip()
        summary = entry.summary.text.strip()
        link = entry.id.text.strip()
        published = datetime.strptime(entry.published.text.strip(), "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
        authors = entry.find_all("author")
        author = authors[0].find("name").text if authors else "Unknown"
        articles.append(format_article(title, summary, link, published, author, "arXiv"))
    return articles

# -----------------------------
# 🔹 Semantic Scholar Scraper
# -----------------------------
def scrape_semantic(keyword, max_results):
    print("Scraping Semantic Scholar...")
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={keyword}&limit={max_results}&fields=title,abstract,url,authors,year"
    response = requests.get(url)
    data = response.json()

    articles = []
    for paper in data.get("data", []):
        title = paper.get("title", "Untitled")
        summary = paper.get("abstract") or "No abstract"
        link = paper.get("url", "")
        author = paper.get("authors", [{}])[0].get("name", "Unknown")
        year = paper.get("year", 2024)
        published = f"{year}-01-01"
        articles.append(format_article(title, summary, link, published, author, "Semantic Scholar"))
    return articles

# -----------------------------
# 🔹 Save Articles to JSON
# -----------------------------
def save_articles(articles, output_path="output/articles.json", mode="append"):
    os.makedirs("output", exist_ok=True)

    existing = []
    if os.path.exists(output_path) and mode == "append":
        with open(output_path, "r", encoding="utf-8") as f:
            existing = json.load(f)

    existing_titles = {item["title"] for item in existing}
    new_articles = [a for a in articles if a["title"] not in existing_titles]
    combined = existing + new_articles

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(combined, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(new_articles)} new articles (total: {len(combined)}) to {output_path}")

# -----------------------------
# 🔹 GPT Keyword Suggestion
# -----------------------------
def suggest_keywords_with_gpt(base_keyword):
    prompt = f"""
Suggest 5 advanced and specific research keywords related to this theme: "{base_keyword}".
They should be suitable for academic paper search (e.g. arXiv or Semantic Scholar).
Return as a numbered list.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(" GPT keyword suggestion error:", e)
        return ""

# -----------------------------
# 🔹 Entry Point
# -----------------------------
if __name__ == "__main__":
    print(" Research Scraper ")

    keyword = input(" Enter keyword (e.g., AI climate change): ").strip()
    if not keyword:
        keyword = "AI climate change"
        print(f" Using default keyword: {keyword}")

    print("\n📌 GPT-suggested keywords for broader search:")
    print(suggest_keywords_with_gpt(keyword))
    print("")

    max_results = input(" Number of papers to fetch per source (e.g. 10): ") or "10"
    mode = input(" Save mode (overwrite / append): ").lower() or "append"

    try:
        max_results = int(max_results)
    except ValueError:
        print("Invalid number. Using default = 10.")
        max_results = 10

    all_articles = []
    all_articles += scrape_arxiv(keyword, max_results)
    all_articles += scrape_semantic(keyword, max_results)

    save_articles(all_articles, mode=mode)
