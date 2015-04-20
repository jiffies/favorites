#!/usr/bin/env python

import os

from flask.ext.script import Manager, Server
from flask.ext.script.commands import ShowUrls, Clean
from favorites import create_app
from favorites.models import flask_db,User,Folder,User_Folder,Webpage,User_Webpage,UserFolder_Webpage
import favorites.models
import populate as data

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('FAVORITES_ENV', 'dev')
app = create_app('favorites.settings.%sConfig' % env.capitalize(), env=env)

manager = Manager(app)
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())

def is_Model(something):
    try:
        return flask_db.Model in something.__bases__
    except (AttributeError,TypeError):
        return False

def all_Model():
    models = []
    names = dir(favorites.models)
    for name in names:
        try:
            item = getattr(favorites.models,name,None)
            if is_Model(item):
                models.append(item)
        except KeyError:
            pass
    return models


@manager.command
def init_db():
    tables = all_Model()
    flask_db.database.create_tables(tables)
    print "create tables: %s " % tables

@manager.command
def drop_tables():
    tables = all_Model()
    flask_db.database.drop_tables(tables)
    print "drop tables: %s " % tables

@manager.command
def populate():
    with flask_db.database.atomic():
        User.insert_many(data.User).execute()
        Folder.insert_many(data.Folder).execute()
        Webpage.insert_many(data.Webpage).execute()
        User_Folder.insert_many(data.User_Folder).execute()
        User_Webpage.insert_many(data.User_Webpage).execute()
        UserFolder_Webpage.insert_many(data.UserFolder_Webpage).execute()
    

    

if __name__ == "__main__":
    manager.run()
