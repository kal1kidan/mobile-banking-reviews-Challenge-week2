-- Count total reviews
SELECT COUNT(*) FROM reviews;

-- Count total banks
SELECT COUNT(*) FROM banks;

-- Sentiment distribution
SELECT sentiment_label, COUNT(*)
FROM reviews
GROUP BY sentiment_label;

-- Average rating per bank
SELECT b.bank_name, AVG(r.rating)
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;
