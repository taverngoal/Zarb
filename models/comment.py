# coding:utf8
__author__ = 'Tavern'
from datetime import datetime
from engine import db


class obj_comments(db.Model):
    __tablename__ = 'abc_comments'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    referid = db.Column('referid', db.Integer, db.ForeignKey('abc_comments.id'), nullable=True)
    created_at = db.Column('created_at', db.DateTime, default=datetime.now())
    nick = db.Column('nick', db.VARCHAR(255))
    content = db.Column('content', db.VARCHAR(500))
    ip = db.Column('ip', db.CHAR(15))
    postid = db.Column('postid', db.Integer)
    photoid = db.Column('photoid', db.Integer)
    albumid = db.Column('albumid', db.Integer)
    email = db.Column('email', db.CHAR(255))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'referid': self.referid,
            'content': self.content,
            'nick': self.nick,
            'ip': self.ip,
            'postid': self.postid,
            'photoid': self.photoid,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'albumid': self.albumid,
            'email': self.email,
        }

