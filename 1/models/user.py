# coding:utf8
from datetime import datetime

__author__ = 'Tavern'

from controller import db


class obj_user(db.Model):
    __tablename__ = 'abc_users'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)                                      # ID
    name = db.Column('name', db.String(255), nullable=False)                                # 字符串
    email = db.Column('email', db.String(255), nullable=False)                              # 电子邮件
    birth = db.Column('birth', db.Date)                                                     # 生日
    enable = db.Column('enable', db.Boolean, default=False)                                 # 是否启用
    avatar = db.Column('avatar', db.String(255))                                            # 头像
    notice = db.Column('notice', db.Boolean, default=False)                                 # 是否邮件提示
    admin = db.Column('admin', db.Boolean, default=False)                                   # 是否管理员
    sign_in_count = db.Column('sign_in_count', db.Integer, default=0)                       # 登陆次数
    last_sign_in_at = db.Column('last_sign_in_at', db.DateTime)                             # 最后登录时间
    last_sign_in_ip = db.Column('last_sign_in_ip', db.String(255))                          # 最后登陆IP
    encrypted_password = db.Column('encrypted_password', db.CHAR(255), nullable=False)      # 加密后的密码

    created_at = db.Column('created_at', db.DateTime, default=datetime.now())               # 创建时间
    updated_at = db.Column('updated_at', db.DateTime)                                       # 更新时间

    def __init__(self, name, email, psd):
        import hashlib
        if id:
            self.id = id
        self.name = name
        self.email = email
        self.encrypted_password = hashlib.md5(psd).hexdigest()