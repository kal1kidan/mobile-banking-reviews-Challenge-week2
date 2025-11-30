# scripts/scraper.py
import os
import time
import pandas as pd
from datetime import datetime
from tqdm import tqdm
from google_play_scraper import app, reviews, Sort
from config import APP_IDS, BANK_NAMES, SCRAPING_CONFIG, DATA_PATHS

class PlayStoreScraper:
    def __init__(self):
        self.app_ids = APP_IDS
        self.bank_names = BANK_NAMES
        self.reviews_per_bank = SCRAPING_CONFIG['reviews_per_bank']
        self.lang = SCRAPING_CONFIG['lang']
        self.country = SCRAPING_CONFIG['country']
        self.max_retries = SCRAPING_CONFIG['max_retries']

    def get_app_info(self, app_id):
        try:
            result = app(app_id, lang=self.lang, country=self.country)
            return {
                'app_id': app_id,
                'title': result.get('title', 'N/A'),
                'score': result.get('score', 0),
                'ratings': result.get('ratings', 0),
                'reviews': result.get('reviews', 0),
                'installs': result.get('installs', 'N/A')
            }
        except Exception as e:
            print(f"Error getting app info for {app_id}: {e}")
            return None

    def scrape_reviews(self, app_id, count=400):
        """Scrape reviews with retry logic"""
        for attempt in range(self.max_retries):
            try:
                result, _ = reviews(
                    app_id,
                    lang=self.lang,
                    country=self.country,
                    sort=Sort.NEWEST,
                    count=count
                )
                if result:
                    return result
                else:
                    # fallback to US if empty
                    if self.country != 'us':
                        print(f"⚠ No reviews for {app_id} in {self.country}. Trying 'us'...")
                        self.country = 'us'
                        continue
            except Exception as e:
                print(f"Attempt {attempt+1} failed: {e}")
                time.sleep(5)
        return []

    def process_reviews(self, reviews_data, bank_code):
        processed = []
        for r in reviews_data:
            processed.append({
                'review_id': r.get('reviewId', ''),
                'review_text': r.get('content', ''),
                'rating': r.get('score', 0),
                'review_date': r.get('at', datetime.now()),
                'user_name': r.get('userName', 'Anonymous'),
                'thumbs_up': r.get('thumbsUpCount', 0),
                'reply_content': r.get('replyContent', None),
                'bank_code': bank_code,
                'bank_name': self.bank_names[bank_code],
                'app_version': r.get('reviewCreatedVersion', 'N/A'),
                'source': 'Google Play'
            })
        return processed

    def scrape_all_banks(self):
        all_reviews = []

        for bank_code, app_id in tqdm(self.app_ids.items(), desc="Scraping banks"):
            print(f"\nScraping {self.bank_names[bank_code]} ({bank_code}) - App ID: {app_id}")
            reviews_data = self.scrape_reviews(app_id, self.reviews_per_bank)
            if not reviews_data:
                print(f"⚠ WARNING: No reviews returned for {self.bank_names[bank_code]} ({app_id})")
            else:
                print(f"Collected {len(reviews_data)} reviews for {self.bank_names[bank_code]}")
            processed = self.process_reviews(reviews_data, bank_code)
            all_reviews.extend(processed)
            time.sleep(2)

        df = pd.DataFrame(all_reviews)
        os.makedirs(os.path.dirname(DATA_PATHS['raw_reviews']), exist_ok=True)
        df.to_csv(DATA_PATHS['raw_reviews'], index=False)
        print(f"\nAll reviews saved to {DATA_PATHS['raw_reviews']}")
        return df

def main():
    scraper = PlayStoreScraper()
    df = scraper.scrape_all_banks()
    print(df.head())
    return df

if __name__ == "__main__":
    main()



