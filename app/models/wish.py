# -*- coding: utf-8 -*-
'''
Created by ZhouSp on  2018/11/8.
'''

from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship

from app.models.base import db, Base

__author__ = 'zhou'


class Wish(Base):
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)
