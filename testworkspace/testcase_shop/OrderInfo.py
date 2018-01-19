#!/user/bin/env python
# -*- coding:utf-8 -*-

import requests
import unittest
from config import *
from testworkspace.common.tool import *
from getShopToken import *

class OrderInfo(unittest.TestCase):
    token = getShopToken()
    ##初始化工作
    def setUp(self):
        # self.token = getShopToken()
        pass

    # 商城下订单
    def test_order(self):
        # 根据抓包得，此接口的数据传输格式为Gzip压缩
        url = URL_SHOP + '/lqmall/merch/order'
        data = {
            'token': self.token,
            "addressId": "10272",   # 收货地址ID
            "purchaseNum": 1,       # 购买数量
            "purchaseType": 2,      # 购买方式 1-现金支付 2-授信购买
            "stockId": "157"        # 商品ID
        }
        s = json.dumps(data)
        response = requests.post(url=url, data=s)
        if response.status_code == 200:
            print response.content

    # 调用三方支付前置接口
    def test_payEncryption(self):
        # 根据抓包得，此接口的数据传输格式为Gzip压缩
        url = URL_SHOP + '/lqmall/merch/payEncryption'
        data = {
            'token': self.token,
            "orderId": "17083",     # 订单ID
            "payStep": 1,           # 支付步骤 1-订金支付 2-尾款/全款支付
            "thirdType": 2,         #  三方类型 1-微信 2-支付宝 3-银行卡
        }
        s = json.dumps(data)
        response = requests.post(url=url, data=s)
        if response.status_code == 200:
            print response.content

    # 退出清理工作
    def tearDown(self):
        pass

if __name__ == '__main__':
    testsuit = unittest.TestSuite()

    testsuit.addTest(OrderInfo('test_payEncryption'))

    unittest.TextTestRunner(verbosity=2).run(testsuit)