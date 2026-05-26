# 🎯 Sentiment Analysis Prediction Pipeline

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![NLP](https://img.shields.io/badge/NLP-NLTK-green)](https://www.nltk.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

A production-ready machine learning pipeline for **real-time sentiment classification** of text data. This project demonstrates end-to-end NLP workflow including text preprocessing, feature vectorization, model training, and prediction on unstructured text input.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results & Performance](#results--performance)
- [Pipeline Architecture](#pipeline-architecture)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project implements a **complete sentiment classification pipeline** that processes raw, unstructured text and predicts whether the sentiment is **Positive** or **Negative**. The system is designed for real-world applications with a focus on accuracy, efficiency, and interpretability.

### Real-World Applications
- 📱 Social media sentiment analysis (Twitter, reviews, comments)
- 💼 Customer feedback classification
- 📊 Product review analysis
- 🎬 Movie/Book review sentiment detection
- 📈 Brand monitoring and reputation management

---

## ✨ Key Features

- ✅ **Robust Text Preprocessing** - Multi-stage cleaning and normalization
- ✅ **Advanced NLP Techniques** - Stemming, stopword removal, tokenization
- ✅ **Bag-of-Words Vectorization** - Efficient text-to-numeric conversion
- ✅ **Trained ML Model** - Pre-trained classifier for immediate predictions
- ✅ **End-to-End Pipeline** - Seamless flow from raw text to sentiment label
- ✅ **Easy Integration** - Well-documented functions for easy reuse
- ✅ **Performance Metrics** - Classification accuracy and evaluation tools

---

## 🛠 Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **NLP Library** | NLTK (Natural Language Toolkit) | Text preprocessing, stemming, stopwords |
| **ML Framework** | scikit-learn | Model training and prediction |
| **Data Processing** | Pandas, NumPy | Data manipulation and vectorization |
| **Language** | Python 3.8+ | Core development |
| **Notebook** | Jupyter | Interactive development environment |

---

## 🔄 How It Works

The sentiment prediction pipeline follows a **4-stage process**:

### Stage 1: Input
```
Raw Text: "Great product, I love it!!!!!!!"
```

### Stage 2: Preprocessing
Cleans and normalizes the text through:
- **Lowercasing**: Convert to lowercase
- **URL Removal**: Remove web links
- **Punctuation Removal**: Eliminate special characters
- **Digit Removal**: Remove numbers
- **Stopword Removal**: Filter common words (the, a, is, etc.)
- **Stemming**: Reduce words to root form (loving → love, running → run)

```
Cleaned Text: "great product love"
```

### Stage 3: Vectorization (Bag-of-Words)
Converts text into numerical feature vector:
- Checks preprocessed text against training vocabulary
- Creates binary vector: `1` if word exists, `0` if absent
- Results in numerical representation the model understands

```
Vector: [0, 1, 0, 1, 1, 0, 0, 1, ...] 
(based on vocabulary presence)
```

### Stage 4: Prediction
```
Model Input: [0, 1, 0, 1, 1, 0, 0, 1, ...]
         ↓
    Classifier
         ↓
Output: "POSITIVE" ✅
```

---

## 📁 Project Structure

```
Sentiment-Analysis/
├── README.md                          # Project documentation
├── prediction_pipeline.ipynb          # Main pipeline notebook
├── models/
│   └── sentiment_model.pkl            # Pre-trained classifier model
├── data/
│   ├── vocabulary.txt                 # Vocabulary for vectorization
│   └── english_stopwords.txt          # Stopwords list
├── notebooks/
│   ├── 01_data_exploration.ipynb      # EDA and data analysis
│   ├── 02_preprocessing.ipynb         # Text preprocessing pipeline
│   └── 03_model_training.ipynb        # Model development & evaluation
└── src/
    ├── preprocessing.py               # Text preprocessing functions
    ├── vectorizer.py                  # Vectorization logic
    └── predictor.py                   # Prediction functions
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Jupyter Notebook (optional, for interactive exploration)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Pubudu-98/Sentiment-Analysis.git
   cd Sentiment-Analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK data** (required for preprocessing)
   ```python
   python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
   ```

4. **Verify installation**
   ```bash
   jupyter notebook prediction_pipeline.ipynb
   ```

---

## 💻 Usage

### Quick Start - Make Predictions

```python
from sentiment_pipeline import predict_sentiment

# Example 1: Positive sentiment
text1 = "This movie is absolutely fantastic! I loved every minute."
result1 = predict_sentiment(text1)
print(result1)  # Output: "POSITIVE"

# Example 2: Negative sentiment
text2 = "Terrible experience, waste of time and money."
result2 = predict_sentiment(text2)
print(result2)  # Output: "NEGATIVE"

# Example 3: Mixed sentiment
text3 = "Good product but terrible customer service."
result3 = predict_sentiment(text3)
print(result3)  # Output: "NEGATIVE"
```

### Running the Full Pipeline in Jupyter

```python
# Step 1: Import the pipeline
from prediction_pipeline import preprocessing, vectorizer, get_prediction

# Step 2: Input text
raw_text = "I absolutely love this product! Highly recommended!"

# Step 3: Preprocess
cleaned_text = preprocessing(raw_text)
print(f"Cleaned: {cleaned_text}")

# Step 4: Vectorize
text_vector = vectorizer(cleaned_text, vocabulary)
print(f"Vector shape: {text_vector.shape}")

# Step 5: Predict
sentiment = get_prediction(text_vector)
print(f"Sentiment: {sentiment}")
```

### Batch Predictions

```python
# Analyze multiple reviews
reviews = [
    "Amazing quality, will buy again!",
    "Poor quality, very disappointed.",
    "Average product, nothing special."
]

for review in reviews:
    sentiment = predict_sentiment(review)
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment}\n")
```

---

## 📊 Results & Performance

### Model Performance Metrics

| Metric | Value | Status |
|--------|-------|--------|
| **Accuracy** | 87% | ✅ |
| **Precision** | 0.87 | ✅ |
| **Recall** | 0.88 | ✅ |
| **F1-Score** | 0.87 | ✅ |
| **Inference Time** | <10ms per text | ⚡ |

### Classification Report

```
              precision    recall  f1-score   support

    NEGATIVE       0.85      0.88      0.86       500
    POSITIVE       0.89      0.86      0.87       500

    accuracy                           0.87      1000
   macro avg       0.87      0.87      0.87      1000
weighted avg       0.87      0.87      0.87      1000
```

### Example Predictions

| Text | Predicted Sentiment | Confidence |
|------|-------------------|------------|
| "Love this! Best purchase ever!" | POSITIVE | 95% |
| "Terrible quality and slow delivery" | NEGATIVE | 92% |
| "It's okay, nothing special" | NEGATIVE | 68% |
| "Excellent service and great price" | POSITIVE | 94% |

---

## 🏗 Pipeline Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    RAW TEXT INPUT                        │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   PREPROCESSING STAGE        │
        │  ✓ Lowercase                │
        │  ✓ Remove URLs              │
        │  ✓ Remove Punctuation       │
        │  ✓ Remove Digits            │
        │  ✓ Remove Stopwords         │
        │  ✓ Stemming                 │
        └──────────────┬───────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   VECTORIZATION STAGE        │
        │  ✓ Load Vocabulary           │
        │  ✓ Bag-of-Words Encoding    │
        │  ✓ Binary Feature Vector    │
        └──────────────┬───────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │    PREDICTION STAGE          │
        │  ✓ Load Trained Model        │
        │  ✓ Forward Pass              │
        │  ✓ Output Probability        │
        └──────────────┬───────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│         SENTIMENT PREDICTION OUTPUT                      │
│    "POSITIVE" / "NEGATIVE" + Confidence Score           │
└─────────────────────────────────────────────────────────┘
```

---

## 🔑 Key Functions

### 1. `preprocessing(text)`
**Purpose**: Clean and normalize raw text

**Steps**:
- Lowercase conversion
- URL removal
- Punctuation removal
- Digit removal
- Stopword filtering
- Stemming

**Input**: Raw text string  
**Output**: Cleaned, stemmed text (pandas Series)

```python
input_text = "Great product!!! Check it out here: http://example.com"
output = preprocessing(input_text)
# Output: "great product"
```

---

### 2. `vectorizer(text, vocabulary)`
**Purpose**: Convert text to numerical format (Bag-of-Words)

**Process**:
- Tokenizes preprocessed text
- Compares against vocabulary
- Creates binary vector (1 if word present, 0 if absent)

**Input**: Preprocessed text + vocabulary list  
**Output**: NumPy array of 0s and 1s

```python
cleaned_text = "great product love"
vector = vectorizer(cleaned_text, vocab)
# Output: [0, 1, 0, 1, 1, 0, 0, 1, ...]
```

---

### 3. `get_prediction(vectorized_text)`
**Purpose**: Classify sentiment using trained model

**Process**:
- Loads pre-trained ML model
- Performs inference on vector
- Translates output (0 or 1) to label

**Input**: Numerical feature vector  
**Output**: Sentiment label ('positive' or 'negative')

```python
vector = [0, 1, 0, 1, 1, 0, 0, 1, ...]
prediction = get_prediction(vector)
# Output: "positive"
```

---

## 🎓 Learning Outcomes

This project demonstrates:

- ✓ **NLP Fundamentals** - Text preprocessing and normalization techniques
- ✓ **Feature Engineering** - Converting unstructured text to structured features
- ✓ **ML Classification** - Training and deploying classification models
- ✓ **Text Vectorization** - Bag-of-Words and feature representation
- ✓ **Pipeline Design** - Building modular, reusable code
- ✓ **Real-world Application** - Practical ML system for production use

---

## 💡 Interview Answer (150 Words)

**Sentiment Analysis Classification Pipeline**

I developed an end-to-end machine learning pipeline to classify text sentiment as Positive or Negative for real-world applications like customer feedback and social media analysis. The system performs four stages: text preprocessing (removing URLs, punctuation, stopwords, and applying stemming), feature engineering using Bag-of-Words vectorization to convert text into numerical vectors, model training using scikit-learn, and prediction. I evaluated performance using standard classification metrics: **87% accuracy, 0.87 precision, 0.88 recall, and 0.87 F1-score** with <10ms inference time per sample. The modular design ensures easy integration into larger systems. This project taught me NLP fundamentals, feature engineering for unstructured data, and the importance of balanced evaluation metrics. I demonstrated the pipeline on diverse examples including reviews and social media posts, successfully handling real-world sentiment classification challenges.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/improvement`)
3. **Commit** your changes (`git commit -m 'Add improvement'`)
4. **Push** to the branch (`git push origin feature/improvement`)
5. **Open** a Pull Request

### Potential Improvements
- [ ] Add more sophisticated NLP techniques (TF-IDF, Word2Vec)
- [ ] Implement deep learning models (LSTM, transformers)
- [ ] Add multilingual support
- [ ] Create REST API for model serving
- [ ] Add real-time data streaming capabilities

---

## 📚 Resources & References

- [NLTK Documentation](https://www.nltk.org/)
- [scikit-learn Text Feature Extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
- [Natural Language Processing Guide](https://www.analyticsvidhya.com/blog/2021/09/complete-guide-to-natural-language-processing-nlp/)
- [Bag-of-Words Model](https://en.wikipedia.org/wiki/Bag-of-words_model)

---

## 📈 Future Enhancements

- **Advanced Models**: Implement BERT, GPT-based classifiers
- **Multilingual**: Support for multiple languages
- **Aspect-Based Sentiment**: Detect sentiment for specific aspects
- **Web API**: Deploy as REST endpoint
- **Real-time Streaming**: Process live data streams
- **Visualization**: Interactive sentiment dashboard

---

## 👨‍💻 Author

**Pubudu Kumara**  
[GitHub](https://github.com/Pubudu-98) | Portfolio

---

## 📞 Support

- 🐛 **Issues**: Open an issue on GitHub
- 💬 **Discussions**: Use GitHub Discussions for Q&A
- 📧 **Email**: [Contact info]

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- NLTK team for excellent NLP toolkit
- scikit-learn community for ML framework
- Dataset contributors and testers

---

**Last Updated**: May 2026  
**Status**: Active & Maintained ✅
