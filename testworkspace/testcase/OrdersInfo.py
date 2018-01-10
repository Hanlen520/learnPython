#!/user/bin/env python
# -*- coding:utf-8 -*-

import requests
import getToken
import unittest
from config import *

class OrdersInfo(unittest.TestCase):
    ##初始化工作
    def setUp(self):
        self.token = getToken.getToken()

    # 退出清理工作
    def tearDown(self):
        pass