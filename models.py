import datetime
from peewee import *
from playhouse.flask_utils import FlaskDB

flask_db = FlaskDB()
database = flask_db.database

class User(flask_db.Model):
    id = PrimaryKeyField()
    username = CharField(unique=True)
