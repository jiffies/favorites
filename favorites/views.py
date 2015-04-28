from flask import render_template,request,abort,redirect,url_for,Blueprint

blueprint = Blueprint("favorites",__name__)

from models import User

@blueprint.route('/')
def hello_world():
    users = User.select()
    return render_template('base.html',users=users)

@blueprint.route('/folders')
def folders():
    user = User.get()
    return render_template('folders.html',folders=user.userfolders)
