#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
import getToken
import unittest
from config import *

class QueryUserInfo(unittest.TestCase):
    ##初始化工作
    def setUp(self):
        self.token = getToken.getToken()

    # app消息通知
    def test_getAmsglist(self):
        url = URL + '/caifu/appMessage/getAmsglist'
        params = {
            'number': 1,
            'token': self.token
        }
        response = requests.get(url=url, params=params)
        self.assertEqual(response.status_code, 200, 'getAmsglist OK')
        print u"app消息通知:", response.content

    # 是否首借查询
    def test_isFirstBorrow(self):
        token = getToken.getToken()
        url = URL + '/caifu/user/isFirstBorrow'
        params = {
            'cellPhone': USERINFO['cellphone'],
            'token': self.token
        }
        response = requests.get(url=url, params=params)
        self.assertEqual(response.status_code, 200, 'isFirstBorrow OK')
        print u"是否首借查询:", response.content

    # 信息披露查询接口
    def test_revealQuery(self):
        url = URL + '/caifu/userInfo/revealQuery'
        params = {
            'cellPhone': USERINFO['cellphone'],
            'token': self.token
        }
        response = requests.get(url=url, params=params)
        self.assertEqual(response.status_code, 200, 'revealQuery OK')
        print u"信息披露查询接口:", response.content

    # 联系信息枚举字段查询
    def test_revealEnumQuery(self):
        url = URL + '/caifu/userInfo/revealEnumQuery'
        params = {
            'token': self.token
        }
        response = requests.get(url=url, params=params)
        self.assertEqual(response.status_code, 200, 'revealEnumQuery OK')
        print u"联系信息枚举字段查询:", response.content

    # 退出清理工作
    def tearDown(self):
        pass