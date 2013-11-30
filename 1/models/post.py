# coding:utf-8
from datetime import datetime

__author__ = 'tavern'

from controller import db


class obj_post(db.Model):
    __tablename__ = "abc_posts"
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.CHAR(255), nullable=False)
    content = db.Column('content', db.TEXT, nullable=False)
    tags = db.Column('tags', db.String(255), nullable=True)
    attchments = db.Column('attchments', db.String(255), nullable=True)
    views = db.Column('views', db.Integer, nullable=True)
    created_at = db.Column('created_at', db.DateTime, default=datetime.now())
    update_at = db.Column('update_at', db.DateTime)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'tags': self.tags,
            'attchments': self.attchments,
            'views': self.views,
            'created_at': self.created_at,
            'update_at': self.update_at
        }
