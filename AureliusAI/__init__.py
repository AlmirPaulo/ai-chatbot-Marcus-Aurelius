from flask import Flask
import logging

#Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(filename='server.log', format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')
app = Flask(__name__)

#Factory
def create_app():
    #Imports
    from AureliusAI import views, simple_views, ai, models
    #Configurations
    app.config['SECRET_KEY'] = 'Use something really secure in deployment, not this silly text.'
    
    #Blueprint registration
    from .ai import ai
    from .simple_views import simple_views
    app.register_blueprint(ai)
    app.register_blueprint(simple_views)

    return app
