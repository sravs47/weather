from weather.exceptions import weatherException
from weather.database_entities.customer_entity import customers
from weather.database_model import db
import uuid
import datetime

class tokens_midlware:
    def create_token(self,customer_model):
        cm_to_ce = customers(username=customer_model.username, password=customer_model.password)
        cust_data = customers.query.filter(customers.username == cm_to_ce.username, customers.password == cm_to_ce.password).first()
        if cust_data is not None:
            cust_data.username = customer_model.username
            cust_data.password = customer_model.password
            cust_data.token_id = uuid.uuid4()
            cust_data.time = datetime.datetime.now()
            db.session.add(cust_data)
            db.session.commit()
        return cust_data.token_id

    def get_time(self,customer_model):
        cm_to_ce = customers(username=customer_model.username, password=customer_model.password)
        cust_data = customers.query.filter(customers.username == cm_to_ce.username,
                                           customers.password == cm_to_ce.password).first()
        return cust_data.time

    def get_token_id(self,customer_model):
        cm_to_ce = customers.customer(username=customer_model.username, password=customer_model.password)
        cust_data = customers.query.filter(customers.username == cm_to_ce.username,
                                           customers.password == cm_to_ce.password).first()
        return cust_data.token_id

    def is_token_id(self,token_id):
        is_token = customers.query.filter(customers.token_id == token_id).first()
        if is_token is not None:
            return True
        return False

    def get_token_time(self,token_id):
        return self.get_token(token_id).time

    def get_token(self, token_id):
        token_data = customers.query.filter(customers.token_id == token_id).first()
        if token_data is not None:
            return token_data
        else:
            raise weatherException({'code':'c1','message':'Not a valid token'})











