import os
import pandas as pd
from scraper import scrape_reviews
from preprocess import clean_review
from llm_analyzer import analyze_review


def run_pipeline(url):
    print("🔍 Scraping reviews...")
    reviews = scrape_reviews(url)

    if not reviews:
        print("❌ No reviews found or scraping failed.")
        return

    final_data = []

    print(f"✅ Found {len(reviews)} reviews")
    print("🤖 Sending reviews to LLM...\n")

    for idx, item in enumerate(reviews, start=1):
        try:
            cleaned = clean_review(item["review"])
            llm_output = analyze_review(cleaned)

            final_data.append({
                "review": cleaned,
                "rating": item.get("rating"),
                "author": item.get("author"),
                "date": item.get("date"),
                "llm_output": llm_output
            })

            print(f"✔ Processed review {idx}")

        except Exception as e:
            print(f"⚠ Error processing review {idx}: {e}")

    if not final_data:
        print("❌ No processed reviews to save.")
        return

    df = pd.DataFrame(final_data)

    os.makedirs("output", exist_ok=True)
    df.to_csv("output/reviews.csv", index=False)
    df.to_json("output/reviews.json", orient="records", indent=4)

    print("\n🎉 Processing complete!")
    print("📁 CSV saved at: output/reviews.csv")
    print("📁 JSON saved at: output/reviews.json")
    print("\n📊 Sample Output:")
    print(df.head())


if __name__ == "__main__":
    url = input("Enter product URL: ").strip()
    run_pipeline(url)