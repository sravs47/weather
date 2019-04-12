import json
from flask import request,Response,Blueprint
from weather.models.customer import customer
from flask_restful import Resource
from weather.middleware.tokens_middleware import tokens_midlware
token_blueprint = Blueprint('token_blueprint',__name__)
from weather.utils import is_newerthan_1hour,JSON_MIME_TYPE,to_dict

class Token(Resource):
    def get(self,token_id):
        pass

class Token_transactions(Resource):
    def post(self):
        data = request.json
        to_model = customer(data['username'],data['password'])
        db_time = tokens_midlware().get_time(to_model)
        if is_newerthan_1hour(db_time):
            tkn_id = tokens_midlware().get_token_id(to_model)
            return Response(json.dumps(tkn_id), status=200, mimetype=JSON_MIME_TYPE)
        else:
            token_id =tokens_midlware().create_token(to_model)
            print("successfully updated token")
            return Response(json.dumps(token_id), status=201, mimetype=JSON_MIME_TYPE)
class token_cheker(Resource):
    def get(self,token_id):
        data = request.json
        is_token = tokens_midlware().is_token_id(token_id)
        return Response(json.dumps(is_token),status=200,mimetype=JSON_MIME_TYPE)












