# coding=utf-8
__author__ = 'tavern'

from .commentController import *
from .postController import *
from settingController import *
from tagController import *
from generalController import *

db.create_all()                                 # 创建数据库所有表