from weather.database_model import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from weather.database_entities.customer_entity import customers
from weather.database_entities.city_entity import cities



class user_cities(db.Model):
    __tablename__='user_city'
    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id',db.Integer,ForeignKey('customer.id'))
    city_id = db.Column('city_id',db.Integer,ForeignKey('city.id'))

