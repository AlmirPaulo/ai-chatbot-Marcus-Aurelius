from . import views
from flask import Blueprint, flash, request
import logging
########## AI dependencies ########
import random
import string  # to process standard python strings
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem import WordNetLemmatizer
##########################################

#Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='server.log', format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

#Blueflash
ai = Blueprint('ai', __name__)

warnings.filterwarnings("ignore")

nltk.download('popular', quiet=True, download_dir='.env/nltk_data')  # for downloading packages|This download_dir may be changed in deployment 

#Get data in database             
with open('alfred-knowledge-base.txt', 'r', encoding='utf8', errors='ignore') as fin:
    raw = fin.read().lower()
#variable with data should be called "raw"
#https://www.youtube.com/watch?v=Up7dVFWW0kY
#https://flask-pymongo.readthedocs.io/en/latest/


sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences
word_tokens = nltk.word_tokenize(raw)  # converts to list of words

lemmer = WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["*nods*", "hello", "I am glad! You are talking to me"]


# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response

#The chatbot
@ai.route('/', methods=['GET', 'POST'])
def ai_chatbot():
    if request.method == 'POST':
        user_response = request.form.get('input')
        user_response = user_response.lower()
        if (user_response != 'bye'):
            if (user_response == 'thanks' or user_response == 'thank you'):
                flash("Marcus Aurelius: You are welcome..")
            else:
                if (greeting(user_response) != None):
                    flash("Marcus Aurelius: " + greeting(user_response))
                else:
                    flash("Marcus Aurelius: ")
                    flash(response(user_response))
                    sent_tokens.remove(user_response)
                    logger.debug(response(user_response))
        else:
            flash("Marcus Aurelius: Good bye my friend!")

    return views.index()
