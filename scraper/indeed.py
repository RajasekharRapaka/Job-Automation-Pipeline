import feedparser

def fetch_indeed():
    url = "https://rss.indeed.com/rss?q=data+engineer&l=USA"
    feed = feedparser.parse(url)

    jobs = []

    for entry in feed.entries:
        jobs.append({
            "Company": entry.get("author", "Unknown"),
            "Role": entry.get("title"),
            "Platform": "Indeed",
            "Location": "USA",
            "Apply Link": entry.get("link"),
            "Posted": entry.get("published", "")
        })

    return jobs
