from flask import Flask
app = Flask(__name__)

from flask_restful import Api
import weather.database_model
from weather.api.token import Token_transactions,token_cheker,token_blueprint
from weather.api.weather import weather_blueprint,weather_data
from weather.api.widgets import widget_blueprint,weather_widget,weather_widget_operations

api = Api(token_blueprint,weather_blueprint,widget_blueprint)
app.register_blueprint(token_blueprint)
app.register_blueprint(weather_blueprint)
app.register_blueprint(widget_blueprint)

api.add_resource(Token_transactions,'/token')
api.add_resource(token_cheker,'/token/<token_id>')
api.add_resource(weather_data,'/weather')
api.add_resource(weather_widget,'/widget')
api.add_resource(weather_widget_operations,'/widget/<widget_id>')

if __name__=='__main__':
    app.run(debug=True)