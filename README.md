# 🚀 LLM Review Summarizer

An AI-powered Python project that scrapes product reviews, processes large text efficiently, and uses Large Language Models (LLMs) to generate meaningful summaries and sentiment insights.

---

## 🔍 Overview

This project automates the process of extracting and analyzing product reviews. It cleans raw text, handles long inputs using chunking, and leverages LLMs to produce concise summaries and sentiment analysis.

---

## ✨ Features

* 🕸️ Web scraping of product reviews
* 🧹 Text cleaning and preprocessing
* ✂️ Chunking for long text handling
* 🤖 LLM-based summarization
* 📊 Sentiment analysis (positive / negative / neutral)
* 💾 Export results to CSV

---

## 🧱 Project Structure

```
LLM-Review-Summarizer/
│── main.py              # Main execution file
│── scraper.py           # Scrapes reviews from web
│── preprocess.py        # Cleans and processes text
│── llm_analyzer.py      # LLM integration logic
│── utils.py             # Helper functions
│── requirements.txt     # Dependencies
│── README.md            # Documentation
```

---

## ⚙️ Installation

```bash
git clone https://github.com/Vidishsharma208/LLM---Review---Summarizer.git
cd LLM---Review---Summarizer
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📂 Output

* Processed reviews
* Generated summaries
* Sentiment insights

All results are stored in the `output/` folder.

---

## ⚠️ Limitations

* Website structure changes can break scraping
* Dynamic websites may require Selenium
* API usage cost depends on input size

---

## 🚀 Future Improvements

* Add support for multiple websites
* Build a Streamlit web interface
* Add visualization dashboards
* Improve sentiment accuracy with fine-tuned models

---

## 🧠 Tech Stack

* Python
* OpenAI API (LLM)
* BeautifulSoup / Requests
* Pandas / NumPy

---

## 👨‍💻 Author

**Vidish Sharma**
B.Tech AIML | Aspiring AI Engineer

---

## ⭐ If you found this useful

Give this repo a ⭐ and support the project!
