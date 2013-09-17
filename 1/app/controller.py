# coding:utf8
__author__ = 'Tavern'
from flask import Blueprint, render_template, flash, redirect, url_for
# from flask.ext.WTF import *
from models import *
from flask.ext.login import login_user, login_required

from models import *

abc = Blueprint('abc', __name__, static_folder='static', template_folder='templates')


@abc.route('/login')
def login():
    # flash("Logged in successfully.")
    return render_template('app/login.html')


@abc.route('/test')
def test():
    return render_template('app/test.html')


@abc.route('/signin', methods=['post'])
def signin(nick=None, psd=None):
    user = obj_user.query.filter_by(nick=nick, password=psd).first()
    if user:
        login_user(user)
        flash(u'成功登录')
        return redirect(url_for('abc.index'))
    else:
        return redirect(url_for('abc.login'))

@abc.route('/')
@login_required
def index():
    return render_template('app/index.html')
