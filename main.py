import praw
import csv
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT')
)

subreddits = ['IIITUna']

def fetch_posts(limit=10):
    results = []
    for sub in subreddits:
        print(f"\n📡 Subreddit: r/{sub}")
        for post in reddit.subreddit(sub).new(limit=limit):
            print(f"🔹 {post.title} ")
            print(f" Body : {post.selftext}", end="")
            print()

if __name__ == "__main__":
    fetch_posts()