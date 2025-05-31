import requests

def get_top_reddit_post(subreddit="memes"):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        posts = res.json()["data"]["children"]
        for post in posts:
            if not post["data"]["stickied"]:
                return post["data"]["title"]
    return "When the code works on the first try."
