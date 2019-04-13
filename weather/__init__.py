from flask import Flask
app = Flask(__name__)


from flask_restful import Api
import weather.database_model
from weather.api.token import Token_transactions,token_cheker,token_blueprint
from weather.api.weather import weather_blueprint,weather_data


api = Api(token_blueprint,weather_blueprint)
app.register_blueprint(token_blueprint)
app.register_blueprint(weather_blueprint)

api.add_resource(Token_transactions,'/token')
api.add_resource(token_cheker,'/token/<token_id>')
api.add_resource(weather_data,'/weather')


if __name__=='__main__':
    app.run(debug=True)