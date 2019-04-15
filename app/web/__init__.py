# -*- coding: utf-8 -*-
'''
Created by ZhouSp on  2018/11/3.
'''
from flask import Blueprint, render_template

web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


from app.web import book, auth, drift, gift, main, wish
