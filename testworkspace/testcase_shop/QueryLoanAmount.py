#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
from config import *
from testworkspace.common.tool import *
from getShopToken import *

class QueryLoanAmount(unittest.TestCase):
    token = getShopToken()
    ##初始化工作
    def setUp(self):
        # self.token = getShopToken()
        pass

    def test_queryLoanAmount(self):
        url = URL_SHOP + '/lqmall/kale/queryLoanAmount'
        data = {
            'token': self.token
        }
        s = json.dumps(data)
        response = requests.post(url=url,data=s)
        if response.status_code == 200:
            print response.content

    def test_queryLoanAmountv1(self):
        url = URL_SHOP + '/lqmall/kale/queryLoanAmount_v1'
        data = {
            'token': self.token,
            "platform":"ios",
            "appVersion": "1.0.0117"
        }
        s = json.dumps(data)
        response = requests.post(url=url,data=s)
        if response.status_code == 200:
            print response.content

    # 退出清理工作
    def tearDown(self):
        pass

if __name__ == '__main__':
    pass