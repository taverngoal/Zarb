#-*- coding:utf-8 -*-

from bae.core.wsgi import WSGIApplication
# from config.engine import app, factory, db
# from old.app.controller import factory, db
from c import app
from bae.api import logging


# factory.Register_Config(conf='config_bae')
# db.create_all()

application = WSGIApplication(app)