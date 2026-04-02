from scraper.linkedin import fetch_linkedin
from scraper.indeed import fetch_indeed
from scraper.dice import fetch_dice

from core.scorer import score_job
from core.dedup import deduplicate

import pandas as pd
from datetime import datetime

jobs = []
jobs += fetch_linkedin()
jobs += fetch_indeed()
jobs += fetch_dice()

for job in jobs:
    job["Match %"] = score_job(job["Role"])
    job["Extracted Date"] = datetime.now().strftime("%Y-%m-%d")
    job["Status"] = "Not Applied"

jobs = deduplicate(jobs)

df = pd.DataFrame(jobs)
df.to_csv("jobs.csv", index=False)

print("✅ Jobs scraped:", len(df))
