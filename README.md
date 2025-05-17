# Railway FAQ Chatbot 🤖🚆

A simple command-line chatbot built using **NLTK** that answers frequently asked questions about Indian Railways such as reservations, delays, complaints, and more.

## 🔧 Features

- Keyword-based matching using lemmatization and stopword removal
- Predefined question-answer pairs (can be easily extended)
- Command-line interface
- Smart preprocessing using NLTK

## 📦 Requirements

- Python 3.x
- NLTK

Install NLTK using pip:

```bash
pip install nltk
```

Also, download the necessary NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

## 🚀 How to Run

1. Clone or download this repository.
2. Open the terminal in the project directory.
3. Run the script:

```bash
python railway_bot.py
```

4. Enter your query when prompted:

```bash
Tell Me. [q to quit]> CAN I RESERVE RAILWAYS BOOKING
```

Expected Output:

```
Recently internet reservation facility has started on Indian Railways. The web site http://www.irctc.co.in is operational, wherein you can get the railway reservation done through Credit Cards.
```

Type `q` to exit the chatbot.

## 📁 File Structure

- `railway_bot.py`: Main script with the chatbot logic
- `README.md`: This file

## 🛠️ Customization

To add more questions and answers, modify the `pairs` list in `railway_bot.py`. Use regular expressions for better matching, or integrate fuzzy matching for improved flexibility.

## 📌 Note

- This bot works offline once the NLTK resources are downloaded.
- It's a basic implementation and can be extended with GUI, web interface, or database-backed FAQs.

## 📃 License

This project is free to use for educational purposes.

---

Made with ❤️ using Python and NLTK
