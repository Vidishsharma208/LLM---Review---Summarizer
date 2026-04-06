import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def fallback_sentiment(review: str) -> str:
    text = review.lower()

    positive_words = [
        "good", "great", "excellent", "amazing", "love", "best",
        "beautiful", "useful", "helpful", "interesting", "enjoyed"
    ]
    negative_words = [
        "bad", "poor", "worst", "hate", "boring", "terrible",
        "awful", "disappointing", "slow", "confusing"
    ]

    pos_score = sum(word in text for word in positive_words)
    neg_score = sum(word in text for word in negative_words)

    if pos_score > neg_score:
        sentiment = "Positive"
    elif neg_score > pos_score:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    short_summary = review[:120].strip()
    if len(review) > 120:
        short_summary += "..."

    return f"Sentiment: {sentiment} | Summary: {short_summary}"


def analyze_review(review: str, retries: int = 3) -> str:
    last_error = None

    for attempt in range(1, retries + 1):
        try:
            response = client.chat.completions.create(
                model="gemini-2.0-flash",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
Analyze this product review.

Return in this format:
Sentiment: <Positive/Negative/Neutral>
Summary: <1-2 line concise summary>

Review:
{review}
"""
                    }
                ],
                temperature=0.2
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            last_error = e
            print(f"Retry {attempt}: {e}")
            time.sleep(3)

    print("⚠ API failed after retries. Using fallback local sentiment analyzer.")
    return fallback_sentiment(review)