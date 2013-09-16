#! -*- coding:utf-8 -*-
from engine import db
from datetime import datetime


class obj_tavern_user(db.Model):
    __tablename__ = 'tavern_users'
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


class obj_tavern_config(db.Model):
    __tablename__ = 'tavern_configs'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    key = db.Column(db.String(255), nullable=False, primary_key=True)
    value = db.Column(db.Text)

    def __init__(self, key, value):
        self.key = key
        self.value = value


class obj_tavern_exception(db.Model):
    __tablename__ = 'tavern_exception'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    args = db.Column('args', db.TEXT, nullable=False)
    message = db.Column('message', db.CHAR(255))
    datetime = db.Column('datetime', db.DateTime, default=datetime.now())
    memo = db.Column('memo', db.CHAR(255))

    def __init__(self, args, message, memo):
        self.args = args
        self.message = message
        self.memo = memo


class obj_blog_post(db.Model):
    __tablename__ = 'blog_posts'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(255), nullable=False)
    content = db.Column('content', db.Text)
    createtime = db.Column('createtime', db.DateTime, nullable=False, default=datetime.now())
    readtimes = db.Column('readtimes', db.Integer, default=0)
    authorid = db.Column('authorid', db.Integer, db.ForeignKey('tavern_users.id'), nullable=True)
    countcomment = db.Column('countcomment', db.Integer, default=0)
    cateid = db.Column('cateid', db.Integer, db.ForeignKey('blog_category.id'), nullable=True)

    author = db.relationship('obj_tavern_user', primaryjoin="obj_blog_post.authorid == obj_tavern_user.id",
                             backref=db.backref('posts', lazy='dynamic'), uselist=False)
    category = db.relationship('obj_blog_category', primaryjoin="obj_blog_post.cateid == obj_blog_category.id",
                               backref=db.backref('posts', lazy='dynamic'), uselist=False)

    def __init__(self, title, content, authorid, createtime=None, readtimes=0, countcomment=0, cateid=None, id=None):
        self.title = title
        self.content = content
        self.id = id
        self.authorid = authorid
        self.createtime = createtime
        self.readtimes = readtimes
        self.countcomment = countcomment
        self.cateid = cateid


class obj_blog_category(db.Model):
    __tablename__ = 'blog_category'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.CHAR(255), nullable=True, unique=True)
    createtime = db.Column('createtime', db.CHAR(255), default=datetime.now())
    memo = db.Column('memo', db.TEXT(500))

    def __init__(self, name, memo, createtime=None, id=None):
        self.name = name
        self.memo = memo
        self.id = id
        self.createtime = createtime


class obj_blog_comments(db.Model):
    __tablename__ = 'blog_comments'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    referid = db.Column('referid', db.Integer, db.ForeignKey('blog_comments.id'), nullable=True)
    datetime = db.Column('datetime', db.DateTime, default=datetime.now())
    nick = db.Column('nick', db.VARCHAR(255))
    content = db.Column('content', db.VARCHAR(500))
    ip = db.Column('ip', db.CHAR(15))
    photoid = db.Column('photoid', db.Integer, db.ForeignKey('blog_photos.id'))
    albumid = db.Column('albumid', db.Integer, db.ForeignKey('blog_albums.id'))
    postid = db.Column('postid', db.Integer, db.ForeignKey('blog_posts.id'))
    email = db.Column('email', db.CHAR(255))


class obj_blog_album(db.Model):
    __tablename__ = 'blog_albums'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.CHAR(255), nullable=False)
    memo = db.Column('memo', db.CHAR(255))
    createtime = db.Column('createtime', db.DateTime)
    faceid = db.Column('faceid', db.Integer)
    faceurl = db.Column('faceurl', db.CHAR(255))
    photonum = db.Column('photonum', db.Integer)
    userid = db.Column('userid', db.Integer, db.ForeignKey('tavern_users.id'), nullable=False)


class obj_blog_photo(db.Model):
    __tablename__ = 'blog_photos'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    originalname = db.Column('originalname', db.CHAR(255), nullable=False)
    displayname = db.Column('displayname', db.CHAR(255), nullable=False)
    width = db.Column('width', db.Integer)
    height = db.Column('height', db.Integer)
    albumid = db.Column('albumid', db.Integer, db.ForeignKey('blog_albums.id'), nullable=False)
    addtime = db.Column('addtime', db.DateTime)
    memo = db.Column('memo', db.TEXT(500))
    url = db.Column('url', db.CHAR(255))
    zipurl = db.Column('zipurl', db.CHAR(255))
    isface = db.Column('isface', db.BOOLEAN(), default=False)
    userid = db.Column('userid', db.Integer, db.ForeignKey('tavern_users.id'))


