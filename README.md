# NLP Application

A desktop-based Natural Language Processing (NLP) application built with Python and Tkinter that enables users to perform multiple text analysis tasks through an interactive graphical interface. The application integrates sentiment analysis, named entity recognition, and emotion detection into a single platform with user authentication support.

## Features

### User Authentication

* User Registration
* User Login
* JSON-based credential storage

### Sentiment Analysis

* Analyze text sentiment using NLTK VADER
* Classify text as Positive, Negative, or Neutral
* Display sentiment polarity scores

### Named Entity Recognition (NER)

* Extract entities from unstructured text
* Identify people, organizations, locations, dates, and other entity types
* Display entity labels and classifications

### Emotion Detection

* Detect emotions expressed in text
* Utilize Transformer-based NLP models
* Display predicted emotion along with confidence scores

## Tech Stack

* Python
* Tkinter
* NLTK
* Transformers (Hugging Face)
* JSON

## Project Structure

```bash
NLPApp/
│
├── app.py
├── db.json
├── api.py
├── mydb.py
├── requirements.txt
└── README.md
```

## How It Works

1. Register or log in to the application.
2. Choose one of the available NLP modules:

   * Sentiment Analysis
   * Named Entity Recognition
   * Emotion Detection
3. Enter text for analysis.
4. View results instantly through the graphical interface.

## Installation

```bash
git clone https://github.com/aishwaryaverma05/NLPApp.git
cd NLPApp

pip install -r requirements.txt
python app.py
```

## Learning Outcomes

* Natural Language Processing fundamentals
* Sentiment Analysis using NLTK
* Named Entity Recognition techniques
* Emotion Detection with Transformer models
* GUI development using Tkinter
* User authentication and JSON data handling

## Future Improvements

* Database integration (SQLite/MySQL)
* User activity history
* Additional NLP tasks such as text summarization and translation
* Enhanced UI/UX design
* Model performance evaluation dashboard

## Author

**Aishwarya Verma**

