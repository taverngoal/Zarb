# coding:utf8
__author__ = 'Tavern'
from ext.flask_login import *
from flask import redirect, url_for

login_manager = LoginManager()
login_manager.login_view = 'abc.login'
login_manager.login_message = '请先登录'
login_manager.session_protection = 'basic'


