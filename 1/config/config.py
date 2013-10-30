# -*- coding: utf-8 -*-
import os
DEBUG = True

if 'SERVER_SOFTWARE' in os.environ:             # 百度环境下加载的配置
    # -*- coding: utf-8 -*-
    from bae.core import const
    # configuration mysql
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (const.MYSQL_USER, const.MYSQL_PASS, const.MYSQL_HOST,
                                                                       int(const.MYSQL_PORT), 'cfnQuUjKaqFpmRifftSC')
    AK = 'z9NR4maoM1CNEUZ3BRvrv2GK'
    SK = 'IRxtOZy9Fxq5s68zHdWyqt7ax2US3U6D'
else:                                           # 本地环境加载的配置
    # configuration mysql
    MYSQL_USER = 'root'
    MYSQL_PWD = '901001'
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_DB = 'sae'
    SQLALCHEMY_DATABASE_URI = "sqlite:///db/sqlite3.db"
    # SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s?charset=utf8" % (MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB)

# configuration page num
PER_PAGE = 10

SQLALCHEMY_POOL_RECYCLE = 10

