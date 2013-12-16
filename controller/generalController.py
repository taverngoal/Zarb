# coding=utf-8

import time

from flask import url_for, redirect, render_template, request, jsonify

from engine import authorize, app
from models import obj_post, obj_comments, obj_tag
from ext import pybcs


__author__ = 'tavern'


@app.route('/login')
def login():
    # flash("Logged in successfully.")
    return render_template('app/login.html')


@app.route('/sign_in', methods=['post'])
def sign_in(nick=None, psd=None):
    return redirect(url_for('login'))


@app.route('/')
def index():
    hotposts = obj_post.query.order_by('comments DESC, created_at DESC ').slice(0, 10)
    comments = obj_comments.query.order_by('created_at DESC').slice(0, 10)
    tags = obj_tag.query.order_by('count DESC').slice(0, 20)
    claz = ['default', 'primary', 'success', 'info', 'warning', 'danger']
    return render_template('app/index.html', posts=hotposts, comments=comments, tags=tags, claz=claz)


@app.route('/admin')
@authorize
def admin():
    return render_template('app/admin.html')


@app.route('/upload', methods=['post'])
def upload():
    upload_file = request.files["imgFile"]
    global json
    if upload_file:
        bcs = pybcs.BCS('http://bcs.duapp.com/', 'Pk4TcR6bcPkNSoTKcc5Vtt9L', 'hWAhVeueCUKpNqP63XUitozqAcQMz6hU',
                        pybcs.HttplibHTTPC)
        b = bcs.bucket('tavern')
        path = '/upload/' + str(time.time()) + str(upload_file.filename[upload_file.filename.rindex('.'):])
        uploading_file = b.object(path)
        file_data = upload_file.getvalue()
        result = uploading_file.put(str(file_data))
        json = jsonify(error=0, url="http://bcs.duapp.com/tavern" + path)
    return json