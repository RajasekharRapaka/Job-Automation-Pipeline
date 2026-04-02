import os

folders = [
    "scraper",
    "core",
    "sheets",
    "output",
    ".github/workflows"
]

files = {
    "scraper/linkedin.py": """import requests
from bs4 import BeautifulSoup

def fetch_linkedin():
    url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=data%20engineer&location=United%20States"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    jobs = []
    for job in soup.find_all("li"):
        title = job.find("h3")
        company = job.find("h4")
        link = job.find("a")

        if title and company and link:
            jobs.append({
                "Company": company.text.strip(),
                "Role": title.text.strip(),
                "Platform": "LinkedIn",
                "Location": "USA",
                "Apply Link": link["href"]
            })

    return jobs
""",

    "core/scorer.py": """def score_job(text):
    score = 0
    text = text.lower()

    if "palantir" in text: score += 30
    if "snowflake" in text: score += 25
    if "pyspark" in text: score += 20
    if "airflow" in text: score += 15

    return score
""",

    "core/dedup.py": """def deduplicate(jobs):
    seen = set()
    result = []

    for job in jobs:
        key = job["Company"] + job["Role"]

        if key not in seen:
            seen.add(key)
            result.append(job)

    return result
""",

    "main.py": """from scraper.linkedin import fetch_linkedin
from core.scorer import score_job
from core.dedup import deduplicate
import pandas as pd
from datetime import datetime

jobs = fetch_linkedin()

for job in jobs:
    job["Match %"] = score_job(job["Role"])
    job["Extracted Date"] = datetime.now().strftime("%Y-%m-%d")
    job["Status"] = "Not Applied"

jobs = deduplicate(jobs)

df = pd.DataFrame(jobs)
df.to_csv("output/jobs.csv", index=False)

print("Pipeline executed successfully!")
""",

    "requirements.txt": """pandas
requests
beautifulsoup4
"""
}

# create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# create files
for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("✅ Full pipeline created!")
