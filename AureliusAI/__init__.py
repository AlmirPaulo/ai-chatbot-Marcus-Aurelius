from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
db = PyMongo()

def create_app():
    #Imports
    from AureliusAI import views, simple_views, ai, models
    #Configurations
    app.config['SECRET_KEY'] = 'SECRET_KEY'
    
    db.init_app(app, uri="mongodb://localhost:27017/ai_knowledge_base")

    #Blueprint registration
    from .ai import ai
    from .simple_views import simple_views
    app.register_blueprint(ai)
    app.register_blueprint(simple_views)

    return app
