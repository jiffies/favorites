#!/usr/bin/env python

import os

from flask.ext.script import Manager, Server
from flask.ext.script.commands import ShowUrls, Clean
from favorites import create_app
from favorites.models import flask_db,User

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('FAVORITES_ENV', 'dev')
app = create_app('favorites.settings.%sConfig' % env.capitalize(), env=env)

manager = Manager(app)
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())

@manager.command
def init_db():
    flask_db.database.create_tables([User])
    

if __name__ == "__main__":
    manager.run()
