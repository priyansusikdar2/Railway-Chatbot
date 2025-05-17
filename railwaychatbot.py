import nltk
from nltk.chat.util import Chat, reflections
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Predefined FAQ pairs
pairs = [
    [
        r"How can I avail internet reservation facility through credit cards?",
        ['Recently internet reservation facility has started on Indian Railways. The web site http://www.irctc.co.in is operational, wherein you can get the railway reservation done through Credit Cards.']
    ],
    [
        r'Why are PNR and reservation availability queries not available after certain timings at night?',
        ['The online PNR and seat availability queries are fetched from the computerized reservation applications. These are shut down daily around 2330 hrs to 0030 hrs IST.']
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
]

# Unique list function
def unique(list1):
    return list(set(list1))

# Lemmatizer instance
lemmatiser = WordNetLemmatizer()

# Preprocessing function
def preprocessing(sent):
    rem_words = ['get', 'avail', 'who', 'where', 'how', 'what', 'why', 'when', 'i', 'can']
    for p in punctuation:
        sent = sent.replace(p, '')
    sent = sent.lower().split()
    stop_words = set(stopwords.words('english'))
    sent = [i for i in sent if i not in stop_words and i not in rem_words]
    sent = [lemmatiser.lemmatize(item, pos="v") for item in sent]
    return unique(sent)

# Bot function
def tellme_bot():
    while True:
        response = input("Tell Me. [q to quit]> ")
        if response.lower() == 'q':
            break

        list_response = preprocessing(response)
        best_match_index = -1
        max_matches = 0

        for i, pair in enumerate(pairs):
            pair_text = pair[0] + " " + " ".join(pair[1])
            list_pair = preprocessing(pair_text)

            match_count = sum(1 for word in list_response if word in list_pair)

            if match_count > max_matches:
                max_matches = match_count
                best_match_index = i

        if best_match_index != -1:
            print(pairs[best_match_index][1][0])
        else:
            print("Unable to answer this question.")

        break  # Remove this if you want the bot to continue until 'q' is typed

# Run the bot when the script is executed
if __name__ == '__main__':
    # Ensure necessary NLTK data is downloaded
    try:
        nltk.data.find('corpora/stopwords')
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('stopwords')
        nltk.download('wordnet')

    tellme_bot()
