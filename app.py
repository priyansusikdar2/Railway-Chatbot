from flask import Flask, request, jsonify, render_template
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from string import punctuation
from nltk.tokenize import word_tokenize

app = Flask(__name__)

pairs = [
    [
        r"How can I avail internet reservation facility through credit cards?",
        ["Recently internet reservation facility has started on Indian Railways. The web site http://www.irctc.co.in is operational, wherein you can get the railway reservation done through Credit Cards."]
    ],
    [
        r'Why are PNR and reservation availability queries not available after certain timings at night?',
        ['The online PNR and seat availability queries are fetched from the computerized reservation applications. These are shut down daily around 23:30 hrs to 00:30 hrs IST.']
    ],
    [
        r'How can I avail the enquiries, through SMS on mobile phones?',
        ['All the enquiries on www.indianrail.gov.in are available on your mobile phone through SMS facility.']
    ],
    [
        r'Why do sometimes the fonts, colors schemes and java scripts behave differently in some browser or browsers?',
        ['This web site is best viewed with Microsoft Internet Explorer 6.0 and above.']
    ],
    [
        r'Where can I get the latest arrival and departure timings of trains, when they get delayed?',
        ['The latest arrival and departure timings of delayed trains will be made available shortly on this web site.']
    ],
    [
        r'Where can I lodge complaint against any type of grievances in the Trains, Platforms, officials for problems on this web site and give suggestions?',
        ['Please use the Feedback & suggestions page on http://www.indianrail.gov.in to submit your complaints and suggestions.']
    ],

    # New questions about booking, availability, timing
    [
        r'How do I book a train ticket online?',
        ['You can book train tickets online at IRCTC official site: https://www.irctc.co.in. You need to register, login, and then make reservations easily using various payment methods.']
    ],
    [
        r'How can I check seat availability for a train?',
        ['Seat availability can be checked on the IRCTC website or Indian Railways enquiry portal: https://www.irctc.co.in or https://enquiry.indianrail.gov.in. Enter train number and date to get availability status.']
    ],
    [
        r'How can I get live train timings or status?',
        ['Live train status and running timings can be checked at https://enquiry.indianrail.gov.in or via SMS by sending TRAIN <train_number> to 139.']
    ],
]

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, '')
    tokens = word_tokenize(text)
    filtered = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return set(filtered)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form.get('user_input', '')
    user_words = preprocess(user_input)
    
    best_match_index = -1
    max_overlap = 0
    
    for i, (question_pattern, answers) in enumerate(pairs):
        question_words = preprocess(question_pattern)
        overlap = len(user_words.intersection(question_words))
        if overlap > max_overlap:
            max_overlap = overlap
            best_match_index = i
    
    if best_match_index != -1 and max_overlap > 0:
        answer = pairs[best_match_index][1][0]
    else:
        answer = "Sorry, I couldn't understand your question. Please ask about train ticket booking, seat availability, live train timings, or IRCTC services."
    
    return jsonify({'response': answer})

if __name__ == '__main__':
    try:
        nltk.data.find('corpora/stopwords')
        nltk.data.find('corpora/wordnet')
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('stopwords')
        nltk.download('wordnet')
        nltk.download('punkt')
    
    app.run(debug=True)
