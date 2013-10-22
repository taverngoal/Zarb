# coding:utf8
__author__ = 'Tavern'
from config.engine import db


class obj_photo(db.Model):
    __tablename__ = 'abc_photos'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    original_name = db.Column('original_name', db.CHAR(255), nullable=False)
    show_name = db.Column('show_name', db.CHAR(255), nullable=False)
    size = db.Column('size', db.BigInteger)
    width = db.Column('width', db.Integer)
    height = db.Column('height', db.Integer)
    show = db.Column('show', db.Boolean)
    album_id = db.Column('album_id', db.Integer, db.ForeignKey('abc_albums.id'), nullable=False)
    created_at = db.Column('created_at', db.DateTime)
    update_at = db.Column('update_at', db.DateTime)
    memo = db.Column('memo', db.TEXT(500))
    url = db.Column('url', db.CHAR(255))
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('abc_users.id'))

