import requests
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
