# coding=utf-8
__author__ = 'tavern'
from flask import jsonify
from flask import request

from engine import *
from models import obj_post, obj_tag


@app.route('/post', methods=['get'])
@app.route('/post/<int:size>/<int:page>', methods=['get'])
def post_list(page=0, size=0):
    posts = obj_post.query.order_by('created_at DESC')
    if size != 0:
        posts = posts.slice(page * size, page * size + size)
    return jsonify(posts=[i.serialize for i in posts])


@app.route('/post', methods=['post'])
def post_add():
    post = jsonC(request.data)                    # 从http传来的数据进行整理
    new_post = obj_post()                         # 创建对象
    new_post.content = post.get('content', None)  # 填充体制内容
    new_post.title = post.get('title', None)      # 填充标题
    new_post.tags = post.get('tags', '').strip()         # 填充分类
    db.session.add(new_post)
    for i in new_post.tags.split(' '):           # 遍历分类
        if not i.strip(): continue
        tag = obj_tag.query.filter_by(title=i).first()
        if not tag:
            tag = obj_tag()
            tag.title = i
            tag.count = 1
            db.session.add(tag)
        else:
            tag.count += 1
        tag.posts.append(new_post)
    return jsonC({'success': True})


@app.route('/post/<int:id>', methods=['get'])
def post_views(id):
    post = obj_post.query.get(id)
    post.views += 1
    return jsonify(post.serialize)


# 修改日志
@app.route('/post/<int:id>', methods=['post'])
def post_edit(id):
    post = jsonC(request.data)
    edit_post = obj_post.query.get(id)
    edit_post.title = post.get('title', None)
    edit_post.content = post.get('content', None)
    old_tags = set(edit_post.tags.split(' '))               # 老分类
    edit_post.tags = post.get('tags', '').strip()
    new_tags = set(edit_post.tags.split(' '))               # 新分类
    del_tags = old_tags - new_tags                          # 被删除的分类
    add_tags = new_tags - old_tags                          # 添加的分类
    for i in del_tags:                                     # 将被删掉的分类拥有日志数量减1
        tag = obj_tag.query.filter_by(title=i).first()
        if not tag:
            continue
        else:
            tag.count -= 1
        tag.posts.remove(edit_post)

    for i in add_tags:                                     # 添加分类
        if not i.strip(): continue
        tag = obj_tag.query.filter_by(title=i).first()
        if not tag:
            tag = obj_tag()
            tag.title = i
            tag.count = 1
            db.session.add(tag)
        else:
            tag.count += 1
        tag.posts.append(edit_post)
    db.session.commit()                             # 只有先存放数据库后才有ID值
    return jsonC({'success': True})


@app.route('/post/count', methods=['get'])
def post_count():
    count = obj_post.query.count()
    return jsonify(count=count)


@app.route('/post/<int:id>', methods=['delete'])
def post_delete(id):
    post = obj_post.query.get(id)
    db.session.delete(post)
    return jsonC({'success': True})