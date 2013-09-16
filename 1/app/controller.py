# coding:utf8
__author__ = 'Tavern'
from flask import Blueprint, url_for, render_template, request, jsonify
from models import *

abc = Blueprint('abc', __name__, url_prefix='/app', static_folder='static')


@abc.route('/')
def index():
    return render_template('app/index.html')
