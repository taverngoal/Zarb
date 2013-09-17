#-*- coding:utf-8 -*-

# from bae.core.wsgi import WSGIApplication
# # from config.engine import app, factory, db
# from test import app
# from bae.api import logging
#
#
# # factory.Register_Config(conf='config_bae')
# # db.create_all()
#
# application = WSGIApplication(app)

from flask import Flask, g, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    return "Hello, world! - Flask\n"


@app.route('/test')
def test():
    return "test, world! - Flask\n"

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)