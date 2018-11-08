# -*- coding: utf-8 -*-
'''
Created by ZhouSp on  2018/11/3.
'''

from flask import Flask, current_app

app = Flask(__name__)

# flask应用实例入栈
ctx = app.app_context()
ctx.push()
a = current_app
b = current_app.config['DEBUG']
print(a)
ctx.pop()

# 上下文管理
with app.app_context():
    a = current_app
    print(a)


# 上下文管理器
class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('process exception')
        else:
            print('no exception')
        print('close resource exception')

        return False

    def query(self):
        print('query data')


try:
    # resource:__enter__方法的返回值
    with MyResource() as resource:
        resource.query()
except Exception as e:
    pass
