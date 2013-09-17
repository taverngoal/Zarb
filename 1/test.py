# coding:utf8

__author__ = 'Tavern'

from flask import Flask
# from config.login import login_manager
# from ext.flask_login import login_required


app = Flask(__name__)
# app.debug = True
# app.secret_key = "!@#$%^&*()(*&^%#$@!#$%^&*()(*&^%$#@"
# login_manager.init_app(app)


@app.route('/')
def index():
    return 'haha'


@app.route('/login')
def login():
    return 'login'


@app.route('/test')
def test():
    return 'asfasdfasdf'




