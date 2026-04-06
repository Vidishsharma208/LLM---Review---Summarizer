# 🚀 LLM Review Summarizer

An AI-powered Python project that scrapes product reviews, processes large text efficiently, and uses Large Language Models (LLMs) to generate meaningful summaries and sentiment insights.

---

## 🔍 Overview

This project automates the process of extracting and analyzing product reviews from e-commerce platforms. It cleans raw text, handles long inputs using chunking, and leverages LLMs to produce concise summaries and sentiment analysis.

---

## 🛍️ Selected Product

The application is tested on the following product:

🔗 https://www.amazon.in/iPhone-Pro-Max-256-Promotion/dp/B0FQFW4MVJ

This is a premium smartphone with advanced features like:

* High-performance A19 Pro chip
* Pro-level camera system
* Large display and battery life

---

## ✨ Features

* 🕸️ Web scraping of product reviews
* 🧹 Text cleaning and preprocessing
* ✂️ Chunking for long text handling
* 🤖 LLM-based summarization
* 📊 Sentiment analysis
* 💾 Export results to CSV

---

## 🧱 Project Structure

```
LLM-Review-Summarizer/
│── main.py
│── scraper.py
│── preprocess.py
│── llm_analyzer.py
│── utils.py
│── requirements.txt
│── README.md
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

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧠 Design Choices

* **Chunking Strategy**: Large review text is split into smaller chunks to handle LLM token limits
* **Modular Architecture**: Separate files for scraping, preprocessing, and LLM interaction
* **API-based LLM Integration**: Used OpenAI API for summarization and sentiment
* **CSV Output**: Easy to analyze and visualize

---

## ⚠️ Limitations

* Amazon structure may change → scraper may break
* Dynamic content may require Selenium
* API usage cost depends on number of reviews
* Rate limits can affect performance

---

## 🎥 Demo Video

https://drive.google.com/file/d/1qp2_GtcIwnHmEuGLLh9Cr_u6xaolnnvQ/view?usp=drive_link

---

## 🚀 Future Improvements

* Add support for multiple websites
* Build Streamlit UI
* Add real-time dashboard
* Improve sentiment accuracy

---

## 🧠 Tech Stack

* Python
* OpenAI API
* BeautifulSoup / Requests
* Pandas

---

## 👨‍💻 Author

Vidish Sharma
B.Tech AIML

---
