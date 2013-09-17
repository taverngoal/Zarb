# -*- coding: utf-8 -*-
DEBUG = True

# configuration page num
PER_PAGE = 10

# configuration mysql
MYSQL_USER = 'root'
MYSQL_PWD = '901001'
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_DB = 'sae'

SQLALCHEMY_POOL_RECYCLE = 10
SQLALCHEMY_DATABASE_URI = "sqlite:///db/foo.db"
# SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s?charset=utf8" % (MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB)
