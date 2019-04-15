# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-4-15 下午3:36
@Desc :
'''

from enum import Enum


class PendingStatus(Enum):
    '''交易状态'''
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4
