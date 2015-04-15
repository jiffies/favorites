import datetime
from peewee import *
from playhouse.flask_utils import FlaskDB
from app import app

DATABASE = 'mysql://root:root@localhost:3306/favorites'
app.config.from_object(__name__)

flask_db = FlaskDB(app)
database = flask_db.database

class User(flask_db.Model):
    id = PrimaryKeyField()
    username = CharField(unique=True)
