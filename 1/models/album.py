# coding:utf8
__author__ = 'Tavern'
from config.engine import db


class obj_album(db.Model):
    __tablename__ = 'abc_albums'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.CHAR(255), nullable=False)
    memo = db.Column('memo', db.CHAR(255))
    createtime = db.Column('createtime', db.DateTime)
    faceid = db.Column('faceid', db.Integer)
    faceurl = db.Column('faceurl', db.CHAR(255))
    photonum = db.Column('photonum', db.Integer)
    userid = db.Column('userid', db.Integer, db.ForeignKey('abc_users.id'), nullable=False)