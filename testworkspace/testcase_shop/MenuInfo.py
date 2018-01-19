#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
from config import *
from testworkspace.common.tool import *
from getShopToken import *

class MenuInfo(unittest.TestCase):
    # 商城下订单
    def test_getOptionalMenus(self):
        # 根据抓包得，此接口的数据传输格式为Gzip压缩
        url = URL + '/caifu/menu/getOptionalMenus'
        response = requests.post(url=url)
        print response
        if response.status_code == 200:
            print response.content

if __name__ == '__main__':
    testsuit = unittest.TestSuite()

    testsuit.addTest(MenuInfo('test_getOptionalMenus'))

    unittest.TextTestRunner(verbosity=2).run(testsuit)