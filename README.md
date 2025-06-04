# IRCTC Chatbot Project

## Overview

This project implements a simple FAQ chatbot for Indian Railways-related queries using Python, NLTK, and Flask. The chatbot answers common questions about train ticket booking, seat availability, live train timings, and other Indian Railways services by matching user queries against predefined FAQs.

---

## Features

- **Natural Language Processing:** Uses NLTK for tokenization, stopword removal, and lemmatization to preprocess user queries and FAQ questions.
- **FAQ Matching:** Matches user input to the best FAQ answer using word overlap after preprocessing.
- **Web Interface:** A Flask-based web application with a simple chat interface where users can type questions and receive answers dynamically.
- **Expanded FAQ:** Includes questions related to internet reservation via credit cards, PNR queries, SMS services, train timings, booking tickets, seat availability, and live train status.
- **Fallback Response:** Provides a helpful fallback message if the user's question is not understood.

---

## Technologies Used

- Python 3.x
- Flask (Web framework)
- NLTK (Natural Language Toolkit)
- HTML/CSS/JavaScript (Frontend)

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-folder>

**Install dependencies:**

pip install -r requirements.txt

**Download NLTK data (stopwords, wordnet, punkt):**
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

**Run the Flask app:**
python app.py

**Open your browser and visit:**
http://127.0.0.1:5000

**How It Works**
User inputs a question via the web interface.

The backend preprocesses the question (tokenization, stopword removal, lemmatization).

It compares the processed input to predefined FAQ questions and finds the best matching question.

Returns the corresponding answer as a response to the frontend.

If no match is found, returns a fallback message.

**License**
This project is open-source and free to use under the MIT License.




