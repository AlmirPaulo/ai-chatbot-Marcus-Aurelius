from AureliusAI import ai, simple_views, models, views, create_app
from urllib.request import urlopen
import pytest, os

def test_app_instance():
    assert create_app != None

def test_log_file_created():
    assert os.path.exists('server.log')

def test_nltk_data_created():
    #change this path in deployment
    assert os.path.exists('.env/nltk_data')
    
@pytest.mark.parametrize('module',[])
def test_logs_debug_mode(module):
    assert module.logger.level == 10
    #assert module.logger.level != 10

@pytest.mark.parametrize('route',['/appinfo','/Marcus_Aurelius', '/'])
def test_check_routes(route):
    url = 'http://127.0.0.1:5000'+route
    resp = urlopen(url)
    assert resp.status == 200

