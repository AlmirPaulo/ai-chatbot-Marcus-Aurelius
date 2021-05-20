from flask import Flask


app = Flask(__name__)

def create_app():

    from AureliusAI import views, simple_views, ai, models
    app.config['SECRET_KEY'] = 'SECRET_KEY'

    #Blueprint registration
    from .ai import ai
    from .simple_views import simple_views
    app.register_blueprint(ai)
    app.register_blueprint(simple_views)

    

    return app
