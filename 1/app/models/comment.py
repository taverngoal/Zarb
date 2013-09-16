# coding:utf8
__author__ = 'Tavern'
from datetime import datetime

from config.engine import db


class obj_comments(db.Model):
    __tablename__ = 'abc_comments'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    referid = db.Column('referid', db.Integer, db.ForeignKey('abc_comments.id'), nullable=True)
    datetime = db.Column('datetime', db.DateTime, default=datetime.now())
    nick = db.Column('nick', db.VARCHAR(255))
    content = db.Column('content', db.VARCHAR(500))
    ip = db.Column('ip', db.CHAR(15))
    photoid = db.Column('photoid', db.Integer, db.ForeignKey('abc_photos.id'))
    albumid = db.Column('albumid', db.Integer, db.ForeignKey('abc_albums.id'))
    email = db.Column('email', db.CHAR(255))
