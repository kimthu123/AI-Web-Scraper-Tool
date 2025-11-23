# 🚀 AI Web Scraper Tool  
An AI-powered research scraper that automatically expands user queries, collects articles from multiple academic sources, filters duplicates, and outputs structured JSON data.  
Designed to speed up research — especially for topics like **AI tackling climate change**.

<p align="center">
  <img src="https://raw.githubusercontent.com/kimthu123/AI-Web-Scraper-Tool/main/preview.jpeg" width="85%" alt="Project Preview"/>
</p>

---

## 🏷️ Badges

<p align="left">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/AI-OpenAI%20API-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Scraper-Async%20Requests-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/Output-JSON-success?style=flat-square"/>
</p>

---

## 🌟 Overview  
This scraper automates research by:

- 🤖 Using **AI to expand** a user-generated query into multiple relevant subtopics.  
- 🔎 Scraping articles from **arXiv, Semantic Scholar**, and more.  
- 🧹 Cleaning and **deduplicating metadata**.  
- 📦 Exporting everything into a clean **JSON dataset**.  
- ⚡ Running fast using asynchronous Python scraping.

The tool is modular, extendable, and designed for real-world research workflows.

---

## ✨ Key Features

### 🤖 AI Topic Expansion  
Uses **OpenAI GPT models** to transform one query into multiple subtopics.

### 🔍 Multi-Source Scraping  
Collects articles based on each subtopic.  
Built with modular functions so new sources can easily be added.

### 🧹 Smart Filtering  
- Duplicate removal  
- Metadata normalization  
- Summary cleaning  
- Relevance filtering  

### 📦 JSON Output  
Produces a clean JSON file ready for dashboards, ML pipelines, or external integrations.

---

## 🛠 Tech Stack

- 🐍 **Python 3**  
- 🤖 **OpenAI API (GPT-3.5 / GPT-4)**  
- 🌐 **aiohttp / Requests**  
- 🧼 **BeautifulSoup / lxml**  
- 📁 **JSON output**  
- 🧰 Optional: **VS Code Devcontainers**

---

## 📁 Project Structure

```
ai-web-scraper/
│
├── expand_query.py       # AI expansion
├── scraper.py            # Main scraping engine
├── filters.py            # Filtering + cleanup
├── output/
│   └── articles.json     # Exported file
└── README.md
```

---

## ⚙️ How It Works

1. User enters a research topic  
2. AI expands it into multiple subtopics  
3. Scraper gathers articles for each one  
4. Filters clean the metadata  
5. Output saved as JSON  
6. Optional: Summaries via OpenAI  

---

## 🚀 Installation

Install dependencies:

```
pip install -r requirements.txt
```

Add your OpenAI API key inside `.env`:

```
OPENAI_API_KEY= ...
```

Run the scraper:

```
python scraper.py
```

Output file:

```
output/articles.json
```

---

## 📄 Example Output

```
{
  "title": "Using AI for Climate Prediction",
  "authors": ["J. Smith", "L. Johnson"],
  "published": "2024-02-10",
  "summary": "This paper explores...",
  "source": "arXiv",
  "topic": "AI for extreme weather prediction",
  "link": "https://arxiv.org/..."
}
```

---

## 🎯 Purpose  
This project aims to automate academic research by:

- Reducing manual search time  
- Improving coverage across multiple research areas  
- Producing structured data for future AI analysis  
- Helping teams work faster with automated article extraction  

---

## 📬 Contact

**Jace (Kim Thu Tran)**  
📍 Melbourne, Australia  
📧 Email: trankimthu.160503@gmail.com  
🐙 GitHub: https://github.com/kimthu123  
🔗 LinkedIn: https://www.linkedin.com/in/kim-thu-tran-769211279/

<p align="center">
  <i>Thank you for checking out this project 💛</i>
</p>
