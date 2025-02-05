# reddit scraper that takes from ethereum subreddit
# works, but i'm not using it because reddit is not the place for news

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
    get_post(SUBREDDIT, save_path)

def get_posts(sub):
    subreddit = reddit.subreddit(sub)
    top_posts = subreddit.new(limit=100)

    posts = []

    for submission in top_posts:    
        if submission.link_flair_text:
            if submission.link_flair_text.lower() == "news" or submission.link_flair_text.lower() == "discussion":
                posts.append({
                    "url": submission.url,
                    "title": submission.title,
                    "sentiment": "__TODO__",
                    "post_id": submission.id
                })

    return posts

def save_to_csv(data, file_path):
    os.makedirs("posts", exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

def get_post(sub, filepath):
    post = get_posts(sub)
    save_to_csv(post, filepath)


if __name__ == "__main__":
    main()