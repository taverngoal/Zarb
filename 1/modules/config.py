__author__ = 'Tavern'
from engine import db
from models import obj_tavern_config


class Config(object):
    itemsStr = ('bingpic', 'adminuser', 'adminpsd', 'title')

    def delitem(self, key):
        obj = self.getitem(key)
        if key in self.__dict__:
            del self.__dict__[key]
        if obj:
            db.session.delete(obj)

    def setitem(self, key, value):
        obj = self.getitem(key)
        if obj:
            obj.value = value
        else:
            obj = obj_tavern_config(key, value)
            db.session.add(obj)
        self.__dict__[key] = value

    def getitem(self, key):
        obj = obj_tavern_config.query.filter_by(key=key).first()
        return obj if obj else ""

    def initAttr(self, key):
        """
        initialize the key in the __dict__  if the key has no value
        :param key:
            the key name
        """
        self.__dict__[key] = self.getitem(key) if not self.__dict__.get(key, None) else self.__dict__[key]

    @property
    def bingpic(self):
        key = 'bingpic'
        self.initAttr(key)
        return self.__dict__[key]

    @bingpic.setter
    def bingpic(self, value):
        key = 'bingpic'
        self.setitem(key, value)

    @property
    def adminuser(self):
        key = 'adminuser'
        self.initAttr(key)
        return self.__dict__[key]

    @adminuser.setter
    def adminuser(self, value):
        key = 'adminuser'
        self.setitem(key, value)

    @property
    def adminpsd(self):
        key = 'adminpsd'
        self.initAttr(key)
        return self.__dict__[key]

    @adminpsd.setter
    def adminpsd(self, value):
        key = 'adminpsd'
        self.setitem(key, value)

    @property
    def title(self):
        key = 'title'
        self.initAttr(key)
        return self.__dict__[key]

    @title.setter
    def title(self, value):
        key = 'title'
        from flask import g
        g.title = key
        self.setitem(key, value)

    @property
    def secret_key(self):
        key = 'secret_key'
        self.initAttr(key)
        return self.__dict__[key]

    @secret_key.setter
    def secret_key(self, value):
        key = 'secret_key'
        self.setitem(key, value)
        db.session.commit()

    def getall(self):
        list = [[a.key, a.value] for a in obj_tavern_config.query]
        return list

    def __setitem__(self, key, value):
        self.setitem(key, value)

    def __getitem__(self, item):
        self.initAttr(item)
        return self.__dict__[item]

    def __delitem__(self, key):
        self.delitem(key)
