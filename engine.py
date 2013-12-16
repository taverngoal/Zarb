# coding:utf8
import json

from flask import Flask, redirect

from ext.flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)                           # 启用框架
app.config.from_object('config.config')         # 注册配置文件
app.secret_key = '!#!@@%asdFDfSDFdgFDdgGgGsfg@^$%GdgSG'     # 设置COOKIE密钥,随便写
db = SQLAlchemy(app)                            # 启动SQLAlchemy组件
app.debug = True                                # 设置debug模式


def jsonC(obj):
    if isinstance(obj, dict):
        return json.dumps(obj)
    elif isinstance(obj, str):
        return json.loads(obj)
    else:
        return None


def authorize(func):
    def unauthorized():
        return redirect('/login')

    def wrapper(*args, **kwargs):
    #if session.get('logined', None):
        return func(*args, **kwargs)
        #els
        # turn unauthorized()

    return wrapper


@app.teardown_request
def teardown_request(exception):
    db.session.commit()