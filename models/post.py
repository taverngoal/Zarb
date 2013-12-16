# coding:utf-8

__author__ = 'tavern'

from datetime import datetime

from .models import *


class obj_post(db.Model):
    __tablename__ = "abc_posts"
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.CHAR(255), nullable=False)
    content = db.Column('content', db.TEXT, nullable=False)
    tags = db.Column('tags', db.String(255), nullable=True, default='')
    attchments = db.Column('attchments', db.String(255), nullable=True)
    views = db.Column('views', db.Integer, nullable=True, default=0)
    comments = db.Column('comments', db.Integer, nullable=True, default=0)
    created_at = db.Column('created_at', db.DateTime, default=datetime.now())
    update_at = db.Column('update_at', db.DateTime)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'comments': self.comments,
            'tags': self.tags,
            'attchments': self.attchments,
            'views': self.views,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'update_at': self.update_at.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.update_at, datetime) else '',
            'tag_objs': [i.serialize for i in self.tag_objs]
        }
