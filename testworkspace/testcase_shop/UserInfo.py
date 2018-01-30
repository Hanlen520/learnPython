#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
from config import *
from testworkspace.common.tool import *
from getShopToken import *

# class UserInfo(unittest.TestCase):
#     token = getShopToken()
#     ##初始化工作
#     def setUp(self):
#         # self.token = getShopToken()
#         pass
#     def test_getglobalInfo(self):
#         print u"test_getglobalInfo-当前token为：", self.token
#         url = 'http://10.1.52.153:8080/proxyTable/borrow/lend/globalInfo'
#         params = {
#             'token': self.token
#         }
#         response = requests.get(url=url, params=params)
#         self.assertEqual(response.status_code, 200, 'revealQuery OK')
#         print u"globalInfo查询接口:", response.content
#
#     def test_lend(self):
#         url = 'http://47.96.171.4/caifu/user/signIn'
#         data = {
#             'name': USERINFO['cellphone'],
#             'password': USERINFO['password']
#         }
#         s = json.dumps(data)
#         response = requests.post(url=url, data=s)
#         token_temp = ""
#         if response.status_code == 200:
#             print response.json()
#         print u"test_lend-当前token为：", token_temp
#         # 根据抓包得，此接口的数据传输格式为Gzip压缩
#         url ='http://10.1.52.153:8080/proxyTable/borrow/orders/lend'
#         data = {
#             'token': token_temp,
#             "amount": "0.01",
#             "cycleId": 1,
#             "debitSuffixBankCardNo": 8351,
#             "debitBankName": u'中国交通银行',
#             "creditCardNo": '6226230030317935',
#             "creditBankName": u'中国民生银行',
#             "paymentPassword": 456456
#         }
#         s = json.dumps(data)
#         response = requests.post(url=url, data=s)
#         if response.status_code == 200:
#             print response.content

if __name__ == '__main__':
    token = getShopToken()
    # print u"当前token为：", token
    url = 'http://10.1.52.153:8080/proxyTable/borrow/orders/lend'
    data = {
        'token': token,
        "amount": "0.02",
        "cycleId": 1,
        "debitSuffixBankCardNo": '8351',
        "paySource":"20",
        "debitBankName": u'中国交通银行',
        "creditCardNo": '6226230030317935',
        "creditBankName": u'中国民生银行',
        "paymentPassword": '456456'
    }
    # s = json.dumps(data)
    response = requests.post(url=url, data=data)
    print response
    if response.status_code == 200:
        print response.content