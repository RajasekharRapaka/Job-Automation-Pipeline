def deduplicate(jobs):
    seen = set()
    result = []

    for job in jobs:
        key = job["Company"] + job["Role"]

        if key not in seen:
            seen.add(key)
            result.append(job)

    return result
