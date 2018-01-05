#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
import getToken
import unittest

class case_getAmsglist(unittest.TestCase):
    def test_getAmsglist(self):
        token = getToken.getToken()
        url = 'http://120.55.42.27/caifu/appMessage/getAmsglist'
        params = {
            'number': 1,
            'token': token
        }
        response = requests.get(url=url, params=params)
        self.assertEqual(response.status_code, 200, 'getAmsglist OK')
        print "test_getAmsglist:", response.content