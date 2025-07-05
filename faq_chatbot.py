import nltk
import ssl
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import numpy as np

# Handle SSL issues on Windows
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download required NLTK data
def ensure_nltk_data():
    """Ensure all required NLTK data is downloaded"""
    required_packages = ['punkt', 'wordnet', 'stopwords', 'averaged_perceptron_tagger']
    
    for package in required_packages:
        try:
            nltk.download(package, quiet=True)
        except Exception as e:
            print(f"Warning: Could not download {package}: {e}")

# Download NLTK data
ensure_nltk_data()

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

faq_data = [
    {"question": "What is your return policy?", "answer": "You can return any item within 30 days."},
    {"question": "How do I track my order?", "answer": "Use the tracking link sent to your email."},
    {"question": "Do you offer international shipping?", "answer": "Yes, we ship worldwide."},
    {"question": "How can I contact customer support?", "answer": "You can email us at support@example.com."},
    {"question": "Can I cancel my order?", "answer": "Yes, before it is shipped. Contact us ASAP."}
]

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return ' '.join(tokens)

processed_questions = [preprocess(faq["question"]) for faq in faq_data]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)

def get_faq_response(user_query):
    user_query = preprocess(user_query)
    user_vector = vectorizer.transform([user_query])
    similarity = cosine_similarity(user_vector, faq_vectors)
    max_index = np.argmax(similarity)

    if similarity[0][max_index] > 0.3:
        return faq_data[max_index]["answer"]
    else:
        return "Sorry, I couldn't find a relevant answer."

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Bot:", get_faq_response(user_input))
