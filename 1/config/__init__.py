# coding:utf8
__author__ = 'Tavern'
import os
if 'SERVER_SOFTWARE' in os.environ:
    import config_bae as config
else:
    import config