import json
from flask import request,Response,Blueprint
from weather.models.customer import customer
from flask_restful import Resource
from weather.middleware.tokens_middleware import tokens_midlware
from weather.utils import JSON_MIME_TYPE
from weather.middleware.token_verification import token_verification


token_blueprint = Blueprint('token_blueprint',__name__)


class Token_transactions(Resource):
    def post(self):
        data = request.json
        to_model = customer(data['username'],data['password'])
        return  token_verification().token_response(to_model)


class token_cheker(Resource):
    def get(self,token_id):
        is_token = tokens_midlware().is_token_id(token_id)
        return Response(json.dumps(is_token),status=200,mimetype=JSON_MIME_TYPE)












