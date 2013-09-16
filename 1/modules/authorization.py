# coding:utf-8
__author__ = 'Tavern'
import hashlib
from models import obj_tavern_config, obj_tavern_user
from .config import Config
from flask import g, redirect, request, url_for, session, jsonify
from functools import wraps


class adminObj(object):
    __name = ''
    __psd = ''
    id = -1

    def __init__(self, name, psd):
        self.__name = name
        self.__psd = psd

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def psd(self):
        return self.__psd

    @psd.setter
    def psd(self, value):
        self.__psd = value


class Authorization(object):
    def __init__(self):
        self.__conf = Config()

    @classmethod
    def admin_required(cls, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not 'admin' in session:
                return redirect(url_for('tavern.login', next=request.url))
            return f(*args, **kwargs)
        return decorated_function

    @classmethod
    def login_required(cls, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if g.user is None:
                return redirect(url_for('tavern.login', next=request.url))
            return f(*args, **kwargs)

        return decorated_function

    @classmethod
    def command_required(cls, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not 'admin' in session:
                from modules.commands import ResultObj
                return ResultObj(u"请先登录！", False, 'str')
            return f(*args, **kwargs)
        return decorated_function

    @classmethod
    def Authenticate_Admin(cls, name, psd):
        config = Config()
        newpsd = Authorization.sha1(psd)
        if name == config.adminuser.value and newpsd == config.adminpsd.value:
            session['admin'] = adminObj(name, newpsd)
            return session['admin']
        else:
            return None

    @classmethod
    def Logout_Admin(cls):
        session.pop('admin', None)

    @classmethod
    def sha1(cls, strs):
        return hashlib.sha1(strs).hexdigest()

    @classmethod
    def currentAdmin(cls):
        if 'admin' in session:
            return session['admin']
        else:
            return adminObj('admin', '123456')

    def changeAdminName(self, newname):
        self.__conf.adminuser = newname

    def changeAdminPsd(self, newpsd):
        self.__conf.adminpsd = newpsd

    def changeUserPsd(self, userobj, newpsd):
        if isinstance(userobj, obj_tavern_user):
            userobj.password = Authorization.sha1(newpsd)
