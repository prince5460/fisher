from flask import current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app.libs.enums import PendingStatus
from app.models.base import db
from app.models.drift import Drift
from app.models.gift import Gift
from app.view_models.gift import MyGifts
from app.view_models.trade import MyTrades
from . import web

__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyTrades(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=view_model.trades)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            # try:
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            # current_user.beans += 0.5
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            # db.session.commit()
        # except Exception as e:
        #     db.session.rollback()  # 事务的回滚
        #     raise e
    else:
        flash('本书已添加至您的赠送清单或心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


# 撤销赠送书籍
@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    gift = Gift.query.filter_by(id=gid, launched=False).first_or_404()
    # 判断这个礼物是否处于交易状态，
    # 处于交易状态是不能直接撤销的
    drift = Drift.query.filter_by(
        gift_id=gid,
        pending=PendingStatus.Waiting
    ).first()
    if drift:
        flash('这个礼物正处于交易状态，请前往鱼漂完成该交易')
    else:
        with db.auto_commit():
            current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
            gift.delete()
    return redirect(url_for('web.my_gifts'))
