import json
from flask import Response,Blueprint,request
from weather.middleware.token_verification import is_expired
from flask_restful import Resource
import requests
from weather.utils import JSON_MIME_TYPE
from functools import lru_cache

weather_blueprint = Blueprint('weather_blueprint',__name__)


class weather_data(Resource):

    @is_expired
    def get(self):
        args = request.args
        return Response(json.dumps(weather_data.get_weather(args['type'],args['value'])),status=200,mimetype=JSON_MIME_TYPE)

    @lru_cache(maxsize=10)
    def get_weather(type,value):
        if type=='name':
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
            data =[]
            r = requests.get(url.format(value)).json()
            weather ={
                'city':value,
                'temperature':r['main']['temp'],
                'description':r['weather'][0]['description'],
                'icon':r['weather'][0]['icon'],
            }
            data.append(weather)
            return data
        elif type=='zip':
            data = []
            url1 = 'http://api.zippopotam.us/us/{}'
            r1 = requests.get(url1.format(value)).json()
            city_name = {
                'city_name': r1['places'][0]['place name']
            }
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
            data = []
            r = requests.get(url.format(city_name['city_name'])).json()
            weather = {
                'city': city_name['city_name'],
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            data.append(weather)
            return data


