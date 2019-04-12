
from weather.database_entities.customer_entity import customer
from weather.database_model import db
import uuid
import datetime

class tokens_midlware:
    def create_token(self,customer_model):
        cm_to_ce = customer(username=customer_model.username,password=customer_model.password)
        cust_data = customer.query.filter(customer.username==cm_to_ce.username,customer.password==cm_to_ce.password).first()
        if cust_data is not None:
            cust_data.username = customer_model.username
            cust_data.password = customer_model.password
            cust_data.token_id = uuid.uuid4()
            cust_data.time = datetime.datetime.now()
            db.session.add(cust_data)
            db.session.commit()
        return cust_data.token_id

    def get_time(self,customer_model):
        cm_to_ce = customer(username=customer_model.username, password=customer_model.password)
        cust_data = customer.query.filter(customer.username == cm_to_ce.username,
                                          customer.password == cm_to_ce.password).first()
        return cust_data.time

    def get_token_id(self,customer_model):
        cm_to_ce = customer(username=customer_model.username, password=customer_model.password)
        cust_data = customer.query.filter(customer.username == cm_to_ce.username,
                                          customer.password == cm_to_ce.password).first()
        return cust_data.token_id

    def is_token_id(self,token_id):
        is_token = customer.query.filter(customer.token_id == token_id).first()
        if is_token is not None:
            return True
        return False













