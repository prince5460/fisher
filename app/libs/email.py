# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-13 下午5:24
@Desc :
'''
from threading import Thread

from flask import render_template, current_app, flash
from app import mail
from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            flash('发送错误')
            raise e


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subject, recipients=[to], sender=current_app.config['MAIL_USERNAME'])
    msg.html = render_template(template, **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
