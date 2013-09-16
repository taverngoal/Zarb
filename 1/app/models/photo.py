# coding:utf8
__author__ = 'Tavern'
from config.engine import db


class obj_photo(db.Model):
    __tablename__ = 'abc_photos'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    originalname = db.Column('originalname', db.CHAR(255), nullable=False)
    displayname = db.Column('displayname', db.CHAR(255), nullable=False)
    width = db.Column('width', db.Integer)
    height = db.Column('height', db.Integer)
    albumid = db.Column('albumid', db.Integer, db.ForeignKey('abc_albums.id'), nullable=False)
    addtime = db.Column('addtime', db.DateTime)
    memo = db.Column('memo', db.TEXT(500))
    url = db.Column('url', db.CHAR(255))
    zipurl = db.Column('zipurl', db.CHAR(255))
    isface = db.Column('isface', db.BOOLEAN(), default=False)
    userid = db.Column('userid', db.Integer, db.ForeignKey('abc_users.id'))

