# -*- coding: utf-8 -*-
'''
Created by ZhouSp on  2018/11/3.
'''
from flask import Flask
from flask_login import LoginManager

from app.models.book import db

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    # 指定静态文件夹路径
    # app = Flask(__name__,static_folder='xxx')
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    # 注册SQLAlchemy
    db.init_app(app)

    # 注册login模块
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    # db.create_all(app=app)
    with app.app_context():
        db.create_all()

    from app.web import web
    register_web_blueprint(app)

    return app


def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
