#-*- coding:utf-8 -*-

from bae.core.wsgi import WSGIApplication
# from config.engine import app, factory, db
from old.app.controller import factory, db
from bae.api import logging
from old import app


factory.Register_Config(conf='config_bae')
db.create_all()

application = WSGIApplication(app)