from weather.database_model import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class cities(db.Model):
    __tablename__ = 'city'
    id = db.Column('id',db.Integer,primary_key=True)
    city = db.Column('city',db.String(20))
    customers = relationship('customers',secondary= 'user_city')


