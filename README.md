📌 Mobile Banking Review Analysis – Week 2 Challenge

This repository contains all work completed for 10 Academy – AI Mastery Program, Week 2 Challenge, focusing on mobile banking reviews, including data scraping, cleaning, sentiment analysis, thematic extraction, and reporting.

The project is structured into two major tasks:

Task-1: Data Collection — Web Scraping & Cleaning

Task-2: Sentiment & Theme Analysis — VADER-based sentiment + Keyword thematic modeling

A detailed Interim Report (4 pages) is also included, summarizing the scraping pipeline and early insights from the data.

📁 Folder Structure
mobile-banking-reviews-Challenge-week2/
│
├── Scripts/                         # All Python scripts for Task-1 & Task-2
│   ├── task1_scraper.py             # Web scraping logic
│   ├── task1_cleaner.py             # Cleaning & preprocessing
│   ├── Sentiment_demo.py  # VADER sentiment + thematic modeling
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
└── requirements.txt                    # All dependencies

🚀 Task 1 — Data Scraping & Early Cleaning
Objective

Collect mobile banking reviews from the provided Google Play Store URLs.

Key Steps

Automated scraping using BeautifulSoup / Play Store API wrapper

Extracted:

Reviewer name

Rating

Review text

Date

Cleaned text by removing:

Emojis

HTML artifacts

URLs

Stopwords

Normalized whitespaces

Stored outputs in:

notebooks/data/raw/reviews_raw.csv
notebooks/data/processed/reviews_clean.csv

Deliverables

✔ task1_scraper.py
✔ task1_cleaner.py
✔ task1_scraping_cleaning.ipynb

🔍 Task 2 — Sentiment + Thematic Analysis
Sentiment Analysis

Because NLTK and spaCy had installation issues, I implemented a stable, modern approach using:

VADER Sentiment Analyzer (works perfectly on short review text)

Output columns:

sentiment_compound

sentiment_label → positive / neutral / negative

Thematic Extraction

Due to gensim failing to install, themes were extracted using:

Keyword frequency analysis

Simple noun extraction (regex-based, no spaCy dependency)

Manual clustering of themes into:

Customer Support

Usability & UI

Bugs / Technical issues

Performance

Security & Trust

Deliverables

✔ task2_sentiment_thematic.py
✔ task2_analysis.ipynb

🌱 Current Branches in the Repository
Branch	Purpose
main	Production-ready code, final results, reports
task-1	Contains scraping + cleaning scripts & notebook
task-2	Sentiment + thematic analysis scripts & notebook

All development happened in the task-specific branches, then merged into main after completion.

📄 Interim Report (4 Pages)

The Interim Report summarizes:

1. Task Overview

Purpose of the challenge

Data sources

Requirements

2. Scraping Strategy

Tools used: BeautifulSoup / Requests

How pagination or dynamic loading was handled

Data schema collected

Error handling & retry logic

3. Data Cleaning Pipeline

Duplicate removal

Tokenization

Lowercasing

Stopword filtering

Text normalization

4. Early Insights

Distribution of ratings

Early sentiment distribution

Initial keyword frequency

Example positive & negative reviews

5. Challenges & Mitigations

Play Store DOM issues

NLTK installation failures

Gensim / spaCy incompatibility with Python 3.14

Solutions used (VADER, regex noun extraction)

6. Structure of the Repository

Explaining the folder structure listed above.

🛠 How to Run the Project
1️⃣ Create environment
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.\.venv\Scripts\activate       # Windows

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run Task-1 scripts
python Scripts/task1_scraper.py
python Scripts/task1_cleaner.py

4️⃣ Run Task-2 analysis
python Scripts/task2_sentiment_thematic.py


Or use the Jupyter Notebooks inside /notebooks.

🙌 Author

Kalkidan Asdesach
10 Academy – Cohort 8
AI Mastery Program | Week 2 Challenge
