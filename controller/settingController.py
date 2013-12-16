# coding=utf-8
__author__ = 'tavern'
from flask import request, jsonify

from engine import *
from models import obj_setting


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