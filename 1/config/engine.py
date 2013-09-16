# coding:utf-8
from hashlib import sha1
from flask import Flask, render_template, request, g
from app import modules as C
from ext.flask_sqlalchemy import SQLAlchemy


class AppFactory(object):
    def __init__(self):
        self.__app__ = Flask(__name__)

    def Register_Blueprints(self, blueprints=None):
        """
        注册蓝图
        :param blueprints:
        """
        if blueprints:
            for i in blueprints:
                self.__app__.register_blueprint(i)

    def Register_Config(self, conf='config'):
        """
        注册配置文件
        :param conf:
        """
        self.__app__.config.from_object(conf)
        self.__app__.secret_key = 'asgsdfnakwe234tgaedfug98a7g9872'

    def Register_Ext(self):
        """
        注册扩展

        """
        self.db = SQLAlchemy(self.__app__)

    def Register_ErrorHandler(self, e404='404.html', e500='500.html', e403='403.html'):
        """
        注册错误
        :param e404:
        :param e500:
        :param e403:
        :return:
        """

        @self.__app__.errorhandler(404)
        def page_not_found(error):
            return render_template(e404), 404

        @self.__app__.errorhandler(500)
        def internal_error(error):
            self.db.session.rollback()
            return render_template(e500), 500

        @self.__app__.errorhandler(403)
        def not_authorized(error):
            return render_template(e403), 403

        return page_not_found, internal_error, not_authorized

    def Register_Hook(self):
        """
        注册勾子

        :return:
        """

        @self.__app__.before_request
        def before_request():
            if not hasattr(g, 'title'):
                g.title = u'还没设置'

        @self.__app__.teardown_request
        def teardown_request(exception):
            self.db.session.commit()

        # @self.__app__.route('/')
        # def default_index():
        #     return redirect(url_for('abc.index'))

        @self.__app__.route('/init', methods=['GET', 'POST'])
        def init_Config():
            if request.method == 'GET':
                return render_template('init.html')
            else:

                conf = C.Config()
                conf.title = request.form['title']
                conf.adminuser = request.form['adminuser']
                conf.adminpsd = sha1(request.form['adminpsd']).hexdigest()
                conf.homepage = request.form['homepage']
            return 'Success'

        return before_request, teardown_request, init_Config #,default_index

    def Register_Logging(self):
        pass

    def CreateApp(self):
        self.Register_Blueprints(None)
        self.Register_Ext()
        self.Register_ErrorHandler()
        self.Register_Hook()
        self.Register_Logging()
        return self.__app__


factory = AppFactory()
app = factory.CreateApp()
db = factory.db


# from tavern.views import tavern
from app.controller import abc

factory.Register_Blueprints([abc])
