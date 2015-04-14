import datetime
from peewee import *

from app import flask_db


class User(flask_db.Model):
    id = PrimaryKeyField()
    username = CharField(unique=True)
