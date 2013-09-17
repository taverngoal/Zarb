# coding:utf8
__author__ = 'Tavern'
from ext.flask_login import *

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = '请先登录'
login_manager.session_protection = 'basic'


