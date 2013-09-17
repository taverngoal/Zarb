# coding:utf8
__author__ = 'Tavern'
from config.engine import db, login_manager


class obj_user(db.Model):
    __tablename__ = 'abc_users'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    nick = db.Column(db.String(255), nullable=False)
    password = db.Column(db.CHAR(255), nullable=False)
    powerid = db.Column(db.Integer, nullable=False)

    def __init__(self, name, nick, psd, powerid, id=None):
        if id:
            self.id = id
        self.name = name
        self.nick = nick
        self.password = psd
        self.powerid = powerid

    @staticmethod
    @login_manager.user_loader
    def load_user(userid):
        return obj_user.get(userid)

    @staticmethod
    def Authorize(nick, psd):

        return