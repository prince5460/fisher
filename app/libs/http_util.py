# -*- coding: utf-8 -*-
'''
Created by ZhouSp on  2018/11/1.
'''

import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        '''
        获取请求url地址的返回值
        :param url:
        :param return_json:
        :return:
        '''
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
