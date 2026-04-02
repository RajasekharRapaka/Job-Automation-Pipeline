import requests
from bs4 import BeautifulSoup

def fetch_dice():
    url = "https://www.dice.com/jobs?q=data%20engineer&location=United%20States"

    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    jobs = []

    for job in soup.find_all("a", {"data-cy": "card-title-link"}):
        jobs.append({
            "Company": "Unknown",
            "Role": job.text.strip(),
            "Platform": "Dice",
            "Location": "USA",
            "Apply Link": "https://www.dice.com" + job.get("href")
        })

    return jobs
