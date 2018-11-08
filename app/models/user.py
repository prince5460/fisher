'''
Created by ZhouSp 18-11-8.
'''
from sqlalchemy import Column, Integer, String, Boolean, Float

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.models.base import db, Base
from app import login_manager


__author__ = 'zhou'


class User(UserMixin, Base):
    # __tablename__ = 'user'#修改表名
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    # 属性的读取
    @property
    def password(self):
        return self._password

    # 属性的赋值
    @password.setter
    def password(self, raw):  # raw表示原始数据
        self._password = generate_password_hash(raw)

    # 校验密码
    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    # # 设置密码
    # def set_password(self, password):
    #     self._password = generate_password_hash(password)
    #
    # # 验证密码
    # def validate_password(self, password):
    #     return check_password_hash(self._password, password)


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))

