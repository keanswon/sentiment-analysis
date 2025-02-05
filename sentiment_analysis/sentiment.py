import pandas as pd
import os

from dotenv import load_dotenv

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


nltk.download('vader_lexicon')

load_dotenv()
filepath = os.environ.get("filepath")

# read posts from reddit that were saved to csv
df = pd.read_csv(filepath, 
                 header=None,
                 names=["article_id", "title"]
    )

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    return scores

def main():
    texts = []

    for title in df['title']:
        texts.append(title)

    for text in texts:
        scores = analyze_sentiment(text)
        print(f"Text: {text}")
        print("Sentimen`t Scores:", scores)
        print("-" * 50)

if __name__ == '__main__':
    main()