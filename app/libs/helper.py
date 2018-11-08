# -*- coding: utf-8 -*-
'''
Created by ZhouSp on  2018/11/1.
'''


def is_isbn_or_key(word):
    '''
    判断是isbn还是关键字
    :param word:
    :return:
    '''
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
