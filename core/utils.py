# core/utils.py

def detect_work_mode(text):
    text = text.lower()

    if "remote" in text:
        return "Remote"
    elif "hybrid" in text:
        return "Hybrid"
    elif "onsite" in text or "on-site" in text:
        return "On-site"
    return "Unknown"


def detect_type(text):
    if "contract" in text.lower():
        return "Contract"
    if "full-time" in text.lower():
        return "Full-time"
    return "Unknown"
