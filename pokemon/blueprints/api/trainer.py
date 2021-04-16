from flask_restful import Resource, reqparse
from pokemon.models.trainers import TrainerModel


param = reqparse.RequestParser()
param.add_argument('id_trainer', type=int)
param.add_argument('nickname', type=str)
param.add_argument('first_name', type=str)
param.add_argument('last_name', type=str)
param.add_argument('email', type=str, required=True, help='Field "email" cannot be left blank.')
param.add_argument('password', type=str, required=True, help='Field "password" cannot be left blank.')
param.add_argument('team', type=str)


class Trainer(Resource):
    def get(self, id_trainer):
        trainer = TrainerModel.find(id_trainer)
        if trainer:
            return trainer.json(), 200
        return {'message': 'trainer not found'}, 404

    def delete(self, id_trainer):
        trainer = TrainerModel.find(id_trainer)
        if trainer:
            trainer.delete()
            return {'message': 'trainer deleted.'}, 200
        return {'message': 'trainer not found'}, 404

class Trainers(Resource):
    def get(self):
        return {'trainers': [trainer.json() for trainer in TrainerModel.query.all()]}

    def post(self):
        dados = param.parse_args()
        trainer = TrainerModel(**dados)
        if TrainerModel.find(dados['id_trainer']):
            return {'message': 'id "{}" already exists.'.format(dados['id_trainer'])}, 400
        try:
            trainer.save()
        except:
            return {'message': 'there was an internal server error while saving the trainers.'}, 500
        return trainer.json(), 200
