from flask import Flask
app = Flask(__name__)

from flask_restful import Api
import weather.database_model
from weather.api.token import Token_transactions,token_cheker
from weather.api.token import token_blueprint

api = Api(token_blueprint)
app.register_blueprint(token_blueprint)
api.add_resource(Token_transactions,'/token')
api.add_resource(token_cheker,'/token/<token_id>')


if __name__=='__main__':
    app.run(debug=True)