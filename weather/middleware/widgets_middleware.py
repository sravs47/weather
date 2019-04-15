from weather.database_entities.city_entity import cities
from weather.database_entities.customer_entity import customers
from weather.database_model import db
from weather.database_entities import user_cities

class widgets_middleware:
    def add_city(self,city_name):
        city_data = cities.query.filter(cities.city==city_name).first()
        if city_data is None:
            data = cities(city=city_name)
            db.session.add(data)
            db.session.commit()
            return city_name
        return None

    def get_city(self,city_name):
        return cities.query.filter(cities.city == city_name).first()

    def get_user(self,token_id):
        return customers.query.filter(customers.token_id==token_id).first()

    def get_user_cities(self,user_id):
        data_list =[]
        data =user_cities.query.filter(user_cities.user_id==user_id)
        for d in data:
            data_list.append(d)
        return data_list

    def get_city_using_id(self,city_id):
        return cities.query.filter(cities.id==city_id).first()

    def add_user_city(self,city_name,token_number):
        self.add_city(city_name)
        city_data1 = self.get_city(city_name)
        user_data = customers.query.filter(customers.token_id == token_number).first()
        user_city_data = user_cities.query.filter(user_cities.user_id==user_data.id,user_cities.city_id==city_data1.id)
        if user_data is not None and user_city_data is None:
            data2 = user_cities(user_id=user_data.id, city_id=city_data1.id)
            db.session.add(data2)
            db.session.commit()
        return {'id':city_data1.id,'city':city_data1.city}

    def delete_user_city(self,c_id):
        user_cities.query.filter(user_cities.city_id==c_id).delete()
        db.session.commit()
        return c_id


#validate payload function
# add city
# add widget
