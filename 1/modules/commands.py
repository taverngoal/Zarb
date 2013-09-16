# coding:utf-8
__author__ = 'Tavern'
from flask import jsonify, url_for, session
import re
from .config import Config
from .authorization import Authorization
from .htmlbuilder import HTMLBuilder


#统一返回对象
class ResultObj(object):
    def __init__(self, message, success, type):
        self.message = message
        self.success = success
        self.type = type
        self.page = ''
        self.method = 'get'

    def GetJson(self):
        return jsonify(self.__dict__)


#命令接入与选择
class Command(object):
    __apps__ = ('tavern', 'blog')

    def __init__(self):
        pass

    @staticmethod
    def push(strs):
        result = ResultObj('', True, 'str')
        if strs:
            try:
                result = Command.reselect(strs)
            except Exception as e:
                result.message = "命令执行失败，错误原因：%s" % e.message
                result.success = False
                from models import obj_tavern_exception, db
                db.session.add(obj_tavern_exception(str(e.args), e.message, u'异常的命令：%s' % strs))
        return result.GetJson()

    @classmethod
    def reselect(cls, strs):
        #跨APP执行命令
        firsttuple = strs.split(' ')[0]
        if firsttuple in [str.lower(i) for i in Command.__apps__]:
            if firsttuple == 'tavern':
                return TavernDo.reselect(strs)
            elif firsttuple == 'blog':
                return BlogDo.reselect(strs)

        #筛选APP或命令
        if strs == 'start':
            return Command.welcome(strs)
        elif re.compile(r'^use\s\S+$').match(strs):        #use  使用使用
            return GeneralDo.appselect(strs)
        elif strs == 'app':                                 #app  当前应用
            return ResultObj(u'当前应用:%s' % session['currentapp'], True, 'str')
        elif strs == 'help':                                  #help
            return GeneralDo.help(strs)
        elif strs == 'show apps':                           #show apps  显示所有APP
            return GeneralDo.showapps(strs)
        elif re.compile(r'^blog\s\S+$').match(strs) or session['currentapp'] == 'blog':        #blog
            return BlogDo.reselect(strs)
        elif re.compile(r'^tavern\s\S+$').match(strs) or session['currentapp'] == 'tavern':        #tavern
            return TavernDo.reselect(strs)
        else:
            return Command.unknown(strs)

    @classmethod
    def unknown(cls, strs):
        return ResultObj(u"未知命令:%s" % strs, False, 'str')

    @classmethod
    def welcome(cls, strs):
        session['currentapp'] = 'tavern'
        return ResultObj(u'欢迎，请输入help获取帮助，当前应用: tavern.', True, 'str')


#命令行执行类母类
class BaseDo(object):
    def __init__(self):
        pass

    @classmethod
    def PageRedirect(cls, url):
        result = ResultObj(u'加载中...', True, type='page')
        result.pageurl = url
        return result


#一般操作
class GeneralDo(object):
    def __init__(self):
        pass

    @classmethod
    def conn(cls, strs):
        result = ResultObj(u'登录失败', False, 'str')
        strs = strs[5:]
        equality = strs.split(':')
        admin = Authorization.Authenticate_Admin(equality[0], equality[1])
        if admin:
            result.message = u"登录成功"
            result.success = True
            return result
        return result

    @classmethod
    def logout(cls, strs):
        Authorization.Logout_Admin()
        return ResultObj(u'成功登出', True, 'str')

    @classmethod
    def showapps(cls, strs):
        lists = []
        for i in Command.__apps__:
            lists.append([i])
        return ResultObj(HTMLBuilder.Table(lists), True, 'block')

    @classmethod
    def appselect(cls, strs):
        appname = strs[4:]
        result = ResultObj(u'当前应用:%s' % strs[4:], True, 'str')
        if not appname in Command.__apps__:
            result.message = u"没用此应用，进入失败。当前应用：%s" % session['currentapp']
            result.success = False
        else:
            session['currentapp'] = appname
        return result

    @classmethod
    def help(cls, strs):
        lists = []
        lists.append(['应用', '命令', '备注', '显示形式'])
        lists.append(['通用', '', '', ''])
        lists.append(['', 'show apps', '显示所有app', '列表'])
        lists.append(['', 'app', '显示当前app', '字符'])
        lists.append(['', 'help', '帮助', '列表'])
        lists.append(['tavern', '', '', ''])
        lists.append(['', 'conn adminname:adminpsd', '登录', '字符'])
        lists.append(['', 'logout', '登出', '字符'])
        lists.append(['', 'configs', '显示所有配置', '字符'])
        lists.append(['', 'set key=value', '设置config的值', '字符'])
        lists.append(['', 'unset key', '删除config的值', '字符'])
        lists.append(['', 'use appname', '进入app', '字符'])
        lists.append(['blog', '', ''])
        lists.append(['', 'post', '添加日志页面', '页面'])
        lists.append(['', 'postlist', '日志列表页面', '页面'])
        lists.append(['', 'cate', '添加日志类别页面', '页面'])
        lists.append(['', 'catelist', '日志类别列表页面', '页面'])
        return ResultObj(HTMLBuilder.Table(lists), True, 'block')


#高级操作
class SuperDo(object):
    def __init__(self):
        pass

    @classmethod
    @Authorization.command_required
    def set(cls, strs):
        strs = strs[4:]
        equality = strs.split('=')
        conf = Config()
        conf[equality[0]] = equality[1]
        mes = u"成功设置%s=%s" % (equality[0], equality[1])
        return ResultObj(mes, True, 'str')

    @classmethod
    @Authorization.command_required
    def unset(cls, strs):
        conf = Config()
        key = strs[6:]
        del conf[key]
        mes = u"成功删除配置%s" % key
        return ResultObj(mes, True, 'str')

    @classmethod
    @Authorization.command_required
    def configs(cls, strs):
        config = Config()
        return ResultObj(HTMLBuilder.Table(config.getall()), True, 'block')


class TavernDo(object):
    def __init__(self):
        pass

    @classmethod
    def reselect(cls, strs):
        if re.compile(r'^tavern\s\S+').match(strs):         #去掉tavern头
            strs = strs[7:]
        if re.compile(r'^set\s\S+=\S+$').match(strs):       #set
            return SuperDo.set(strs)
        elif re.compile(r"^unset\s\S+$").match(strs):       #unset
            return SuperDo.unset(strs)
        elif re.compile(r'^conn\s\S+:\S+$').match(strs):    #conn
            return GeneralDo.conn(strs)
        elif strs == 'logout':                                  #logout
            return GeneralDo.logout(strs)
        elif strs == 'configs':                               #configs
            return SuperDo.configs(strs)
        else:
            return Command.unknown(strs)


#Blog的操作
class BlogDo(object):
    def __init__(self):
        pass

    @classmethod
    def reselect(cls, strs):
        if re.compile(r'^blog\s\S+').match(strs):   #去掉blog头
            strs = strs[5:]
        if re.compile(r'^post$').match(strs):       #blog post
            return BlogDo.PostAdd(strs)
        elif strs == 'postlist':                    #blog postlist
            return BlogDo.PostList(strs)
        elif strs == 'cate':                    #blog postlist
            return BlogDo.CateAdd(strs)
        elif strs == 'catelist':                    #blog postlist
            return BlogDo.CateList(strs)
        else:
            return Command.unknown(strs)

    @classmethod
    @Authorization.command_required
    def PostAdd(cls, strs):
        return BaseDo.PageRedirect(url_for('blog.adminPost'))

    @classmethod
    @Authorization.command_required
    def PostList(cls, strs):
        return BaseDo.PageRedirect(url_for('blog.adminPostList'))

    @classmethod
    @Authorization.command_required
    def CateAdd(cls, strs):
        return BaseDo.PageRedirect(url_for('blog.adminCategory'))

    @classmethod
    @Authorization.command_required
    def CateList(cls, strs):
        return BaseDo.PageRedirect(url_for('blog.adminCateList'))