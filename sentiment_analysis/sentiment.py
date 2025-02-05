import pandas as pd
import datetime as dt
import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv

from sentiment_words import sentiment_dict

load_dotenv()
filepath = os.environ.get("filepath")

# read posts from reddit that were saved to csv
df = pd.read_csv(filepath, 
                 header=None,
                 names=["article_id", "title"]
    )

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sia.lexicon.update(sentiment_dict)
    scores = sia.polarity_scores(text)
    return scores

def main():
    texts = []
    sentiment_path = os.environ.get('sentiment_path')

    date = dt.datetime.now().strftime('%d/%m/%Y')

    for title in df['title']:
        texts.append(title)

    cumulative_score = 0
    cumulative_scores = []

    for text in texts:
        scores = analyze_sentiment(text)
        cumulative_score += scores['compound']
        cumulative_scores.append(scores['compound'])

    cumulative_score = round(cumulative_score, 7)
    average_score = round(sum(cumulative_scores) / len(cumulative_scores), 7)

    print(cumulative_score)
    print()

    current_date_stats = {
        "Date": date,
        "Cumulative Score": cumulative_score,
        "Average Score": average_score
    }


    title_df = pd.DataFrame([current_date_stats])    

    if not os.path.isfile(sentiment_path):
        title_df.to_csv(sentiment_path, index=False)
        print('csv file created at:', sentiment_path)
    else:
        # If it does exist, append without writing the header
        title_df.to_csv(sentiment_path, mode='a', header=False, index=False)
        print('appended to:', sentiment_path)

if __name__ == '__main__':
    main()