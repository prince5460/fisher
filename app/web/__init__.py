# -*- coding: utf-8 -*-
'''
Created by ZhouSp on  2018/11/3.
'''
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book, auth, drift, gift, main, wish
