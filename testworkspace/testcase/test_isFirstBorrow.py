#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
import getToken
import unittest

class case_isFirstBorrow(unittest.TestCase):
    def test_isFirstBorrow(self):
        token = getToken.getToken()
        url = 'http://120.55.42.27/caifu/user/isFirstBorrow'
        params = {
            'cellPhone': '13572489850',
            'token': token
        }
        response = requests.get(url=url, params=params)
        self.assertEqual(response.status_code, 200, 'isFirstBorrow OK')
        print "test_isFirstBorrow:", response.content