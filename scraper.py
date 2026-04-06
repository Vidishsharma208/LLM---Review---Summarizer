import requests
from bs4 import BeautifulSoup
import time


def scrape_reviews(url, retries=3):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for attempt in range(retries):
        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=30   # increased timeout
            )

            response.raise_for_status()

            soup = BeautifulSoup(response.text, "lxml")
            reviews = []

            paragraphs = soup.find_all("p")

            for p in paragraphs[:20]:
                text = p.get_text(strip=True)

                if len(text) > 30:
                    reviews.append({
                        "review": text,
                        "rating": None,
                        "author": None,
                        "date": None
                    })

            return reviews

        except requests.exceptions.Timeout:
            print(f"Timeout on attempt {attempt+1}, retrying...")
            time.sleep(3)

        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return []

    return []