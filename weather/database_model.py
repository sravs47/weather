from flask_sqlalchemy import SQLAlchemy
from weather import app

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rootroot'
app.config['MYSQL_DB'] = 'weather'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootroot@localhost/weather'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
