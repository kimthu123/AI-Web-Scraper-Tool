

# 🧠 AI Research Article Scraper Web App

A lightweight web application built with **Python Flask** and **HTML/CSS/JS** to search, save, and download AI research articles from **arXiv** and **Semantic Scholar**.

---

## 📂 Project Structure

| File / Folder | Description |
|----------------|-------------|
| `app.py` | Flask backend (runs the web server) |
| `scraper.py` | Handles scraping from arXiv and Semantic Scholar |
| `run_scraper.py` | CLI runner / bridge for direct testing |
| `search.py` | PHP bridge (legacy, replaced by Flask) |
| `index.html` | Frontend page (search, save, download, history) |
| `requirements.txt` | Dependency list |
| `output/` | (Optional) server-side saved outputs |

---

## ⚙️ Setup Instructions

### 🧩 Prerequisites
- Python **3.8+**
- Internet connection for API access (Semantic Scholar + arXiv)

### 📦 Install Dependencies
```bash
py -m pip install flask flask-cors requests beautifulsoup4 python-dotenv openai requirements.txt

▶️ Run the Application

py app.py

Then open your browser at:
👉 http://127.0.0.1:5000

⸻

🚀 Features

🔍 1. Search Articles
	•	Enter a keyword and result limit (1–170).
	•	Fetches papers from arXiv and Semantic Scholar via the backend.
	•	Displays results in the left panel.

💾 2. Save Selected
	•	Check desired items in “Search Results” and click Save selected.
	•	Saved articles appear in the middle “Saved Articles” list.
	•	Saved data is stored in browser localStorage (persistent per browser origin).

📥 3. Download Selected (JSON)
	•	Check items in “Saved Articles” and click Download selected (JSON).
	•	A .json file will be downloaded to your browser’s default Downloads folder.
	•	JSON structure follows format_article() from scraper.py.

🕓 4. Search History
	•	The right-hand “Search History” records up to 50 previous search queries.
	•	You can “Open” a past keyword, “Delete” one entry, or “Clear all”.

⸻

🧾 Example JSON Format

{
  "title": "Title",
  "date": "YYYY-MM-DD",
  "contentGroup": "Articles",
  "internalTags": ["Machine Learning"],
  "author": {
    "name": "Author Name",
    "email": "",
    "organization": ""
  },
  "publication": {
    "name": "arXiv / Semantic Scholar",
    "url": "https://..."
  },
  "publicTags": [],
  "summary": "Abstract text",
  "sourceUrl": "https://...",
  "language": "en",
  "readingTime": 3,
  "imageUrl": "",
  "relatedContent": [],
  "content": "<p>Abstract text</p>"
}


⸻

⚠️ Notes & Limitations
	•	The Semantic Scholar API allows up to 100 results per request, processed in paginated order.
	•	arXiv supports higher batch sizes but may throttle excessive queries.
	•	localStorage data is domain-specific (127.0.0.1 ≠ localhost).
	•	All saved data is cleared when Incognito mode is turned off.
	•	If GPT classification is not required, return "Uncategorized" in classify_topic_with_gpt().

⸻

🕓 Version History
	•	Base Flask integration
	•	arXiv + Semantic Scholar scraping
	•	Save to localStorage
	•	Download selected as JSON
	•	Search history (keywords)

⸻

📜 License

MIT License — Free for educational and research use.

This `.md` file preserves the structure and content of your original README but adds proper Markdown formatting for GitHub readability.
