from weather.utils import is_newerthan_1hour,JSON_MIME_TYPE
from weather.middleware.tokens_middleware import tokens_midlware
from flask import Response
import json

class token_verification:
    def token_response(self,to_model):
        db_time = tokens_midlware().get_time(to_model)
        if is_newerthan_1hour(db_time):
            tkn_id = tokens_midlware().get_token_id(to_model)
            return Response(json.dumps(tkn_id), status=200, mimetype=JSON_MIME_TYPE)
        else:
            token_id =tokens_midlware().create_token(to_model)
            print("successfully updated token")
            return Response(json.dumps(token_id), status=201, mimetype=JSON_MIME_TYPE)
