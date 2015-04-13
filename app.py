from flask import Flask,render_template,request,abort,redirect,url_for
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'code4awesome'

toolbar = DebugToolbarExtension(app)

@app.route('/')
def hello_world():
    app.logger.debug(dir(request))
    return render_template('base.html',name="jiffies")

@app.errorhandler(404)
def page_not_found(error):
    return '<html><body><script type="text/javascript" src="http://www.qq.com/404/search_children.js" charset="utf-8"></script></body></html>',404

if __name__ == "__main__":
    app.run()
