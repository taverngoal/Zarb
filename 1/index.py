#-*- coding:utf-8 -*-

from bae.core.wsgi import WSGIApplication
from engine import app, factory, db
from bae.api import logging


factory.Register_Config(conf='config_bae')
db.create_all()

application = WSGIApplication(app)