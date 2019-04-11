'''
Created by ZhouSp 18-11-8.
'''
from flask import current_app
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger, desc
from sqlalchemy.orm import relationship

from app.models.base import db, Base
from app.spider.yushu_book import YuShuBook

__author__ = 'zhou'


class Gift(Base):
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 对象代表一个礼物,具体
    # 类代表礼物这个事物,它是抽象的,不是具体的一个
    @classmethod
    def recent(cls):
        # 链式调用
        # distinct这个关键字来过滤掉多余的重复记录只保留一条,sql_mode=only_full_group_by
        recent_gift = Gift.query.filter_by(
            launched=False).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()

        return recent_gift
