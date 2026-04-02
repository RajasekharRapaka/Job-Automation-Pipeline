def score_job(text):
    score = 0
    text = text.lower()

    if "palantir" in text: score += 30
    if "snowflake" in text: score += 25
    if "pyspark" in text: score += 20
    if "airflow" in text: score += 15

    return score
