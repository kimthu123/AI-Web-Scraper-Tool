🌐 AI Web Scraper — Intelligent Research Automation

A project by Jace (Thu Tran)

An AI-powered research scraper that automatically expands user queries, collects academic articles, cleans data, and produces structured research insights in seconds.

This tool helps reduce manual searching, speeds up research, and demonstrates how AI + automation can accelerate real-world workflows.

✨ Overview

The AI Web Scraper takes a single topic—like “AI for climate change”—and automatically:

Expands it into multiple meaningful subtopics using AI

Scrapes relevant articles from research sources (arXiv, Semantic Scholar, etc.)

Cleans, formats, and filters the raw data

Builds structured JSON output

(Optional) Summarises content using AI

This project was originally built for a client project about
“Mapping AI innovations for climate change solutions.”

🚀 Core Features
🔹 1. AI-Powered Topic Expansion

Uses OpenAI (GPT-3.5 or GPT-4) to transform one user query into 10–20 relevant research directions.

Example:
Input:

"AI for climate change"


Expanded automatically to:

AI for flood prediction

Carbon modelling & simulations

Satellite image ML

Renewable energy optimisation

AI for heatwave forecasting

Grid stability using machine learning

🔹 2. High-Speed Web Scraping

Scrapes dozens to hundreds of articles per run

Supports multiple data sources

Async scraping for faster performance

Handles pagination & rate limits

🔹 3. Smart Filtering & Deduplication

Removes repeated papers

Normalises formats

Cleans metadata (authors, abstract, published date)

Rejects irrelevant results

🔹 4. Clean JSON Output

Optimised for:

dashboards

ML models

research review

automation pipelines

🔹 5. Modular Architecture

Each feature is an independent module:

Expansion

Scraper

Filters

Output JSON

Easy to plug in new data sources or swap tools.

🧠 AI Integration Details
Query Expansion

OpenAI generates subtopics like:

AI for wildfire prediction
Satellite ML for climate monitoring
AI for crop yield forecasting
Energy optimisation with machine learning
AI + IoT for environmental sensing

Article Insight Extraction (Optional)

AI can also:

summarise articles

extract key ideas

group by topic

evaluate relevance

🏗 Tech Stack
Layer	Tools
🧠 AI Model	OpenAI GPT-3.5 / GPT-4
🌐 Scraping	requests, aiohttp, BeautifulSoup
⚙️ Backend Logic	Python 3
🗂 Data	JSON, async pipelines
🧪 Dev Tools	VSCode, devcontainers, GitHub
📂 Project Structure
ai-web-scraper/
│
├── expand_query.py       # AI-powered topic expansion
├── scraper.py            # Main scraping logic
├── filters.py            # Cleansing & dedupe logic
├── utils/
│   └── clean_text.py     # Text preprocessing (optional)
├── output/
│   └── articles.json     # Final structured dataset
└── README.md             # You're reading it

🌱 Why I Built This

As a Software Development student exploring AI-assisted engineering, I wanted to create a tool that:

reduces repetitive research tasks

speeds up topic exploration

automates scraping + processing

helps people find insights quickly

showcases how AI + scripting works together

This project taught me a lot about:

✨ API integration
✨ async Python
✨ prompt engineering
✨ data pipelines
✨ and how to structure real-world tools

🧪 How It Works (Flow)
User Topic
   ↓
AI Query Expansion (GPT)
   ↓
Scraper fetches articles
   ↓
Data cleaning + dedupe
   ↓
JSON output

▶️ How to Run
1. Install dependencies
pip install -r requirements.txt

2. Add your OpenAI API key

Create .env file:

OPENAI_API_KEY=your_key_here

3. Run the scraper
python scraper.py

4. See your results
output/articles.json

📊 Example Output
{
  "title": "AI-Assisted Climate Modelling",
  "authors": ["J. Smith", "L. Wang"],
  "published": "2024-01-12",
  "summary": "Machine learning models enhance climate prediction accuracy...",
  "source": "arXiv",
  "topic": "AI for extreme weather",
  "link": "https://arxiv.org/..."
}

🤝 Contributions

Open to PRs, improvements, new features, or new scraping sources!
Ideas welcomed 💡

💌 Contact

📍 Melbourne, Australia
📧 Email: trankimthu.160503@gmail.com

🐙 GitHub: github.com/kimthu123
🔗 LinkedIn: https://www.linkedin.com/in/kim-thu-tran-769211279/

<p align="center"> <i>Thanks for checking out my AI Web Scraper — hope it helps or inspires your next idea ✨</i> </p>
