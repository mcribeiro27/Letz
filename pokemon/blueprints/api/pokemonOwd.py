from flask_restful import Resource, reqparse
from pokemon.models.pokemonOwned import PokemonOwdModel
from pokemon.models.trainers import TrainerModel
from flask_jwt_extended import jwt_required


param = reqparse.RequestParser()
param.add_argument('id_poke_owd', type=int)
param.add_argument('name', type=str)
param.add_argument('level', type=int)
param.add_argument('pokemon_id', type=int, required=True)
param.add_argument('trainer', type=int)

class PokemonOwned(Resource):

    @jwt_required()
    def post(self, id_trainer):

        dados = param.parse_args()
        dados['trainer'] = id_trainer
        pokemon= PokemonOwdModel(**dados)
    
        if not TrainerModel.find(id_trainer):
            return{'message': 'Trainer not found'}, 404
        
        try:
            pokemon.save()
        except:
            return {'message': 'there was an internal server error while saving the pokemon.'}, 500
        return pokemon.json(), 201


    def get(self, id_trainer):
        if TrainerModel.find(id_trainer):
            return {'pokemons': [pokemon.json() for pokemon in PokemonOwdModel.query.all()]}, 200
        return {'message': 'Trainer not found'}, 404

class GetPokemonById(Resource):
    def get(self, id_trainer, id_poke_owd):
        if TrainerModel.find(id_trainer):
            pokemon = PokemonOwdModel.find(id_poke_owd)
            if pokemon:
                return pokemon.json()
            return {'message': 'pokemon not found'}, 404
        return {'message': 'Trainer not found'}, 404

    @jwt_required()
    def delete(self, id_trainer, id_poke_owd):
        if TrainerModel.find(id_trainer):
            pokemon = PokemonOwdModel.find(id_poke_owd)
            if pokemon:
                try:
                    pokemon.delete()
                except:
                    return {'message': 'internal error'}, 500
                return {'message': f'pokemon {id_poke_owd} deleted'}
        return {'message': 'Trainer not found'}, 404
