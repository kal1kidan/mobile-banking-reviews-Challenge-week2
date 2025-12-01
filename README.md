# 📌 Mobile Banking Review Analysis – Week 2 Challenge

This repository contains all work completed for **10 Academy – AI Mastery Program, Week 2 Challenge**, focusing on **mobile banking reviews**. The project covers data scraping, cleaning, sentiment analysis, thematic extraction, and reporting.

---

## 📁 Project Structure

```
mobile-banking-reviews-Challenge-week2/
│
├── Scripts/                         # Python scripts for Task-1 & Task-2
│   ├── task1_scraper.py             # Web scraping logic
│   ├── task1_cleaner.py             # Cleaning & preprocessing
│   └── Sentiment_demo.py            # VADER sentiment + thematic extraction
│
├── notebooks/
│   ├── task1_scraping_cleaning.ipynb   # Task-1 exploratory notebook
│   ├── task2_analysis.ipynb            # Task-2 analysis & visualizations
│   └── data/
│       ├── raw/
│       │   └── reviews_raw.csv         # Original scraped reviews
│       ├── interim/
│       └── processed/
│           └── reviews_clean.csv       # Cleaned dataset
│
├── reports/
│   └── Interim_Report.pdf              # 4-page early analysis report
│
├── README.md                           # Project documentation
└── requirements.txt                    # Python dependencies
```

---

## 🚀 Task 1 — Data Scraping & Cleaning

**Objective:** Collect mobile banking reviews from Google Play Store and preprocess them for analysis.

**Key Steps:**

* Automated scraping using **BeautifulSoup** / Play Store API wrapper
* Extracted:

  * Reviewer name
  * Rating
  * Review text
  * Review date
* Cleaned text by removing:

  * Emojis
  * HTML artifacts
  * URLs
  * Stopwords
  * Extra whitespace

**Outputs:**

* `notebooks/data/raw/reviews_raw.csv` – Raw scraped reviews
* `notebooks/data/processed/reviews_clean.csv` – Cleaned dataset

**Deliverables:**

✔ `task1_scraper.py`
✔ `task1_cleaner.py`
✔ `task1_scraping_cleaning.ipynb`

---

## 🔍 Task 2 — Sentiment & Thematic Analysis

**Sentiment Analysis:**

* Implemented using **VADER Sentiment Analyzer**
* Output columns:

  * `sentiment_score` → compound sentiment score
  * `sentiment_label` → positive / neutral / negative

**Thematic Extraction:**

* Due to installation issues with **gensim** and **spaCy**, themes were extracted via:

  * Keyword frequency analysis
  * Regex-based noun extraction (no spaCy dependency)
* Manual clustering of themes into:

  * Customer Support
  * Usability & UI
  * Bugs / Technical issues
  * Performance
  * Security & Trust

**Deliverables:**

✔ `task2_sentiment_thematic.py`
✔ `task2_analysis.ipynb`

---

## 🌱 Branches

| Branch | Purpose                                          |
| ------ | ------------------------------------------------ |
| main   | Production-ready code, final results, reports    |
| task-1 | Scraping + cleaning scripts & notebook           |
| task-2 | Sentiment + thematic analysis scripts & notebook |
| task-3 | PostgreSQL database insertion scripts/notebooks  |
| task-4 | Insights, visualizations, and recommendations    |

All development happened in **task-specific branches**, then merged into `main` after completion.

---

## 📄 Interim Report (4 Pages)

The report summarizes:

1. **Task Overview:** Purpose, data sources, requirements
2. **Scraping Strategy:** Tools used, pagination handling, data schema
3. **Data Cleaning Pipeline:** Duplicate removal, tokenization, normalization
4. **Early Insights:** Rating distribution, sentiment distribution, keyword frequency
5. **Challenges & Solutions:** Play Store DOM issues, NLTK/gensim/spaCy installation issues
6. **Repository Structure:** Folder and file organization

---

## 🛠 How to Run the Project

1️⃣ **Create virtual environment**

```bash
python -m venv .venv
# Activate
# Mac/Linux
source .venv/bin/activate
# Windows
.\.venv\Scripts\activate
```

2️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Run Task-1 scripts**

```bash
python Scripts/task1_scraper.py
python Scripts/task1_cleaner.py
```

4️⃣ **Run Task-2 analysis**

```bash
python Scripts/task2_sentiment_thematic.py
```

Or use the Jupyter Notebooks in `/notebooks`.

---

## 🙌 Author

**Kalkidan Asdesach**
10 Academy – AI Mastery Program

---

