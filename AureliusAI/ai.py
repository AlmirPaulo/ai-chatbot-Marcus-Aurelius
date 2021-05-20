from . import views
from flask import Blueprint, flash
import logging

#Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='server.log', format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

#Blueprint
ai = Blueprint('ai', __name__)

#The chatbot
@ai.route('/', methods=['GET', 'POST'])
def ai_chatbot():
    #Work on the adaptation of the AI code
    return views.index()
