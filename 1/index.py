#-*- coding:utf-8 -*-

from bae.core.wsgi import WSGIApplication
from controller import app

application = WSGIApplication(app)