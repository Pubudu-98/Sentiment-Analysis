# Simple Sentiment Analysis Prediction Pipeline

This project implements a streamlined prediction pipeline for classifying the sentiment (Positive or Negative) of a given text input using a pre-trained Machine Learning model. The core of the pipeline is built around essential Natural Language Processing (NLP) techniques: Preprocessing, Vectorization, and Classification.

## 🚀 How It Works (The Pipeline)

The `prediction_pipeline.ipynb` notebook demonstrates the four key stages required to turn raw text into a sentiment prediction:

1.  **Input:** A raw string of text (e.g., "great product, I love it!!!!!!").
2.  **Preprocessing:** Cleans the text by removing noise, standardizing case, and reducing words to their roots.
3.  **Vectorization:** Converts the clean text into a numerical format (a feature vector) that the model can understand.
4.  **Prediction:** The trained model classifies the numerical vector as either 'positive' or 'negetive'.

## 🛠️ Project Structure

The notebook relies on several external files that must be correctly located in the directory structure:

| File/Path | Description | Purpose |
| :--- | :--- | :--- |
| `prediction_pipeline.ipynb` | The main execution script containing the pipeline logic. | Executes the prediction flow. |
| `../static/model/sentiment_model.pkl` | The serialized (pickled) machine learning classification model (e.g., Logistic Regression). | Used by `model.predict()` to make the final classification. |
| `../static/model/corpora/vocabulary.txt` | A list of all unique words (`tokens`) the model was trained on. | Used by the `vectorizer` to create the numerical input vector. |
| `../static/model/corpora/stopwords/english` | A list of common English words (stopwords) to be removed during preprocessing. | Used by the `preprocessing` function to clean the text. |

## ⚙️ Key Functions

### 1. `preprocessing(text)`
This function is the text-cleaning step. It applies the following in order:
* Lowercasing
* URL removal
* Punctuation removal (via `remove_punctuation`)
* Digit removal
* Stopword removal (using the loaded `sw` list)
* Stemming (using the `PorterStemmer`)

**Input:** Raw text string.
**Output:** A clean, stemmed pandas Series object containing the processed text (e.g., "great product love").

### 2. `vectorizer(ds, vocabulary)`
This function implements the **Bag-of-Words (BoW)** vectorization model.
* It checks the preprocessed text (`ds`) against the training vocabulary (`tokens`).
* It creates a binary vector: `1` if a vocabulary word is present in the text, `0` if it is absent.

**Input:** Preprocessed text and the vocabulary list.
**Output:** A NumPy array (vector) of 0s and 1s, ready for the model.

### 3. `get_prediction(vectorized_txt)`
The final classification step.
* It feeds the numerical vector into the pre-loaded `model`.
* It translates the model's numerical output (0 or 1) into a readable sentiment label.

**Input:** The numerical feature vector.
**Output:** The sentiment label: `'positive'` (for prediction `0`) or `'negetive'` (for prediction `1`).

## 🔑 How to Run

1.  Ensure all required files (`.pkl` model, `vocabulary.txt`, `english` stopwords list) are correctly placed relative to the notebook as shown in the paths above.
2.  Run all cells in the `prediction_pipeline.ipynb` notebook sequentially.
3.  The final cells demonstrate the entire pipeline execution for test text inputs.
