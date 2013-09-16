# coding:utf8
from flask import jsonify

__author__ = 'Tavern'
from models import *
from datetime import datetime
from engine import db


class BaseService(object):
    def __init__(self):
        self._collection = object

    def Delete(self, id):
        obj = self._collection.get(id)
        if obj:
            db.session.delete(obj)
            return {'result': True}

    def Edit(self, id):
        return {'result': True}

    def Get(self, id):
        return self._collection.get(id)

    def GetOr404(self, id):
        return self._collection.filter_by(id=id).first_or_404()

    def GetAll(self, orderby=None):
        return self._collection

    def GetByPage(self, pagesize, pageindex, orderby=None):
        start = (pageindex - 1) * pagesize
        return self.GetSlice(start, start + pagesize)

    def GetSlice(self, startindex, endindex, orderby=None):
        return self._collection.slice(startindex, endindex)

    def GetPageCount(self, pagesize):
        totalcount = self._collection.count()
        l = totalcount % pagesize
        count = totalcount / pagesize
        return count if l == 0 else count+1


class PostService(BaseService):
    def __init__(self):
        BaseService.__init__(self)
        self._collection = obj_blog_post.query

    def add(self, title, content, authorid, cateid=None, createtime=datetime.now()):
        post = obj_blog_post(title, content, authorid, createtime, cateid=cateid)
        success, message = self.checkout(post)
        if success:
            db.session.add(post)
        return jsonify(success=success, message=message)

    def edit(self, title, content, authorid, cateid=None):
        pass

    def checkout(self, post):
        message = "成功"
        success = False
        if len(post.title) > 255:
            message = "标题过长"
        elif len(post.title) == 0 or not post.title:
            message = "标题不能为空"
        else:
            success = True
        return success, message


class CategoryService(BaseService):
    def __init__(self):
        BaseService.__init__(self)
        self._collection = obj_blog_category.query

    def add(self, name, memo, createtime=None):
        cate = obj_blog_category(name, memo, createtime)
        success, message = self.checkout(cate)
        if success:
            db.session.add(cate)
        return jsonify(success=success, message=message)

    def edit(self, name, memo, id):
        cate = self.Get(id)
        if cate:
            newcate = obj_blog_category(name, memo, cate.createtime)
            success, message = self.checkout(newcate)
            if success:
                cate.name = name
                cate.memo = memo
            return jsonify(success=success, message=message)
        return jsonify(success=False, message='找不到该类别')

    def checkout(self, cate):
        message = "成功"
        success = False
        if len(cate.name) > 255:
            message = "类别名过长"
        elif len(cate.name) == 0 or not cate.name:
            message = "类别名不能为空"
        else:
            success = True
        return success, message

