# coding:utf-8
from datetime import datetime

__author__ = 'tavern'

from controller import db


class obj_setting(db.Model):
    __tablename__ = "abc_settings"
    __table_args__ = {'mysql_engine': 'InnoDB'}
    key = db.Column('key', db.String(255), primary_key=True)
    value = db.Column('value', db.String(255))