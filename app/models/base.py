'''
Created by ZhouSp 18-11-8.
'''
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger

__author__ = 'zhou'

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True  # 在数据库中不创建表
    # create_time = Column('create_time',Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attr_dict):
        for key, value in attr_dict.items():
            if hasattr(self, key) and key != 'id':  # 判断一个对象是否包含某个属性
                setattr(self, key, value)
