# Sentiment Analysis Project - Machine Learning (🧠 Real-Time Sentiment Analysis Application)

A Natural Language Processing (NLP) project that performs real-time sentiment analysis on tweets, classifying them as **positive**, **negative**, or **neutral**. The project leverages traditional machine learning and deep learning models (Logistic Regression, LSTM, and BERT), and displays live insights using **H2O Wave**.

---

## 📌 Overview

Sentiment analysis uses natural language processing and machine learning techniques to analyze the emotional tone or sentiment behind a piece of text. It involves identifying and categorizing opinions expressed in a text as positive, negative, or neutral. This application focuses on real-time tweet analysis to help understand public opinion trends across social media platforms.

---

## 🛠️ Features

- 🐦 Real-time tweet streaming using the Twitter API
- 🧹 Text preprocessing using NLTK and SpaCy (tokenization, lemmatization, stopword removal)
- ⚙️ Model training using:
  - Logistic Regression (Scikit-learn)
  - LSTM (TensorFlow/Keras)
  - BERT (HuggingFace Transformers)
- 📊 Live sentiment visualization using H2O Wave
- 📈 Dashboard for tracking sentiment trends over time

---

## 🧪 Tech Stack

- **Programming Language**: Python 3.10
- **Libraries**:
  - `nltk`, `spacy` – NLP preprocessing
  - `scikit-learn`, `tensorflow`, `torch`, `transformers` – ML & DL models
  - `tweepy` – Twitter streaming API
  - `h2o-wave` – Real-time web app dashboard
- **IDE**: Visual Studio Code
- **Version Control**: Git + GitHub
- **Environment Management**: Conda

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/RealTimeSentimentApp.git
cd RealTimeSentimentApp
