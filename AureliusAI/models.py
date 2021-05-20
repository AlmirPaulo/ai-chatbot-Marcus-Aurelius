from flask_pymongo import PyMongo
from . import create_app

db = PyMongo(create_app(),uri='mongodb://localhost:27017/ai_knowledge_base')



