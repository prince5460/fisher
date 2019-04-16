# -*- coding: utf-8 -*-
'''
Created by ZhouSp on  2018/11/1.
'''
import click

from app import create_app
from app.models.base import db
from app.models.book import Book
from app.models.drift import Drift
from app.models.gift import Gift
from app.models.user import User
from app.models.wish import Wish

app = create_app()

# # shell创建数据库
# @app.cli.command()
# @click.option('--drop', is_flag=True, help='Create after drop.')
# def initdb(drop):
#     """Initialize the database."""
#     if drop:
#         db.drop_all()
#     db.create_all()
#     click.echo('Initialized database.')
#

# 注册shell上下文处理函数
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Book=Book, User=User, Wish=Wish, Gift=Gift, Drift=Drift)

if __name__ == '__main__':
    app.run()
