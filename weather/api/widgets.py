import json
from flask import request,Response,Blueprint
from flask_restful import Resource
from weather.utils import JSON_MIME_TYPE
from weather.middleware.token_verification import is_expired
from weather.middleware.widgets_middleware import widgets_middleware
from concurrent.futures import ThreadPoolExecutor,as_completed

widget_blueprint = Blueprint('widget_blueprint',__name__)

class weather_widget(Resource):
    @is_expired
    def post(self):
        data = request.json
        print(data['city'])
        token_number = request.headers.get('auth_token')
        x =widgets_middleware().add_user_city(data['city'],token_number)
        return Response(json.dumps(x),status=201,mimetype=JSON_MIME_TYPE)

    @is_expired
    def get(self):
        token_number = request.headers.get('auth_token')
        users_data = widgets_middleware().get_user(token_number)
        cities_list = widgets_middleware().get_user_cities(users_data.id)
        widgets = []

        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(widgets_middleware().get_city_using_id(city.city_id)) for city in cities_list]

        print(len(futures))
        for future in  as_completed(futures):
            widget=future.result()
            widgets.append({'Widget ID': widget.id,'City Name': widget.city})



        # for future in futures:
        #     try:
        #         data = future.result()
        #     except Exception as e:
        #         print(e)
        return Response(json.dumps("testing"),status=200,mimetype=JSON_MIME_TYPE)

class weather_widget_operations(Resource):
    @is_expired
    def delete(self,widget_id):
        res = widgets_middleware().delete_user_city(widget_id)
        return Response(json.dumps(res),status = 200, mimetype=JSON_MIME_TYPE)


















