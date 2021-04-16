from flask import Flask
from pokemon.ext import configuration


def minimal_app():
    '''
        Esta app, é para facilitar os testes 
    ''' 
    app = Flask(__name__)
    configuration.init_app(app)
    return app

def create_app():
    '''
    Para evitar o problema de circular import
    '''
    app = minimal_app()
    configuration.load_extensions(app)
    return app
