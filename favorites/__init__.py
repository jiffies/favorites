from flask import Flask
from favorites.models import flask_db
from favorites.extensions import (
            debug_toolbar,
        )

def create_app(object_name, env="prod"):
    app = Flask(__name__)
    app.config.from_object(object_name)
    app.config['ENV'] = env

    debug_toolbar.init_app(app)
    flask_db.init_app(app)

    import views
    app.register_blueprint(views.blueprint)

    @app.errorhandler(404)
    def page_not_found(error):
        return '<html><body><script type="text/javascript" src="http://www.qq.com/404/search_children.js" charset="utf-8"></script></body></html>',404

    return app

