import re


def clean_review(text):
    text = text.encode("utf-8", "ignore").decode()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9.,!? ]", "", text)
    return text.strip()