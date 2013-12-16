# coding=utf-8
from flask import jsonify

from engine import *
from models import obj_tag


@app.route('/tag/<int:tag_id>/postlist', methods=['get'])
@app.route('/tag/<int:tag_id>/postlist/<int:size>/<int:page>', methods=['get'])
def tag_postlist(tag_id, page=0, size=0):
    posts = obj_tag.query.get(tag_id).posts.order_by("created_at DESC")
    if size != 0:
        posts = posts.slice(page * size, page * size + size)
    return jsonify(posts=[i.serialize for i in posts])


@app.route('/tag/<int:tag_id>/postlist/count', methods=['get'])
def tag_postlist_count(tag_id):
    count = obj_tag.query.get(tag_id).posts.count()
    return jsonify(count=count)


@app.route('/tag/<int:tag_id>/name', methods=['get'])
def tag_getname(tag_id):
    return obj_tag.query.get(tag_id).title
