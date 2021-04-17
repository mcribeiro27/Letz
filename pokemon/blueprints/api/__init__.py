from flask import Blueprint
from flask_restful import Api

from .trainer import Trainer, Trainers
from .login import Authenticate
from .pokemonOwd import PokemonOwned, GetPokemonById


bp = Blueprint('api', __name__, url_prefix='/trainer')
api = Api(bp)

def init_app(app):
    api.add_resource(Trainer, '/<id_trainer>')
    api.add_resource(Trainers, '')
    api.add_resource(Authenticate, '/authenticate')
    api.add_resource(PokemonOwned, '/<id_trainer>/pokemon')
    api.add_resource(GetPokemonById, '/<id_trainer>/pokemon/<id_poke_owd>')
    app.register_blueprint(bp)