#! -*- coding:utf-8 -*-
from engine import db


tag_posts_Table = db.Table('abc_tag_posts',
                           db.Column('tag_id', db.Integer, db.ForeignKey('abc_tags.id')),
                           db.Column('post_id', db.Integer, db.ForeignKey('abc_posts.id')))
