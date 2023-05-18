import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
import sqlite3

conn = sqlite3.connect('scraped_data.db')
c = conn.cursor()

sia = SentimentIntensityAnalyzer()

c.execute('SELECT text FROM reviews')
reviews_text = c.fetchall()


for review_text in reviews_text:

    sentiment_score = sia.polarity_scores(review_text[0])
    

    print(f"Review: {review_text[0]}")
    print(f"Sentiment Score: {sentiment_score}")
    print("\n")


conn.close()
