# coding:utf8
__author__ = 'Tavern'
from config.engine import db


class obj_album(db.Model):
    __tablename__ = 'abc_albums'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.CHAR(255), nullable=False)
    memo = db.Column('memo', db.CHAR(255))
    created_at = db.Column('created_at', db.DateTime)
    update_at = db.Column('update_at', db.DateTime)
    face_id = db.Column('face_id', db.Integer)
    enable = db.Column('enable', db.Boolean)
    show = db.Column('show', db.show)
    faceurl = db.Column('faceurl', db.CHAR(255))
    photo_num = db.Column('photo_num', db.Integer)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('abc_users.id'), nullable=False)