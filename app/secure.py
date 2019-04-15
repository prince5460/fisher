# -*- coding: utf-8 -*-
'''
Created by ZhouSp on  2018/11/3.
'''

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zhou123@localhost/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '4589a439-61b8-4663-a87a-2206afb5d7b2'

MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'admin@zhouhy.com'
MAIL_PASSWORD = 'asxffmpxxouebich'
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书<admin@zhouhy.com>'
MAIL_DEFAULT_SENDER = 'admin@zhouhy.com'
