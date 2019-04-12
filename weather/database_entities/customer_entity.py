from weather.database_model import db
import datetime

class customer(db.Model):
    id = db.Column('id',db.Integer,primary_key=True)
    username = db.Column('username',db.String(20))
    password = db.Column('password',db.String(20))
    token_id = db.Column('token_id',db.String(200))
    time = db.Column('time',db.DateTime)

    def __init__(self,username,password,token_id=None,time=datetime.datetime.now()):
        self.username=username
        self.password=password
        self.token_id=token_id
        self.time = time
