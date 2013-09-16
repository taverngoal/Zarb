# coding:utf8
__author__ = 'Tavern'
from flask import Blueprint, render_template

abc = Blueprint('abc', __name__, url_prefix='/', static_folder='static', template_folder='templates')


@abc.route('/')
def index():
    return render_template('app/index.html')
