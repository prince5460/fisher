# -*- coding: utf-8 -*-
'''
Created by ZhouSp on  2018/11/5.
'''


class BookViewModel:
    def __init__(self, data):
        self.title = data['title']
        self.publisher = data['publisher']
        self.pages = data['pages']
        self.author = ','.join(data['author'])
        self.price = data['price']
        self.summary = data['summary']
        self.image = data['image']
        self.isbn = data['isbn']
        self.pages = data['pages']
        self.binding = data['binding']
        self.pubdate = data['pubdate']

    # 用属性访问调用函数
    @property
    def intro(self):
        intros = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return '/'.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class _BookViewModel:

    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]

        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            # returned['total'] = len(data['books'])
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]

        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': ','.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image'].split("('")
        }
        return book
