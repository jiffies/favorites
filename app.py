from flask import Flask,render_template,request,abort,redirect,url_for
from flask_debugtoolbar import DebugToolbarExtension
from playhouse.flask_utils import FlaskDB

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'code4awesome'
DATABASE = 'mysql://root:root@localhost:3306/favorites'
app.config.from_object(__name__)

flask_db = FlaskDB(app)
database = flask_db.database

toolbar = DebugToolbarExtension(app)

@app.route('/')
def hello_world():
    app.logger.debug(dir(request))
    users = User.select()
    return render_template('base.html',users=users)


@app.errorhandler(404)
def page_not_found(error):
    return '<html><body><script type="text/javascript" src="http://www.qq.com/404/search_children.js" charset="utf-8"></script></body></html>',404

if __name__ == "__main__":
    from models import User
    app.run()
