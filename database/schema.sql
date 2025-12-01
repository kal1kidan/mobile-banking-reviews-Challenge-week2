-- Banks table
CREATE TABLE IF NOT EXISTS banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(255),
    app_name VARCHAR(255)
);

-- Reviews table
CREATE TABLE IF NOT EXISTS reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INT REFERENCES banks(bank_id),
    review_text TEXT,
    rating INT,
    review_date DATE,
    sentiment_label VARCHAR(50),
    sentiment_score FLOAT,
    source VARCHAR(50),
    nouns TEXT,
    identified_theme TEXT,
    noun_text TEXT
);
-- Check how many positive/negative/neutral
SELECT sentiment_label, COUNT(*) 
FROM reviews
GROUP BY sentiment_label;
-- Check average rating per bank
SELECT b.bank_name, AVG(r.rating) AS avg_rating
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;
-- Count how many reviews you inserted
SELECT COUNT(*) FROM reviews;