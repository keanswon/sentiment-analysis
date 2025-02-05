# file to 

from sentiment_analysis.reddit_scraper import get_posts

import praw
import os
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

reddit_client_id = os.environ.get("reddit_client_id")
reddit_client_secret = os.environ.get("reddit_client_secret")

post_id = None

reddit = praw.Reddit(client_id=reddit_client_id,
                    client_secret=reddit_client_secret,
                    user_agent='reddit scraper by sean')

save_path = os.environ.get("filepath")
SUBREDDIT = "ethereum"

def main():
    subreddit = reddit.subreddit(SUBREDDIT)
    top_posts = subreddit.hot(limit=1000)


    for submission in top_posts:   
        if submission.link_flair_text.lower() == 'news' or submission.link_flair_text.lower() == 'discussion': 
            print(submission.link_flair_text)
            


if __name__ == "__main__":
    main()