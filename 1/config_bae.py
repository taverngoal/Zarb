# -*- coding: utf-8 -*-
from bae.core import const
DEBUG = True

# configuration page num
PER_PAGE = 10

# configuration mysql
SQLALCHEMY_POOL_RECYCLE = 10
# SQLALCHEMY_DATABASE_URI = "sqlite:///db/foo.db"
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (const.MYSQL_USER, const.MYSQL_PASS, const.MYSQL_HOST,
                                                                   int(const.MYSQL_PORT), 'wbreGfHAdijPKMJFqwns')
AK = 'z9NR4maoM1CNEUZ3BRvrv2GK'
SK = 'IRxtOZy9Fxq5s68zHdWyqt7ax2US3U6D'
