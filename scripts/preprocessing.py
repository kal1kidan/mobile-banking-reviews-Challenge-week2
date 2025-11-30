# scripts/preprocessing.py
import os
import pandas as pd
import re
from config import DATA_PATHS
from datetime import datetime

class ReviewPreprocessor:
    def __init__(self, input_path=None, output_path=None):
        self.input_path = input_path or DATA_PATHS['raw_reviews']
        self.output_path = output_path or DATA_PATHS['processed_reviews']
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.input_path)
        return self.df

    def remove_duplicates(self):
        before = len(self.df)
        self.df = self.df.drop_duplicates(subset=['review_text', 'bank_code'])
        print(f"Removed {before - len(self.df)} duplicate reviews")

    def remove_amharic_reviews(self):
        # Keep only reviews with mostly English letters
        pattern = re.compile(r'^[A-Za-z0-9\s.,!?\'"-]+$')
        before = len(self.df)
        self.df = self.df[self.df['review_text'].apply(lambda x: bool(pattern.match(str(x))))]
        print(f"Removed {before - len(self.df)} Amharic/non-English reviews")

    def clean_text(self):
        self.df['review_text'] = self.df['review_text'].astype(str)
        self.df['review_text'] = self.df['review_text'].str.replace(r'\s+', ' ', regex=True).str.strip()
        self.df = self.df[self.df['review_text'].str.len() > 0]

    def normalize_dates(self):
        self.df['review_date'] = pd.to_datetime(self.df['review_date']).dt.date

    def save_data(self):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        self.df.to_csv(self.output_path, index=False)
        print(f"Processed data saved to {self.output_path}")

    def process(self):
        self.load_data()
        self.remove_duplicates()
        self.remove_amharic_reviews()
        self.clean_text()
        self.normalize_dates()
        self.save_data()
        return self.df
