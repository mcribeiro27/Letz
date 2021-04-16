from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import safe_str_cmp
from pokemon.models.trainers import TrainerModel


class Authenticate(Resource):
    param = reqparse.RequestParser()
    param.add_argument('email', type=str, required=True, help='Field "email" cannot be left blank.')
    param.add_argument('password', type=str, required=True, help='Field "password" cannot be left blank.')

    @classmethod
    def post(cls):
        dados = Authenticate.param.parse_args()
        trainer = TrainerModel.find_by_email(dados['email'])

        if trainer and safe_str_cmp(trainer.password, dados['password']):
            token = create_access_token(identity=trainer.id_trainer)
            return {'access_token': token}, 200
        return {'message': 'email or password is incorrect!'}, 401
