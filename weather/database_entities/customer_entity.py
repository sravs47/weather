from weather.database_model import db

import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref



class customers(db.Model):
    __tablename__ = 'customer'
    id = db.Column('id',db.Integer,primary_key=True)
    username = db.Column('username',db.String(20))
    password = db.Column('password',db.String(20))
    token_id = db.Column('token_id',db.String(200))
    time = db.Column('time',db.DateTime)
    city_relation = relationship('cities',secondary='user_city')
#
# class cities(db.Model):
#     __tablename__ = 'city'
#     id = db.Column('id',db.Integer,primary_key=True)
#     city = db.Column('city',db.String(20))
#     customers = relationship('customer',secondary= 'user_city')


# class user_cities(db.Model):
#     __tablename__='user_city'
#     id = db.Column('id', db.Integer, primary_key=True)
#     user_id = db.Column('user_id',db.Integer,ForeignKey('customer.id'))
#     city_id = db.Column('city_id',db.Integer,ForeignKey('city.id'))
#
#     customer_detail = relationship(customer_details,backref('user_city'))
#     citi = relationship(cities,backref('user_city'))


