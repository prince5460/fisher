# -*- coding: utf-8 -*-
'''
Created by ZhouSp on  2018/11/3.
'''
from flask import jsonify, request, render_template, flash
import json

from flask_login import current_user

from app.forms.book import SearchForm
from app.view_models.book import BookViewModel, BookCollection
from models.gift import Gift
from models.wish import Wish
from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


@web.route('/book/search')
def search():
    '''
    :param q:关键字 isbn or key
    :param page:
    :return:
    '''

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__)#__dict__将对象转换成字典

    else:
        # return jsonify(form.errors)
        flash('搜索的关键字不符合要求，请重新输入关键字')
    return render_template('search_result.html', books=books)


@web.route("/book/<isbn>/detail")
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishs = False

    # 取出每本书的详情
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    # 三种情况的判断
    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id).first():
            has_in_wishs = True

    # 赠书人列表和索要人列表
    trade_gifts = Gift.query.filter_by(isbn=isbn).all()
    trade_wishs = Wish.query.filter_by(isbn=isbn).all()
    return render_template("book_detail.html", book=book,
                           wishes=trade_wishs, gifts=trade_gifts,
                           has_in_wishs=has_in_wishs, has_in_gifts=has_in_gifts)
