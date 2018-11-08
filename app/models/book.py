# -*- coding: utf-8 -*-
'''
Created by ZhouSp on  2018/11/3.
'''

from sqlalchemy import Column, Integer, String

from app.models.base import db, Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(20), default='佚名')
    binding = Column(String(20))
    publisher = Column(String(30))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(100))
