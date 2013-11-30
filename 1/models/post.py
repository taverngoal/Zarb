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
    update_at= db.Column('update_at', db.DateTime)