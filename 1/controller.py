# coding:utf8
from flask import Flask, render_template, __version__, redirect, url_for
from config.login import login_manager
from ext.flask_sqlalchemy import SQLAlchemy
#from ext.flask_login import login_required, login_user,
# from models import obj_user

__author__ = 'Tavern'

app = Flask(__name__)                           # 启用框架
app.config.from_object('config.config')         # 注册配置文件
app.secret_key = '!#!@@%asdFDfSDFdgFDdgGgGsfg@^$%GdgSG'     # 设置COOKIE密钥
login_manager.init_app(app)                     # 启动ext.login组件
db = SQLAlchemy(app)                            # 启动SQLAlchemy组件
app.debug = True                                # 设置debug模式

global current_user, controller_name, action_name


@app.route('/login')
def login():
    # flash("Logged in successfully.")
    return render_template('app/login.html', aa=__version__)


@app.route('/test')
def test():
    return render_template('app/test.html')


@app.route('/signin', methods=['post'])
def signin(nick=None, psd=None):
# user = obj_user.query.filter_by(nick=nick, password=psd).first()
# user
# if user:
#     login_user(user)
#     flash(u'成功登录')
#     return redirect(url_for('abc.index'))
# else:
    return redirect(url_for('login'))


@app.route('/')
#@login_required
def index():
    return render_template('app/index.html')
