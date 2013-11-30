# coding:utf8
import json

from flask import Flask, render_template, __version__, redirect, url_for, request, jsonify

from ext.flask_sqlalchemy import SQLAlchemy


__author__ = 'Tavern'

app = Flask(__name__)                           # 启用框架
app.config.from_object('config.config')         # 注册配置文件
app.secret_key = '!#!@@%asdFDfSDFdgFDdgGgGsfg@^$%GdgSG'     # 设置COOKIE密钥,随便写
db = SQLAlchemy(app)                            # 启动SQLAlchemy组件
app.debug = True                                # 设置debug模式
from models import *                                 # 加载所有模型

db.create_all()                                 # 创建数据库所有表


@app.teardown_request
def teardown_request(exception):
    db.session.commit()


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
    posts = obj_post.query.all()
    return render_template('app/index.html', posts=posts)


@app.route('/admin')
def admin():
    return render_template('app/admin.html')


@app.route('/post', methods=['get'])
def post_list():
    return jsonify(posts=[i.serialize for i in obj_post.query.all()])


@app.route('/post', methods=['post'])
def post_add():
    post = jsonC(request.data)
    new_post = obj_post()
    new_post.content = post.get('content', None)
    new_post.title = post.get('title', None)
    db.session.add(new_post)
    return jsonC({'success': True})


@app.route('/post/<int:id>', methods=['get'])
def post_get(id):
    obj_post.query.get(id)
    return jsonify(obj_post.query.get(id).serialize)


def jsonC(obj):
    if isinstance(obj, dict):
        return json.dumps(obj)
    elif isinstance(obj, str):
        return json.loads(obj)
    else:
        return None