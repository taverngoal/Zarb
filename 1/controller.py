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
    posts = obj_post.query.order_by('comments DESC')
    return render_template('app/index.html', posts=posts)


@app.route('/admin')
@authorize
def admin():
    return render_template('app/admin.html')


@app.route('/post', methods=['get'])
def post_list():
    return jsonify(posts=[i.serialize for i in obj_post.query.order_by('created_at DESC')])


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
    post = obj_post.query.get(id)
    post.views += 1
    return jsonify(post.serialize)


@app.route('/post/<int:id>', methods=['post'])
def post_edit(id):
    post = jsonC(request.data)
    edit_post = obj_post.query.get(id)
    edit_post.title = post.get('title', None)
    edit_post.content = post.get('content', None)
    return jsonC({'success': True})


@app.route('/post/<int:id>', methods=['delete'])
def post_delete(id):
    post = obj_post.query.get(id)
    db.session.delete(post)
    return jsonC({'success': True})


@app.route('/setting/account', methods=['get'])
def setting_get_account():
    nick = obj_setting.query.get('nick')
    name = obj_setting.query.get('name')
    return jsonify(nick=nick.value if nick else None, name=name.value if name else None)


@authorize
@app.route('/setting/account', methods=['post'])
def setting_set_account():
    account = jsonC(request.data)
    print account
    nick = obj_setting.query.get('nick')
    name = obj_setting.query.get('name')
    psd = obj_setting.query.get('psd')
    if nick:
        nick.value = account.get('nick', None)
    if name:
        name.value = account.get('name', None)
    if psd:
        psd.value = account.get('psd', None)
    return jsonify(success=True)


@app.route('/comment/<int:postid>', methods=['get'])
def comments_get(postid):
    comments = obj_comments.query.filter_by(postid=postid)
    return jsonify(comments=[i.serialize for i in comments])


@app.route('/comment', methods=['post'])
def comment_add():
    comment = jsonC(request.data)
    new_comment = obj_comments()
    new_comment.content = comment.get('content', None)
    new_comment.nick = comment.get('nick', None)
    db.session.add(new_comment)
    return jsonC({'success': True})


def jsonC(obj):
    if isinstance(obj, dict):
        return json.dumps(obj)
    elif isinstance(obj, str):
        return json.loads(obj)
    else:
        return None