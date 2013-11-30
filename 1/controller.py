# coding:utf8
from flask import Flask, render_template, __version__, redirect, url_for
from ext.flask_sqlalchemy import SQLAlchemy

__author__ = 'Tavern'

app = Flask(__name__)                           # 启用框架
app.config.from_object('config.config')         # 注册配置文件
app.secret_key = '!#!@@%asdFDfSDFdgFDdgGgGsfg@^$%GdgSG'     # 设置COOKIE密钥,随便写
db = SQLAlchemy(app)                            # 启动SQLAlchemy组件
app.debug = True                                # 设置debug模式
from models import *                                 # 加载所有模型
db.create_all()                                 # 创建数据库所有表


@app.route('/login')
def login():
    # flash("Logged in successfully.")
    return render_template('app/login.html', aa=__version__)


@app.route('/test')
def test():
    return render_template('app/test.html')


@app.route('/sign_in', methods=['post'])
def sign_in(nick=None, psd=None):
    return redirect(url_for('login'))


@app.route('/')
def index():
    return render_template('app/index.html')
