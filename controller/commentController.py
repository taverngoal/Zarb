# coding=utf-8
# from flask import request, jsonify

from flask import request, jsonify

from engine import *
from models import obj_comments, obj_post


@app.route('/comment/<int:postid>', methods=['get'])
@app.route('/comment/<int:postid>/<int:size>/<int:page>', methods=['get'])
def comments_get(postid, size=0, page=0):
    comments = obj_comments.query.filter_by(postid=postid).order_by('created_at DESC')
    if size:
        comments = comments.slice(page * size, page * size + size)

    return jsonify(comments=[i.serialize for i in comments])


@app.route('/comment', methods=['post'])
def comment_add():
    comment = jsonC(request.data)
    new_comment = obj_comments()
    new_comment.content = comment.get('content', None)
    new_comment.nick = comment.get('nick', None)
    new_comment.email = comment.get('email', None)
    new_comment.postid = comment.get('postid', None)
    post = obj_post.query.get(new_comment.postid)
    post.comments += 1
    db.session.add(new_comment)
    return jsonC({'success': True})


@app.route('/comment/count/<int:postid>')
def comment_count(postid):
    count = obj_comments.query.filter_by(postid=postid).count()
    return jsonify(count=count)