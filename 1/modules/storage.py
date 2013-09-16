#! -*- coding:UTF-8 -*-
__author__ = 'Tavern'
import pybcs
from pybcs.object import Object


class Storage:
    def __init__(self, AK, SK, bucketname='tavern', HOST='http://bcs.duapp.com/'):
        self.bcs = pybcs.BCS(HOST, AK, SK)
        self.   BUCKET = bucketname
        self.bucketManager = self.bcs.bucket(self.BUCKET)
        pass

    def getlist(self):
        return self.bucketManager.list_objects()

    def createobj(self, filePath):
        obj = self.bucketManager.object(str(filePath))
        return obj

    def pushlocalfile(self, obj, filename, header={}):
        if isinstance(obj, Object):
            obj.put_file(filename, header)

    def putcontent(self, obj, content, header={}):
        if isinstance(obj, Object):
            obj.put(content, header)

    def downloadobj(self, obj, path):
        if isinstance(obj, Object):
            obj.get_to_file(path)

    def deleteobj(self, obj):
        if isinstance(obj, Object):
            obj.delete()

    def getcontent(self, obj, headers={}):
        if isinstance(obj, Object):
            return obj.get(headers)
