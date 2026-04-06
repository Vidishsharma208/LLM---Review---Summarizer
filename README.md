
# LLM Product Review Analyzer

## Chosen Product URL
Best Buy Laptop URL: ...

## Features
- Review scraping
- Text cleaning
- Token chunking
- LLM summarization
- Sentiment analysis
- CSV export
- Retry logic

## How to Run
pip install -r requirements.txt
python main.py

## Limitations
- Website structure may change
- Dynamic JS websites may need Selenium
- API cost depends on review count

## Requirements.txt

🔹 requests

For fetching product page HTML.

🔹 beautifulsoup4

For scraping review text and metadata.

🔹 pandas

To store final review + LLM summaries in CSV/DataFrame.

🔹 numpy

Useful for data preprocessing and optional text operations.

🔹 openai

For OpenAI-compatible API calls.

🔹 python-dotenv

For loading .env API key securely.

🔹 tiktoken

For token counting and chunking long reviews.

🔹 lxml

Faster HTML parsing than default parser.
=======
# LLM---Review---Summarizer

